class Config:
    """
    A parent configuration class
    """
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources/{}?apiKey{}'
class ProdConfig(Config):
    """
    A child production  configuration class that inherits from the parent Config class above
    """
class DevConfig(Config):
    """
    A child development configuration class that inherits from the parent Config class above
    """
    Debug= True