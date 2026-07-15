"""def my_decorator(func):
    def wrapper():
        print("Function shuru ho raha hai")
        func()
        print("Function khatam ho gaya")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
"""




"""def outer():
    print("Outer function shuru")

    def inner():
        print("Inner function chal raha hai")

    inner()   # andar hi call kar diya

outer()
"""



"""import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time liya: {end - start} seconds")
    return wrapper


@measure_time
def slow_function():
    time.sleep(2)   # 2 second ruk jao
    print("Function complete hua")

slow_function()"""



"""def log_activity(func):
    def wrapper(a, b):
        print(f"{func.__name__} chal raha hai")
        result = func(a, b)
        print(f"{func.__name__} complete ho gaya")
        return result
    return wrapper


@log_activity
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))





def log_activity(func):
    def wapper(x, y):
        print(f"{func.__name__} chal raha hai")
        result = func(x, y)
        print(f"{func.__name__} complete ho gaya")
        return result
    return wapper


@log_activity
def multiply_numbers(x, y):
    return x * y


print(multiply_numbers(5, 4))
"""
