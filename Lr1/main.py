
def calculate(x, y, op):
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            print('Invalid input operation')

if __name__ == '__main__':
    print(calculate(1, 2, '+'))

