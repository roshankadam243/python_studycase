Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('This is a stirng{}'.format("INSERTED"))
This is a stirngINSERTED
print('This is a stirng {}'.format("INSERTED"))
This is a stirng INSERTED
print('The {} {} {}' .format('fox','brown','quick'))
The fox brown quick
print('The {2} {0} {1}' .format('fox','brown','quick'))
The quick fox brown
print('The {0} {0} {0}' .format('fox','brown','quick'))
The fox fox fox
print('The {} {} {}' .format(f='fox',b='brown',q='quick'))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('The {} {} {}' .format(f='fox',b='brown',q='quick'))
IndexError: Replacement index 0 out of range for positional args tuple
print('The {q} {f} {b}' .format(f='fox',b='brown',q='quick'))
The quick fox brown
print('The {b} {b} {b}' .format(f='fox',b='brown',q='quick'))
The brown brown brown
print('I once caught a fish %s.' %'this \tbig')
I once caught a fish this 	big.
print('I once caught a fish %r.' %'this \tbig')

I once caught a fish 'this \tbig'.
print('Floating point numbers: %5.0f' %(13.144))
Floating point numbers:    13
print('Floating point numbers: %1.2f' %(13.144))
Floating point numbers: 13.14
print('{0:7} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
SyntaxError: multiple statements found while compiling a single statement
print('{0:7} | {1:9}'.format('Fruit', 'Quantity'))
Fruit   | Quantity 
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
Fruit    | Quantity 
>>> print('{0:2} | {1:9}'.format('Fruit', 'Quantity'))
Fruit | Quantity 
>>> result = 100/777
>>> print(result)
0.1287001287001287
>>> print("The result was{}.format(result))
...       
SyntaxError: incomplete input
>>> print("The result was{}".format(result))
...       
The result was0.1287001287001287
>>> print("The result was {}".format(result))
...       
The result was 0.1287001287001287
>>> print("The result was {r}".format(r=result))
...       
The result was 0.1287001287001287
>>> print("The result was {r:2.3f}".format(r=result))
...       
The result was 0.129
>>> print("The result was {r:5.6f}".format(r=result))
...       
The result was 0.128700
>>> result = 104.12345
...       
>>> name = "Sam"
...       
>>> print(f'Hello, his name is {name}')
...       
Hello, his name is Sam
>>> age=12
...       
>>> print(f'{name} is (age) year of old')
...       
Sam is (age) year of old
>>> print(f'{name} is {age} years of old')
...       
Sam is 12 years of old
