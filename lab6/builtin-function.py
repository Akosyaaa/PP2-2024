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
s=input()
t=s
x=iter(t)
ans=True
for i in s[::-1]:
    if i!=next(x):
        ans=False
        break
print(ans)
#Ex4
import math
import time
number=int(input("Write a number "))
milisecond=int(input("Write a milisecond "))
seconds=milisecond/1000
time.sleep(seconds)
print(math.sqrt(number))
#Ex5
n=int(input())
mylist=list()
for i in range(n):
    a=input()
    if a=="true" or a=="True":
        mylist.append(True)
    else:
        mylist.append(False)
mytuple=tuple(mylist)
x=all(mytuple)
print(x)
