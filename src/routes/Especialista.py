from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
import re

# Entities
from models.entities.Especialista import Especialista
# Models
from models.EspecialistaModel import EspecialistaModel

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
        dni = request.json['dni']
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        numero_colegiatura = request.json['numero_colegiatura']

        # Verificar restricciones
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return jsonify({'message': f"El correo electrónico '{correo}' no tiene un formato válido"}), 400

        existing_especialista = EspecialistaModel.get_especialista_by_correo(correo)
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

@main.route('/update/<id_especialista>', methods=['PUT'])
def update_especialista(id_especialista):
    try:
        id_especialista = int(id_especialista)
        nombre_perfil = request.json['nombre_perfil']
        correo = request.json['correo']
        contrasenna = generate_password_hash(request.json['contrasenna'], method="pbkdf2")
        dni = request.json['dni']
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        numero_colegiatura = request.json['numero_colegiatura']

        especialista = Especialista(id_especialista, nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura)

        affected_rows = EspecialistaModel.update_especialista(especialista)

        if affected_rows == 1:
            return jsonify(especialista.id_especialista)
        else:
            return jsonify({'message': "Especialista no existe, no pudo ser actualizado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id_especialista>', methods=['DELETE'])
def delete_especialista(id_especialista):
    try:
        especialista = Especialista(id_especialista)

        affected_rows = EspecialistaModel.delete_especialista(especialista)

        if affected_rows == 1:
            return jsonify({'message': "Se eliminó correctamente el especialista: " + especialista.id_especialista})
        else:
            return jsonify({'message': "Especialista no existe, no pudo ser borrado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500