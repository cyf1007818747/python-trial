# experimented in Python 3.12.2
# ! please arrange in alphabetical order

def all_trial():
    bool_list1 = []
    bool_list2 = [True, False]
    bool_list3 = [True, True]
    print('bool_list1:', all(bool_list1)) # >>: True # *
    print('bool_list2:', all(bool_list2))
    print('bool_list3:', all(bool_list3))

def any_trial():
    bool_list1 = []
    bool_list2 = [True, False]
    bool_list3 = [True, True]
    print('bool_list1:', any(bool_list1)) # >>: False # *
    print('bool_list2:', any(bool_list2))
    print('bool_list3:', any(bool_list3))

def bin_trial():
    num1 = 10
    num2 = -10
    print('num1:', bin(num1)) # >>: 0b1010
    print('num2:', bin(num2)) # >>: -0b1010
    # related functions
    print("---- related functios -----")
    print('format(10, "#b")', format(10, '#b')) # >>: 0b1010 # *
    print('format(10, "b")', format(10, 'b')) # >>: 1010 # *
    print("abc{10:#b}def:", f'abc{10:#b}def') # >>: abc0b1010def # *
    print("abc{10:b}def:", f'abc{10:b}def') # >>: abc1010def # *

def bool_trial():
    print("bool(0):", bool(0)) # >>: False
    print("bool(1):", bool(1)) # >>: True
    print("bool(0.0):", bool(0.0)) # >>: False
    print("bool(0.1):", bool(0.1)) # >>: True # *
    print("bool(''):", bool('')) # >>: False
    print("bool('abc'):", bool('abc')) # >>: True
    print("bool([]):", bool([])) # >>: False
    print("bool([1]):", bool([1])) # >>: True
    print("bool({}):", bool({})) # >>: False
    print("bool({'a': 1}):", bool({'a': 1})) # >>: True

def callable_trial():
    def func1():
        return 1
    
    class MyClass:
        def __init__(self):
            pass
        # (minor) this will make the class instance callable
        # def __call__(self):
        #     return 2
    
    obj1 = MyClass()

    print("callable(None):", callable(None)) # >>: False
    print("callable(func1):", callable(func1)) # >>: True
    print('callable(func1()):', callable(func1())) # >>: False
    print("callable(MyClass):", callable(MyClass)) # >>: True
    print("callable(obj1):", callable(obj1)) # >>: False # *
    print("callable(1):", callable(1)) # >>: False
    print("callable('abc'):", callable('abc')) # >>: False
    print("callable([1,2]):", callable([1,2])) # >>: False

# transform unicode into character
def chr_trial():
    print('chr(65):', chr(65)) # >>: A
    print('chr(97):', chr(97)) # >>: a
    print('chr(8364):', chr(8364)) # >>: €

def complex_trial():
    print('complex(1, 2):', complex(1, 2)) # >>: (1+2j)
    print('complex(1.1, 2.2):', complex(1.1, 2.2)) # >>: (1.1+2.2j)
    print('complex("1+2j"):', complex("1+2j")) # >>: (1+2j)
    print('complex("1.1+2.2j"):', complex("1.1+2.2j")) # >>: (1.1+2.2j)
    # operations
    print("complex(1, 2) + complex(3, 4):", complex(1, 2) + complex(3, 4)) # >>: (4+6j)
    print("complex(1, 2) * complex(3, 4):", complex(1, 2) * complex(3, 4)) # >>: (-5+10j)

def delattr_trial():
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj1 = MyClass()
    print('obj1.a:', obj1.a) # >>: 1

    delattr(obj1, 'a')
    try: # *
        print('obj1.a:', obj1.a) # raises error
    except AttributeError as e: # *
        print('error:', e) # >> error: 'MyClass' object has no attribute 'a'

def divmod_trial():
    print('divmod(10, 3):', divmod(10, 3)) # >>: (3, 1)
    print('divmod(10.5, 3.2):', divmod(10.5, 3.2)) # >>: (3.0, 0.8999999999999995) # *
    print('10.5 // 3.2:', 10.5 // 3.2) # >>: 3.0
    print('10.5 % 3.2:',10.5 % 3.2) # >>: 0.8999999999999995
 
def enumerate_trial():
    list1 = ['a', 'b', 'c']
    print("--enumerate(list1):")
    for i, v in enumerate(list1):
        print(i, v)

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    print("--enumerate(dict1.items()):")
    for i, (k, v) in enumerate(dict1.items()): # *
        print(i, k, v)

# executes a string into the evaluated result
# caution: may cause security issues
def eval_trial():
    x = 1
    print('eval("x + 1"):', eval("x + 1")) # >>: 2
    y = 'print(234)'
    eval(y) # >> 234 # *

def filter_trial():
    list0 = [-1, 0, 1, 2]
    print('list0:', list0)
    filter(None, list0) # does not change the list
    print('list0:', list0)
    list0_filtered0 = filter(None, list0)
    print('list0_filtered0:', list0_filtered0) # >>: <filter object at 0x10ea8b4c0> # *
    list0_filtered1 = list(filter(None, list0))
    print('list0_filtered:', list0_filtered1) # >>: [-1, 1, 2]
    list0_filtered2 = list(filter(lambda x: x > 0, list0)) # *
    print('list0_filtered2:', list0_filtered2) # >>: [1, 2]

    def is_even(n):
        return n % 2 == 0

    list1 = [1, 2, 3, 4, 5]
    list1_filtered0 = list(filter(is_even, list1))
    print('list1_filtered0:', list1_filtered0) # >>: [2, 4]
    list1_filtered1 = [num for num in list1 if is_even(num+1)] # *
    print('list1_filtered1:', list1_filtered1) # >>: [1, 3, 5]
    list1_filtered2 = [item for item in list1 if item % 3 == 1] # *
    print('list1_filtered2:', list1_filtered2) # >>: [1, 4]

def repr_trial(): 
    # repr of funcitons
    print("repr(all_trial):", repr(all_trial)) # special output of <function all_trial at 0x10ea894e0>
    print("repr(all_trial()):", repr(all_trial())) # calls the function and returns None

    # repr of classes
    print("-----------------")
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point({self.x}, {self.y}), created by Chris on Mar 27'
    
    p1 = Point(1, 2)
    print('repr(p1):', repr(p1)) # >> repr(p1): Point(1, 2), created by Chris on Mar 27

filter_trial()