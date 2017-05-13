def add (first, second):
    return map(lambda x,y: round(x+y, 9), first, second)
    
def subtract (first, second):
    return map(lambda x,y: round(x-y, 9), first, second)
    
def multiply (first, second):
    return map(lambda x,y: round(x*y, 9), first, second)
    
def divide (first, second):
    return map(lambda x,y: round(float(x)/y, 9), first, second)
    
def xtothepowerofy(first, second): 
    return map(lambda x,y: round(x**y, 9), first, second)
    
      
def square(values): 
    return map(lambda x: round(x*x, 9), values)
    
def cube(values): #7 cube
    return map(lambda x: round (x*x*x, 9), values)
    

def inverse(values): #8
    return map(lambda x: 'undefined' if x == 0 else round(1/float(x), 9), values)
   
   
    
    
def zscore(values):
    mean = sum(values)/len(values)
    std = sum(map(lambda x: ((x - mean)**2), values))/len(values)
    return map(lambda x: round((x-mean)/std, 9), values)
    

    
def factorialBC(values): 
    valid = filter(lambda x: x >=1 and x < 69, values) # get rid of invalid input
    invalid = [x for x in values if x not in valid]
    print 'invalid entries', invalid
    return map(lambda x: 1 if x == 1 else (reduce(lambda a, b: a*b, range(1, x+1))), valid) #get factorial to work
    
def DMS(values):
    degrees = [int(x) for x in values]
    minutes_float = [60*(float(x) - int(x)) for x in values]
    minutes = [int(x) for x in minutes_float]
    seconds = [round(60*(float(x) - int(x)), 4) for x in minutes_float]
    return map(lambda a, b, c: (str(a) + ' deg ' + str(b) + " min " + str(c) + ' sec'), degrees, minutes, seconds)
    
    
def zscore(values):
    mean = sum(values)/len(values)
    std = sum(map(lambda x: ((x - mean)**2), values))/len(values)
    return map(lambda x: round((x-mean)/std, 9), values)
   


