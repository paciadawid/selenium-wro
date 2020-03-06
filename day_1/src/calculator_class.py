class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.mul(5, 4))
