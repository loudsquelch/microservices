class BaseConfig:
    """Base configuration"""
    TESTING = False
    REMOTE_API_TOKEN = "secret"
    REMOTE_INSTANCES_API_URL = "https://api.cam.ctl.io/services/instances/"
    REMOTE_WATCHER_API_URL = "https://api.monitoring.ctl.io/scopes/"

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass