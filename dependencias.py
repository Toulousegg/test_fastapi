from models import db
from sqlalchemy.orm import sessionmaker

def CrearSession():
    try: #este try es literalmente para intentar hacer algo, pero si no funciona nos vamos al finally
        Session = sessionmaker(bind=db) #aqui estoy creando una conexion con la db
        session = Session() # y aqui la estancia de esa conexion
        #return session este return esta bien, pero igual no estamos cerrando la sesion caso de algun problema inesperado porque este return no deja que mas nada se ejecute, que hacemos?
        yield session #le ponemos el yield, que es igual a un return pero no termina la funcion ahi
    finally: #esto ejecuta independientemente si lo anterior funciona o no
        session.close() #para cerrar la sesion