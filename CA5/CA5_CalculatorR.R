#Beth Craig
#Student Number 10331736

#CA5 Part a

#####################################################################

#                 10 functions

######################################################################

#Add
add <- function(x, y){
  result <- x + y
  return(result)
  
  }
  

#Subtract
subtract <- function(x, y){
  result <- x-y
 
  return (result)
  
  }

#Multiply
multiply <- function(x, y){
  result <- x*y
  
  return (result)
  }

#Divide first by second
divide <- function(x, y){
    if (y == 0) {
    result = 'invalid'
  } else {
    result = x/y
    return (result)}
  }

#X to the power of Y
xToPowerY <- function(x, y) {

  return (x^y)
  }

#Squre
square <- function(x){
  result = x*x
  return(result)
  }

#Cube
cube <- function(x){
  result = x*x*x
  return(result)
}

#Inverse
inverse <- function(x){
   if (x ==0) {
    result = 'undefined'
  } else {
    result <-1/x
  }
   return (result)
}
#note if 0 entered R gives Inf as answer so, unlike Python,
#guarding against 0 is not strictly required 

#Factorial

factorial_BC <-function(x){
    if (x < 0 | x > 170) {
    result <- 'invalid'
  } else if (x == 0) {
    result <- 1
  } else {
    result <- factorial(x)
  }
   return (result)
}

#Convert to Degrees, Minutes, Seconds
DMS = function(x) {
  degrees <- trunc(x)
  minutes_float <- (x%%1)*60
  minutes <- minutes_float - abs(minutes_float%%1)
  seconds<-round(minutes_float%%1*60, digits = 2)
  print (paste(degrees, 'degrees', minutes, 'minutes', seconds, 'seconds'))
}

##############################################################################

#                  Calls to proove functions work

##############################################################################


#Adding,Subtracting, Divinding, Multiplying
answer_add_3 <- add(1,2)
answer_add_4 <- add(2,2)
answer_add_0 <- add(-2,2)
answer_subtract_3 <- subtract(7,4)
answer_subtract_0 <- subtract(7,7)
answer_subtract_11 <- subtract(7,-4)
answer_multiply_28 <- multiply(7,4)
answer_multiply_49 <- multiply(7,7)
answer_multiply_neg_28 <- multiply(-7,4)

answer_divide_4 <- divide(28,7)
answer_divide_1 <- divide(7,7)
answer_divide_neg_4 <- divide(-28,7)
answer_divide_invalid <- divide(28, 0)

#TO the Power Of
answer_xToPowerY_16 <-xToPowerY(2, 4)

#Square and Cube
answer_square_25 <- square(5)
answer_square_neg_gives_plus_25 <- square(-5)
answer_cube_125 <- cube(5)
answer_cube_neg_125 <- cube(-5)

#Inverse
answer_inverse_0.2 <- inverse(5)
answer_inverse_undefined_0 <- inverse(0)
answer_inverse_neg_0.5<- inverse(-2)
answer_inverse_2 <- inverse(0.5)


#Factorial
answer_factorial_1 <- factorial_BC(0)
answer_factorial_6 <- factorial_BC(3)
answer_factorial_invalid_negative <- factorial_BC(-3)
answer_factorial_invalid_200 <- factorial_BC(200)

#DMS

answer_DMS_10_38_42 <-DMS(10.645)
answer_DMS_negative_5_30_0<-DMS(-5.5)


