import CsvReader


def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    c = b - a
    return c


def multiplication(a, b):
    c = a * b
    return c


def division(a, b):
    c = a / b
    return c


def square(a):
    c = a ** 2
    return c


def squareroot(a):
    c = a ** (1 / 2)
    return c


def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(b, a)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squaring(self, a):
        self.result = square(a)
        return self.result

    def squarerooting(self, a):
        self.result = squareroot(a)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)
