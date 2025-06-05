Plugin for IvoryOS
===================

This is a `plugin template <https://gitlab.com/heingroup/ivoryos-plugin-template>`_ for extending IvoryOS with standalone pages. It demonstrates how to structure a plugin using Flask's Blueprint system and integrate with IvoryOS through an entry point.

Features
--------

- Uses Flask's ``Blueprint`` to modularize the plugin.
- Includes a WebSocket (``SocketIO``) integration.
- Includes hardware access for components that are initialized for IvoryOS
- Can function as a standalone page or as part of the IvoryOS ecosystem.

.. image:: https://gitlab.com/heingroup/ivoryos-plugin-template/-/raw/main/docs/img.png
   :alt: Plugin Structure Image

Plugin structure
----------------

.. code-block::

    ivoryos_plugin/
    ├── templates/
    │   ├── example.html    # Template file for the plugin
    ├── __init__.py
    ├── plugin.py           # Main plugin file
    README.rst              # README file (optional)


Quick start
------------------------------------

.. code-block::

    git clone https://gitlab.com/heingroup/ivoryos-plugin-template
    pip install ivoryos



Register the plugin in ``ivoryos``
-----------------------------------

Each plugin must define an entry point under ``ivoryos.plugins`` so that it can be discovered by IvoryOS.

.. code-block:: python

    from ivoryos_plugin.plugin import plugin
    ivoryos.run(__name__, blueprint_plugins=plugin)


Note for ``plugin.py``
------------------------------------

- The plugin must define a ``main`` function inside a Flask ``Blueprint``. This function serves as the main route of the plugin (quick access in the navigation panel).

.. code-block:: python

    from flask import render_template, Blueprint, current_app
    import os

    plugin = Blueprint("plugin", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

    @plugin.route('/')
    def main():
        base_exists = "base.html" in current_app.jinja_loader.list_templates()
        return render_template('example.html', base_exists=base_exists)


- Import ``deck`` from ``global_config`` if accessing hardware components that are initialized for ``IvoryOS``

.. code-block:: python

    # [access hardware] Comment back this block if need access to control hardware
    # to get the component, user global_config.deck.hardware_name (e.g. global_config.deck.balance)
    from ivoryos.utils.global_config import GlobalConfig
    global_config = GlobalConfig()



**Keynotes:**

1. The Blueprint name need to be unique (e.g. ``plugin`` as in ``Blueprint("plugin", __name__, template_folder=...)``)

.. code-block:: python

    plugin = Blueprint("plugin", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

2. Include ``main()`` as the main route for the plugin.

Running the plugin standalone
-----------------------------

This plugin can also run as a standalone Flask app by executing:
Example: run with Flask

.. code-block:: python

    if __name__ == '__main__':
        app = Flask(__name__)
        app.register_blueprint(plugin)
        app.run()

Example: run with websocket

.. code-block:: python

    if __name__ == '__main__':
        app = Flask(__name__)
        app.register_blueprint(plugin)
        socketio = SocketIO(app)
        init_socketio(socketio)
        socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

This initializes the Flask app and runs the ``plugin Blueprint`` independently.

