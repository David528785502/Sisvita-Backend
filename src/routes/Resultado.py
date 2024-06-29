from flask import Blueprint, jsonify, request
from models.entities.Resultado import Resultado
from models.ResultadoModel import ResultadoModel

main = Blueprint('resultado_blueprint', __name__)

@main.route('/save', methods=['POST'])
def save_result():
    try:
        id_usuario = request.json['id_usuario']
        id_test = request.json['id_test']
        respuestas = request.json['respuestas']
        resultado = request.json['resultado']

        resultado_entry = Resultado(None, id_usuario, id_test, respuestas, resultado)
        affected_rows = ResultadoModel.save_resultado(resultado_entry)

        if affected_rows == 1:
            return jsonify({'message': 'Resultado guardado con éxito'}), 201
        else:
            return jsonify({'message': 'Error al guardar el resultado'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/usuario/<int:id_usuario>', methods=['GET'])
def get_resultados_by_usuario(id_usuario):
    try:
        resultados = ResultadoModel.get_resultados_by_usuario(id_usuario)
        return jsonify(resultados), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
