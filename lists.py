Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_list = [1,2,3,4]
print(my_list)
[1, 2, 3, 4]
print(mylist[1,'one',3,'two'])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(mylist[1,'one',3,'two'])
NameError: name 'mylist' is not defined. Did you mean: 'my_list'?
print(mylist = [1,'one',3,'two'])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(mylist = [1,'one',3,'two'])
TypeError: 'mylist' is an invalid keyword argument for print()
mylist = [1,'one',3,'two']
print(my_list)
[1, 2, 3, 4]
print(mylist)
[1, 'one', 3, 'two']
my_list = ['STRING',100,29.30]
print(my_list)
['STRING', 100, 29.3]
len.(my_list)
SyntaxError: invalid syntax
len(my_list)
3
my_list[2]
29.3
name = "STRING"
len(name)
6
name.translate()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name.translate()
TypeError: str.translate() takes exactly one argument (0 given)
my_list[3] = ['Zero']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    my_list[3] = ['Zero']
IndexError: list assignment index out of range
my_list[2] = ['ZERO']
print(my_list)
['STRING', 100, ['ZERO']]
my_list[2] = 'ZERO'
print(my_list)
['STRING', 100, 'ZERO']
print(my_list + mylist)
['STRING', 100, 'ZERO', 1, 'one', 3, 'two']
my_list.append('SEVEN')
print('my_list')
my_list
print(my_list)
['STRING', 100, 'ZERO', 'SEVEN']
mylist.pop()
'two'
print(mylist)
[1, 'one', 3]
print(new_list = my_list + mylist)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(new_list = my_list + mylist)
TypeError: 'new_list' is an invalid keyword argument for print()
new_list = my_list + mylist
print(new_list)
['STRING', 100, 'ZERO', 'SEVEN', 1, 'one', 3]
popped_item = new_list()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    popped_item = new_list()
TypeError: 'list' object is not callable
>>> popped_item = new_list.pop()
>>> print(popped_item)
3
>>> new_list.pop(0)
'STRING'
>>> print(new_list[:-1])
[100, 'ZERO', 'SEVEN', 1]
>>> print(new_list[-1:])
['one']
>>> print(new_list[1:])
['ZERO', 'SEVEN', 1, 'one']
>>> print(new_list[:1])
[100]
>>> print(new_list[::-1])
['one', 1, 'SEVEN', 'ZERO', 100]
>>> new_list.append('TWO')
>>> new_list[0] = 34
>>> print(new_list)
[34, 'ZERO', 'SEVEN', 1, 'one', 'TWO']
>>> nlist = ['a','s','d','f','g']
>>> numlist = [3,1,5,4,6,2]
>>> nlist.sort()
>>> print(nlist)
['a', 'd', 'f', 'g', 's']
>>> print(numlist)
[3, 1, 5, 4, 6, 2]
>>> numlist.sort()
>>> sorted_list = numlist
>>> print(sorted_list)
[1, 2, 3, 4, 5, 6]
>>> sorted_list.reverse()
>>> print(sorted_list)
[6, 5, 4, 3, 2, 1]
>>> sorted_list.remove(6)
>>> print(sorted_list)
[5, 4, 3, 2, 1]
