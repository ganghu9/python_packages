def add_num(x, y):
    print(f'adding {x} and {y}')

    result = x + y

    print(f'result: {result}')

    return result


def main(x0, y0):
    x1 = x0 * 3
    y1 = y0 * 4
    return add_num(x1, y1)


if __name__ == '__main__':
    a = 5
    b = 7
    c = main(a, b)
    print(f'3x{a} + 4x{b} = {c}')

