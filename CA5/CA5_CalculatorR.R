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
answer_add_3 <- add(1,2)
answer_add_4 <- add(2,2)
answer_add_0 <- add(-2,2)
answer_subtract_3 <- subtract(7,4)
answer_s
#Square and Cube
answer_square_25 <- square(5)
answer_square_neg_gives_plus_25 <- square(-5)
answer_cube_125 <- cube(5)
answer_cube_neg_125 <- cube(-5)

#DMS

answer_DMS_10_38_42 <-DMS(10.645)
answer_DMS_negative_5_30_0<-DMS(-5.5)


