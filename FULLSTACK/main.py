from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Montar la carpeta "CSS" en la ruta "/CSS"
app.mount("/CSS", StaticFiles(directory="CSS"), name="CSS")
# Montar la carpeta "raw" en la ruta "/raw"
app.mount("/raw", StaticFiles(directory="raw"), name="raw")

# Crear una ruta que devuelva una respuesta HTML
@app.get("/", response_class=HTMLResponse)
async def read_html():
    # Lee el contenido del archivo HTML
    with open("index.html", "r") as f:
        html_content = f.read()
    # Devuelve el contenido HTML como respuesta
    return html_content


# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse, StreamingResponse
# import os

# app = FastAPI()

# # Montar la carpeta "CSS" en la ruta "/CSS"
# app.mount("/CSS", StaticFiles(directory="CSS"), name="CSS")
# # Montar la carpeta "raw" en la ruta "/raw"
# app.mount("/raw", StaticFiles(directory="raw"), name="raw")

# # Crear una ruta que devuelva una respuesta HTML con un video
# @app.get("/", response_class=HTMLResponse)
# async def read_html():
#     # Lee el contenido del archivo HTML
#     with open("index.html", "r") as f:
#         html_content = f.read()
#     # Devuelve el contenido HTML como respuesta
#     return html_content

# # Crear una ruta que transmita el archivo de video con el tiempo de inicio especificado
# @app.get("/video")
# async def video():
#     def iterfile():
#         with open("./raw/masterclass.mp4", mode="rb") as file_like:
#             # Ajustar la posición del archivo para el tiempo de inicio especificado
#             file_like.seek(402 * 1000)
#             while True:
#                 # Leer el archivo en trozos de 8KB
#                 chunk = file_like.read(8192)
#                 if not chunk:
#                     break
#                 yield chunk
#     # Devolver la respuesta de transmisión (StreamingResponse)
#     return StreamingResponse(iterfile(), media_type="video/mp4")

