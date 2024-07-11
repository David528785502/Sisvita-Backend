from flask import Blueprint, jsonify, request
from models.ResultadoModel import ResultadoModel

main = Blueprint('resultado_blueprint', __name__)

@main.route('/')
def get_all_resultados():
    return jsonify(ResultadoModel.get_all_resultados())

@main.route('/<int:id_resultado>')
def get_resultado_by_id(id_resultado):
    resultado = ResultadoModel.get_resultado_by_id(id_resultado)
    if resultado:
        return jsonify(resultado)
    return jsonify({'message': 'Resultado not found'}), 404

# routes/resultado_routes.py

@main.route('/add', methods=['POST'])
def add_resultado():
    data = request.get_json()
    try:
        if ResultadoModel.add_resultado(data['id_usuario'], data['id_test'], data['id_test_tomado_temporal']):
            return jsonify({'message': 'Resultado added successfully'}), 201
        else:
            return jsonify({'message': 'Failed to add resultado'}), 500
    except KeyError as e:
        return jsonify({'message': f'Missing key {e}'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@main.route('/delete/<int:id_resultado>', methods=['DELETE'])
def delete_resultado(id_resultado):
    if ResultadoModel.delete_resultado(id_resultado):
        return jsonify({'message': 'Resultado deleted successfully'})
    return jsonify({'message': 'Resultado not found or not deleted'}), 404

@main.route('/by-user/<int:id_usuario>')
def get_resultados_by_id_usuario(id_usuario):
    try:
        resultados = ResultadoModel.get_resultados_by_id_usuario(id_usuario)
        if resultados:
            return jsonify(resultados)
        else:
            return jsonify({'message': 'No results found for this user'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@main.route('/by-test/<int:id_test>')
def get_resultados_by_id_test(id_test):
    try:
        resultados = ResultadoModel.get_resultados_by_id_test(id_test)
        if resultados:
            return jsonify(resultados)
        else:
            return jsonify({'message': 'No results found for this test'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500
