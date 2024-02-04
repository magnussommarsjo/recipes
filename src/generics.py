"""
Examples of how to use generics in Python.

Many of these examples requires Python 3.12 or later.
"""


from typing import Generic, TypeVar



# Gneric functions =====================================================================
def add[T](a: T, b: T) -> T:
    """Generic add method that reuires same type on both arguments.
    
    Returns same type as input arguments.
    """
    return a + b

# Pre python 3.12
U = TypeVar("U")
def add_v2(a: U, b: U) -> U:
    """Generic add method that reuires same type on both arguments.
    
    Returns same type as input arguments.
    """
    return a + b

# Generic classes ======================================================================
class Box[T]:
    """Generic class that can hold any type of value."""
    def __init__(self, value: T):
        self.value = value
    
    def return_value(self) -> T:
        return self.value

# Pre python 3.12
class Box_v2(Generic[U]):
    """Generic class that can hold any type of value."""
    def __init__(self, value: U):
        self.value = value
    
    def return_value(self) -> U:
        return self.value



if __name__ == "__main__":
    int_value = add(1, 2)
    str_value = add("a", "b")

    box_int = Box(1)
    box_value = box_int.return_value()
