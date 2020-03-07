def fibonacci_1(n):
    if type(n) != int or n <= 0:
        return False

    fib_list = [0, 1]
    if n == 1:
        return fib_list[0]
    if n == 2:
        return fib_list[1]
    else:
        for i in range(n-2):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]

print(fibonacci_1(10))


def fibonacci_2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_2(n-2) + fibonacci_2(n-1)

print(fibonacci_2(10))


def fibonacci_3(n):
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b

print(fibonacci_3(10))
