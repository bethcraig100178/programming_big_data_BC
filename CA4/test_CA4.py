
import unittest
from CA4_010517 import *

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = self.read_data()
        self.commits = self.data.get_Commits() 

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
       
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        self.assertEqual(' ', commits[0]['date'])
        self.assertEqual('', commits[0]['dayOfTheWeek'])
        self.assertEqual(' ', commits[0]['comment_line_count'])
        self.assertEqual(' ', commits[0]['changes']) 
        self.assertEqual(' ', commits[0]['comment'])
        self.assertEqual(' ', commits[0]['numberfies']) 
     
if __name__ == '__main__':
    unittest.main()
