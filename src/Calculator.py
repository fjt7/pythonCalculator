from Csv.Csv import CsvReader
import math


# Functions for addition, subtraction, multiplication, division, square, and square root

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = float(a)
    b = float(b)
    c = round(b / a, 9)
    return c


def square(a):
    a = int(a)
    b = a * a
    return b


def squareroot(a):
    return round(math.sqrt(float(a)), 9)  # Second Parameter Rounds By (Decimal Places)


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
        self.result = subtraction(a, b)
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
