from werkzeug.security import check_password_hash
from utils.DateFormat import DateFormat

class Usuario():

    def __init__(self, id_usuario, nombre_perfil=None, contrasenna=None, correo=None, numero=None, fecha_nacimiento=None, ubigeo=None) -> None:
        self.id_usuario = id_usuario
        self.nombre_perfil = nombre_perfil
        self.contrasenna = contrasenna
        self.correo = correo
        self.numero = numero
        self.fecha_nacimiento = fecha_nacimiento
        self.ubigeo = ubigeo

    def to_JSON(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre_perfil': self.nombre_perfil,
            'contrasenna': self.contrasenna,
            'correo': self.correo,
            'numero': self.numero,
            'fecha_nacimiento': DateFormat.convert_date(self.fecha_nacimiento),
            'ubigeo': self.ubigeo
            }

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)