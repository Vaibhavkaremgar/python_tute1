def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()

# This code defines a simple decorator that wraps a function to add behavior before and after its execution.
# When the decorated function is called, it will print messages before and after the original function's execution.
