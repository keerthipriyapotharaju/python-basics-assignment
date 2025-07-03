def rev(n):
    rev=0
    while(n>0):
        digits=n%10
        rev=rev*10+digits
        n=n//10
    return rev
a=1234
print(rev(a))