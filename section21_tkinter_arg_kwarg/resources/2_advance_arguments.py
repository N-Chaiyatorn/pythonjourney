# default and optional arguments quiz
def foo(a, b=4, c=6): 
    print(a, b, c)
foo(1)

def bar(a, b=4, c=6): 
    print(a, b, c)
bar(4, 9)

def baz(a, b=4, c=6):
    print(a, b, c)
baz(20, c=6)

################################

# unlimited positional arguments
def args(*args):
    for n in args:
        print(n)


# unlimited keyword arguments
def kwargs(**kwargs):
    print(kwargs)
kwargs(a=1,b=2)

# quiz
def test1(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
test1(1, 2)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
all_aboard(4, 7, 3, 0, x=10, y=64)