from fastapi import APIRouter
from models import User
from models import db
from sqlalchemy.orm import sessionmaker #esto es importante porque para poder hacer cualquier cosa en la db tenemos que abrir y cerrar sesion en la db 
#porque si abrimos una sesion, hacemos la cambios pero no cerramos la sesion se hace una fila enorme de sesiones y un dia no podremos hacer mas nada de tantas sesiones abiertas

auth_router = APIRouter(prefix='/auth', tags=['auth']) #este prefix que pasamos es un prefixo que indica que el www.%.com/{prefix}/... SIEMPRE va a ser igual, solo despues de el prefix que va a cambiar

#va a quedar dominio/auth/blablabla

#siempre que creemos una ruta son dos etapas, la primera es usar el roteador -- despues definimos el camino o ruta -- y el tipo de requisicion que hace esa cosa --
#                                                                             ↓                                     ↓                                             ↓
#       ↓----------------------------------------------------------------------                                     ↓                                             ↓
#       ↓              ↓---------------------------------------------------------------------------------------------                                             ↓
#       ↓        ↓-----↓-------------------------------------------------------------------------------------------------------------------------------------------
#       ↓        ↓     ↓
@auth_router.get('/home') #esa arroba se llama "decorator", eso basicamente es para decir que esta linea de codigo junto con su funcion se tiene que ejecutar siempre y cuando tenga un get en la ruta definida
def sla(): #y esta es la segunda, simplemente una funcion que diga que hace esa ruta
    '''
    Docstring para home, nya, ichi ni san, nya, arigatoooooooo
    '''
    return {'mensaje': 'accesaste a la ruta de auth/home'}

@auth_router.get('/')
async def auth(): #este funcion es async, POR QUE????, porque esas funciones asincronas permiten que el framework atienda varias peticiones al mismo tiempo
    return {'mensaje': 'accesaste a la ruta de auth'}

@auth_router.post ('/create')
async def create_conta(email: str, senha: str, username: str):
    Session = sessionmaker(bind=db) #aqui estoy creando una conexion con la db
    session = Session() # y aqui la estancia de esa conexion
    usuario = session.query(User).filter(User.email==email).all() #aqui estoy buscando un usuario en la mi tabla de usuarios y filtrando la info para encontrarlos mas rapido

    if len(usuario) > 0:
        print("error, ese usuario ya existe")
        return {'mensaje': 'usuario ya existe'}

    else:
        NewUser = User(username, email, senha)
        session.add(NewUser) #aqui estoy adicionando la info que coloque en la sesion y...
        session.commit() #posteriormente subirla a la db, como este aqui, esto se hace para poner todos los cambios de una vez en una sola modificacion, asi evitamos trancarnos como lo dijimos antes
        print('usuario registrado con exito')
        return {'mensaje': 'usuario registrado con exito'}
    
    #ESTO SE PUEDE HACER, PERO NO ES LO MAS SEGURO NI LO MAS RECOMENDADO, ESTO ES SOLO PARA ENTENDER LA LOGICA
    #por que no esta bien? por varias cosas, una de ellas es que si da un error en nuestro codigo, la sesion va a continuar abierta y nunca va a cerrarse por si sola#
    # entonces lo que hacemos es hacer una funcion python normal que independientemente si sale bien o no nos va a cerrar la sesion y asi tambien podemos usar esa sesion 
    # en todos los otros links, porque todos o casi todos van a depender de una sesion para hacer cualquier cosa
    # 
    # otro problema es #