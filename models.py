from sqlalchemy import create_engine,Column, Integer, String, ForeignKey #estoy importando los tipos de datos que voy a usar en la base de datos porque sqlalchemy necesita saber que tipo de datos va a manejar
from sqlalchemy.orm import declarative_base
import sqlalchemy_utils #ese sqlalchemy_utils es un extra de sqlalchemy que nos da herramientas extras a nuestro proyecto, son cosas utiles (no lo voy a usar pero se entiende)
#si queremos hacer una nueva funcion y necesitamos por ejemplo el nombre del usuario tenemos que hacer una migracion de la db, para eso usamos la biblioteca alembic, para iniciarla
#escribimos en cmd "alembic init alembic" para crear un directorio alembic para poder usarlo, ahi va a crear dos cosas, una carpeta con el nombre alembic y un archivo .ini
#para usarlo tenemos que poner nuestra direccion de db y pegarla en el archivo .ini y en el env.py dentro de la carpeta alembic necesitas 


#crear la conexion a la base de datos
db = create_engine('postgresql://postgres:123correof@localhost/cursofastapi') #aqui estoy creando la conexion a la base de datos usando postgresql, con el usuario postgres, la contrasena 123correof y la base de datos cursofastapi

#creando la base de la base de datos
base = declarative_base() #aqui le estoy diciendo a sqlalchemy que lo que le voy a pasar ahora que lo guarde, lo entienda, entienda las palabras clave, que guarde metadata, que guarde un registro interno y todo eso 
#necesito esto para ponerlo en el parametro del nombre de nuestra db para que el sqlalchemy sepa que hacer con toda esa info

#crear la tabla de usuarios
#usuarios
# pedidos
# itemsPedidos

class User(base): #aqui estoy creando la clase user que va a representar la tabla de usuarios en la base de datos
    __tablename__ = 'users' #aqui estoy definiendo el nombre de la tabla en la base de datos 

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True) 
    username = Column('username', String, unique=True, index=True, nullable=False)
    email = Column('email', String, unique=True, index=True, nullable=False)
    full_name = Column('full_name', String)
    senha = Column('hashed_password', String, nullable=False)

    def __init__(self, username, email, senha): #esto sirve basicamente para darle un valor a nuestros datos (u objetos) de la base de datos, aqui vamos a decirle los parametros que ellos van a tener, donde self se refiere automaticamente a lo que esta escrito despues de Class (en este caso, user), y le da valores utilizables a ese user#
        self.username = username #aqui le digo "el parametro username dentro de self (user) es igual al username informado arriba", se que suena medio obvio pero lo entiendes mejor porque eres idiota
        self.email = email
        self.senha = senha

#crear la tabla de pedidos
class Order(base): #ese nombre despues de class es el nombre con el cual voy a poder interactuar con esa db en mi codigo python, este es el nombre de la variable por asi decirlo
    __tablename__ = 'orders' 

    id = Column('id', Integer, primary_key=True, index=True) 
    title = Column('title', String, index=True)
    description = Column('description', String, index=True)
    owner_id = Column('owner_id', Integer, ForeignKey('users.id')) #aqui estoy definiendo la relacion entre la tabla de pedidos y la tabla de usuarios, diciendo que el owner_id es una clave foranea que hace referencia al id de la tabla de usuarios
    buyer_id = Column('buyer_id', Integer, ForeignKey('users.id')) #aqui digo quien es el comprador, un comprador puede tener varios productos y un producto varios compradores
    items_id = Column('items_id', Integer, ForeignKey('items.id')) #aqui quiero que las ordenes puedan tener muchos productos, donde varios compradores puedan tener ese producto
    price = Column('price', Integer, index=True)

    def __init__(self, title, description, owner_id, buyer_id, price):
        self.title = title
        self.description = description
        self.owner_id = owner_id
        self.buyer_id = buyer_id

class Items(base):
    __tablename__= 'items'

    id = Column('id', Integer, primary_key=True, index=True)
    nomeitem = Column('nomeitem', String, index=True)
    owner_id = Column('owner_id', Integer, ForeignKey('users.id')) #un item con un solo creador o dueno
    price = Column('price', Integer, index=True)

    def __init__(self, nomeitem, owner_id, price):
        self.nomeitem = nomeitem
        self.owner_id = owner_id
        self.price = price

#ejecutar la creacion de la tabla (crear las tablas en la base de datos)
base.metadata.create_all(bind=db) #esto CREA la base de datos, sin este codigo no se te sube nada, el "bind={la variable que guarda la conexion a la db}"


#para subir los cambios que hacemos a nuestra base de datos, tenemos que usar el comando "alembic revision --autogenerate -m '{mensaje de los cambios, es tipo un commit}'"
#ahi, el creara un archivo con la nueva version y te mostrara los cambios, para poder implementar, osea, confirmar eses cambios usas el comando "alembic upgrade head"
#ahi todo cambia, si quieres eliminar o agregar una nueva columna a tu db es solo borrarla o escribirla en este archivo y usar esos dos comandos