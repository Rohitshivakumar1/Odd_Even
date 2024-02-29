def inp():
    s=[]
    si=int(input("how many numbers"))
    for i in range(si):
        s.append(int(input("enter numbers")))
    return s

def even(z):
    stroage1=[]
    for num in inp:
        if num%2==0:
            stroage1.append(num)
    return stroage1

def odd(z):
    stroage2=[]
    for num in inp():
        if num%2!=0:
            stroage2.append(num)
    return stroage2

def cons(eve ,od):
    dict3={}
    dict3["even"]=eve
    didct3["odd"]=od
    return dict3

z=inp()
a=even(z)
b=odd(z)
s=cons(a,b)
print(s)
