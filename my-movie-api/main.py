from fastapi import FastAPI

app = FastAPI()

app.title = 'My app with FastAPi'
app.version = '0.0.1'

@app.get('/', tags=['home'])
def message():
    return 'Hello, World!'

# Podemos agregar uvicorn main:app --reaload
# Al ejecutar nuestro código en la términal. 
# También podemos agregar el flag --port para decirle
# Donde escuchara nuestra app, en este caso usamos el puerto 5000

# También si queremos compartir mediante red podemos usar:
# uvicorn main:app --reload --port 5000 --host 0.0.0.0