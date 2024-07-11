from utils.DateFormat import DateFormat

class Resultado:
    def __init__(self, id_resultado, id_usuario, nombre_perfil, ubigeo, id_test, test, diagnostico, color, fecha, id_test_tomado_temporal):
        self.id_resultado = id_resultado
        self.id_usuario = id_usuario
        self.nombre_perfil = nombre_perfil
        self.ubigeo = ubigeo
        self.id_test = id_test
        self.test = test
        self.diagnostico = diagnostico
        self.color = color
        self.fecha = fecha
        self.id_test_tomado_temporal = id_test_tomado_temporal

    def to_JSON(self):
        return {
            'id_resultado': self.id_resultado,
            'id_usuario': self.id_usuario,
            'nombre_perfil': self.nombre_perfil,
            'ubigeo': self.ubigeo,
            'id_test': self.id_test,
            'test': self.test,
            'diagnostico': self.diagnostico,
            'color': self.color,
            'fecha': DateFormat.convert_date(self.fecha),
            'id_test_tomado_temporal': self.id_test_tomado_temporal
        }