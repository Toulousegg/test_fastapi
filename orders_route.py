from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencias import CrearSession
from schemas import orderschema
from models import Order

orders_router = APIRouter(prefix='/orders', tags=['orders']) #este prefix que pasamos es un prefixo que indica que el www.%.com/{prefix}/... SIEMPRE va a ser igual, solo despues de el prefix que va a cambiar

#va a quedar dominio/orders/blablabla



#siempre que creemos una ruta son dos etapas, la primera es usar el roteador -- despues definimos el camino o ruta -- y el tipo de requisicion que hace esa cosa --
#                                                                             ↓                                     ↓                                             ↓
#       ↓----------------------------------------------------------------------                                     ↓                                             ↓
#       ↓              ↓---------------------------------------------------------------------------------------------                                             ↓
#       ↓        ↓-----↓-------------------------------------------------------------------------------------------------------------------------------------------
#       ↓        ↓     ↓
#@orders_router.get('/lista') #esa arroba se llama "decorator", eso basicamente es para decir que esta linea de codigo junto con su funcion se tiene que ejecutar siempre y cuando tenga un get en la ruta definida
#def lista(): #y esta es la segunda, simplemente una funcion que diga que hace esa ruta
    #'''
    #Docstring para lista, asi creo un perra explicacion que aparece en el /docs, nomames esto esta perron
    #'''
    #return {'mensaje': 'accesaste a la ruta de ordenes/lista'}

@orders_router.post('/order')
def create_order(orderschema: orderschema, session: Session = Depends(CrearSession)): #este funcion es async, POR QUE????, porque esas funciones asincronas permiten que el framework atienda varias peticiones al mismo tiempo
    neworder = Order(title=orderschema.title, description=orderschema.description) 
    session.add(neworder)
    session.commit()
    return {f"pedido creado bien mamalon. ID del pedido {neworder.id}"}