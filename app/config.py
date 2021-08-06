class Config:
    '''
    General configuration parent class
    '''
    TOPHEADLINE_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

    CATEGORIES_API_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'


    SEARCH_ITEM_URL = 'https://newsapi.org/v2/everything?q={}&from=2021-08-06&sortBy=popularity&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True