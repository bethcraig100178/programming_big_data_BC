from calculator import Calculator
import unittest

class MyTest(unittest.TestCase):


        
    def testADD(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.add(2.5,2), 4.5) #test for same numbers
        self.assertEqual(myCalculator.add(2, 3.5), 5.5) #test for two different numbers
        self.assertEqual(myCalculator.add(4,0), 4) #test for 0 
        self.assertEqual(myCalculator.add(-3, -2), -5) # test for adding minus numbers
        self.assertEqual(myCalculator.add(-3, 2), -1) # test for adding plus and minus numbers
        self.assertEqual(myCalculator.add(-3.22222222222222222222, -2.666666666666666666666666), -5.888888889) # test for rounding to 9 decimal places
        
    def testSUBTRACT(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.subtract(2.5,2.5), 0.0) #test if same two numbers
        self.assertEqual(myCalculator.subtract(5.3,2), 3.3) #test for 2 different numbers
        self.assertEqual(myCalculator.subtract(4,0), 4) # test for 0
        self.assertEqual(myCalculator.subtract(-2.5,-2), -0.5) # test for two minus numbers
        self.assertEqual(myCalculator.subtract(-5, 2), -7) # test for one plus and one minus number
        self.assertEqual(myCalculator.subtract(-3.22222222222222222222, -2.666666666666666666666666), -0.555555556) #test for rounding to 9 decimal places
        
    def testMULTIPLY(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.multiply(2.5,2.5), 6.25) #test for same numbers
        self.assertEqual(myCalculator.multiply(2.5,3), 7.5) #test for two different numbers
        self.assertEqual(myCalculator.multiply(-2,3), -6) #test a plus and a minus give a minus
        self.assertEqual(myCalculator.multiply(-2,-3), 6) #test 2 minus give a plus
        self.assertEqual(myCalculator.multiply(-2, 0), 0) #test for 0 as input
        self.assertEqual(myCalculator.multiply(2.55555555555555555555555555555, 2), 5.111111111) #test for rounding to 9 decimal places
        
    def testDIVIDE(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.divide(2.5,2.5), 1)#test for same numbers
        self.assertEqual(myCalculator.divide(2,3), 0.666666667)#test for two different numbers and rounding to 9 decimal places
        self.assertEqual(myCalculator.divide(-3,-2), 1.5)#test 2 minus give a plus
        self.assertEqual(myCalculator.divide(-2,3), -0.666666667)#test a plus and a minus give a minus
        self.assertEqual(myCalculator.divide(0,2), 0)  #test for 0 as first number
        self.assertEqual(myCalculator.divide(2,0), 'undefined')  #test for 0 as second number 
        
    def testXtothepowerofY(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.xtothepowerofy(2,2), 4) # test for same two numbers
        self.assertEqual(myCalculator.xtothepowerofy(2,3), 8) # test for two different numbers
        self.assertEqual(myCalculator.xtothepowerofy(3,2), 9) #test for x not equal to 2
        self.assertEqual(myCalculator.xtothepowerofy(0,2), 0) #test for x equal to 0
        self.assertEqual(myCalculator.xtothepowerofy(2,0), 1) #test for y equal to 0
        self.assertEqual(myCalculator.xtothepowerofy(-2, 3), -8) #test for negative x with positive y
        self.assertEqual(myCalculator.xtothepowerofy(2, -3), 0.125) #test for positive x with negative yield
        self.assertEqual(myCalculator.xtothepowerofy(-2, -3), -0.125) # test for negative x and negative y
        
    def testSQUARE(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.square(2.5), 6.25) #test for positive
        self.assertEqual(myCalculator.square(-2.5), 6.25) #test for negative
        self.assertEqual(myCalculator.square(2.555555555555555555555555555555555555555), 6.530864198) #test for rounding to 9 decimal places
        self.assertEqual(myCalculator.square(0), 0) #test for 0 input
        
    def testCUBE(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.cube(2.5), 15.625) # test for positive input
        self.assertEqual(myCalculator.cube(-2.5), -15.625)#test for negative input
        self.assertEqual(myCalculator.cube(0), 0) #test for 0 input
        self.assertEqual(myCalculator.cube(2.555555555555555555555555555555555555555), 16.689986283) #test for rounding to 9 decimal places
       
        
    def testINVERSE(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.inverse(2.5), 0.4) #test for positive input
        self.assertEqual(myCalculator.inverse(-2.5), -0.4) #test for negative input
        self.assertEqual(myCalculator.inverse(0), 'undefined') #test for 0 as input
        self.assertEqual(myCalculator.inverse(2.555555555555555555555555555555), 0.391304348) #test for rounding to 9 decimal places
        
    def testFACTORIAL(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.factorial(70), 'invalid')
        self.assertEqual(myCalculator.factorial(6), 720)
        self.assertEqual(myCalculator.factorial(0), 1) #check 0! is 1
        
        
    def testCONVERTDEGREESTODMS(self):
        myCalculator = Calculator()
        self.assertEqual(myCalculator.convertdegreestoDMS(30.0), ('30 degrees, 0 minutes and 0 seconds')) #check calculated correctly when only degrees
        self.assertEqual(myCalculator.convertdegreestoDMS(30.5), ('30 degrees, 30 minutes and 0 seconds')) #check calculated correctly when only degrees and minutes
        self.assertEqual(myCalculator.convertdegreestoDMS(30.234), ('30 degrees, 14 minutes and 2 seconds')) # check seconds calculated correctly
        self.assertEqual(myCalculator.convertdegreestoDMS(0.01), ('0 degrees, 0 minutes and 36 seconds')) # check when input is less than 1
        self.assertEqual(myCalculator.convertdegreestoDMS(-30.21), ('-30 degrees, -12 minutes and -36 seconds')) # check for negative input
        self.assertEqual(myCalculator.convertdegreestoDMS(0.0), ('0 degrees, 0 minutes and 0 seconds')) #test for 0 input
        self.assertEqual(myCalculator.convertdegreestoDMS(30.88888888888888888888888), ('30 degrees, 53 minutes and 20 seconds')) #test for rounding to whole numbers regardless of input
    
if __name__ == '__main__':
    unittest.main()
