def is_palindrom(s="")
    r=s[::-1]
    if s==r:
        return True
    else:
        return False
word=input()
print(is_palindrom(word))