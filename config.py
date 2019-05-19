import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = '0ccdc00543fa4815af0c11bc4fdabc14'
    


class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
