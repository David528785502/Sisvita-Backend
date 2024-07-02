class TestTomadoTemporal():

    def __init__(self, id_test_tomado_temporal):
        self.id_test_tomado_temporal = id_test_tomado_temporal

    def to_JSON(self):
        return {
            'id_test_tomado_temporal': self.id_test_tomado_temporal,
        }