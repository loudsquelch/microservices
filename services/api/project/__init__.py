import os

from flask import Flask

def create_app(script_info=None):
    # instantiate app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    #print(app.config, file=sys.stderr)

    # Set up extensions

    # Register blueprints
    from project.api.version import version_blueprint
    app.register_blueprint(version_blueprint)

    from project.api.instances import instances_blueprint
    app.register_blueprint(instances_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {
            "app": app
        }
    
    return app