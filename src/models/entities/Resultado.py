class Resultado():

    def __init__(self, id_resultado, id_usuario, id_test, respuestas, resultado) -> None:
        self.id_resultado = id_resultado
        self.id_usuario = id_usuario
        self.id_test = id_test
        self.respuestas = respuestas
        self.resultado = resultado

    def to_JSON(self):
        return {
            'id_resultado': self.id_resultado,
            'id_usuario': self.id_usuario,
            'id_test': self.id_test,
            'respuestas': self.respuestas,
            'resultado': self.resultado
        }
