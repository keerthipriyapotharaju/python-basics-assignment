def sum(n):
    if not n:
        return 0
    else:
        return n[0]+sum(n[1:])
a=[1,2,3,4,5]
print(sum(a))