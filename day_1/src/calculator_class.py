class Calculator:


    def check_type(self, a, b):
        if type(a) not in [int, float] or type(b) not in [int, float]:
            return False

    def add(self, a, b):
        if not self.check_type(a, b):
            return False
        return a + b

    def sub(self, a, b):
        if not self.check_type(a, b):
            return False
        return a - b

    def mul(self, a, b):
        if not self.check_type(a, b):
            return False
        return a * b

    def div(self, a, b):
        if not self.check_type(a, b):
            return False
        if b == 0:
            return False
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.mul(5, 4))
