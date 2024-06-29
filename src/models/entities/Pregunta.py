class Pregunta:

    def __init__(self, id_pregunta, texto=None, opciones=None, id_test=None):
        self.id_pregunta = id_pregunta
        self.texto = texto
        self.opciones = opciones
        self.id_test = id_test

    def to_JSON(self):
        return {
            'id_pregunta': self.id_pregunta,
            'texto': self.texto,
            'opciones': self.opciones,
            'id_test': self.id_test
        }
