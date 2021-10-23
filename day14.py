class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class NewCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        result = self.first // self.second
        return result

while True:
    num1 = float(input("숫자1:"))
    op = input("+,-,*,/,** 중 택1:")
    num2 = float(input("숫자2:"))

    if op == "+":
        a = NewCal(num1,num2)
        print(a.add())
    elif op == "-":
        b = NewCal(num1,num2)
        print(b.sub())
    elif op == "*":
        c = NewCal(num1,num2)
        print(c.mul())
    elif op == "**":
        d = NewCal(num1,num2)
        print(d.pow())
    else:
        e = NewCal(num1,num2)
        print(e.div())

    print("")





