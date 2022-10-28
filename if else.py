x="hello"
y="hello"
if x==y:
    print("TRUE")
else:
    print("False")    



x=1
y=5
if x>y:
    print('TRUE')
else:
    print('FALSE')


x=22
y=33
z=55
if (x<y) and (y<z):
    print("yes")
else:
    print("no")   



x=2
y=2
if x<y:
    print("x is less than y")
elif x==y:
    print("x is equal to y") 
else:
    print("x is greater than y")


x=20
if x<30:
    print("x is less than 30")
    if x<10:
        print("x is greater than 10")
    else:
        print("x is either greater than or equal to 10 but less than 30")
else:
    print("x is either equal or greater than 30")            
