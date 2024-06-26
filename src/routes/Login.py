from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from models.LoginModel import LoginModel

main = Blueprint('login_blueprint', __name__)

@main.route('/login', methods=['POST'])
def login():
    try:
        correo = request.json['correo']
        contrasenna = request.json['contrasenna']

        login_entry = LoginModel.get_login_by_correo(correo)

        if login_entry and check_password_hash(login_entry.contrasenna, contrasenna):
            tipo = login_entry.tipo
            if tipo == 2:
                return jsonify({'message': "Bienvenido Especialista"}), 200
            elif tipo == 3:
                return jsonify({'message': "Bienvenido Usuario"}), 200
        return jsonify({'message': "Credenciales incorrectas"}), 401
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500