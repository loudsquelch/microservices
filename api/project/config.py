class BaseConfig:
    """Base configuration"""
    TESTING = False
    REMOTE_API_TOKEN = "secret"

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass