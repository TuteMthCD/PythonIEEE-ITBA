
def lothar(number: int):
    counter = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        counter += 1

    return counter

count = lothar(int(input()))
print(count)
