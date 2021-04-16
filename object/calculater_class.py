class Calculator:
    def __init__(self, num = 0):
        self.result = num

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator(3)

print(cal1.add(3))
