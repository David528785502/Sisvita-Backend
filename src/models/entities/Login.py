from werkzeug.security import check_password_hash

class Login():

    def __init__(self, id_login, correo=None, contrasenna=None, tipo=None) -> None:
        self.id_login = id_login
        self.correo = correo
        self.contrasenna = contrasenna
        self.tipo = tipo

    def to_JSON(self):
        return {
            'id_login': self.id_login,
            'correo': self.correo,
            'contrasenna': self.contrasenna,
            'tipo': self.tipo
        }

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)