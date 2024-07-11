from flask import Blueprint, jsonify, request

# Entities
from models.entities.Pregunta import Pregunta
# Models
from models.PreguntaModel import PreguntaModel

main = Blueprint('pregunta_blueprint', __name__)

@main.route('/')
def get_preguntas():
    try:
        preguntas = PreguntaModel.get_preguntas()
        return jsonify(preguntas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_pregunta>')
def get_pregunta(id_pregunta):
    try:
        pregunta = PreguntaModel.get_pregunta(id_pregunta)
        if pregunta is not None:
            return jsonify(pregunta)
        else:
            return jsonify({'message': "No se encontró pregunta"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_pregunta():
    try:
        id_test = int(request.json['id_test'])
        texto = request.json['texto']

        pregunta = Pregunta(None, id_test, texto)
        affected_rows = PreguntaModel.add_pregunta(pregunta)

        if affected_rows == 1:
            return jsonify({'message': "Se añadió correctamente la pregunta"})
        else:
            return jsonify({'message': "No se pudo añadir la pregunta"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id_pregunta>', methods=['DELETE'])
def delete_pregunta(id_pregunta):
    try:
        affected_rows = PreguntaModel.delete_pregunta(id_pregunta)

        if affected_rows == 1:
            return jsonify({'message': "Se eliminó correctamente la pregunta"})
        else:
            return jsonify({'message': "Pregunta no existe, no pudo ser borrada"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/test/<id_test>')
def get_preguntas_by_id_test(id_test):
    try:
        preguntas = PreguntaModel.get_preguntas_by_id_test(id_test)
        return jsonify(preguntas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
