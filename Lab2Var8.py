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
    print ("Глянь какой красивый квадрат Полиби")
    polibi = {"А":"11", "Б":"12", "В":"13",
    "Г":"14", "Д":"15", "Е":"16", "Ё":"21",
    "Ж":"22", "З":"23", "И":"24","Й":"25",
    "К":"26", "Л":"31", "М":"32", "Н":"33",
    "О":"34", "П":"35", "Р":"36", "С":"41",
    "Т":"42", "У":"43", "Ф":"44", "Х":"45",
    "Ц":"46", "Ч":"51", "Ш":"52", "Щ":"53",
    "Ъ":"54", "Ы":"55", "Ь":"56", "Э":"61",
    "Ю":"62", "Я":"63"}
    print(polibi)
    word = input("Введите строку, которую нужно расшифровать: ")
    def decode(word):
        new_txt = ""
        list_fraze = []
        step = 2
        for i in range(0, len(word), 2):
            list_fraze.append(word[i:step])
            step += 2
        key_polibi_list = list(polibi.keys())
        val_polibi_list = list(polibi.values())  
 
        for x in list_fraze:
            if x in val_polibi_list:
                i = val_polibi_list.index(x)
                new_txt += key_polibi_list[i]
            else:
                new_txt += x[0:1]
        return new_txt
    new_word = decode(word)
    print (new_word)