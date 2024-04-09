def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
            if operation == "add":
                print("Result:", add(num1, num2))
            elif operation == "subtract":
                print("Result:", subtract(num1, num2))
            elif operation == "multiply":
                print("Result:", multiply(num1, num2))
            elif operation == "divide":
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation")
        except ValueError:
            print("Please enter valid numbers")
        except KeyboardInterrupt:
            print("\nCalculator closed.")
            break
