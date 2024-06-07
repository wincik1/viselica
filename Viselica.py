import os
import random

clear = lambda: os.system("cls")

words = ["банан","бургер","квиз","мышь","море","квокка","операция",]
word = random.choice(words)

print("Привет! Я загадал слово, а ты должен угадать его по буквам")
input("Нажми Enter чтобы продолжить")
clear()
print("Начинаем!")

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    print(f"Использованные буквы: {letters}")
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print('*', end=" ")
            isWin = False
    print()
    if isWin == True:
        print("Ты угадал!")
        break
    letter = input("Введите букву: ")
    letters.append(letter)
    clear()
    if letter not in word:
        hp -= 1
        print(f"Осталось попыток: {hp}")

    if hp == 0:
       print('Ты проиграл!')
