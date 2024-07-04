from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from models.LoginModel import LoginModel
from models.UsuarioModel import UsuarioModel
from models.EspecialistaModel import EspecialistaModel

main = Blueprint('login_blueprint', __name__)

@main.route('/', methods=['POST'])
def login():
    try:
        correo = request.json['correo']
        contrasenna = request.json['contrasenna']

        login_entry = LoginModel.get_login_by_correo(correo)

        if login_entry and check_password_hash(login_entry.contrasenna, contrasenna):
            tipo = login_entry.tipo  # Asignar 3 para usuarios, 2 para especialistas
            if tipo == 2:
                especialista = EspecialistaModel.get_especialista_by_correo(correo)
                if especialista:
                    return jsonify({'message': "Bienvenido Especialista", 'especialista': especialista}), 200
                else:
                    return jsonify({'message': "Especialista no encontrado"}), 404
            elif tipo == 3:
                usuario = UsuarioModel.get_usuario_by_correo(correo)
                if usuario:
                    return jsonify({'message': "Bienvenido Usuario", 'usuario': usuario}), 200
                else:
                    return jsonify({'message': "Usuario no encontrado"}), 404
        return jsonify({'message': "Credenciales incorrectas"}), 401
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500