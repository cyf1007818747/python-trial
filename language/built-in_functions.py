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

# int -> str
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

def float_trial():
    print('float(1):', float(1)) # >>: 1.0
    print('float("1.1"):', float("1.1")) # >>: 1.1
    try:
        print('float("1.1a"):', float("1.1a")) # raises error
    except ValueError as e:
        print('error calling float("1.1a"):', e)
    print('float("1.1e2"):', float("1.1e2")) # >>: 110.0 # *
    print('float("1.1E-003"):', float("1.1E-003")) # >>: 0.0011 # *
    print('float("  1.1e+2\n "):', float("  1.1e+2\n ")) # >>: 110.0 # spaces and newlines are ignored
    print('float("nan"):', float("nan")) # >>: nan
    print('float("inf"):', float("inf")) # >>: inf
    print('float("-InFiNity"):', float("-InFiNity")) # >>: -inf # case-insensitive
    
# case insensitive
# format returns a string !!
def format_trial():
    print('format(123, "d"):', format(123, "d")) # >>: 123 # decimal representation
    print('format(123, "x"):', format(123, "x")) # >>: 7b # hexadecimal
    print('format(123, "b"):', format(123, "b")) # >>: 1111011 # binary # *
    print('format(123, "o"):', format(123, "o")) # >>: 173 # octal
    print('format(123, "e"):', format(123, "e")) # >>: 1.230000e+02 # *
    print('format(123456, "0.3e"):', format(123456, "0.3e")) # >>: 1.235e+05
    print('format(123, "f"):', format(123, "f")) # >>: 123.000000
    print('format(123, "0.4f"):', format(123, "0.4f")) # >>: 123.0000 # *
    print('format(123, "g"):', format(123, "g")) # >>: 123 # general format
    print('format(123, "n"):', format(123, "n")) # >>: 123 # number format
    print('-----------------')
    print('"ab {:8} cd".format(123):', "ab {:8} cd".format(123)) # >>: ab      123 cd # *
    print('"ab {:<8} cd".format(123):', "ab {:<8} cd".format(123)) # >>: ab 123      cd
    print('"ab {:<8} cd".format(123456):', "ab {:<8} cd".format(123456)) # >>: ab 123456  cd
    print('"ab {:>8} cd".format(123):', "ab {:>8} cd".format(123)) # >>: ab      123 cd
    print('"ab {:^8} cd".format(123):', "ab {:^8} cd".format(123)) # >>: ab   123    cd
    # Places the sign to the left most position
    print('"ab {:=8} cd".format(-123):', "ab {:=8} cd".format(-123)) # >>: ab -    123 cd
    print('"ab {:+8} cd".format(123):', "ab {:+8} cd".format(123)) # >>: ab     +123 cd
    # Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
    print('"ab {: } cd".format(123):', "ab {: } cd".format(123)) # >>: ab  123 cd
    print('"ab {: } cd".format(-123):', "ab {: } cd".format(-123)) # >>: ab -123 cd
    print('"ab {:,} cd".format(12345678):', "ab {:,} cd".format(12345678)) # >>: ab 12,345,678 cd
    print('"ab {:_} cd".format(123):', "ab {:_} cd".format(12345678)) # >>: ab 12_345_678 cd
    # the meanings of combinations are very case specific
    print('"ab {:,<8} cd".format(12345):', "ab {:,<8} cd".format(12345)) # >>: ab 12345,,, cd
    print('"ab {:b} cd".format(123):', "ab {:b} cd".format(123)) # >>: ab 1111011 cd # *
    # the rest is the same as the first few lines above
 
# the attribute argument is a string
def getattr_trial():
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj1 = MyClass()
    print('getattr(obj1, "a"):', getattr(obj1, "a")) # >>: 1
    # *
    try:
        print('getattr(obj1, "c"):', getattr(obj1, "c"))
    except AttributeError as e:
        print('Error:', e) # >> Error: 'MyClass' object has

def globals_trial():
    # the returned type is dict[str, Any]
    print('globals():', globals()) # a dictionary of global variables

def hasattr_trial():
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj1 = MyClass()
    print('hasattr(obj1, "a"):', hasattr(obj1, "a")) # >>: True
    print('hasattr(obj1, "c"):', hasattr(obj1, "c")) # >>: False

def hash_trial():
    print('hash(1):', hash(1)) # >>: 1
    print('hash("abc"):', hash("abc")) # >>: 542026347
    print('hash((1, 2, 3)):', hash((1, 2, 3))) # >>: 2528502973977326415
    try:
        print('hash([1, 2, 3]):', hash([1, 2, 3]))
    except TypeError as e:
        print('Error:', e) # Error: unhashable type: 'list'
        
def hex_trial():
    print('hex(-10):', hex(-10)) # >>: -0xa
    print('hex(17):', hex(17)) # >>: 0x11

def id_trial():
    a = 1
    b = 1
    print('id(a):', id(a)) # >>: 4375034912
    print('id(b):', id(b)) # >>: 4375034912
    print('id(1):', id(1)) # >>: 4375034912
    print('id(1.0):', id(1.0)) # >>: 4377989840
    print('id("abc"):', id("abc")) # >>: 4374579320
    print('id("abc"):', id("abc")) # >>: 4374579320
    print('id("abc"): ', id("ab"+"c")) # >>: 4374579320

def input_trial():
    print('input("Enter a number: ")') # waits for input
    num = input("Enter a number: ")
    print('num:', num)
    import sys
    print("Enter your paragraph. Signal EOF with Ctrl+D (or Ctrl+Z on Windows) when done:")
    paragraph = sys.stdin.read()
    print("\nYou entered:")
    print(paragraph)

def int_trial():
    print('int(1.1):', int(1.1)) # >>: 1
    print('int("1234"):', int("1234")) # >>: 1234
    print('int("1_234"):', int("1_234")) # >>: 1234 # *
    # // print('int("0b10000"):', int("0b10000")) !! raises error (see the next line)
    # when and ONLY when you specify base = 0 can you use prefix in string to specify base (like below) # *
    print('int("0b10000"):', int("0b10000", 0))
    print('int("0x10000"):', int("0x10000", 0))
    # print('int("1,234"):', int("1,234")) !! raises error
    print('int("256", 16):', int("256", 16)) # >>: 598
    # // print('int(100, 16):', int(100, 16)) !! raises error since 100 is not str while base is given
    # the second arg base means the given string is represented in that base # *
    print('int("-100", 16):', int("-100", 16)) # >>: -256 # *
    # // print('int("-100", -16):', int("-100", -16)) # raises error: base can only be >= 2 and <= 36, or 0
    print('int("-100", 0):', int("-100", 0))

def isinstance_trial():
    class MyClass:
        pass

    obj1 = MyClass()
    print('isinstance(obj1, MyClass):', isinstance(obj1, MyClass)) # >>: True
    print('isinstance(obj1, int):', isinstance(obj1, int)) # >>: False
    print('isinstance(1, int):', isinstance(1, int)) # >>: True
    print('isinstance(1, (int, float)):', isinstance(1, (int, float))) # >>: True # *
    print('isinstance(1.5, int | float):', isinstance(1.5, int | float)) # >>: True # *
    print('isinstance(1, int | MyClass):', isinstance(1, int | MyClass)) # >>: True
    print('isinstance(1.5, int | MyClass):', isinstance(1.5, int | MyClass)) # >>: False

def issubclass_trial():
    class MyClass:
        pass

    class MySubClass(MyClass):
        pass

    print('issubclass(MySubClass, MyClass):', issubclass(MySubClass, MyClass)) # >>: True # *
    print('issubclass(MySubClass, MyClass):', issubclass(MyClass, MySubClass)) # >>: False
    print('issubclass(MySubClass, int):', issubclass(MySubClass, int)) # >>: False
    print('issubclass(MySubClass, object):', issubclass(MySubClass, object)) # >>: True # *
    print('issubclass(int, object):', issubclass(int, object)) # >>: True # *
    print('issubclass(MySubClass, int | MyClass):', issubclass(MySubClass, int | MyClass)) # >>: True
    print('issubclass(int, MyClass | float):', issubclass(int, MyClass | float)) # >>: False

def len_trial():
    print('len([1, 2, 3]):', len([1, 2, 3])) # >>: 3
    print('len("abc"): ', len("abc")) # >>: 3
    print('len({}):', len({})) # >>: 0
    try:
        print('len(1):', len(1)) # raises error # *
    except TypeError as e:
        print('Error:', e)
    try:
        print('len(range(2**100)):', len(range(2**100))) # raises error
    except OverflowError as e:
        print('Error:', e)
    except Exception as e: # this is to catch all other exceptions # *
        print('Error-:', e)

def locals_trial():
    # the returned type is dict[str, Any]

    a = 1
    mystr = "csfbvser"
    myarr = [1,2,3]
    print('locals() in parent func:', locals()) # a dictionary of local variable
    
    def nested_func():
        b = 2
        print('locals() in nested func:', locals())
        myarr.append(4)

    nested_func()

    if True:
        c = 3
        print('locals() in if block:', locals())

def map_trial():
    list1 = [1, 2, 3]

    map(lambda x: x, list1) # does not change the list
    print('list1:', list1) # >>: [1, 2, 3]

    list1_mapped0 = map(lambda x: x, list1)
    print('list1_mapped0:', list1_mapped0) # >>: <map object at 0x10ea8b4c0>

    list1_mapped1 = list(map(lambda x: x, list1)) # have to wrap with a list # *
    print('list1_mapped1:', list1_mapped1) # >>: [1, 2, 3] 

    list1_mapped2 = list(map(lambda x: x + 1, list1)) # *
    print('list1_mapped2:', list1_mapped2) # >>: [2, 3, 4]
    
    def square(x):
        return x * x

    list1_mapped3 = list(map(square, list1))
    print('list1_mapped3:', list1_mapped3) # >>: [1, 4, 9]

    list1_mapped4 = [item*6 for item in list1 if item % 2 == 1] # *
    print('list1_mapped4:', list1_mapped4) # >>: [6, 18]

# If multiple items are maximal, the function returns the first one encountered
def max_trial():
    print('max(1, 2, 3):', max(1, 2, 3)) # >>: 3
    print('max([1, 2, 3]):', max([1, 2, 3])) # >>: 3
    print('max("abc"): ', max("abc")) # >>: c # *
    list0 = range(100, 200)
    print('max(list0):', max(list0)) # >>: 199
    print(max(list0, key=lambda x: x % 10)) # >>: 109 # *

# min_trial is similar to max_trial

# int -> str
def oct_trial():
    print('oct(-10):', oct(-10)) # >>: -0o12
    print('oct(17):', oct(17)) # >>: 0o21

def open_trial(file_format):
    if file_format == 'txt':
        with open('../resources/test-text.txt', 'r') as file: # *
            print('file:\n', file) 
            # read 100 characters. If no arg, read the whole file # *
            file_read = file.read(100)
            print('file_read:\n', file_read) 
            print('-----------------')
            for line in file: # starts at the end of file_read  # *
                print(line, end='')
            print()

    if file_format == 'json':
        with open('../resources/package.json', 'r') as file:
            import json
            json_data = json.load(file)
            print('json_data:\n', json_data)
            print('len(json_data):', len(json_data))
            # // print('json_data[scripts]:', json_data[scripts]) invalid
            print('json_data["scripts"]:\n', json_data["scripts"])
            print('json_data["scripts"]["build]:\n', json_data["scripts"]["build"])

            json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
            json_data2 = json.loads(json_string) # NOTE: it is loads here, where s represents string
            print('json_data2["name"]:', json_data2["name"])

    if file_format == 'csv':
        import csv
        with open('../resources/example.csv', 'r') as file:
            csv_reader = csv.reader(file)
            # for row in csv_reader:
            #     print(row)
            #     print('row[0]:', row[0])

            for i in range(2):
                next(csv_reader)

            for i, row in enumerate(csv_reader):
                print(i, '--', row[2])

    if file_format == 'binary':
        with open('../resources/test-image.png', 'rb') as file:
            print('file:\n', file)
            file_read100 = file.read(100)
            print('file_read100:\n', file_read100)
            print('---- rest of the file ----')
            # print(file.read()) # very large output
            # for item in file:
            #     print(len(item))
    
    if file_format == "txt-append":
        import datetime
        with open('../resources/test-text.txt', 'a') as file:
            file.write("File appended by Chris at "+str(datetime.datetime.now())+"\n")
    
def ord_trial():
    print('ord("A"):', ord("A")) # >>: 65
    print('ord("a"):', ord("a")) # >>: 97
    print('ord("€"):', ord("€")) # >>: 8364
    # // print('ord("abc"):', ord("abc")) # raises error

def pow_trial():
    print('pow(2, 3):', pow(2, 3)) # >>: 8
    print('2**5:', 2**5) # >>: 32
    print('pow(2, 3, 5):', pow(2, 3, 5)) # >>: 3 # 2^3 % 5 = 8 % 5 = 3

def print_trial():
    print('abc', 'def', 'ghi') # >>: abc def ghi
    print('abc', 'def', 'ghi', sep=', ') # >>: abc, def, ghi
    print('abc', 'def', 'ghi', end='---') # >>: abc def ghi---
    print('abc', 'def', 'ghi', sep='-', end='\n\n\n') # >>: abc-def-ghf 
    # print with file arg
    import sys
    # // print('print to file test 1:', file=sys.stdin) raises error
    print('print to file test 2', file=sys.stdout)
    print('print to file test 3', file=sys.stderr)
    # txt_file = open('../resources/test-text.txt', 'w') !! this will overwrite the whole file
    txt_file = open('../resources/test-text.txt', 'a')
    print('print to file test 4', file=txt_file)

# range trial is omitted
    
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
    
def reversed_trial():
    list1 = [1, 2, 3]
    print('reversed(list1):', reversed(list1)) # >>: <list_reverseiterator object at 0x10f9a1d20>
    list1_reversed = list(reversed(list1))
    print('list1_reversed:', list1_reversed) # >>: [3, 2, 1]

def round_trial():
    print('round(1.1):', round(1.1)) # >>: 1
    print('round(1.5):', round(1.5)) # >>: 2
    print('round(1.6):', round(1.6)) # >>: 2
    print('round(1.123456, 3):', round(1.123456, 3)) # >>: 1.123
    print('round(1.128456, 2):', round(1.128456, 2)) # >>: 1.13
    print('round(1.123456, 0):', round(1.123456, 0)) # >>: 1.0
    print('round(1234.5678):', round(1234.5678)) # >>: 1235
    print('round(1234.5678, -3):', round(1234.5678, -3)) # >>: 1000.0

def setattr_trial():
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj1 = MyClass()
    obj1.a = 10
    print('obj1.a:', obj1.a) # >>: 10
    setattr(obj1, 'a', 100)
    print('obj1.a:', obj1.a) # >>: 100

def slice_trial():
    list1 = [1, 2, 3, 4, 5]
    print('list1[1:3]:', list1[1:3]) # >>: [2, 3]
    print('list1[1:]:', list1[1:]) # >>: [2, 3, 4, 5]
    print('list1[:3]:', list1[:3]) # >>: [1, 2, 3]
    print('list1[:]:', list1[:]) # >>: [1, 2, 3, 4, 5]
    print('list1[1:4:2]:', list1[1:4:2]) # >>: [2, 4] # *
    print('list1[::2]:', list1[::2]) # >>: [1, 3, 5] # *
    print('list1[::-1]:', list1[::-1]) # >>: [5, 4, 3, 2, 1] # *
    print('list1[::-2]:', list1[::-2]) # >>: [5, 3, 1] # *

def sorted_trial():
    list2 = ['b', 'a', 'c']
    print('sorted(list2):', sorted(list2)) # >>: ['a', 'b', 'c'] !! does not modify list2
    print('sorted(list2, reverse=True):', sorted(list2, reverse=True)) # >>: ['c', 'b', 'a']
    list3 = ["apple", "banana", "blueberry", "cherry", "orange","e", "d", "d", "apricot"]
    list3_sorted = sorted(list3, key=lambda s: (s[0], -ord(s[1]) if len(s) > 1 else 0)) # *
    print('list3_sorted:', list3_sorted)
    
def str_trial():
    print('str(1):', str(1)) # >>: 1
    print('str(1.1):', str(1.1)) # >>: 1.1
    print('str([1, 2, 3]):', str([1, 2, 3])) # >>: [1, 2, 3]
    map1 = {"a": 1, "b": 2}
    print('str(map1):', str(map1)) # >>: {'a': 1, 'b': 2} # *
    print('str((1, 2, 3)):', str((1, 2, 3))) # >>: (1, 2, 3)
    print('str(True):', str(True)) # >>: True
    print('str(False):', str(False)) # >>: False
    
def sum_trial():
    list1 = [1, 2, 3]
    print('sum(list1):', sum(list1)) # >>: 6
    print('sum(list1, 10):', sum(list1, 10)) # >>: 16

def super_trial():
    class Parent:
        def __init__(self):
            self.a = 1
            self.b = 2

    class Child(Parent):
        def __init__(self):
            super().__init__() # *
            self.c = 3

    obj1 = Child()
    print('obj1.a:', obj1.a) # >>: 1
    print('obj1.b:', obj1.b) # >>: 2
    print('obj1.c:', obj1.c) # >>: 3

def tuple_trial():
    print('tuple([1, 2, 3]):', tuple([1, 2, 3])) # >>: (1, 2, 3)
    print('tuple("abc"): ', tuple("abc")) # >>: ('a', 'b', 'c')
    print('tuple({1, 2, 3}):', tuple({1, 2, 3})) # >>: (1, 2, 3)
    print('tuple((1, 2, 3)):', tuple((1, 2, 3))) # >>: (1, 2, 3)
    map1 = {"a": 1, "b": 2}
    print('tuple(map1):', tuple(map1)) # >>: ('a', 'b')
    print('list(map1):', list(map1)) # >>: ['a', 'b']
    print('tuple(map1.items()):', tuple(map1.items())) # >>: (('a', 1), ('b', 2))
    print('list(map1.items()):', list(map1.items())) # >>: [('a', 1), ('b', 2)] inner is still tuple # *

def type_trial():
    print('type(1):', type(1)) # >>: <class 'int'>
    print('type("abc"):', type("abc")) # >>: <class 'str'>
    print('type([1, 2, 3]):', type([1, 2, 3])) # >>: <class 'list'>
    print('type((1, 2, 3)):', type((1, 2, 3))) # >>: <class 'tuple'>
    print('type({1, 2, 3}):', type({1, 2, 3})) # >>: <class 'set'>
    print('type({1: 2, 3: 4}):', type({1: 2, 3: 4})) # >>: <class 'dict'>
    print('type(1) == int:', type(1) == int) # >>: True
    print('type({1: 2, 3: 4}) == dict:', type({1: 2, 3: 4}) == dict) # >>: <class 'dict'>

def vars_trial():
    # vars() without arg returns the local variables
    abc = 123
    de = 456
    print('vars():', vars()) # >>: {'abc': 123, 'de': 456}

    # vars() on class
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj1 = MyClass()
    print('vars(obj1):', vars(obj1)) # >>: {'a': 1, 'b': 2}

    # vars() on module
    import sys
    # print('vars(sys):\n', vars(sys))
    print('vars(sys):\n', vars(sys)['getrefcount'])

def zip_trial():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print('zip(list1, list2):', zip(list1, list2)) # >>: <zip object at 0x10f9a1d20>
    list3 = list(zip(list1, list2))
    print('list3:', list3) # >>: [(1, 'a'), (2, 'b'), (3, 'c')]
    list4 = list(zip(list1, list2, list1)) 
    print('list4:', list4) # >>: [(1, 'a', 1), (2, 'b', 2), (3, 'c', 3)]
    list5 = list(zip(list1, [6,7,8,9,10])) # lengths can be different # *
    print('list5:', list5) # >>: [(1, 6), (2, 7), (3, 8)]
    list6 = list(zip([6,7,8,9,10], [11,12,13], []))
    print('list6:', list6) # >>: []

    # use zip to transpose matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    transposed = list(map(list, zip(*matrix)))
    print('transposed:', transposed)

    transposed2 = [[row[j] for row in matrix] for j in range(len(matrix[0]))]
    print('transposed2:', transposed2)

    transposed3 = [[ matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print('transposed3:', transposed3)

zip_trial()