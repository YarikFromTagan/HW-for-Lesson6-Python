# Задача №2 ко 2-му семинару
# 
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system("cls")

def Fact(n):    
    factorial = lambda n: 1 if n <=1 else n * factorial(n-1)
    return factorial(n)

n = int(input("Введите N = "))
k = [i for i in range(1, n+1)]    
lst_f = list(map(Fact, k))    

print('\n')
print(lst_f)
print('\n')