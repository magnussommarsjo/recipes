"""
Examples og how to work with decorators in Python.
"""


from functools import wraps
from typing import Callable, ParamSpec, TypeVar



def basic_decorator(func):
    """Basic decorator that does nothing."""
    def wrapper(*args, **kwargs):
        print("Before function call")
        value = func(*args, **kwargs)
        print("After function call")
        return value
    return wrapper

# Type annotations for decorators
def decorator_with_type_annotations[T, **P](func: Callable[P, T]) -> Callable[P, T]:
    """Decorator with type annotations."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("Before function call")
        value = func(*args, **kwargs)
        print("After function call")
        return value
    return wrapper


# Pre-python 3.12
T = TypeVar("T")
P = ParamSpec("P")
def decorator_with_type_annotations_v2(func: Callable[P, T]) -> Callable[P, T]:
    """Decorator with type annotations."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("Before function call")
        value = func(*args, **kwargs)
        print("After function call")
        return value
    return wrapper

def decorator_with_arguments(statement: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator with arguments"""
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            print(statement)
            return func(*args, **kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    @basic_decorator
    def my_function():
        print("Inside my_function")
    
    @decorator_with_type_annotations
    def add(a: int, b: int) -> int:
        return a + b

    my_function()
    add(1, 2)
