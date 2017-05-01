#Add
add <- function(x, y){
  x + y}

#Subtract
subtract <- function(x, y){
  x - y}

#Multiply
multiply <- function(x,y){x*y}

#Divide first by second
divide <-function(x,y){x/y}

#X to the power of Y
xToPowerY <- function(x, y) {x^y}

#Squre
square <- function(x){x*x}

#Cube
cube <- function(x){x*x*x}

#Inverse
inverse <- function(x){
  if (x <=0) {
    result = 'undefined'
  } else {
    result <-1/x
  }
  return (result)
}
#note if 0 entered R gives Inf as answer so, unlike Python,
#guarding against 0 is strictly required 

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
  degrees <- x - (x%%1)
  minutes_float <- (x%%1)*60
  minutes <- minutes_float - (minutes_float%%1)
  seconds<-round(minutes_float%%1*60, digits = 2)
  print (paste(degrees, 'degrees', minutes, 'minutes', seconds, 'seconds'))
}



#Calls to proove functions work
answer_add_3 <- add(1,2)
answer_subtract_3 <- subtract(7,4)
answer_multiply_28 <- multiply(7,4)
answer_divide_7 <- divide(28,4)
answer_xToPowerY_16 <-xToPowerY(2, 4)
answer_square_25 <- square(5)
answer_cube_125 <- cube(5)
answer_inverse_0.2 <- inverse(5)
answer_inverse_undefined_0 <- inverse(0)
answer_inverse_undefined_negative <- inverse(-2)

answer_factorial_1 <- factorial_BC(0)
answer_factorial_6 <- factorial_BC(3)
answer_factorial_invalid_negative <- factorial_BC(-3)
answer_factorial_invalid_200 <- factorial_BC(200)

answer_DMS_10_38_42 <-DMS(10.645)







