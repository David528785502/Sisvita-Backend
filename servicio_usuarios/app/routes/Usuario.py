from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
import re

# Entities
from models.entities.Usuario import Usuario
# Models
from models.UsuarioModel import UsuarioModel
from models.LoginModel import LoginModel

main = Blueprint('usuario_blueprint', __name__)

@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_usuario>')

def get_usuario(id_usuario):
    try:
        usuario = UsuarioModel.get_usuario(id_usuario)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({'message': "No se encontró usuario"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])

def add_usuario():
    try:
        id_usuario = int(request.json['id_usuario'])
        nombre_perfil = request.json['nombre_perfil']
        contrasenna = generate_password_hash(request.json['contrasenna'], method="pbkdf2")
        correo = request.json['correo']
        numero = int(request.json['numero'])
        fecha_nacimiento = request.json['fecha_nacimiento']
        ubigeo = int(request.json['ubigeo'])

        # Verificar si el número tiene exactamente 9 dígitos
        if not (isinstance(numero, int) and len(str(numero)) == 9):
            return jsonify({'message': f"El número '{numero}' debe tener exactamente 9 dígitos"}), 400

        # Verificar si el correo electrónico tiene el formato correcto
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return jsonify({'message': f"El correo electrónico '{correo}' no tiene un formato válido"}), 400

        # Verificar si el ubigeo tiene exactamente 6 dígitos
        if not (isinstance(ubigeo, int) and len(str(ubigeo)) == 6):
            return jsonify({'message': f"El número '{ubigeo}' debe tener exactamente 6 dígitos"}), 400
        
        # Verificar si el correo electrónico ya existe
        existing_usuario = LoginModel.get_login_by_correo(correo)
        if existing_usuario:
            return jsonify({'message': f"El correo electrónico '{correo}' ya está registrado"}), 400

        usuario = Usuario(id_usuario, nombre_perfil, contrasenna, correo, numero, fecha_nacimiento, ubigeo)

        affected_rows = UsuarioModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify({'message': "Se añadió correctamente el usuario"})
        else:
            return jsonify({'message': "No se pudo añadir usuario"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    try:
        usuario = Usuario(id_usuario)
        correo = UsuarioModel.get_usuario(id_usuario)

        affected_rows = UsuarioModel.delete_usuario(usuario) and LoginModel.delete_login_by_correo(correo['correo'])

        if affected_rows == 1:
            return jsonify({'message': "Se eliminó correctamente el usuario: " + usuario.id_usuario})
        else:
            return jsonify({'message': "Usuario no existe, no pudo ser borrado"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500