#=============================================================================================================================

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#=============================================================================================================================

x = "awesome"

def myfunc1():
  x = "fantastic"
  print("Python is " + x)

myfunc1()

print("Python is " + x)


#=============================================================================================================================

'''
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example
If you use the global keyword, the variable belongs to the global scope:
'''

def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)

#=============================================================================================================================














