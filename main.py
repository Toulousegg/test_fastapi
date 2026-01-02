from fastapi import FastAPI
from passlib.context import CryptContext #este modulo es para criptografar las contraseñas
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app=FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

from auth_route import auth_router #esto es MUY IMPORTANTE, porque si tu importas un archivo al main se crea un circulo en que nada se inicia porque el main necesita el otro para funcionar y el otro necesita del main para funcionar, entonces SIEMPRE importar archivos despues de crear la aplicacion como esta escrito arriba#
from orders_route import orders_router

app.include_router(auth_router) #esto sirve basicamente para que el framework usa nuestras rutas y las reconozca como caminos normales y los use, sin esto es como tener las rutas y todo bien
app.include_router(orders_router) #pero no va a entrar a ningun lugar ni va a hacer nada, es basicamente decirle al fastapi "estas rutas de ese archivo ahi, las ves?, usalas pos webon", y tambien aparecen en /docs

#para ejecutar nuestro codigo tenemos que ejecutar esto en el terminal uvicorn main:app --reload

#end point
# %/ordens (esto es un endpoint para saber que va a aparecer en el url %.com/ordens, estas rutas se pueden hacer de tres maneras, aqui mismo (no es recomendado), en un archivo unicamente para eso
# que es bueno, o dividir las rutas de cada funcion de la pagina en archivos diferentes, osea, si tu app va a tener ordenes, admin, auth, etc... hacer un archivo para cada una de las rutas
#para esas funciones


#requisiciones
#RestAPIs 
# Get -> lectura/obtener algo ----------
#                                       } algunas de las RestAPIs se limitan a estas dos, porque los put/patch o delete tambien se pueden ejecutar con el comando post
# Post -> enviar/crear algo ------------
# Put/Patch -> editar
# Delete -> eliminar