#Ex1
def Akerke(N):
    for i in range(N):
        yield i**2
N=7
squares=Akerke(N)
for Akerke in squares:
    print(Akerke)
#Ex2
def Akerke(n):
    for i in range(n+1):
        if i%2==0:
            yield i
try:
    n=int(input())
    if n<0:
        print("Please enter a positive integer")
    else:
        print(','.join(map(str,Akerke(n))))
except ValueError:
    print("Invalid input")
#Ex3
def Akerke(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=40
for numm in Akerke(n):
    print(numm)
#Ex4
def square(a,b):
    for i in range(a,b+1):
        yield i**2
a=4
b=9
for i in square(a,b):
    print(i)
#Ex5
def Akerke(n):
    while n>=0:
        yield n
        n-=1
n=5
for i in Akerke(n):
    print(i)