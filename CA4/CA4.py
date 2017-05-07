

#CA4
#Name Beth Craig
#Student Number 10331736


#create alias for the file

file = 'changes_python.log'

class Commit(object): #create a class for commits

    '''CLass Commit'''
    
    def __init__(self, revision = None, author = None, date = None, dayOfTheWeek = None, comment_line_count = None, changes = None, comment = None, numberfiles = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.dayOfTheWeek = dayOfTheWeek
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.numberfiles = numberfiles

class MineForObjects(object): #create a class to store output from mining the file

    ''' Class to store objects resulting from mining a file'''
    
    def __init__(self, file):   
        self.file = file #create alias for file name
        self.data = [line.strip() for line in open(file, 'r')] # import the information from file, strip the white space and store each line as an object in a list
        self.commits = []
        self.authors = {}
        self.numberfiles = {}
        self.numberA ={}
        self.numberM = {}
        self.numberD = {}
        self.numberR = {}
        self.days_atleastone_commit = {}
        self.Mon = {}
        self.Tue = {}
        self.Wed = {}
        self.Thu = {}
        self.Fri = {}
        
        
        
    def add_commits(self):
        sep = 72*'-' #create alias for the seperator between instances of commit
        current_commits = None
        index = 0
        while True:
            try:
                current_commit = Commit()
                details = self.data[index+1].split('|')
                current_commit.revision = details[0].strip()
                current_commit.author = details[1].strip()
                current_commit.date = details[2].strip()
                current_commit.dayOfTheWeek = current_commit.date.split()[3][1:4]
                current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
                current_commit.changes = self.data[index+2:self.data.index('', index+1)]
                current_commit.numberfiles = len(self.data[index+3:self.data.index('', index+1)])
                current_commit.comment = self.data[index - current_commit.comment_line_count:index]
                index = self.data.index(sep, index + 1)
                self.commits.append(current_commit)
            except IndexError:
                break
        
       
    def commits_per_author(self):
        #Create dictionary to count number of commits per author
        for i in range(len(self.commits)):
            self.authors[self.commits[i].author] = self.authors.get(self.commits[i].author, 0) + 1
        
            
    def files_per_author(self):
        #Statistic 1 Create dictionary to count number of files per author
        for i in range(len(self.commits)):
            self.numberfiles[self.commits[i].author] = self.numberfiles.get(self.commits[i].author, 0) + self.commits[i].numberfiles
        
            
    def amd_per_author(self):        
        #Statistic 2 Create dictionary to count number of A, M and D per authors
        total = 0
        totalA = 0
        totalM = 0
        totalD = 0
        totalR = 0

        for i in range(len(self.commits)):
            for file in range(self.commits[i].numberfiles+1):
                if self.commits[i].changes[file].split()[0] == 'A':
                    totalA = totalA + 1
                    self.numberA[self.commits[i].author] = self.numberA.get(self.commits[i].author, 0) + 1
                elif self.commits[i].changes[file].split()[0] == 'M':
                    totalM = totalM + 1
                    self.numberM[self.commits[i].author] = self.numberM.get(self.commits[i].author, 0) + 1    
                elif self.commits[i].changes[file].split()[0] == 'D':
                    totalD = totalD + 1
                    self.numberD[self.commits[i].author] = self.numberD.get(self.commits[i].author, 0) + 1  
                elif self.commits[i].changes[file].split()[0] == 'R':
                    totalR = totalR + 1
                    self.numberR[self.commits[i].author] = self.numberR.get(self.commits[i].author, 0) + 1  

        total = totalA + totalM+ totalD + totalR  #sanity check, should be equal to number of files         
        print total, totalA, totalM, totalD, totalR
        
        
    def unique_days_commit(self):
        #Statistic 3 Count number of unique days at least one commit was made on
        authordate = []
        for i in range(len(self.commits)):
            if (self.commits[i].author, self.commits[i].date.split()[0]) not in authordate:
                authordate.append((self.commits[i].author, self.commits[i].date.split()[0]))
                self.days_atleastone_commit[self.commits[i].author] = self.days_atleastone_commit.get(self.commits[i].author, 0) + 1 
       
    def dayOfTheWeek_per_author(self):
        #Statistic 4 Count number of commits by author and day of the week
        totalByDay = 0
        totalMon = 0
        totalTue = 0
        totalWed = 0
        totalThu = 0
        totalFri = 0
        # iterate through commits to find Mon, Tue etc
        for i in range(len(self.commits)):
            if self.commits[i].dayOfTheWeek == 'Mon':
                totalMon = totalMon + 1
                self.Mon[self.commits[i].author] = self.Mon.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Tue':
                totalTue = totalTue + 1
                self.Tue[self.commits[i].author] = self.Tue.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Wed':
                totalWed = totalWed + 1
                self.Wed[self.commits[i].author] = self.Wed.get(self.commits[i].author, 0) + 1    
            elif self.commits[i].dayOfTheWeek == 'Thu':
                totalThu = totalThu + 1
                self.Thu[self.commits[i].author] = self.Thu.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].dayOfTheWeek == 'Fri':
                totalFri = totalFri + 1
                self.Fri[self.commits[i].author] = self.Fri.get(self.commits[i].author, 0) + 1 
        totalByDay =  totalMon + totalTue + totalWed + totalThu + totalFri  #sanity check
        
        print 'total commits by day', totalByDay
        
       
        
trial = MineForObjects(file)
trial.add_commits()
print len(trial.commits)
trial.commits_per_author()
print 'the number of commits per author', trial.authors
trial.files_per_author()
print 'the number of files per authoer', trial.numberfiles
trial.amd_per_author()
print 'the number of adds per author', trial.numberA
print 'the number of deletes per author', trial.numberD
print 'the number of modifies per author', trial.numberM
print 'the number of R per author', trial.numberR
trial.unique_days_commit()
print 'number of days at least one commit was made', trial.days_atleastone_commit
trial.dayOfTheWeek_per_author()
print 'commits on a monday', trial.Mon
print 'commits on a tuesday', trial.Tue
print 'commits on a wed', trial.Wed
print 'commits on a thur', trial.Thu
print 'commits on a fri', trial.Fri


