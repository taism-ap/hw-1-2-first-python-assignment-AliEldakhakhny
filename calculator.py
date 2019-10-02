print("Welcome to Ali's Calculator")
x=int(input("PLease choose a number"))
y=int(input("Please choose another number"))
z=input("Please choose an operation")

def a(x,y):
    return x+y
def s(x,y):
    return x-y
def m(x,y):
    return x*y
def d(x,y):
    return x/y

if z== '+':
    print(a(x,y))
if z== '-':
    print(s(x,y))
if z== '*':
    print(m(x,y))
if z== '/':
    print(d(x,y))
