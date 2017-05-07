
import unittest
from CA4 import *

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.trial = Mine_for_Commits(file)
        self.trial.add_commits()
        self.trial.commits_per_author()
        self.trial.files_per_author()
        self.trial.amd_per_author()
        self.trial.unique_days_commit()
        self.trial.dayOfTheWeek_per_author()
        self.trial.month_per_author()
        
    
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.trial.data))

    def test_number_of_commits(self):
        self.assertEqual(422, len(self.trial.commits))

    def test_first_commit(self):
        self.assertEqual('Thomas', self.trial.commits[0].author)
        self.assertEqual('r1551925', self.trial.commits[0].revision)
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', self.trial.commits[0].date)
        self.assertEqual('Fri', self.trial.commits[0].dayOfTheWeek)
        self.assertEqual('Nov', self.trial.commits[0].month)
        self.assertEqual(1, self.trial.commits[0].comment_line_count)
        self.assertEqual(['Changed paths:', 'M /cloud/personal/client-international/android/branches/android-15.2-solutions/settings.gradle'], self.trial.commits[2].changes) 
        self.assertEqual(['Renamed folder to the correct name'], self.trial.commits[0].comment)
        self.assertEqual(4, self.trial.commits[0].numberfiles) 
        
    def test_commits_per_author(self):
        self.assertEqual(26, self.trial.authors['Vincent'])
        self.assertEqual(422, sum(self.trial.authors.values()))
        
    def test_files_per_author(self):
        self.assertEqual(337, self.trial.numberfiles['Vincent'])
        self.assertEqual(3011, sum(self.trial.numberfiles.values()))
         
    def test_amd(self):
        self.assertEqual(260, self.trial.numberA['Vincent'])
        self.assertEqual(45, self.trial.numberM['Vincent'])
        self.assertEqual(32, self.trial.numberD['Vincent'])        
        self.assertEqual(3009, (sum(self.trial.numberA.values())+sum(self.trial.numberM.values())+sum(self.trial.numberD.values())))#two R files so 3011-2 expected
        
        
        
     
if __name__ == '__main__':
    unittest.main()
