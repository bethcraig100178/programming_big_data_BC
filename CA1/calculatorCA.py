

class Calculator(object):  

    def __init__(self):
        self.version = 'version1.0'
        
# calculator performance functions       
    def add(self, first, second): # 1. adds 2 numbers together
        self.add = round(first + second, 9)
        return self.add
        
    def subtract(self, first, second): # 2. minus 2 numbers 
        return round(first - second, 9)  
        
    def multiply(self, first,second): # 3. multiply 2 numbers 
        return round(first * second, 9)  
        
    def divide(self, first,second): #4. first divided by second
        if second == 0:
            return 'undefined'
        else:
            return round(float(first)/second, 9)

    def xtothepowerofy(self, first, second): #5
        return round(first**second, 9)        
          
    def square(self, number): # 6 square
        return round(number * number, 9)  
        
    def cube(self, number): #7 cube
        return round(number * number * number, 9)  

    def inverse(self, number): #8
       
        if number == 0:
            return 'undefined'
        else:
            return round(1.0/number, 9)


    def convertdegreestoDMS(self, number): #9
        
        degrees = int(number)
        minutes_float = ((number - degrees)*60)
        minutes = int(minutes_float)
        seconds = ((minutes_float - minutes)*60)
        seconds = int(seconds)
        answer = (degrees, minutes, seconds)
        return '{0} degrees, {1} minutes and {2} seconds' .format(answer[0], answer[1], answer[2])       
            
    def factorial(self, number): #10 only positive integer <70
        
        if number < 0 or number > 69:
            return 'invalid'
        elif number == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial = factorial * i
            return factorial
