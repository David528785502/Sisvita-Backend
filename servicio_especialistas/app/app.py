from flask import Flask
from flask_cors import CORS
import os

# Routes
from routes import Especialista

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    # Blueprints

    app.register_blueprint(Especialista.main, url_prefix='/api/especialistas')

    # Error handlers
    app.register_error_handler(404, page_not_found)

    # Obtener el puerto del entorno, si no está disponible, usar 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)