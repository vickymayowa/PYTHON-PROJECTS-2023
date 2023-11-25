def greet (name) : 
    print(f"Hello {name}!")

greet("Alice")

def add_numbers (a , b):
    return a * b
result = add_numbers(5 , 10)
print(result)

def min_max(numbers):
    return min(numbers), max(numbers)
    min_value , max_value = min_max([ 1 , 2 , 3, 4, 5])
    print(min_value, max_value)