from setuptools import setup, find_packages

setup(
    name="ivoryos_live_plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-socketio",
        "opencv-python",
        "ivoryos",
    ],
    include_package_data=True,
    zip_safe=False,
)
