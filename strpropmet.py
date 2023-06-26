Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = "Sam"
name[0] = 'P'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name[0] = 'P'
TypeError: 'str' object does not support item assignment
name[1:]
'am'
last_letters = name[1:]
last_letters
'am'
'P'+last_letters
'Pam'
x = 'Hello World'
x + ' it is beutiful outside!'
'Hello World it is beutiful outside!'
x = x + ' it is beutiful outside!'
x
'Hello World it is beutiful outside!'
letter = 'z'
>>> letter * 4
'zzzz'
>>> 2 + 3
5
>>> '2' + '3'
'23'
>>> x = 'Hello World'
>>> x.expandtabs()
'Hello World'
>>> x.count()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x.count()
TypeError: count() takes at least 1 argument (0 given)
>>> x.upper()
'HELLO WORLD'
>>> x.count('Hello')
1
>>> x.count('o')
2
>>> x.lower()
'hello world'
>>> x.split()
['Hello', 'World']
>>> x = 'Hi it is a string there'
>>> x.split()
['Hi', 'it', 'is', 'a', 'string', 'there']
>>> x.split(i)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x.split(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> x.split('i')
['H', ' ', 't ', 's a str', 'ng there']
>>> y = 'ii it iipli iti'
>>> y.split('i')
['', '', ' ', 't ', '', 'pl', ' ', 't', '']
>>> print('hello')
hello
