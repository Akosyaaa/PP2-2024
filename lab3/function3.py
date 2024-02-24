def is_prime(n=100000):
    d=2
    while n%d!=0:
        d+=1
    return d==n
u=int(input())
print(is_prime(u))