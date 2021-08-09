from datetime import time
from ssl import HAS_TLSv1_2
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import article_by_category, article_categories, get_news_articles, search_article , article_by_source


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    topHeadline = get_news_articles()

    title = 'Home'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('main.search', article_title = search_article))
    else:
        return render_template('index.html', title = title, headline = topHeadline)

@main.route('/search/<article_title>')
def search(article_title):
    '''
    View function to display the search results
    '''
    search_article_list = article_title.split(" ")
    article_name_format = "+".join(search_article_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_title}'
    return render_template('search.html', title = title, searchResults = searched_articles)

@main.route('/categories')
def categories():
    '''
    Sources function to display available category sources

    '''
    general_categories = article_categories('general')
    entertainment_categories = article_categories('entertainment')
    technology_categories = article_categories('technology')
    
    title = 'Source List'

    return render_template('sourceList.html', general = general_categories, entertainment = entertainment_categories, technology = technology_categories, title = title )


@main.route('/bbc-news')
def bbc_news():
    '''
    Sources function to display available  sources articles

    '''
    bbc = article_by_source('bbc-news')

    title = 'BBC Source'
    h2 = 'BBC Source'
    return render_template('sources.html',  sourcename = bbc, title =title, h2=h2 )


@main.route('/cnn-news')
def cnn_news():
    '''
    Sources function to display available  sources articles

    '''

    cnn = article_by_source('cnn-news')

    title = 'CNN Source'
    h2 = 'CNN Source'
    return render_template('sources.html',  sourcename = cnn, title = title, h2=h2)


@main.route('/fox-news')
def fox_news():
    '''
    Sources function to display available  sources articles

    '''

    fox = article_by_source('fox-news')

    title = 'Fox Source'
    h2 = 'Fox Source'
    return render_template('sources.html',  sourcename= fox, title=title, h2=h2 )



@main.route('/abc-news')
def abc_news():
    '''
    Sources function to display available  sources articles

    '''

    abc = article_by_source('abc-news')

    title = 'ABC Source'
    h2 = 'ABC Source'
    return render_template('sources.html',  sourcename = abc, title=title, h2=h2)



@main.route('/mtv-news')
def mtv_news():
    '''
    Sources function to display available  sources articles

    '''

    mtv = article_by_source('mtv-news')

    title = 'MTV Source'
    h2 = 'MTV Source'
    return render_template('sources.html',  sourcename = mtv, title = title, h2 =h2 )


@main.route('/general')
def general():
    '''
    Sources function to filter general articles

    '''

    general = article_by_category('general')

    title = 'General Articles'
    h2 = 'General Articles'
    return render_template('categoryArticles.html',  general = general, title = title, h2 =h2 )


@main.route('/entertainment')
def entertainment():
    '''
    Sources function to filter articles based on entertainment

    '''

    entertainment = article_by_category('entertainment')

    title = 'Entertainment Articles'
    h2 = 'Entertainment Articles'

    return render_template('categoryArticles.html',  entertainment = entertainment, title = title, h2=h2)


@main.route('/health')
def health():
    '''
    Sources function to filter articles based on health

    '''

    health = article_by_category('health')

    title = 'Health Articles'
    h2 = 'Health Articles'
    return render_template('categoryArticles.html',  health = health, title=title, h2=h2 )

@main.route('/science')
def science():
    '''
    Sources function to filter articles based on science

    '''

    science = article_by_category('science')

    title = 'Science Articles'
    h2 = 'Science Articles'
    return render_template('categoryArticles.html',  science = science, title =title, h2=h2 )

@main.route('/business')
def business():
    '''
    Sources function to filter articles based on health

    '''

    business = article_by_category('business')

    title = 'Business Articles'
    h2 = 'Business Articles'
    return render_template('categoryArticles.html',  business = business, title = title, h2=h2 )



@main.route('/technology')
def technology():
    '''
    Sources function to filter articles based on health

    '''

    technology = article_by_category('technology')

    title = 'Technology Articles'
    h2 = 'Technology Articles'
    return render_template('categoryArticles.html',  technology = technology, title = title, h2=h2 )
