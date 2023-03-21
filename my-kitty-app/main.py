# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# app = FastAPI() # Llamamos a FastAPI

# app.title = 'My app with FastAPi'
# app.version = '0.0.1'

# @app.get('/', tags=['home']) # Llamamos a la clase y el método. Asignamos una ruta y un nombre.
# def message(): # EL mensaje que será transmitido en el Front-end
#     return {'Hello':'World!'} # Podemos retornar también HTML, o un Diccionario

# # Podemos agregar uvicorn main:app --reaload
# # Al ejecutar nuestro código en la términal. 
# # También podemos agregar el flag --port para decirle
# # Donde escuchara nuestra app, en este caso usamos el puerto 5000

# # También si queremos compartir mediante red podemos usar:
# # uvicorn main:app --reload --port 5000 --host 0.0.0.0

# --- Método GET con HTMLResponse --- #

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Agregamos el diccionario con import.
from Cats_of_world import cats
# Ahora nuestro dict está en la variable cats.

app = FastAPI() # Guardamos el método de FastAPI a una variable.

app.title = 'My CatApp with FastAPI' # Título de la documentación.
app.version = '0.0.1' # Versión, será mostrada en las etiquetas de la cabecera.



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<div id="logo" class="lg left"><a href="https://cats.com"><img class="nolazy" src="https://cats.com/wp-content/themes/ribosome/img/cats-com-logo.svg" width="500" height="120" alt="Cats.com"></a></div><div id="attachment_66850" style="width: 1010px" class="wp-caption alignnone"><img aria-describedby="caption-attachment-66850" decoding="async" class="wp-image-66850 size-full" src="https://cats.com/wp-content/uploads/2023/03/man-stroking-a-small-kitten.jpg" alt="man stroking a small kitten" width="1000" height="667" srcset="https://cats.com/wp-content/uploads/2023/03/man-stroking-a-small-kitten.jpg 1000w, https://cats.com/wp-content/uploads/2023/03/man-stroking-a-small-kitten-768x512.jpg 768w, https://cats.com/wp-content/uploads/2023/03/man-stroking-a-small-kitten-624x416.jpg 624w, https://cats.com/wp-content/uploads/2023/03/man-stroking-a-small-kitten-540x360.jpg 540w" sizes="(max-width: 1000px) 100vw, 1000px" /><p id="caption-attachment-66850" class="wp-caption-text">A number of scientific studies have explored cats&#8217; ability to understand human emotions.</p></div>')

@app.get('/cats', tags=['cats of world'])
def get_cats_ow():
    return cats

@app.get('/cats/{id}', tags=['ID Cat'])
def get_cat_id(id: int):
    '''
     # **ARG: Choose a number from 1 to 36**
     
     ### **id = int (1:36)**
     
     ---
     
     ## **Return Params**:
       ``` 
        - breed : str
        
        - weight : str
        
        - size : str
        
        - color : str
       ``` 
    '''
    for value in cats.values():
        if value["id"] == id:
            return value
    return []

# --- Parametros QUERY --- #

@app.get('/cats/', tags=['Cat Breed'])
def get_breed_by_id(id_cat: int = None, breed_cat: str = None):
    '''
    **If you don't remember a breed, don't worry.**
    
    # Use **GET ID** to find a breed of cat
    
    __Choose from 1 to 36__
    '''
    
    ## ---- variables ---- ##
    results = []  # Lista vacía para almacenar los resultados de la búsqueda
    ## ---- variables ---- ## 
    
    # Si se proporciona un id_cat pero no es válido, devuelve 'ID inválido'
    if id_cat is not None and id_cat not in cats:
        return 'Invalid ID'
    
    # Si se proporciona un id_cat, devuelve la información de la raza del gato correspondiente
    elif id_cat is not None:
        value = cats[id_cat]
        
        # Si se proporciona un breed_cat y no coincide con la raza del gato, devuelve "Raza de gato no encontrada"
        if breed_cat is not None and value['breed'].lower() != breed_cat.lower():
            return 'Cat breed not found'
        
        # Devuelve información sobre la raza del gato
        return {
            "breed": value['breed'], 
            "weight": value['weight'], 
            "size": value['size'],
            "color": value['color']
        }
    
    # Si se proporciona un breed_cat, busca y devuelve todas las razas de gatos que coincidan
    elif breed_cat is not None:
        for value in cats.values():
            if value['breed'].lower() == breed_cat.lower():
                results.append(
                    {
                        "id": value["id"],
                        "breed": value["breed"], 
                        "weight": value["weight"], 
                        "size": value["size"], 
                        "color": value["color"]
                    }
                )
        # Si se encuentran razas de gatos, devuelve la lista de resultados
        if len(results) > 0:
            return results
        else:
            # Si no se encuentra ninguna raza de gato, devuelve "Raza de gato no encontrada"
            return "Cat breed not found"
    
    # Si no se proporciona ni id_cat ni breed_cat, devuelve "Proporcione el parámetro ID o breed"
    else:
        return "Please provide either ID or breed parameter"
