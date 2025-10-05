import os
from flask import Flask
from dotenv import load_dotenv


load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__, static_folder="../static", template_folder="templates")
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-key"),
    )

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
