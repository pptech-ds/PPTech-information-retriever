import inspect

def Foo():
   return(inspect.currentframe().f_code.co_name)

print(Foo)

