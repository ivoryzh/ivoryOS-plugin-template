
# Hello World Plugin for IvoryOS

This is a template plugin for extending Ivory OS with standalone pages. 
It demonstrates how to structure a plugin using Flask's Blueprint 
and integrate with IvoryOS through an entry point.

## Features

- Uses Flask's `Blueprint` to modularize the plugin.
- Includes a WebSocket (`SocketIO`) integration.
- Includes hardware access for components that are initialized for **IvoryOS**
- Can function as a standalone page or as part of the IvoryOS.
- Can support direct config (option 1) or entry point in `setup.py` for automatic discovery (option 2).
![img.png](docs%2Fimg.png)
## Plugin Structure

```
ivoryos_plugin/
├── templates/
│   ├── example.html    # Template file for the plugin
├── __init__.py         
├── plugin.py           # Main plugin file
MANIFEST.in             # installation include/exclude (optional)
setup.py                # Plugin installation file (optional)
README.md
```

## Main Plugin File: `plugin.py`

The plugin must define a `main` function inside a Flask `Blueprint`.
This function serves as the main route of the plugin (quick access in navigation panel).

```python
from flask import render_template, Blueprint, current_app
import os

plugin = Blueprint("plugin", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

@plugin.route('/')
def main():
    base_exists = "base.html" in current_app.jinja_loader.list_templates()
    return render_template('example.html', base_exists=base_exists)
```

## Blueprint in Flask

Flask's `Blueprint` is used to organize routes and views into separate modules. This makes it easy to create modular and reusable components.

- `Blueprint("plugin", __name__, template_folder=...)` defines a new component that can be registered in a Flask app. The blueprint's name ("plugin") need to be unique.
- The `@plugin.route('/')` decorator sets up a route for the plugin. "/" is recommended, but any routes can work.

## Option 1 - Plugin Registration in `ivoryos.run()`
```python
from ivoryos_plugin.plugin import plugin
ivoryos.run(__name__, blueprint_plugins=plugin)
```
## Option 2 - Plugin Registration in `setup.py`

Each plugin must define an entry point under `ivoryos.plugins` so that it can be discovered by IvoryOS.

```python
from setuptools import setup, find_packages

setup(
    ...,
    entry_points={
        "ivoryos.plugins": [
            "plugin = ivoryos_plugin.hello_world",  # Plugin entry point
        ],
    },
    ...
)
```
### Installing the Plugin

To install the plugin in a Python environment:

```sh
pip install .
```

Once installed, IvoryOS will automatically detect and load the plugin based on the entry point.

## Keynotes
1. Attribute name matches the Blueprint name (e.g. both named `plugin` in the example)
```
plugin = Blueprint("plugin", __name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
```

2. Include `main()` as the main route for the plugin
3. For automatic integration (option 2), entry point includes `ivoryos.plugins` in setup.py has the attribute name included (e.g. named `plugin` in the example.

## Running the Plugin Standalone

This plugin can also run as a standalone Flask app by executing:

```python
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(plugin)
    app.run()
    
    # ------------------------------------------
    # ---- Option 2 - run with websocket -------
    # ------------------------------------------
    # socketio = SocketIO(app)
    # init_socketio(socketio)
    # socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
```

This initializes the Flask app and runs the `Blueprint` independently.



## Support
Ivory Zhang: ivoryzhang@chem.ubc.ca 

## Roadmap

## License
