from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
import re

# Entities
from models.entities.Especialista import Especialista
# Models
from models.EspecialistaModel import EspecialistaModel
from models.LoginModel import LoginModel

main = Blueprint('especialista_blueprint', __name__)

@main.route('/')
def get_especialistas():
    try:
        especialistas = EspecialistaModel.get_especialistas()
        return jsonify(especialistas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_especialista>')
def get_especialista(id_especialista):
    try:
        especialista = EspecialistaModel.get_especialista(id_especialista)
        if especialista != None:
            return jsonify(especialista)
        else:
            return jsonify({'message': "No se encontró especialista"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_especialista():
    try:
        id_especialista = int(request.json['id_especialista'])
        nombre_perfil = request.json['nombre_perfil']
        correo = request.json['correo']
        contrasenna = generate_password_hash(request.json['contrasenna'], method="pbkdf2")
        dni = int(request.json['dni'])
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        numero_colegiatura = int(request.json['numero_colegiatura'])

        # Verificar restricciones
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return jsonify({'message': f"El correo electrónico '{correo}' no tiene un formato válido"}), 400

        # Verificar si el dni tiene exactamente 8 dígitos
        if not (isinstance(dni, int) and len(str(dni)) == 8):
            return jsonify({'message': f"El número '{dni}' debe tener exactamente 8 dígitos"}), 400

        # Verificar si el numero_colegiatura tiene exactamente 5 dígitos
        if not (isinstance(numero_colegiatura, int) and len(str(numero_colegiatura)) == 5):
            return jsonify({'message': f"El número '{numero_colegiatura}' debe tener exactamente 5 dígitos"}), 400

        existing_especialista = LoginModel.get_login_by_correo(correo)
        if existing_especialista:
            return jsonify({'message': f"El correo electrónico '{correo}' ya está registrado"}), 400

        especialista = Especialista(id_especialista, nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura)

        affected_rows = EspecialistaModel.add_especialista(especialista)

        if affected_rows == 1:
            return jsonify({'message': "Se añadió correctamente el especialista"})
        else:
            return jsonify({'message': "No se pudo añadir especialista"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id_especialista>', methods=['DELETE'])
def delete_especialista(id_especialista):
    try:
        especialista = Especialista(id_especialista)
        correo = EspecialistaModel.get_especialista(id_especialista)

        affected_rows = EspecialistaModel.delete_especialista(especialista) and LoginModel.delete_login_by_correo(correo['correo'])

        if affected_rows == 1:
            return jsonify({'message': "Se eliminó correctamente el especialista: " + especialista.id_especialista})
        else:
            return jsonify({'message': "Especialista no existe, no pudo ser borrado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500