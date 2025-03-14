from flask import Flask, render_template, Blueprint, current_app
from flask_socketio import SocketIO
import os

plugin = Blueprint("plugin", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
socketio = None


def init_socketio(sio):
    """ Attach SocketIO to this plugin """
    global socketio
    socketio = sio

    @socketio.on('connect')
    def handle_connect():
        pass


@plugin.route('/')
def main():
    base_exists = "base.html" in current_app.jinja_loader.list_templates()
    return render_template('example.html', base_exists=base_exists)


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(plugin)

    # ------------------------------------------
    # ---- Option 1 - run without websocket ----
    # ------------------------------------------
    app.run()

    # ------------------------------------------
    # ---- Option 2 - run with websocket -------
    # ------------------------------------------
    # socketio = SocketIO(app)
    # init_socketio(socketio)
    # socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
