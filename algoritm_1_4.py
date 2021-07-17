# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

leter = list("abcdefghijklmnopqrstuvwxyz")
print("Введите 2 буквы английского алфавита:")
start = leter.index(input("\tпервая = "))
print("Порядковый номер:", start+1)
end = leter.index(input("\tвторая = "))
print("Порядковый номер:", end+1)
print("Букв между ними:")
if (end - start)!=0:
  print(abs(end - start)-1)
else:
  print('Введена одна и та же буква')
