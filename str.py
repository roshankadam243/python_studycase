#strings
print('Hello')
print("Hello")
print('this is also a string')
print("I don't do that")
#print('I'm back')
print("I'm back")

print('hello \nworld') #new line
print('hello \tworld') #tab 

#length
print(len('h m'))
print(len('hey'))

#strings are ordered seqeunces
#it means we can use indexing and slicing to grab sub section of the strings

#Indexing notation uses [] notation after the strings or variable assinged
#indexing allows you to gran a single character from string
mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[8])
print(mystring[9])
print(mystring[-2])
print(mystring[-3])


#slicing allows you to grab a sub section of mutliple character
#syntax: [start:stop:step]
#start:numerical index for slice start
#stop:index you will go upto(but not include)
#step:size of the jump you take

mystring = 'abcdefghijk'
print(mystring)
print(mystring[2:])

print(mystring[:3])#but not include
print(mystring[3:6])
print(mystring[1:3])

print(mystring[::])#valid syntax, also print whole string value
print(mystring[::2])
print(mystring[2:9:2])#output: cegi

print(mystring[::-1])#reverse string


