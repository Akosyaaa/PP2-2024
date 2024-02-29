#Ex1
import math
def multiply(numbers):
    return math.prod(numbers)

numbers=[1,2,3,4]
result = multiply(numbers)
print(result)
#Ex2
def count(string):
    upper_count=sum(1 for char in string if char.isupper())
    lower_count=sum(1 for char in string if char.islower())
    return upper_count,lower_count
input_string="Hello,my name is Akerke"
upper,lower=count(input_string)
print("number of upper case letter:",upper)
print("lower case letters:",lower)
#Ex3

