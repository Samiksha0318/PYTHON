#Loops

#While and for loop
x=1
while x<6:
    print(x)
    x +=1

x=1
while x<6:
    print(x)
    if x==6:
        break
    x+=1

 
x=1 
while x<6:
    x += 1
    if x==5:
        continue#to skip cuurent iteration and move on to the next
    print(x)
else:
    print("out of range")


#For loop

num=[10,20,30,40]
for x in num:
    print(x)

for x in "hello":
    print(x)

#break in for loop
num=[10,20,30,40,50]
for x in num:
    if x==30:
        break
    print(x)


num=[10,20,30,40,50]
for x in num:
    print(x)  
    if x==30:
        break

#range
for x in range(6):
    print(x)

for x in range (2,6):
    print(x)   

for x in range (3,10,2):
    print(x)

for x in range(5):
    print(x)
else:
    print("process ends")  


#nested loops:

a=(2,43)
b=(5,6)
for x in a:
    for y in b:
        print(x,y)


x=[10,20,30,40]
for x in a:
    pass
print("hello")




      
         
        