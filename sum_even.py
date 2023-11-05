#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int = 1234
sum_even = 0

while var_int > 0:
    raqam = var_int % 10
    if raqam % 2 == 0:
        sum_even += raqam
    var_int = var_int // 10

print(sum_even)
