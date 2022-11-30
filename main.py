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
from fastapi import status
from fastapi import HTTPException
from fastapi import(
    Body, Query, Path, Form, 
    Header, Cookie, 
    UploadFile, File
    )

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
        default= 'http://www.example.com'
        )
    # avatar: Optional[FilePath] = Field(default=None)
    password: str = Field(
        ...,
        min_length=8,
        max_length=50
        )
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Andy",
    #             "last_name": "Cervantes",
    #             "age": 27,
    #             "hair_color": "black",
    #             "is_married": True
    #         }
    #     }

class PersonOut(BaseModel):
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
        # avatar: Optional[FilePath] = Field(default=None)

class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="maria21"
        )

# Home
@app.get(
    path='/', 
    status_code= status.HTTP_200_OK,
    tags= ["Home"]
    )
def home():
    return {'Hello': 'World'}

# Request and Response Body

@app.post(
    path='/person/new', 
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person in app"
    )
def create_person(person: Person = Body(...)):
    """
     ## Tittle:
     # Create Person
    
     ## Description:
     This path operation creates a person in the app and save the information in the data base
    
     ## Parameters:
    - Request body parameter:
        - **person: Person** -> A person model with first name, last name, agem hair color, and marital status
    
     ## Results:
     Returns a person model with first name, last name, age, hair color, and marital status
    ![Http-200](https://http.cat/200)
    """
    
    return person

# Validaciones: Query Parameters

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
    )
def show_person(
    name: Optional[str] = Query(
        None, 
        min_lenght=1, 
        max_lenght=50,
        title='Person Name',
        description="This is the person name. It's between 1 and 50 characteres",
        example= "Your name"
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

persons = [21, 32, 13, 44, 5, 1]

@app.get(
    path='/person/details/{person_id}',
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
    )
def show_person(
    person_id: int = Path(
        ...,
        gt= 0,
        title= "Person ID",
        description= "This is the person ID. It is required",
        example= 1
        )
):
    if person_id not in persons:
        raise HTTPException(
                status_code= status.HTTP404_NOT_FOUND,
                details= "This person doesn't exist"
            )
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_207_MULTI_STATUS,
    tags=["Persons"]
    )
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

# Forms

# Login account
@app.post(
          path="/login",
          response_model=LoginOut,
          status_code=status.HTTP_200_OK,
          tags=["Persons"]
          )
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)

# Cookies and Headers Parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Contact Forms"]
    )
def contact(
    first_name: str = Form(
        ...,
        max_lenght=200,
        min_lenght=1
    ),
    last_name: str = Form(
        ...,
        max_lenght=200,
        min_lenght=1
    ),
    email:  EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
        ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent

# Files
@app.post(
    path="/post-image",
    tags=["Upload Image"]
    )
def post_image(
    image: UploadFile = File(...)
):
    return{
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }
    
# ~