

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
                current_commit.month = current_commit.date.split()[5]
                current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
                current_commit.changes = self.data[index+2:self.data.index('', index+1)]
                current_commit.numberfiles = len(self.data[index+3:self.data.index('', index+1)])
                index = self.data.index(sep, index + 1)
                current_commit.comment = self.data[index - current_commit.comment_line_count:index]
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
        
    def month_per_author(self):
        #Statistic 4 Count number of commits by author and day of the week
        totalByMonth = 0
        totalJul = 0
        totalAug = 0
        totalSep = 0
        totalOct = 0
        totalNov = 0
        # iterate through commits to find Jul, Aug etc
        for i in range(len(self.commits)):
            if self.commits[i].month == 'Jul':
                totalJul = totalJul + 1
                self.Jul[self.commits[i].author] = self.Jul.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].month == 'Aug':
                totalAug = totalAug + 1
                self.Aug[self.commits[i].author] = self.Aug.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].month == 'Sep':
                totalSep = totalSep + 1
                self.Sep[self.commits[i].author] = self.Sep.get(self.commits[i].author, 0) + 1    
            elif self.commits[i].month == 'Oct':
                totalOct = totalOct + 1
                self.Oct[self.commits[i].author] = self.Oct.get(self.commits[i].author, 0) + 1 
            elif self.commits[i].month == 'Nov':
                totalNov = totalNov + 1
                self.Nov[self.commits[i].author] = self.Nov.get(self.commits[i].author, 0) + 1 
        totalByMonth =  totalJul + totalAug + totalSep + totalOct + totalNov  #sanity check
        
        print 'total commits by month', totalByMonth 


 
        
        



