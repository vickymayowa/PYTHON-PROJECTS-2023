def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't Divide by 0"
    return x / y


operation_dict = {
    "add": add,
    "subtract": subtract,
    "divide": divide,
    "multiply": multiply,
}


def main():

    while True:
        print("Options:")
        print("Enter 'add' for subtraction")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiply")
        print("Enter 'divide' for divide")
        print("Enter 'quit' to end the program")

        user_input = input("Input Your Details:")

        if user_input == "quit":
            break
        
        elif user_input in operation_dict:
          num1 = float(input("Enter the first number"))
          num2 = float(input("Enter the first number"))
          operation = operation_dict[user_input]
          result = operation(num1 , num2)
          print("Result:", result)
        else:
            print("Invalid Input")
