from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth']) #este prefix que pasamos es un prefixo que indica que el www.%.com/{prefix}/... SIEMPRE va a ser igual, solo despues de el prefix que va a cambiar

#va a quedar dominio/auth/blablabla

#siempre que creemos una ruta son dos etapas, la primera es usar el roteador -- despues definimos el camino o ruta -- y el tipo de requisicion que hace esa cosa --
#                                                                             ↓                                     ↓                                             ↓
#       ↓----------------------------------------------------------------------                                     ↓                                             ↓
#       ↓              ↓---------------------------------------------------------------------------------------------                                             ↓
#       ↓        ↓-----↓-------------------------------------------------------------------------------------------------------------------------------------------
#       ↓        ↓     ↓
@auth_router.get('/sla') #esa arroba se llama "decorator", eso basicamente es para decir que esta linea de codigo junto con su funcion se tiene que ejecutar siempre y cuando tenga un get en la ruta definida
def sla(): #y esta es la segunda, simplemente una funcion que diga que hace esa ruta
    '''
    Docstring para sla, nya, ichi ni san, nya, arigatoooooooo
    '''
    return {'mensaje': 'accesaste a la ruta de auth/sla'}

@auth_router.get('/')
async def auth(): #este funcion es async, POR QUE????, porque esas funciones asincronas permiten que el framework atienda varias peticiones al mismo tiempo
    return {'mensaje': 'accesaste a la ruta de auth'}