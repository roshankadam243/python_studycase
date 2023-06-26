Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> True
True
>>> False
False
>>> tyep(False)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tyep(False)
NameError: name 'tyep' is not defined
>>> type(False)
<class 'bool'>
>>> false
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> 1==1
True
>>> 1<2
True
>>> 1>2
False
>>> 'roshan'=='Roshan'
False
>>> 2.3>-2.3
True
>>> -1437>-12
False
>>> b = None
>>> b
>>> b =
SyntaxError: incomplete input
>>> set([1,1,2,3])
{1, 2, 3}
