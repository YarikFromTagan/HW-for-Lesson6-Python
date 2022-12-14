# Задача №3 из 2-го семинара.

# Задайте список из n чисел последовательности (1 + 1/n)^n
# и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

import os
os.system("cls")

n = int(input("Для создания последовательности (1 + 1/n)^n введите n = "))

k = list(i for i in range(1, n+1))
lst_n = list(map(lambda i: (round((1 + 1 / i)**i, 2)), k)) # формирование списка последовательности (1 + 1/n)^n
dict_n = {k[i] : lst_n[i] for i in range(len(k))}

print(f"\nДля n = {n} {lst_n}")
print(f"Сумма {round(sum(lst_n), 2)}")
print("\n")

print("***Так как условие задачи и пример не совпадают,")
print("(по условию требуется задать список, а в примере выведен словарь)")
print("представлен второй вариант ответа\n")

print(f"Для n = {n} {dict_n}")
print(f"Сумма {round(sum(lst_n), 2)}")
print("\n")
