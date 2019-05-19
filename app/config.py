class Config:
    """
    A parent configuration class
    """
class ProdConfig(Config):
    """
    A child production  configuration class that inherits from the parent Config class above
    """
class DevConfig(Config):
    """
    A child development configuration class that inherits from the parent Config class above
    """
    Debug= True