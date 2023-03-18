# Métodos HTTP
El protocolo **HTTP** es aquel que define un conjunto de métodos de petición que indican la acción que se desea realizar para un recurso determinado del servidor.

Los principales métodos soportados por HTTP y por ello usados por una API REST son:
- POST: crear un recurso nuevo.
- PUT: modificar un recurso existente.
- GET: consultar información de un recurso.
- DELETE: eliminar un recurso.

Como te diste cuenta con estos métodos podemos empezar a crear un CRUD en nuestra aplicación.

## ¿De qué tratará nuestra API?
El proyecto que estaremos construyendo a lo largo del curso será una API que nos brindará información relacionada con películas, por lo que tendremos lo siguiente:

### Consulta de todas las películas
Para lograrlo utilizaremos el método **GET** y solicitaremos todos los datos de nuestras películas.

### Filtrado de películas
También solicitaremos información de películas por su id y por la categoría a la que pertenecen, para ello utilizaremos el método **GET** y nos ayudaremos de los parámetros de ruta y los parámetros query.

### Registro de peliculas
Usaremos el método **POST** para registrar los datos de nuestras películas y también nos ayudaremos de los esquemas de la librería pydantic para el manejo de los datos.

### Modificación y eliminación
Finalmente para completar nuestro CRUD realizaremos la modificación y eliminación de datos en nuestra aplicación, para lo cual usaremos los métodos **PUT** y **DELETE** respectivamente.

Y lo mejor es que todo esto lo estarás construyendo mientras aprendes FastAPI, te veo en la siguiente clase donde te enseñaré cómo puedes utilizar el método **GET**.
