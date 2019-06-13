#!/usr/local/bin/puthon3

"""This is the descrition of the module"""

var = "This is a variable."

class Foo:
    """Foo class descrition"""

    def __str__(self):
        """Foo.__str__() method descrition."""
        return ("This is a Foo instance.")

def function1():
    """Function1 descrition."""
    print("This is call of finction1().")

def function2(param : int)-> str:
    """Function2 descrition. It takes an int and returns a str."""
    print("This is a call of function2().")
    return str(param)

""" Resultat :
D02 git:(master) ✗ python3
Python 3.7.3 (default, Jun  6 2019, 00:57:50) 
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import module
>>> help(module)
Help on module module:


NAME
    module - This is the descrition of the module

CLASSES
    builtins.object
        Foo
    
    class Foo(builtins.object)
     |  Foo class descrition
     |  
     |  Methods defined here:
     |  
     |  __str__(self)
     |      Foo.__str__() method descrition.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    finction2(param: int) -> str
        Function2 descrition. It takes an int and returns a str.
    
    function1()
        Function1 descrition.

DATA
    var = 'This is a variable.'

FILE
    /Users/schebbal/piscine_python_django/D02/module.py


>>> var
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'var' is not defined
>>> module.var
'This is a variable.'
>>> f = module.Foo()
>>> f
<module.Foo object at 0x100c55518>
>>> module.function1()
This is call of finction1().
>>> module.function2(1)
This is a call of function2().
'1'
>>> 
[6]  + 8289 suspended  python3
➜  D02 git:(master) ✗ python3
Python 3.7.3 (default, Jun  6 2019, 00:57:50) 
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from module import module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'module' from 'module' (/Users/schebbal/piscine_python_django/D02/module.py)
>>> from module import var
>>> var
'This is a variable.'
>>> function1()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'function1' is not defined
>>> from module import function1, function2
>>> function1()
This is call of finction1().
>>> function2(5)
This is a call of function2().
'5'
>>> 
"""