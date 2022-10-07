#Single Strings
print('HELLO WORLD')

#Double Strings
print("HELLO WORLD")

x="hello"
print(x)
print(type(x))

#multiline strings
a="""hello coders.
welcome to the world of coding.
enjoy creating things."""
print(a)

#access strings as array using index
myDict={"jake": "jakes value"}
print(myDict["jake"])

#looping through a string
t="hello"
for i in range(len(t)):
  print(t[i])

#string length
b="hello world"
print(len(b))

#slice
c="hello,world"
slice_obj=slice(5,11)
print(c[slice_obj])

#slice from start
print(c[:5])
print(c[-5:-2])