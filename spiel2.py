import random

tries= 0
tries2= 110
55
def is_valid(user_input):
    if user_input.isdigit():
        user_number= int(user_input)
        if user_number >= 1 and user_number <= max_number:
            return True
        else:
            return False
    else:
        return False
print("Введите максимальный предел угадываемого числа")
max_number = int(input())
secret_number= random.randint(1, max_number)
print('Добро пожаловать в игру "Угадай число"')



while True:


    print("Введите число от 1 до ", max_number)
    user_input = input()





    if not is_valid(user_input):
        continue

    user_number= int(user_input)

    tries += 1


    if secret_number > user_number:
        print("Загаданное число больше введённого")
    elif secret_number < user_number:
        print("Загаданное число меньше введённого")
    else:
        beg= 0
        end = max_number
        while True:

            number3= end - (end - beg) // 2
            beg != end != number3



            if secret_number > number3:
                beg= end - (end - beg) // 2
                number3= beg
                tries2 += 1

            elif secret_number < number3:
                end= beg + (end - beg) // 2
                number3= end
                tries2 += 1
            tries2 += 1
            print("Ура! Вы угадали загаданное число.")
            print(
                "Минимальное количество попыток,которое бы вам потребовалось при поиске с использованием логики среднего числа:", tries2)
            print("Вам потребовалось", tries, "попыток.")
            break
        print("Сыграйте ещё раз!")
        print("Введите максимальный предел угадываемого числа")