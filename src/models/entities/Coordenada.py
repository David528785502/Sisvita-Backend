class Coordenada:
    def __init__(self, id_coordenada, y, x):
        self.id_coordenada = id_coordenada
        self.y = y
        self.x = x

    def to_json(self):
        return {
            'id_coordenada': self.id_coordenada,
            'y': self.y,
            'x': self.x
        }
