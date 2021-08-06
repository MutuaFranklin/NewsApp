from flask import render_template,request,redirect,url_for
from app import app
# from .models import articlesource
from .requests import article_categories, get_news_articles, search_article


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


@app.route('/sources')
def sources():
    '''
    Sources function to display available category sources

    '''
    general_categories = article_categories('general')
    entertainment_categories = article_categories('entertainment')
    technology_categories = article_categories('technology')



    # title = f'search results for {article_title}'
    return render_template('sources.html', general = general_categories, entertainment = entertainment_categories, technology = technology_categories )

