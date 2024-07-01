class Pregunta():

    def __init__(self, id_pregunta, id_test=None, texto=None):
        self.id_pregunta = id_pregunta
        self.id_test = id_test
        self.texto = texto
        
    def to_JSON(self):
        return {
            'id_pregunta': self.id_pregunta,
            'id_test': self.id_test,
            'texto': self.texto,
        }