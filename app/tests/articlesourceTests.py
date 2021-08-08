import unittest
from models import articlesource


Source = articlesource.Source

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


    


if __name__ == '__main__':
    unittest.main()