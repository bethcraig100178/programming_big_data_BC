from calculator import *

def done(user_input): # quit programme if user enters 'Done'
    user_input = user_input.lower()
    if user_input == 'done':
        print 'You have now quit the programme'
        quit()
        
        
def showInstructions(): # quit programme if user enters 'Done'
    print '1. Add 2 numbers\n2. Subtract second number entered from the first number entered\n3. Multiply 2 numbers together'
    print '4. Divide the 1st number entered by the 2nd number entered\n5. Raise the 1st number entered to the power of the 2nd number entered'
    print '6. Square a number\n7. Cube a number\n8. Get the inverse of a number'
    print '9. Convert degrees in decimal format to degrees, minutes and seconds'
    print '10. Factorial of integers between 1 and 69\n'
        
def getUserInputFloat(str): #get user input a number and convert to a float
    while True:
        user_input = raw_input(str).lower() #input
        done(user_input)
        if user_input == 'show': 
            showInstructions()
            continue
        try:
            number = float(user_input)
        except:
            print 'A numerical value is required. Try again.\n'
            continue
        break
    return number
    
def getUserInputInt(str): #getuserinput and convert to an integer
    while True:
        user_input = raw_input(str).lower() #input
        done(user_input)
        if user_input == 'show': 
            showInstructions()
            continue
        try:
            number = int(user_input)
        except:
            print 'An integer value is required. Try again.\n'
            continue
        break
    return number



#User defined functions

#random functions
def userInstructions():
    print '-----------------------------------------------------------------------------'
    print 'User Instructions\n'
    print 'This programme allows you to perform 10 functions found on a scientific calculator\n'
    print 'To choose a function you enter the corresponding number (between 1 and 10) from the following list and follow on screen instructions\n'
    print '1. Add 2 numbers\n2. Subtract second number entered from the first number entered\n3. Multiply 2 numbers together'
    print '4. Divide the 1st number entered by the 2nd number entered\n5. Raise the 1st number entered to the power of the 2nd number entered'
    print '6. Square a number\n7. Cube a number\n8. Get the inverse of a number'
    print '9. Convert degrees in decimal format to degrees, minutes and seconds'
    print '10. Factorial of integers between 1 and 69'
    print "At anytime you may enter 'Done' to quit the programme or 'Show' to print the list of functions\n"
    print '-----------------------------------------------------------------------------'

#Body of Code to Operate the Calculator 

myCalculator = Calculator() 
userInstructions() # print instructions to screen

while True: # getting valid input
    while True: 
        choice = raw_input('Enter your choice of function\n').lower() # user chooses an operation from a defined list
        done(choice)
        if choice == 'show': 
            showInstructions()
            continue
        try:
            choice = int(choice)
        except:
            print 'Invalid input. A number between 1 and 10 is required. Try again\n'
            continue
        if choice > 0 and choice <= 5: # 2 numbers required for these functions
            first = getUserInputFloat('Enter the first number\n')
            second = getUserInputFloat('Enter the second number\n')
            break
        elif choice > 5 and choice <=9: # only one number required for these functions
            number = getUserInputFloat('Enter the number\n')
            break
        elif choice == 10: # only integers between 1 and 69 allowed
            while True:
                print 'Only possible for positive integers between 1 and 69\n'
                number = getUserInputInt('Enter a positive integer between 1 and 69\n') #input
                if number <= 69 and number >= 0: break
                else: 
                    print 'Invalid input. Try again.'
                    continue
            break
        else:
            print 'Invlaid input. A number between 1 and 10 is required. Try again\n'
            continue
        
    if choice == 1: #computation
        output = myCalculator.add(first, second)
    elif choice == 2:
        output = myCalculator.subtract(first, second)
    elif choice == 3:
        output = myCalculator.multiply(first, second)  
    elif choice == 4:
        output = myCalculator.divide(first, second)
    elif choice == 5:
        output = myCalculator.xtothepowerofy(first, second) 
    elif choice == 6:
        output = myCalculator.square(number) 
    elif choice == 7:
        output = myCalculator.cube(number)   
    elif choice == 8:
        output = myCalculator.inverse(number) 
    elif choice == 9:
        output = myCalculator.convertdegreestoDMS(number) 
    elif choice == 10:
        output = myCalculator.factorial(number) 
        
    print 'Answer: {0}.\n' .format(output)
    while True: #looping if user wants to carry out further calculations
        user_input = raw_input("Hit enter to choose another function or enter 'Done' to quit the programme\n").lower()
        done(user_input)
        if user_input == 'show': 
            showInstructions()
            continue
        elif len(user_input) < 1: break
        else:
            print "Invalid input.\n"
            continue
    
    
    
   
    
    




        
