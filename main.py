def eratosthenes(n):
    # Создаем список чисел от 2 до n
    numbers = list(range(2, n + 1))
    primes = []

    while len(numbers) > 0:
        # Берем первое число из списка и добавляем его в список простых чисел
        prime = numbers[0]
        primes.append(prime)

        # Удаляем все числа, кратные текущему простому числу
        numbers = [x for x in numbers if x % prime != 0]

    return primes


n = int(input("Введите натуральное число: "))
result = eratosthenes(n)
print("Простые числа до", n, ":", result)

