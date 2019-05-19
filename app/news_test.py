import unittest
from models import news
News= news.News
class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of our News class
    """
    def setUp(self):
        """
        A setUp method to run before every test
        """
        self.new_news =News(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__=='__main__'
    unittest.main()