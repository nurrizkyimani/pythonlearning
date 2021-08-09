#argument vs parameter

def print_name(name):
  print(name)


def positional(a, b,c, d=5):
  print(a,b,c, d)

positional(1,3,4)

positional(a=1, b=3, c=5)


def testaandk(a,b,c, *args, **kwargs):
  print(a,b,c)

  for arg in args:
    print(arg)
  
  for key in kwargs: 
    print(key)  

testaandk(1,2,4, 2,5,6,3,2,2, k=5,l=9, w=9)

def unpacking(a,b,c):
  print(a,b,c)

mylist = (1,3,5)

unpacking(*mylist)