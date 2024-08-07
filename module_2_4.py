numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# любое число можно представить в виде: number = X * Y
# если nuumber простое число, то в целочисленном поле X и Y, могут быть только 1 и number
# X и Y можно представить, как X = int(X/10)*10 + X % 10 и Y = int(Y/10)*10 + Y % 10
# примем factor1 = X % 10, faktor2 = Y % 10, тогда:
# number = 100 * (int(X/10) * int(Y/10)) + 10 * (factor1 * int(Y/10) + faktor2 * int(X/10)) + factor1 * faktor2))
# отсюда получаем: Y = (number - (factor1 * factor2) - 10 * factor2 * int(X)) / (100 * int(X) + 10 * factor1)
# из условия мы знаем что Х и Y целые числа, поэтому:
#создаем функцию для расчета уравнения 
#где:  
#  number - это число, которое будет проверяться на простоту
#  factor1 и factor2 - это цифры в конце множетелей проверяемого на простоту числа, 
#  при умножении которых в конце числа может быть 1,3,7,9
#  x - это целочисленный множитель 

def equation(number, factor1, factor2, x):
   result = (number - (factor1 * factor2) - 10 * factor2 * x) / (100 * x + 10 * factor1)
   return result

#перебираем все числа в списке
for i in range(len(numbers)):
  x=1
  #исключаем 1 и 0
  if numbers[i] == 1 or numbers[i] == 0:
    continue
  #Вносим в список primes простые числа меньше 10
  if numbers[i] == 2 or numbers[i] == 3 or numbers[i] == 5 or numbers[i] == 7:
    primes.append(numbers[i])
    continue
  #вносим в список not_primes четные числа кроме 2 и числа оканчивающиеся на 5 и 0
  if (numbers[i] != 2 and numbers[i] % 2 == 0):
    not_primes.append(numbers[i])
    continue
  #вносим в список not_primes числа оканчивающиеся на 5 и 0
  if numbers[i] % 10 == 5 or numbers[i] % 10 == 0:
    not_primes.append(numbers[i])
    continue
    #проверяем делимость на простые числа 3 и 7
  if numbers[i] % 3 == 0 or numbers[i] % 7 == 0:
    not_primes.append(numbers[i])
    continue
  #простые числа могут оканчиваться только на 1, 3, 7, 9
  #если число окончивается на 1 то множители данного числа должны оканчиваться
  #на 1 и 1 или 3 и 7 или 9 и 9
  if numbers[i] % 10 == 1:
    factors1 = [1, 3, 9]
    factors2 = [1, 7, 9]
    # перебираем все целочисленные множетели x, которые меньше чем проверяемое число деленное на 7
    while x < numbers[i]/7:
      for j in range(len(factors1)):
        if equation(numbers[i], factors1[j], factors2[j], x) %1 == 0:
          if equation(numbers[i], factors1[j], factors2[j], x) != 0:
            flag = True
            x += 1
            break
        else:
          x += 1
          flag = False
  #если число окончивается на 3 то множители данного числа должны оканчиваться
  #на 1 и 3 или 9 и 7 
  if numbers[i] % 10 == 3:
    factors1 = [1, 3]
    factors2 = [3, 7]
    while x < numbers[i]/7:
      for j in range(len(factors1)):
        if equation(numbers[i], factors1[j], factors2[j], x) %1 == 0:
          flag = True
          x += 1
          break
        else:
          x += 1
          flag = False
  #если число окончивается на 7 то множители данного числа должны оканчиваться
  #на 1 и 7 или 3 и 9 
  if numbers[i] % 10 == 7:
    factors1 = [1, 3]
    factors2 = [7, 9]
    while x < numbers[i]/7:
      for j in range(len(factors1)):
        if equation(numbers[i], factors1[j], factors2[j], x) %1 == 0:
          flag = True
          x += 1
          break
        else:
          x += 1
          flag = False
  #если число окончивается на 9 то множители данного числа должны оканчиваться
  #на 1 и 9 или 3 и 3 или 7 и 7 
  if numbers[i] % 10 == 9:
    factors1 = [1, 3, 7]
    factors2 = [9, 3, 7]
    while x < numbers[i]/7:
      for j in range(len(factors1)):
        if equation(numbers[i], factors1[j], factors2[j], x) %1 == 0:
          flag = True
          x += 1
          break
        else:
          x += 1
          flag = False
  if flag == True:
    not_primes.append(numbers[i])
    continue
  else:
    primes.append(numbers[i])
print(f' prime = {primes}')
print(f' not_prime = {not_primes}')