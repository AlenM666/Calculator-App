# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2
    def minus(self, num1, num2):
        return num1 - num2
    def krat(self,num1, num2):
        return num1 * num2
    def deljeno(self, num1, num2):
        return num1 / num2



c = Calculator(5, 5)
while True:
    print("1. Plus")
    print("2. Minus")
    print("3. Množenje")
    print("4. Delenje")
    choice = int(input('Choice (1/2/3/4): '))
    if choice not in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == 1:
            print(num1, '+', num2, '=', c.add(num1, num2))
        elif choice == 2:
            print(num1, '-', num2, '=', c.minus(num1, num2))
        elif choice == 3:
            print(num1, '*', num2, '=', c.krat(num1, num2))
        elif choice == 4:
            print(num1, '/', num2, '=', c.deljeno(num1, num2))

        next_calculation = input("lets do next calculation? (yes/no): ")
        if next_calculation == "no":
            exit()
    else:
        continue







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
