#python es una ... no te deja iterar mas de 1000 veces por alguna razon

def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def number_e(ite: int):
    e = 1
    for i in range(1,ite):
        e += 1/factorial(i)
    return e

print(number_e(int(input())))
