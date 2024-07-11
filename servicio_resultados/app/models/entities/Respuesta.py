class Respuesta():

    def __init__(self, id_respuesta, id_usuario, id_test_tomado_temporal, id_pregunta, id_test, valor):
        self.id_respuesta= id_respuesta
        self.id_usuario = id_usuario
        self.id_test_tomado_temporal = id_test_tomado_temporal
        self.id_pregunta = id_pregunta
        self.id_test = id_test
        self.valor = valor

    def to_JSON(self):
        return {
            'id_respuesta': self.id_respuesta,
            'id_usuario': self.id_usuario,
            'id_test_tomado_temporal': self.id_test_tomado_temporal,
            'id_pregunta': self.id_pregunta,
            'id_test': self.id_test,
            'valor': self.valor,
        }