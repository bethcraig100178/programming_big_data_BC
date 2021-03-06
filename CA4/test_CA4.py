
import unittest
from CA4 import *

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.trial = Mine_for_Commits(file) # set up the object
        self.trial.add_commits() #parse the data and add each of the 422 commits as a list of objects
        self.trial.commits_per_author() #parse each of 422 commits to get the commits per author
        self.trial.files_per_author() # parse 422 commits for #files per author
        self.trial.amdr_per_author() #parse 422 commits for # A, M and D files per author
        self.trial.am_per_author() #Metric 3 parse 422 commits for # A and M files per author
        self.trial.am_per_author_from_r1537319() # Metric 3 parse commits from Vincents 1st (i = 124) until the end (i = 0) for A and M files
        self.trial.unique_days_commit() #Metric 2 parse 422 commits for unique author, date combinations to get # days each author made at least 1 commit
        self.trial.dayOfTheWeek_per_author() #parse 422 commits for #commits made each day of the week per author
        self.trial.month_per_author() # Metric 1 parse 422 commits for # commits each month per author
        
        
################################################################################################################################################################################################### 

#                Test the file loaded correctly 

###################################################################################################################################################################################################       
    
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.trial.data)) #overall check to make sure data loaded correctly

    def test_number_of_commits(self):
        self.assertEqual(422, len(self.trial.commits)) # checking there are the right number of commit objects

    def test_first_commit(self): # test that each element of the first commit was parsed correctly
        self.assertEqual('Thomas', self.trial.commits[0].author)
        self.assertEqual('r1551925', self.trial.commits[0].revision)
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', self.trial.commits[0].date)
        self.assertEqual('Fri', self.trial.commits[0].dayOfTheWeek)
        self.assertEqual('Nov', self.trial.commits[0].month)
        self.assertEqual(1, self.trial.commits[0].comment_line_count)
        self.assertEqual(['Changed paths:', 'M /cloud/personal/client-international/android/branches/android-15.2-solutions/settings.gradle'], self.trial.commits[2].changes) 
        self.assertEqual(['Renamed folder to the correct name'], self.trial.commits[0].comment)
        self.assertEqual(4, self.trial.commits[0].numberfiles) 
        
    def test_commits_per_author(self): #test the number of commits per author
        self.assertEqual(26, self.trial.authors['Vincent']) #test one author 
        self.assertEqual(422, sum(self.trial.authors.values()))#reconciliation
        
    def test_files_per_author(self): #test the number of files per author
        self.assertEqual(337, self.trial.numberfiles['Vincent']) # test one author
        self.assertEqual(3011, sum(self.trial.numberfiles.values())) #reconciliation
        
        
################################################################################################################################################################################################### 

#             Test code for Metric 1

###################################################################################################################################################################################################  
         
    def test_month(self): # Metric 1 test the number of commits per month by author
        self.assertEqual(24, self.trial.Nov['Vincent'])#test one author
        self.assertEqual(422, (sum(self.trial.Jul.values())+sum(self.trial.Aug.values())+sum(self.trial.Sep.values())+sum(self.trial.Oct.values())+sum(self.trial.Nov.values()))) # reconciliation 
        
        
################################################################################################################################################################################################### 

#             Test code for Metric 2

###################################################################################################################################################################################################  
        
    def test_unique_days(self): #Metric 2 test the number of unique author date combinations
        self.assertEqual(10, self.trial.days_atleastone_commit['Vincent']) #test one author
        self.assertEqual(135, sum(self.trial.days_atleastone_commit.values())) # reconciliation there are 135 unique combinations of author and date
        
################################################################################################################################################################################################### 

#               Test code for Metric 3

###################################################################################################################################################################################################  
        
    def test_amd(self): #test the number of A, M and D files
        self.assertEqual(260, self.trial.numberA['Vincent']) # note 2 'R' files as well as the A, M and D files
        self.assertEqual(45, self.trial.numberM['Vincent']) #test one author for M
        self.assertEqual(32, self.trial.numberD['Vincent']) # test one author for D       
        self.assertEqual(3009, (sum(self.trial.numberA.values())+sum(self.trial.numberM.values())+sum(self.trial.numberD.values())))#reconciliation two R files so 3011-2 expected
        
    def test_am_per_author(self): # Metric 3 test number of files added or modified 
        self.assertEqual(305, self.trial.numberAM['Vincent'])
        self.assertEqual(2242, sum(self.trial.numberAM.values()))#reconciliation
        
    def test_am_per_author_from_r1537319(self): #Metric 3 test number of files added or modified from date of Vincents 1st commit
        self.assertEqual(305, self.trial.numberAM124['Vincent'])
        self.assertEqual(907, sum(self.trial.numberAM124.values()))
        


################################################################################################################################################################################################### 

#               Test code not used in the end

###################################################################################################################################################################################################


    def test_dayoftheweek(self): #test the number of commits per day of the week by author, not used in the end
        self.assertEqual(1, self.trial.Mon['Vincent']) #test one author
        self.assertEqual(422, (sum(self.trial.Mon.values())+sum(self.trial.Tue.values())+sum(self.trial.Wed.values())+sum(self.trial.Thu.values())+sum(self.trial.Fri.values()))) # reconciliation 
        
  
        
        
        
        
        
     
if __name__ == '__main__':
    unittest.main()
