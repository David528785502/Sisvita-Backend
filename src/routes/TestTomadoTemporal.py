from flask import Blueprint, jsonify, request

# Entities
from models.entities.TestTomadoTemporal import TestTomadoTemporal
# Models
from models.TestTomadoTemporalModel import TestTomadoTemporalModel

main = Blueprint('test_tomado_temporal_blueprint', __name__)

@main.route('/')
def get_all_tests():
    try:
        tests = TestTomadoTemporalModel.get_all_tests()
        return jsonify(tests)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_test_tomado_temporal>')
def get_test(id_test_tomado_temporal):
    try:
        test = TestTomadoTemporalModel.get_test(id_test_tomado_temporal)
        if test is not None:
            return jsonify(test)
        else:
            return jsonify({'message': "Test not found"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_test():
    try:
        id_test_tomado_temporal = int(request.json['id_test_tomado_temporal'])
        test = TestTomadoTemporal(id_test_tomado_temporal)
        affected_rows = TestTomadoTemporalModel.add_test(test)

        if affected_rows == 1:
            return jsonify({'message': "Test added successfully"})
        else:
            return jsonify({'message': "Failed to add test"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id_test_tomado_temporal>', methods=['DELETE'])
def delete_test(id_test_tomado_temporal):
    try:
        affected_rows = TestTomadoTemporalModel.delete_test(id_test_tomado_temporal)

        if affected_rows == 1:
            return jsonify({'message': "Test deleted successfully"})
        else:
            return jsonify({'message': "Test does not exist, could not be deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500