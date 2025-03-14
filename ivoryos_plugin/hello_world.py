from flask import Flask, render_template, jsonify, Blueprint, current_app
from flask_socketio import SocketIO
import time
import os


hello_world = Blueprint("hello_world", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
socketio = None

def init_socketio(sio):
    """ Attach SocketIO to this plugin """
    global socketio
    socketio = sio


    @socketio.on('connect')
    def handle_connect():
        pass


@hello_world.route('/')
def main():
    base_exists = "base.html" in current_app.jinja_loader.list_templates()
    return render_template('example.html', base_exists=base_exists)



if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello_world)
    socketio = SocketIO(app)
    init_socketio(socketio)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
