from flask import render_template,request,redirect,url_for
from app import app
# from .models import articlesource
from .requests import article_by_category, article_categories, get_news_articles, search_article , article_by_source


# Source = articlesource.Source


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    topHeadline = get_news_articles()

    title = 'NewsApp'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_title=search_article))
    else:
        return render_template('index.html', title = title, headline = topHeadline)


@app.route('/categories')
def categories():
    '''
    Sources function to display available category sources

    '''
    general_categories = article_categories('general')
    entertainment_categories = article_categories('entertainment')
    technology_categories = article_categories('technology')



    # title = f'search results for {article_title}'
    return render_template('sourcesbycategories.html', general = general_categories, entertainment = entertainment_categories, technology = technology_categories )


@app.route('/bbc-news')
def bbc_news():
    '''
    Sources function to display available  sources articles

    '''
    bbc = article_by_source('bbc-news')

   


    # title = f'search results for {article_title}'
    return render_template('sources.html',  bbc = bbc )


@app.route('/cnn-news')
def cnn_news():
    '''
    Sources function to display available  sources articles

    '''

    cnn = article_by_source('cnn-news')

    # title = f'search results for {article_title}'
    return render_template('sources.html',  cnn = cnn )


@app.route('/fox-news')
def fox_news():
    '''
    Sources function to display available  sources articles

    '''

    fox = article_by_source('fox-news')

    # title = f'search results for {article_title}'
    return render_template('sources.html',  fox = fox )



@app.route('/abc-news')
def abc_news():
    '''
    Sources function to display available  sources articles

    '''

    abc = article_by_source('abc-news')

    # title = f'search results for {article_title}'
    return render_template('sources.html',  abc = abc )



@app.route('/mtv-news')
def mtv_news():
    '''
    Sources function to display available  sources articles

    '''

    mtv = article_by_source('mtv-news')

    # title = f'search results for {article_title}'
    return render_template('sources.html',  mtv = mtv )


@app.route('/general')
def general():
    '''
    Sources function to filter general articles

    '''

    general = article_by_category('general')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  general = general )


@app.route('/entertainment')
def entertainment():
    '''
    Sources function to filter articles based on entertainment

    '''

    entertainment = article_by_category('entertainment')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  entertainment = entertainment )


@app.route('/health')
def health():
    '''
    Sources function to filter articles based on health

    '''

    health = article_by_category('health')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  health = health )

@app.route('/science')
def science():
    '''
    Sources function to filter articles based on science

    '''

    science = article_by_category('science')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  science = science )

@app.route('/business')
def business():
    '''
    Sources function to filter articles based on health

    '''

    business = article_by_category('business')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  business = business )



@app.route('/technology')
def technology():
    '''
    Sources function to filter articles based on health

    '''

    technology = article_by_category('technology')

    # title = f'search results for {article_title}'
    return render_template('categoryArticles.html',  technology = technology )
