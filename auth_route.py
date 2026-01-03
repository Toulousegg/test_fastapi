from fastapi import APIRouter, Depends, HTTPException
from models import User
#from models import db estas dos importanciones eran importantes para poder hacer la session en este mismo archivo pero no lo voy a hacer porque no es lo ideal, pero se puede, voy a comentar las otras lineas
#from sqlalchemy.orm import sessionmaker #esto es importante porque para poder hacer cualquier cosa en la db tenemos que abrir y cerrar sesion en la db 
#porque si abrimos una sesion, hacemos la cambios pero no cerramos la sesion se hace una fila enorme de sesiones y un dia no podremos hacer mas nada de tantas sesiones abiertas
from dependencias import CrearSession
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

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
async def create_conta(usuario_schema: UserSchema, session = Depends(CrearSession)): #antes de hacer el archivo 'dependencias.py', los parametros eran solo los primeros 3, despues de crear el archivo puedo pasar el parametro session que hace referencia al return de la funcion create_session
    #Session = sessionmaker(bind=db) #aqui estoy creando una conexion con la db
    #session = Session() # y aqui la estancia de esa conexion
    usuario = session.query(User).filter(User.email==usuario_schema.email).all() #aqui estoy buscando un usuario en la mi tabla de usuarios y filtrando la info para encontrarlos mas rapido

    #if len(usuario) > 0:#si la lista de usuario de arriba es mayor que 0, osea, que hay uno o mas, no permitir crear la cuenta, pero esta forma es medio lenta, trabajas con listas desnecesarias
    if usuario: #aqui literalmente es, si usuario es None ok, pero si es not None, no lo dejes porque esta repetido, es lo mismo que el de arriba pero mejorado
        print("error, ese usuario ya existe")
        #return {'mensaje': 'usuario ya existe'} para no pasar el este mensaje y hacerle un codigo especial usamos la biblioteca httpexception
        raise HTTPException(status_code=400, detail="usuario ya existente") #aqui estamos diciendo que cuando aparezca esto en vez de mostrar simplemente usuario ya existe va a mostrar el codigo 400 y si explicacion, es mas tipo el codigo 200 que salio bien o el 500 que hubo un fallo

    else:
        senha_nova = bcrypt_context.hash(usuario_schema.senha)
        NewUser = User(usuario_schema.username, usuario_schema.email, senha_nova, usuario_schema.fullname)
        session.add(NewUser) #aqui estoy adicionando la info que coloque en la sesion y...
        session.commit() #posteriormente subirla a la db, como este aqui, esto se hace para poner todos los cambios de una vez en una sola modificacion, asi evitamos trancarnos como lo dijimos antes
        print('usuario registrado con exito')
        return {'mensaje': f'usuario registrado con exito, {usuario_schema.username}'}
