from flask import Blueprint, jsonify, request
from models.RespuestaModel import RespuestaModel
from models.entities.Respuesta import Respuesta

main = Blueprint('respuesta_blueprint', __name__)

@main.route('/')
def get_all_respuestas():
    respuestas = RespuestaModel.get_all_respuestas()
    return jsonify(respuestas)

@main.route('/<id_respuesta>')
def get_respuesta_by_id(id_respuesta):
    respuesta = RespuestaModel.get_respuesta_by_id(id_respuesta)
    if respuesta:
        return jsonify(respuesta)
    else:
        return jsonify({'message': 'Respuesta not found'}), 404

@main.route('/test-tomado-temporal/<id_test_tomado_temporal>')
def get_respuesta_by_id_test_temporal_tomado(id_test_tomado_temporal):
    respuestas = RespuestaModel.get_respuesta_by_id_test_tomado_temporal(id_test_tomado_temporal)
    return jsonify(respuestas)

@main.route('/add', methods=['POST'])
def add_respuesta():
    data = request.get_json()
    # Create a Respuesta object by explicitly passing parameters:
    respuesta = Respuesta(
        id_respuesta=data.get('id_respuesta'), 
        id_usuario=data.get('id_usuario'), 
        id_test_tomado_temporal=data.get('id_test_tomado_temporal'), 
        id_pregunta=data.get('id_pregunta'), 
        id_test=data.get('id_test'), 
        valor=data.get('valor')
    )
    affected_rows = RespuestaModel.add_respuesta(respuesta)
    if affected_rows:
        return jsonify({'message': 'Respuesta added successfully'}), 201
    return jsonify({'message': 'Failed to add respuesta'}), 500

@main.route('/delete/<id_respuesta>', methods=['DELETE'])
def delete_respuesta(id_respuesta):
    affected_rows = RespuestaModel.delete_respuesta(id_respuesta)
    if affected_rows:
        return jsonify({'message': 'Respuesta deleted successfully'})
    return jsonify({'message': 'Respuesta not found or not deleted'}), 404