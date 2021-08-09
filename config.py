import os


class Config:
    '''
    General configuration parent class
    '''
   
    NEWSAPP_API_KEY = os.environ.get('NEWSAPP_API_KEY')
    
    TOPHEADLINE_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

    CATEGORIES_API_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'

    SEARCH_ITEM_URL = 'https://newsapi.org/v2/everything?q={}&from=2021-08-06&sortBy=popularity&apiKey={}'
    
    SOURCE_API_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    ARTICLE_BY_CATEGORY = 'https://newsapi.org/v2/everything?q={}&apiKey={}'


    # https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5449b648c646487785e2184297d70841
    # https://newsapi.org/v2/everything?q=apple&from=2021-08-06&sortBy=popularity&apiKey='5449b648c646487785e2184297d70841'


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

config_options = {
'development':DevConfig,
'production':ProdConfig
}