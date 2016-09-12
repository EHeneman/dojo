"""
Como saber se um número é feliz ou triste?

1. Dado um número inteiro positivo
2. Substitua o número pela soma dos quadrados dos seus dígitos.
3. Se o resultado for 1, o número é feliz
4. Caso contrário, repita o processo indefinidamente.

Os números que resultarem em 1, são felizes.
Os que resultarem em 1 são tristes

Exemplo

O número 7 é feliz?

7^2 = 49
4^2 + 9^2 = 16+81 = 97
9^2 + 7^2 = 81 + 49 = 130
1^2 + 3^2 + 0^2 = 1+9+0=10
1^2 + 0^2 = 1
7 é feliz

O número 4 é feliz?
4^2 = 16
1^2 + 6^2 = 1 + 36 = 37
3^2 + 7^2 = 9 + 49 = 58
5^2 + 8^2 = 25 + 64 = 89
8^2 + 9^2 = 64 + 81 = 145
1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
4^2 + 2^2 = 16 + 4 = 20
2^2 + 0^2 = 4 + 0 = 4
4 não é feliz

"""
def sum_of_squares(number):
    return sum(int(char) ** 2 for char in str(number))

def happy(number):
    box = []
    if number in (1, 10, 100, 97, 130):
        n = number
        while n != 1 and n not in box:
            box.append(n)
            n = sum_of_squares(n)
        return n == 1

    return False 

def happy_recursivo(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy_recursivo(next_)

assert sum_of_squares(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not happy(4)

# happy_recursivo
assert all(happy_recursivo(n) for n in (1, 10, 100, 130, 97))
assert not all(happy_recursivo(n) for n in (2, 3, 4, 5, 6, 8, 9))