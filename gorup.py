from math import *

import time

print("solving quadratic equation using almighty formula ")
print("a(x**2)+bx+c=0")
# Inputting parameters
FirstValue = float(input("Enter the value of \"a\" : "))
SecondValue = float(input("Enter the value of \"b\" : "))
ThirdValue = float(input("Enter the value of \"c\" : "))
product = FirstValue * ThirdValue
# Getting the roots of the equation
try:
  D1 = ( -SecondValue + (sqrt((SecondValue ** 2) - (4 * product)))) / (2 *FirstValue)
  D2 = ( -SecondValue - (sqrt((SecondValue ** 2) - (4 * product)))) / (2 *FirstValue)

  print("First root = {:.2f}".format(D1))
  print("Second root = {:.2f}".format(D2))
except ValueError:
    print ("no real root")
    
end = time.time()
print("The run time of this program is : {:.0f}".format(end ))