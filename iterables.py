"""#iterator
nums = [1,2,3,4]
it = iter(nums)

print(it.__next__())
#print(it.__next__())
#print(it.__next__())
#print(it.__next__())
print(next(it))

#user defined or custom object/class iterator
class First_ten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration
    
values = First_ten()
print(values.__next__())
print(values.__next__())

print(next(values))
print("continue from 4 down")
for i in values:
    print(i)
"""
#Generators
# 1st e.g
"""
def first_ten():
    #return 5
    yield 1
    yield 2
    yield 3
    yield 4

values = first_ten()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print("continue till the end")
#using for loop to execute
for i in values:
    print(i)

# 2nd eg

def first_ten():
    k = 1

    while k <= 10:
        ans = k*k
        yield ans
        k += 1

values = first_ten()

for i in values:
    print(i)
"""

# 3rd eg
"""def my_generator():
    n = 1
    print('this is printed first')
    yield n

    n += 1
    print('this is printed second')
    yield n

    n += 1
    print('this is printed last')
    yield n

a = my_generator()

next(a)
next(a)
next(a)

print("Using for loop...")
for item in my_generator():
    print(item)
"""
# 4th eg    
"""
def countdown(n):
    print("Starting countdown!")
    while n > 0:
        print('hi')
        yield n   # Pause and return the current value of n
        n -= 1    # Decrease n by 1
    print("Countdown finished!")

# Create the generator
c = countdown(3)

# Call next() manually
print(next(c))  # Outputs: Starting countdown! 3
print(next(c))  # Outputs: 2
print(next(c))  # Outputs: 1

# If you call next(c) again here, it will raise StopIteration

# Using a for loop
print("Using for loop...")
for num in countdown(3):
    print(num)
"""

# decorators
# 1st eg
"""
'''
def div(a,b):
    #originally, there is no if statement to do the swapping so that the order will always be 'a' > 'b'
    #if a<b: doing this means u have to modify the code to include the if block
    #    a,b = b,a
    print(a/b)

div(2,4)
# we can use decorators to achieve the same purpose without modifying the div funtion
'''


def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div1 = smart_div(div)
div1(2,4)
"""
# 2nd eg
"""
def my_deco(func):
    def inner_func():
        print("I got decorated")
        func()
    return inner_func

def simple_func():
    print("i am a simple func")

decor = my_deco(simple_func)
decor()

# or we use the @decorator syntax
def my_deco(func):
    def inner_func():
        print("I got decorated")
        func()
    return inner_func

@my_deco
def simple_func():
    print("i am a simple func")

simple_func()
"""
