#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
#To'rt xonali butun son berilgan. Undagi toq raqamlar sonini toping.

#"var_int" o'zgaruvchisini yarating va unga to'rt xonali butun son qiymatini belgilang.

#"var_int" o'zgaruvchisidagi toq raqamlar sonini chop eting.
var_int = 4567
toq_raqamlar = ""
for raqam in str(var_int):
    if int(raqam) % 2 != 0:
        toq_raqamlar += raqam
print(toq_raqamlar)