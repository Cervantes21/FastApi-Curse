#Python
from typing import Optional
from enum import Enum
from email_validator import validate_email, EmailNotValidError

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import HttpUrl
from pydantic import FilePath
 

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "Brown"
    black = "Black"
    blonde = "Blonde"
    red = "Red"
class Cities(Enum):
    cuernavaca = "Cuernavaca"
    temixco = "Temixco"
    jiutepec = "Jiutepec"
    tepoztlan = "Tepoztlan"
    xochitepec = "Xochitepec"
    zapata = "Emiliano Zapata"
    cuautla = "Cuautla"
    yautepec = "Yautepec"
class States(Enum):
    ags="Aguascalientes"
    bjc="Baja California" 
    bjcs="Baja California Sur"
    camp="Campeche"
    chps="Chiapas"
    chhh="Chihuahua"
    cdmx="Ciudad de México"
    coa="Coahuila"
    col="Colima"
    dg="Durango"
    edo_mx="Estado de México"
    gto="Guanajuato"
    gro="Guerrero"
    hdgo="Hidalgo"
    jal="Jalisco"
    mich="Michoacán"
    mor="Morelos"
    nay="Nayarit"
    nl="Nuevo León"
    oax="Oaxaca"
    pbl="Puebla"
    qro="Querétaro"
    qroo="Quintana Roo"
    slp="San Luis Potosí"
    snl="Sinaloa"
    sonora="Sonora"
    tab="Tabasco"
    tam="Tamaulipas"
    tlax="Tlaxcala"
    ver="Veracruz"
    yuc="Yucatán"
    zac="Zacatecas"
class Countries(Enum):
    mx="México"
    arg="Argentina"
    col="Colombia"
    br="Brásil"
        
class Location(BaseModel):
    city: Optional[Cities] = Field(...)
    state: Optional[States] = Field(...)
    country: Optional[Countries] = Field(...)


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
        )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    email: EmailStr = Field(
        ...,
        title='Email',
        description='The email of the person that will receive the package.'
        )
    website: HttpUrl = Field(
        ...,
        url='http://www.example.com'
        )
    avatar: Optional[FilePath] = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Andy",
                "last_name": "Cervantes",
                "age": 27,
                "hair_color": "black",
                "is_married": True
            }
        }
@app.get('/')
def home():
    return {'Hello': 'World'}

# Request and Response Body

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_lenght=1, 
        max_lenght=50,
        title='Person Name',
        description="This is the person name. It's between 1 and 50 characteres",
        example="Sarah"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required",
        example=30
        )
):
    return {name: age}

# Validaciones: Path Parameters

@app.get('/person/details/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Details",
        description="This is the person details.",
        example=0000
        )
):
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put("/person/detail/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title = "Person ID",
        description= "This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results= person.dict()
    results.update(location.dict())
    return person