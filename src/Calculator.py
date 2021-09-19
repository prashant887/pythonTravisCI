class Calculator:
    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def add(self):
        return self.numOne + self.numTwo

    def sub(self):
        return self.numOne - self.numTwo


if __name__ == '__main__':
    calc = Calculator(4, 5)
    print(calc.add())
    print(calc.sub())
