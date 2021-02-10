print ("1 - Игра угадай число")
print ("2 - создание простых функций")
print ("3 - Сортировка списка")
print ("4 - Шифрование строк")
while True:
    zad = input("Выберите номер задания:")
    if not zad.isnumeric():
        print("Введите целое число")
    else:
        zad = int(zad)
        if((zad < 1) or (zad > 4)):
            print ("Введите цифру от 1 до 4")
        else:
            break
if (zad == 1):
    from random import randint
    otv = int(randint(1,11))
    hp = 3
    while True:
        while True:
            OtvPlayer = input("Попробуйте угадать число:")
            if not (OtvPlayer.isnumeric()):
                print ("Введите целое число от 1 до 10")
            else:
                OtvPlayer = int(OtvPlayer)
                break
        count = 0
        score = 0
        if (OtvPlayer == otv):
            print ("Мои поздравления, вы угадали число")
            print("Если вы хотите выйти, то просто введите нуль, в противном случае нажмите любую клавишу")
            score+=1
            marker = input()
            if (marker == 0):
                print ("Ваш счет: ", score)
                break
            else:
                otv = int(randint(1,11))
                continue
        elif (hp != 0):
            hp-=1
            print("У вас осталось запасных жизней:", hp)
        else:
            print("GGWP, жизни кончились")
            break
if (zad==2):
    def capitalize(stroka):
        _s = stroka.title()
        return _s
    while(True):
        _stroka = input("Введите строку: ")
        if not _stroka.isdigit():
            print ("Ваша новая строка: ", capitalize(_stroka))
            break
        else:
            print("Введите строку c буквенными значениями")
if (zad == 3):
    from random import randint
    while True:
        size = input("Введите размер массива:")
        if not size.isnumeric():
            print("Введите целое число")
        else:
            size = int(size)
            break
    s = []
    i = 0
    for i in range(size):
        s.append(randint(0,100))
    for x in s:
        print(x)
    def rasch(mass):
        rasst = len(mass)
        swaps = True
        while rasst > 1 or swaps:
            rasst = max(1, int(rasst / 1.25))
            swaps = False
            for i in range(len(mass) - rasst):
                j = i + rasst
                if mass[i] > mass[j]:
                    mass[i], mass[j] = mass[j], mass[i]
                    swaps = True
        return mass
    s = rasch(s)
    print (s)
if (zad == 4):
    print("Глянь какой красивый квадрат Полибия")
    matrix =[[А, Б, В, Г, Д, Е], [Ё, Ж, З, И, Й, К], [Л, М, Н, О, П, Р], [С, Т, У, Ф, Х, Ц], [Ч, Ш, Щ, Ъ, Ы, Ь], [ Э, Ю, Я]]
    print (matrix)
   


    
