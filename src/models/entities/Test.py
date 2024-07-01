class Test():

    def __init__(self, id_test, nombre=None, descripcion=None):
        self.id_test = id_test
        self.nombre = nombre
        self.descripcion = descripcion

    def to_JSON(self):
        return {
            'id_test': self.id_test,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
        }