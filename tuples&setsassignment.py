#TUPLES

#unpack a tuple
numbers=(10,20,30)
(num1,num2,num3)=numbers
print(num1)
print(num2)
print(num3)


numbers1=(10,20,30,40,50,60,70,80)
(num1,num2,*num3)=numbers1
print(num1)
print(num2)
print(num3)


numbers2=(10,20,30,40,50,60,70,80)
(num1,*num2,num3)=numbers2
print(num1)
print(num2)
print(num3)


#for loop
t=(10,20,30,40,50)
for x in t:
    print(x)

#looping through index numbers
t1=("a","b","c","d","e")
for i in range(len(t1)):
    print(t1[i])


#joining tuples
t3=(0,1,2,3,4)
t4=(5,6,7,8,9)
t5=t3+t4
print(t5)


#multiplication of tuples
t6=(0,1,2,3,4)
t7=(t6)*2
print(t7)


#SETS
myset={10,20,30,40}
print(type(myset))

s={'avvbby',2,50,4,'kgfhth'}
print(s)

#access items
s1={1,3,4}
for x in s1:
    print(x)

#add,remove,pop items
s3={10,20,30,40}
s3.add(90)
print(s3)

s6={9,4,7,2,5}
s6.remove(4)
print(s6)

s7={"dnjjvnjfr","gyfgv","gvughu"}
s7.pop()
print(s7)

#discard item
a={"dnnjn","jdjrenj","ncrnfjn"}
a.discard("dnnjn")
print(a)

#union of sets
b={1,3,4,5}
c={"a","b"}
d=b.union(c)
print(d)

e={1,3,4,4,5,5,5}
f={"a","b",5,6}
g=e.union(f)
print(g)

#intersection
h=e.intersection(f)
print(h)

#symmetric difference
i=e.symmetric_difference(f)
print(i)







