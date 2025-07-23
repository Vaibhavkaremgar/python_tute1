def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")   
if __name__ == "__main__":
    greet("Alice")  

