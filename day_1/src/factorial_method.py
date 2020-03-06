def factorial(value):
    try:
        if value > 0:
            result = 1
            for i in range(1, value + 1):
                result *= i
            return result
        elif value == 0:
            return 1
        else:
            return False
    except TypeError as e:
        print("ERROR: {}".format(e))
        return False


if __name__ == "__main__":
    result = factorial("1")
    print(result)
