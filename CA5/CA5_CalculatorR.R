

#Add
add <- function(){
  x <- as.numeric(readline(prompt = "enter first number"))
  y <-as.numeric(readline(prompt = "enter second number"))
  result <- x+y
  print(result)
  return (result)
  
  }
  

#Subtract
subtract <- function(){
  x <- as.numeric(readline(prompt = "enter first number"))
  y <-as.numeric(readline(prompt = "enter second number"))
  result <- x-y
  print(result)
  return (result)
  
  }

#Multiply
multiply <- function(){
  x <- as.numeric(readline(prompt = "enter first number"))
  y <-as.numeric(readline(prompt = "enter second number"))
  result <- x*y
  print(result)
  return (result)
  }

#Divide first by second
divide <- function(){
  x <- as.numeric(readline(prompt = "enter first number"))
  y <-as.numeric(readline(prompt = "enter second number"))
  if (y == 0) {
    result = 'invalid'
  } else {
    result = x/y
    print(result)
    return (result)}
  }

#X to the power of Y
xToPowerY <- function() {
  x <- as.numeric(readline(prompt = "enter first number"))
  y <-as.numeric(readline(prompt = "enter second number"))
  print(x^y)
  return (x^y)
  }

#Squre
square <- function(){
  x <- as.numeric(readline(prompt = "enter the number"))
  result = x*x
  print(result)
  return(result)
  }

#Cube
cube <- function(){
  x <- as.numeric(readline(prompt = "enter the number"))
  result = x*x*x
  print(result)
  return(result)
}

#Inverse
inverse <- function(){
  x <- as.numeric(readline(prompt = "enter the number"))
  if (x ==0) {
    result = 'undefined'
  } else {
    result <-1/x
  }
  print(resut)
  return (result)
}
#note if 0 entered R gives Inf as answer so, unlike Python,
#guarding against 0 is strictly required 

#Factorial

factorial_BC <-function(){
  x <- as.numeric(readline(prompt = "enter the number"))
  if (x < 0 | x > 170) {
    result <- 'invalid'
  } else if (x == 0) {
    result <- 1
  } else {
    result <- factorial(x)
  }
  print(result)
  return (result)
}

#Convert to Degrees, Minutes, Seconds
DMS = function() {
  x <- as.numeric(readline(prompt = "enter angle"))
  degrees <- x - (x%%1)
  minutes_float <- (x%%1)*60
  minutes <- minutes_float - (minutes_float%%1)
  seconds<-round(minutes_float%%1*60, digits = 2)
  print (paste(degrees, 'degrees', minutes, 'minutes', seconds, 'seconds'))
}



#Calls to proove functions work

#Input is Numeric
answer_input_numeric_6 <- input_is_numeric(6)
answer_input_numeric_invalid <- input_is_numeric('hi')

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
answer_DMS_negative_6_30_0<-DMS(-5.5)


#User App

print ("Menu\n1. Add\n 2. Subtract\n3. Multiply\n4. Divide\n5. x to the power of Y\n6. Square\n7. Cube\n8. Inverse\n9. Factorial\n10. DMS")

proceed <- 'y'
while (proceed == 'y'){
  choice <- readline(prompt = "Enter your choice of function\n")
  if (choice == 1){add()}
  else if (choice == 2){subtract()}
  else if (choice == 3){multiply()}
  else if (choice == 4){divide()}
  else if (choice == 5){xToPowerY()}
  else if (choice == 6) {square()}
  else if (choice == 7){cube()}
  else if (choice == 8){inverse()}
  else if (choice == 9){factorial_BC()}
  else if (choice == 10){DMS()}
  proceed <- readline(prompt = "enter y or n")
}  
