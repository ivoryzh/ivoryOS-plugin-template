from setuptools import setup, find_packages

setup(
    name="ivoryos_plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-socketio",
    ],
    entry_points={
        "ivoryos.plugins": [
            "plugin = ivoryos_plugin.hello_world",  # Plugin entry point
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
