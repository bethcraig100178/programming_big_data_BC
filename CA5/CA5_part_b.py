
#Beth Craig
#Student Number 10331736

class Calculator(object):  #set up calculator class

    def __init__(self):
        self.version = 'version1.0'

    def add (self, first, second):
        return map(lambda x,y: round(x+y, 9), first, second)
        
    def subtract (self, first, second):
        return map(lambda x,y: round(x-y, 9), first, second)
        
    def multiply (self, first, second):
        return map(lambda x,y: round(x*y, 9), first, second)
        
    def divide (self, first, second):
        return map(lambda x,y: 'undefined' if y ==0 else round(float(x)/y, 9), first, second) #guard against zero division
        
    def xtothepowerofy(self, first, second): 
        return map(lambda x,y: round(x**y, 9), first, second)
                
    def square(self, values): 
        return map(lambda x: round(x*x, 9), values)
        
    def cube(self, values): #7 cube
        return map(lambda x: round (x*x*x, 9), values)
        

    def inverse(self, values): #8
        return map(lambda x: 'undefined' if x == 0 else round(1/float(x), 9), values) #guard against zero division
       
      
    def factorialBC(self, values): 
        valid = filter(lambda x: x >= 0 and x < 69 and x%1 == 0, values) # get rid of invalid input (numbers less than 0, greater than 69 and non-integers) # use of filter function
        invalid = [x for x in values if x not in valid]
        print 'invalid entries', invalid #print invalid entries so the user knows what was filtered out
        return map(lambda x: 1 if x == 0 else (reduce(lambda a, b: a*b, range(1, x+1))), valid) #use of reduce function

        
    def DMS(self, values):#convert degress in decimal format to degrees, minutes and seconds
        degrees = [int(x) for x in values] # use of list comprehension
        minutes_float = [60*(float(x) - int(x)) for x in values] #multiply float part of degrees by 60 to get minutes
        minutes = [int(x) for x in minutes_float]
        seconds = [round(60*(float(x) - int(x)), 4) for x in minutes_float] #multiply float part of minutes by 60 to get seconds
        return map(lambda a, b, c: (str(a) + ' deg ' + str(b) + " min " + str(c) + ' sec'), degrees, minutes, seconds)
        
        
    def zscore(self, values):
        mean = sum(values)/len(values) #calculate mean of the numbers in the list
        std = sum(map(lambda x: ((x - mean)**2), values))/len(values) #calculate the standard deviation of the numbers in the list. sums of squares divided by n
        return map(lambda x: round((x-mean)/std, 9), values) #calculate z-score as number - mean, divided by standard deviation
 

#Some calls to check functionality  
trial = Calculator()
q = [0, 1,-2,3.333333333333333333333333333333333333333] #uses 0, positive and negative numbers and checks for rounding
p = [3, 4,5,6]
r = [0,1,5.5, 7, 70] #for factorial to check for invalid 
s = [10.623, 70.0, -30.56] #for converting dregree to degrees, minutes and seconds

print 'add', trial.add(q, p)
print 'subtract', trial.subtract(q, p)
print 'multiply', trial.multiply(q, p)
print 'divide', trial.divide(p, q)
print 'xtothepowerofy', trial.xtothepowerofy(p, q)
print 'square', trial.square(q)
print 'cube', trial.cube(q)
print 'inverse' ,trial.inverse(q)
print 'factorialBC', trial.factorialBC(r)
print 'DMS', trial.DMS(s)
print 'z-score', trial.zscore(s)
