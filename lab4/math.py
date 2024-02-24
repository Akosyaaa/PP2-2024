#Ex1
import math

def limmarilin(n):
    radians=n*math.pi/180
    return radians

n=float(input("Input degree"))
radians=limmarilin(n)
print("Output radian",radians)
#Ex2
def trapezoid(base1,base2,height):
    area=((base1+base2)*height)/2
    return area

base1=float(input("Base,first value:"))
base2=float(input("Base,second value:"))
height=float(input("Height:"))
area=trapezoid(base1,base2,height)
print("Expected Output:",area)
#Ex3
import math

def regular_polygon(n, s):
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    return area
n=int(input("Input number of sides:"))
s=int(input("Input the length of a side:"))
area=regular_polygon(n,s)
print("The area of the polygon is:",area)
#Ex4
def Akerke(b,h):
    area=b*h
    return area
b=float(input("Length of base:"))
h=float(input("Height of parallelogram:"))
area=Akerke(b,h)
print("Expected Output:",area)