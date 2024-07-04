# routes/coordenada.py

from flask import Blueprint, jsonify, request
from models.entities.Coordenada import Coordenada
from models.CoordenadaModel import CoordenadaModel

main = Blueprint('coordenada_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_all_coordenadas():
    try:
        coordenadas = CoordenadaModel.get_all_coordenadas()
        return jsonify(coordenadas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_coordenada():
    try:
        data = request.get_json()
        ubigeo = int(data.get('ubigeo'))

        # Verificar si el ubigeo tiene exactamente 6 dígitos
        if not (isinstance(ubigeo, int) and len(str(ubigeo)) == 6):
            return jsonify({'message': f"El ubigeo '{ubigeo}' debe tener exactamente 6 dígitos"}), 400

        id_coordenada = CoordenadaModel.add_coordenada(ubigeo)

        return jsonify({'id_coordenada': id_coordenada, 'message': "Coordenada agregada correctamente"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500