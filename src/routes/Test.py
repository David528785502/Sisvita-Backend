from flask import Blueprint, jsonify, request
from models.TestModel import TestModel
from models.entities.Test import Test
from models.PreguntaModel import PreguntaModel
from models.entities.Pregunta import Pregunta

main = Blueprint('test_blueprint', __name__)

@main.route('/')
def get_tests():
    try:
        tests = TestModel.get_tests()
        return jsonify(tests)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_test>')
def get_test(id_test):
    try:
        test = TestModel.get_test(id_test)
        if test:
            return jsonify(test)
        else:
            return jsonify({'message': "Test not found"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_test():
    try:
        nombre = request.json['nombre']
        descripcion = request.json['descripcion']
        test = Test(None, nombre, descripcion)
        if TestModel.add_test(test):
            return jsonify({'message': "Test added successfully"})
        else:
            return jsonify({'message': "Failed to add test"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id_test>', methods=['DELETE'])
def delete_test(id_test):
    try:
        if PreguntaModel.delete_preguntas_by_test(id_test) and TestModel.delete_test(id_test):
            return jsonify({'message': "Test deleted successfully"})
        else:
            return jsonify({'message': "Failed to delete test or test not found"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500