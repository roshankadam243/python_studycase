Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myset = set()
type(myset)
<class 'set'>
myset.add(5)
myset.add(3,4,2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myset.add(3,4,2)
TypeError: set.add() takes exactly one argument (3 given)
myset.add('Sam')
print(myset)
{5, 'Sam'}
>>> myset.clear(5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    myset.clear(5)
TypeError: set.clear() takes no arguments (1 given)
>>> myset.clear()
>>> print(myset)
set()
>>> myset.add(5)
>>> myset.add('Jose')
>>> myset.add('Apple')
>>> myset.add(2.3)
>>> myset.add(100)
>>> myset.pop(5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myset.pop(5)
TypeError: set.pop() takes no arguments (1 given)
>>> myset.remove(5)
>>> print(myset)
{'Apple', 2.3, 100, 'Jose'}
>>> myset.copy()
{'Apple', 2.3, 100, 'Jose'}
>>> print(myset)
{'Apple', 2.3, 100, 'Jose'}
>>> myset.add(2.3)
>>> print(myset)
{'Apple', 2.3, 100, 'Jose'}
>>> mylist = [1,2,3,4,'jose',44,'Jose',5,6,3,2,1,'Sam','Jose',2.4,2.4]
>>> print(mylist)
[1, 2, 3, 4, 'jose', 44, 'Jose', 5, 6, 3, 2, 1, 'Sam', 'Jose', 2.4, 2.4]
>>> set(mylist)
{1, 2, 3, 4, 5, 6, 2.4, 44, 'jose', 'Jose', 'Sam'}
>>> mytuple = (1,2,3,'Jose','Jose',3.4,2.3100,2,3,3.4)
>>> print(mytuple)
(1, 2, 3, 'Jose', 'Jose', 3.4, 2.31, 2, 3, 3.4)
>>> set(mytuple)
{1, 2, 3.4, 3, 2.31, 'Jose'}
