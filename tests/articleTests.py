import unittest
from app.models import Articles, Source



# Article = articles.Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Football','https://media.istockphoto.com/photos/nairobi-downtown-capital-city-of-kenya-picture-id639495906?k=6&m=639495906&s=612x612&w=0&h=JBhS5G5WeI1LEChjGUuga_smUsW8adTmZ0TQ4JmTqN4=','Premier begins soon as the team prepare..','Fabrizio Romano', 'https://hackaday.com/2021/08/06/this-week-in-security-insecure-chargers-request-forgeries-and-kernel-security/', '12/8/2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))





class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('CNN','CNN-News','CNN an American based Media organization','"https://abcnews.go.com"', 'general"', 'en')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


    
    


# if __name__ == '__main__':
#     unittest.main()