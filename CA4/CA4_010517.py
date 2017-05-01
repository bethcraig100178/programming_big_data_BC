

#CA4
#Name Beth Craig
#Student Number 10331736


changes_file = 'changes_python.log' #create alias for file name
    
data = [line.strip() for line in open(changes_file, 'r')] # import the information from changes_file, strip the white space and store each line as an object in a list

print len(data) #check import is correct

sep = 72*'-' #create alias for the seperator between instances of commit

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

   
            

commits = []
current_commits = None
index = 0

#Create a list of the commits  ie each element in the list commits is an object of class Commit
#search for seperator
#read line for revision, author, date, comment_line_count etc
#get next commit

while True:
    try:
        current_commit = Commit()
        details = data[index+1].split('|')
        #print details
        current_commit.revision = details[0].strip()
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.dayOfTheWeek = current_commit.date.split()[3][1:4]
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('', index+1)]
        current_commit.numberfiles = len(data[index+3:data.index('', index+1)])
        current_commit.comment = data[index - current_commit.comment_line_count:index]
        index = data.index(sep, index + 1)
        commits.append(current_commit)
    except IndexError:
        break
        
print(len(commits)) #sanity check to make sure file has been read correctly. 

#Create dictionary to count number of commits per author
authors = {}
for i in range(len(commits)):
    authors[commits[i].author] = authors.get(commits[i].author, 0) + 1
    
#Statistic 1 Create dictionary to count number of files per author
numberfiles = {}
for i in range(len(commits)):
    numberfiles[commits[i].author] = numberfiles.get(commits[i].author, 0) + commits[i].numberfiles
    
#Statistic 2 Create dictionary to count number of A, M and D per authors
numberA ={}
numberM = {}
numberD = {}
total = 0
totalA = 0
totalM = 0
totalD = 0


for i in range(len(commits)):
    for file in range(commits[i].numberfiles+1):
        if commits[i].changes[file].split()[0] == 'A':
            totalA = totalA + 1
            numberA[commits[i].author] = numberA.get(commits[i].author, 0) + 1
        elif commits[i].changes[file].split()[0] == 'M':
            totalM = totalM + 1
            numberM[commits[i].author] = numberM.get(commits[i].author, 0) + 1    
        elif commits[i].changes[file].split()[0] == 'D':
            totalD = totalD + 1
            numberD[commits[i].author] = numberD.get(commits[i].author, 0) + 1     

total = totalA + totalM+ totalD   #sanity check, should be equal to number of files         
      
print total, totalA, totalM, totalD
print 'Number A', numberA
print 'Number M', numberM
print 'NUmber D', numberD
print 'Number commits:\n', authors
print 'Number of files:\n', numberfiles



#Statistic 3 Count number of unique days at least one commit was made on
daysByAuthor = {}
authordate = []
for i in range(len(commits)):
    if (commits[i].author, commits[i].date.split()[0]) not in authordate:
        authordate.append((commits[i].author, commits[i].date.split()[0]))
        daysByAuthor[commits[i].author] = daysByAuthor.get(commits[i].author, 0) + 1 
        
        
print 'Number of unique days at least one commit was made:\n', daysByAuthor


#Statistic 4 Count number of commits by author and day of the week

dayOfTheWeek = {}
Mon = {}
Tue = {}
Wed = {}
Thu = {}
Fri = {}
totalByDay = 0
totalMon = 0
totalTue = 0
totalWed = 0
totalThu = 0
totalFri = 0


for i in range(len(commits)):
    if commits[i].dayOfTheWeek == 'Mon':
        totalMon = totalMon + 1
        Mon[commits[i].author] = Mon.get(commits[i].author, 0) + 1 
    elif commits[i].dayOfTheWeek == 'Tue':
        totalTue = totalTue + 1
        Tue[commits[i].author] = Tue.get(commits[i].author, 0) + 1 
    elif commits[i].dayOfTheWeek == 'Wed':
        totalWed = totalWed + 1
        Wed[commits[i].author] = Wed.get(commits[i].author, 0) + 1    
    elif commits[i].dayOfTheWeek == 'Thu':
        totalThu = totalThu + 1
        Thu[commits[i].author] = Thu.get(commits[i].author, 0) + 1 
    elif commits[i].dayOfTheWeek == 'Fri':
        totalFri = totalFri + 1
        Fri[commits[i].author] = Fri.get(commits[i].author, 0) + 1 
totalByDay =  totalMon + totalTue+totalWed+totalThu+totalFri  #sanity check
print 'Monday', Mon
print 'Tuesday', Tue
print 'Wednesday', Wed
print 'Thursday', Thu
print 'Friday', Fri


print 'total', totalByDay
