class Calculator:
    print("Calculator")
    print("Available operations: add, sub, mul, div")
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def cal(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"


a = float(input("Enter (a) value: "))
b = float(input("Enter  (b) value: "))
operation = input("Enter operation [add, sub, mul, div]: ")

calc = Calculator(a, b, operation)
result = calc.cal()
print("Result:", result)

