import urllib.request,json
from .models import Articles, Source


# Getting api key
api_key = None
# Getting the news base url
base_url = None

category_articles_url = None

search_url = None

categories_url = None

source_url = None


# Getting api key an source links
def configure_request(app):
    global api_key,base_url, categories_url, search_url, source_url, category_articles_url
    api_key = app.config['NEWSAPP_API_KEY']
    base_url = app.config['TOPHEADLINE_API_BASE_URL']
    categories_url = app.config['CATEGORIES_API_URL']
    search_url = app.config['SEARCH_ITEM_URL']
    source_url = app.config['SOURCE_API_URL']
    category_articles_url = app.config['ARTICLE_BY_CATEGORY']





def get_news_articles():
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = base_url.format(api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)


    return articles_results


def search_article(article_query):
    search_article_url =search_url.format(article_query, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)


    return search_article_results


def process_results(article_list):
    '''
    '''
    article_results = []
    for article_item in article_list:
        title = article_item.get('title')
        image = article_item.get('urlToImage')
        description = article_item.get('description')
        author = article_item.get('author')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')
       

        if image:
            article_object = Articles(title, image, description, author, url, publishedAt)
            article_results.append(article_object)
            

    return article_results

def article_categories(category):
    sourceCategories_url = categories_url.format(category,api_key)
    with urllib.request.urlopen(sourceCategories_url) as url:
        source_categories_data = url.read()
        source_categories_response = json.loads(source_categories_data)

        source_categories_results = None

        if source_categories_response['sources']:
            source_categories_list = source_categories_response['sources']
            source_categories_results = process_category_results(source_categories_list)


    return source_categories_results

def process_category_results(category_list):
    '''
    '''
    category_results = []
    for category_item in category_list:
        id = category_item.get('id')
        name = category_item.get('name')
        category = category_item.get('category')
        description = category_item.get('description')
        language = category_item.get('language')
        url = category_item.get('url')

        category_object = Source(id, name, category, description, language, url)
        category_results.append(category_object)

       
       

    return category_results


def article_by_source(source):
    source_articles_url = source_url.format(source,api_key)
    with urllib.request.urlopen(source_articles_url) as url:
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)

        source_articles_results = None

        if source_articles_response['articles']:
            source_articles_list = source_articles_response['articles']
            source_articles_results = process_results(source_articles_list)


    return source_articles_results


def article_by_category(source):
    category_articles = category_articles_url.format(source,api_key)
    with urllib.request.urlopen(category_articles) as url:
        category_articles_data = url.read()
        category_articles_response = json.loads(category_articles_data)

        category_articles_results = None

        if category_articles_response['articles']:
            category_articles_list = category_articles_response['articles']
            category_articles_results = process_results(category_articles_list)


    return category_articles_results

