import itertools 
user=str(input("Enter the string: "))
def permutations(user):
    for i  in itertools.permutations(user):
        a=''.join(i) 
        print(a)
permutations(user)