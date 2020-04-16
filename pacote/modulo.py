def sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

if __name__ == '__main__':
    print(sum(1, 2))
    print(sum(2,3, 90))
    print(sum(1, 1))



