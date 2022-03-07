from pony.orm import Database, Required, Set, Optional
from pony.orm.core import PrimaryKey

#  from uuid import UUID

db = Database()
db.bind(provider="sqlite", filename="inventario.db", create_db=True)


class Producto(db.Entity):
    id = PrimaryKey(int, column="id_producto", auto=True)
    categoria = Required("Categoria")
    largo = Optional(float, nullable=True)
    ancho = Optional(float, nullable=True)
    espesor = Optional(float, nullable=True)
    calidad = Required(int)
    cantidad = Required(int)


class Categoria(db.Entity):
    id = PrimaryKey(int, column="id_categoria", auto=True)
    nombre = Required(str)
    forma = Optional(str, nullable=True)
    dimensiones = Optional(int, nullable=True, column="dimensionalidad")
    productos = Set(Producto)


db.generate_mapping(create_tables=True)
