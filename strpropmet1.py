Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print((2+3)*(2+5))
35
>>> print(2+10*10+3)
105
>>> x='Hello World'
>>> x
'Hello World'
>>> x.upper
<built-in method upper of str object at 0x0000025B648A4CF0>
>>> x.upper()
'HELLO WORLD'
>>> upper
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    upper
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> cls
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> x.lower()
'hello world'
>>> x.split()
['Hello', 'World']
>>> x = 'Hi this is a string'
>>> x.split()
['Hi', 'this', 'is', 'a', 'string']
>>> x.split(i)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.split(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> x.split('i')
['H', ' th', 's ', 's a str', 'ng']
