class Especialista():

    def __init__(self, id_especialista, nombre_perfil=None, correo=None, contrasenna=None, dni=None, nombres=None, apellidos=None, numero_colegiatura=None) -> None:
        self.id_especialista = id_especialista
        self.nombre_perfil = nombre_perfil
        self.correo = correo
        self.contrasenna = contrasenna
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_colegiatura = numero_colegiatura

    def to_JSON(self):
        return {
            'id_especialista': self.id_especialista,
            'nombre_perfil': self.nombre_perfil,
            'correo': self.correo,
            'contrasenna': self.contrasenna,
            'dni': self.dni,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'numero_colegiatura': self.numero_colegiatura
        }