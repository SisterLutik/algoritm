import random

print("Введите диапазон для генерации случайного целого числа:")
start = int(input("\tначало = "))
end = int(input("\tконец = "))
print("Случайное целое число: ", random.randint(start, end))
print("Введите диапазон для генерации случайного вещественного числа:")
start = float(input("\tначало = "))
end = float(input("\tконец = "))
print("Случайное вещественное число: ", random.uniform(start, end))

leter = list("abcdefghijklmnopqrstuvwxyz")
print("Введите диапазон (буквенный) для генерации случайной буквы английского алфавита:")
start = leter.index(input("\tначало = "))
end = leter.index(input("\tконец = "))
ind = random.randint(start, end)
print("Случайная буква: ",leter[ind])