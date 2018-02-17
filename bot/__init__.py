from flask import Flask
from .utils import get_instance_folder_path
from .config import configure_app

# Configure flask app
app = Flask(__name__, instance_path=get_instance_folder_path(), instance_relative_config=True)
configure_app(app)

# Import blueprints.
from .main import main

# Register blueprints.
app.register_blueprint(main, url_prefix='/')