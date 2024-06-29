from flask import Blueprint, jsonify, request
from models.entities.Test import Test
from models.entities.Pregunta import Pregunta
from models.TestModel import TestModel

main = Blueprint('test_blueprint', __name__)

@main.route('/tests', methods=['GET'])
def get_tests():
    try:
        tests = TestModel.get_tests()
        return jsonify(tests), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/tests', methods=['POST'])
def add_test():
    try:
        data = request.json
        test = Test(0, data['nombre'], data['descripcion'])
        test_id = TestModel.add_test(test)
        if test_id:
            for pregunta in data['preguntas']:
                nueva_pregunta = Pregunta(0, pregunta['texto'], pregunta['opciones'], test_id)
                TestModel.add_pregunta(nueva_pregunta)
            return jsonify({'message': 'Test added successfully'}), 201
        else:
            return jsonify({'message': 'Failed to add test'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/tests/resultados', methods=['POST'])
def submit_test_result():
    try:
        data = request.get_json()
        test_id = data.get('testId')
        respuestas = data.get('respuestas')

        # Lógica para procesar las respuestas y calcular el resultado

        resultado = calcular_resultado(test_id, respuestas)

        return jsonify({'message': 'Test submitted successfully', 'resultado': resultado})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

def calcular_resultado(test_id, respuestas):
    # Lógica de procesamiento del test
    # Puedes implementar tu lógica de cálculo aquí
    # Por ejemplo, contar respuestas correctas, calcular puntaje, etc.
    # Devuelve un resultado basado en las respuestas
    return {
        'testId': test_id,
        'resultado': 'Tu nivel de ansiedad es moderado',
        'color': 'amarillo'  # Verde, amarillo o rojo según el resultado
    }

