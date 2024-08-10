numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in range(len(numbers)):
    if numbers[i] == 1 or numbers[i] == 0:
        continue
    for j in range(2, int(numbers[i])+1):
        if numbers[i] % j == 0:
            if j != numbers[i]:
                not_prime.append(numbers[i])
                break
            else:
                prime.append(numbers[i])
print(f' Простые числа : {prime}')
print(f' Составные числа : {not_prime}')


