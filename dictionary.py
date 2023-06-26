Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict = {'key1':'value1','key2':'value2'}
type(dict)
<class 'dict'>
dict['key1']
'value1'
prices = {'apple':200, 'orange':150.50, 'milk':189.3}
prices['apple']
200
d = {'k1':211, 'k2':'Sam', 'k3':[1,2,3,4], 'k4':{'insidek4':23}}
print(d)
{'k1': 211, 'k2': 'Sam', 'k3': [1, 2, 3, 4], 'k4': {'insidek4': 23}}
d[k4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d[k4]
NameError: name 'k4' is not defined
d['k4']
{'insidek4': 23}
d['k3']
[1, 2, 3, 4]
d['k4']['insidek4']
23
d = {'k1':'a','b','c'}
SyntaxError: ':' expected after dictionary key
d = {'k1': ['a','b','c']}
>>> mylist = d['k1']
>>> print(mylist)
['a', 'b', 'c']
>>> letter = mylist[2]
>>> print(letter.upper())
C
>>> d['k1']
['a', 'b', 'c']
>>> d['k1'][2].upper
<built-in method upper of str object at 0x00007FFCCE3D1408>
>>> d['k1'][2].upper()
'C'
>>> letter.upper()
'C'
>>> d = {'k1':100,'k2':200}
>>> d['k3']=300
>>> print(d)
{'k1': 100, 'k2': 200, 'k3': 300}
>>> d['k1']=10
>>> print(d)
{'k1': 10, 'k2': 200, 'k3': 300}
>>> d['k4']='NEW VALUE'
>>> print(d)
{'k1': 10, 'k2': 200, 'k3': 300, 'k4': 'NEW VALUE'}
>>> d.keys()
dict_keys(['k1', 'k2', 'k3', 'k4'])
>>> d.items()
dict_items([('k1', 10), ('k2', 200), ('k3', 300), ('k4', 'NEW VALUE')])
>>> d.values()
dict_values([10, 200, 300, 'NEW VALUE'])
>>> a={"k1"=23}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a={"k1":23}
>>> a['k2']=34
>>> print(a)
{'k1': 23, 'k2': 34}
>>> b={"k1":43,'k2':32}
>>> print(b)
{'k1': 43, 'k2': 32}
