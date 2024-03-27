# experimented in Python 3.12.2
# ! please arrange in alphabetical order

def all_trial():
    bool_list1 = []
    bool_list2 = [True, False]
    bool_list3 = [True, True]
    print('bool_list1:', all(bool_list1)) # >> True # *
    print('bool_list2:', all(bool_list2))
    print('bool_list3:', all(bool_list3))

def any_trial():
    bool_list1 = []
    bool_list2 = [True, False]
    bool_list3 = [True, True]
    print('bool_list1:', any(bool_list1)) # >> False # *
    print('bool_list2:', any(bool_list2))
    print('bool_list3:', any(bool_list3))

def bin_trial():
    num1 = 10
    num2 = -10
    print('num1:', bin(num1)) # >> 0b1010
    print('num2:', bin(num2)) # >> -0b1010
    # related functions
    print("---- related functios -----")
    print('format(10, "#b")', format(10, '#b')) # >> 0b1010 # *
    print('format(10, "b")', format(10, 'b')) # >> 1010 # *
    print("abc{10:#b}def:", f'abc{10:#b}def') # >> abc0b1010def # *
    print("abc{10:b}def:", f'abc{10:b}def') # >> abc1010def # *
    

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

    


bin_trial()