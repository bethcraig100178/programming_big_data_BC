

#CA4
#Name Beth Craig
#Student Number 10331736


#create alias for the file

file = 'changes_python.txt'

class Commit(object): #create a class for commits

    '''CLass Commit'''
    
    def __init__(self, revision = None, author = None, date = None, dayOfTheWeek = None, month = None, comment_line_count = None, changes = None, comment = None, numberfiles = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.dayOfTheWeek = dayOfTheWeek
        self.month = month
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.numberfiles = numberfiles

class Mine_for_Commits(object): #create a class to store output from mining the file

    ''' Class to store objects resulting from mining a file of commits'''
    
    def __init__(self, file):   
        self.file = file 
        self.data = [line.strip() for line in open(file, 'r')] # import the information from file, strip the white space and store each line as an object in a list
        self.commits = [] #empty list to sotre commits in
        self.authors = {} # the following are all empty dictionaires to store output of functions
        self.numberfiles = {}
        self.numberAM = {}
        self.numberA ={}
        self.numberM = {}
        self.numberD = {}
        self.numberR = {}
        self.numberAM124 = {}
        self.numberA124 ={}
        self.numberM124 = {}
        self.numberD124 = {}
        self.numberR124 = {}
        self.days_atleastone_commit = {}
        self.Jul = {}
        self.Aug = {}
        self.Sep = {}
        self.Oct = {}
        self.Nov = {}
        self.Mon = {}
        self.Tue = {}
        self.Wed = {}
        self.Thu = {}
        self.Fri = {}
        
        
        
    def add_commits(self): # pasrse through the file and add the commits as objects
        sep = 72*'-' #create alias for the seperator between instances of commit
        current_commits = None
        index = 0
        while True:
            try:
                current_commit = Commit() #initiate a new object
                details = self.data[index+1].split('|') #split the first line of the commit by the | and store output as strings in a list
                current_commit.revision = details[0].strip() #isolate and store the relevent string characters for each element of the commit
                current_commit.author = details[1].strip() 
                current_commit.date = details[2].strip()
                current_commit.dayOfTheWeek = current_commit.date.split()[3][1:4]
                current_commit.month = current_commit.date.split()[5]
                current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
                current_commit.changes = self.data[index+2:self.data.index('', index+1)]
                current_commit.numberfiles = len(self.data[index+3:self.data.index('', index+1)])
                index = self.data.index(sep, index + 1) # move the index to the beginning of the next commit
                current_commit.comment = self.data[index - current_commit.comment_line_count:index]#easiest way to get to the comment line is to count back from the next commit 
                self.commits.append(current_commit) #add the commit object that has just been created to the list of commits
            except IndexError:
                break
        
    
    
    def commits_per_author(self):
        #Create dictionary to count number of commits per author
        for i in range(len(self.commits)):
            self.authors[self.commits[i].author] = self.authors.get(self.commits[i].author, 0) + 1
        
            
    def files_per_author(self):
        #Create dictionary to count number of files per author
        for i in range(len(self.commits)):
            self.numberfiles[self.commits[i].author] = self.numberfiles.get(self.commits[i].author, 0) + self.commits[i].numberfiles 
        
 ######################################################################################################################################################################################
 
 #                       Metric 1           
 
 ######################################################################################################################################################################################
    
    def month_per_author(self):
        #Metric 1 Count number of commits by author and month
        # iterate through commits to find Jul, Aug etc 
        for i in range(len(self.commits)):
            if self.commits[i].month == 'Jul':
                self.Jul[self.commits[i].author] = self.Jul.get(self.commits[i].author, 0) + 1 #where month = July, add a count to the key of the author, or create a key for the author if one does not yet exist
            elif self.commits[i].month == 'Aug':
                self.Aug[self.commits[i].author] = self.Aug.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].month == 'Sep':
                self.Sep[self.commits[i].author] = self.Sep.get(self.commits[i].author, 0) + 1    
            elif self.commits[i].month == 'Oct':
                self.Oct[self.commits[i].author] = self.Oct.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].month == 'Nov':
                self.Nov[self.commits[i].author] = self.Nov.get(self.commits[i].author, 0) + 1 
                
                
                
#######################################################################################################################################################################################


#                       Metric 2

#######################################################################################################################################################################################            
                
    def unique_days_commit(self):
        #Metric 2 Count number of unique days at least one commit was made on
        authordate = [] #set up empty list to store unique tuples of author and date
        for i in range(len(self.commits)):
            if (self.commits[i].author, self.commits[i].date.split()[0]) not in authordate: #check author, date tuple does not already exist
                authordate.append((self.commits[i].author, self.commits[i].date.split()[0])) #add the author,date tuple to the list if it doesnt exist
                self.days_atleastone_commit[self.commits[i].author] = self.days_atleastone_commit.get(self.commits[i].author, 0) + 1 #add a count to the author or create the author key if it does not already exist
                
                
                
                
                
    
#######################################################################################################################################################################################


#                       Metric 3

#######################################################################################################################################################################################      
    
    
    def amdr_per_author(self):        
        #Create dictionary to count number of A, M, D and R per authors for all 422 commits
        for i in range(len(self.commits)):
            for file in range(self.commits[i].numberfiles+1):
                if self.commits[i].changes[file].split()[0] == 'A':
                    self.numberA[self.commits[i].author] = self.numberA.get(self.commits[i].author, 0) + 1 #add a count to the author or create the author key if it does not already exist
                elif self.commits[i].changes[file].split()[0] == 'M':
                    self.numberM[self.commits[i].author] = self.numberM.get(self.commits[i].author, 0) + 1    
                elif self.commits[i].changes[file].split()[0] == 'D':
                    self.numberD[self.commits[i].author] = self.numberD.get(self.commits[i].author, 0) + 1  
                elif self.commits[i].changes[file].split()[0] == 'R':
                    self.numberR[self.commits[i].author] = self.numberR.get(self.commits[i].author, 0) + 1  
                    
                    
    def am_per_author(self):        
        #Metric 3 Create dictionary to count number of A and M per author for all 422 commits
        for i in range(len(self.commits)):
            for file in range(self.commits[i].numberfiles+1):
                if self.commits[i].changes[file].split()[0] == 'A' or self.commits[i].changes[file].split()[0] == 'M' :
                    self.numberAM[self.commits[i].author] = self.numberAM.get(self.commits[i].author, 0) + 1 #add a count to the author or create the author key if it does not already exist
                
    
    def find_r1537319(self):        
    #Metric 3 find the i for Vincents 1st commit
        for i in range(len(self.commits)):
            if self.commits[i].revision == 'r1537319': #revision number of Vincent's first commit identified from the .txt file
                print i 
                
                  
   
    def am_per_author_from_r1537319(self): #Metric 3 Create dictionary to count number of A and M per author from Vincent's 1st commit to the  
        for i in range(0,125): #range so that only commits dated after Vincents first commit (124) are parsed. commit[0] is the latest date, commit[422] is earliest
            for file in range(self.commits[i].numberfiles+1):
                if self.commits[i].changes[file].split()[0] == 'A' or self.commits[i].changes[file].split()[0] == 'M' : 
                    self.numberAM124[self.commits[i].author] = self.numberAM124.get(self.commits[i].author, 0) + 1 #add a count to the author or create the author key if it does not already exist
        
#################################################################################################################################################################################      

#                            Other code not used in the end

################################################################################################################################################################################



    def dayOfTheWeek_per_author(self):
        #Count number of commits by author and day of the week - not used in the end
        # iterate through commits to find Mon, Tue etc
        for i in range(len(self.commits)):
            if self.commits[i].dayOfTheWeek == 'Mon':
               self.Mon[self.commits[i].author] = self.Mon.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Tue':
               self.Tue[self.commits[i].author] = self.Tue.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Wed':
                self.Wed[self.commits[i].author] = self.Wed.get(self.commits[i].author, 0) + 1    
            elif self.commits[i].dayOfTheWeek == 'Thu':
                self.Thu[self.commits[i].author] = self.Thu.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Fri':
                self.Fri[self.commits[i].author] = self.Fri.get(self.commits[i].author, 0) + 1 
        
        
#################################################################################################################################################################################   


