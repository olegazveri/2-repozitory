print ("Текстовый квест")
print ("Вы оказались в подземелье, где обитают страшные монстры.Чтобы выбраться оттуда вам нужно войти в один из трёх порталов. 1 большой и ярко светится, 2 синего цвета и в виде тругольника, 3 небольшой и красного цвета.")
print ("В какой портал войдёте?")
a = input()
if a == "1":
    print ("Вы попали в пустоту и ваше сознание не смогло справиться с сильным отчаянием, после чего вы погибли")
if a == "3":
    print ("Вы спокойно покинули подземелье. Проснувшись дома в кровати вы забили об этом подземелье как о страшном сне.")
elif a == "2":
    print ("Вы оказались на земле,НО она уже не такая как прежде и здесь бродят монстры.")
    print ("Перед вами находятся два монстра. Первый с мечом и в броне, второй атакует огнём.Чтобы выжить вам надо выбрать монстра, которого вы сможете одолеть.")
    print ("Какой слабее,первый или второй?")
    b = input()
    if b == "первый":
        print ("Вы были правы так как он медленный и вы спокойно смогли избежать всех его ударов. Поздравляю вы выжили, но после погибли так как быстро выдохлись, а монстры решили все сразу на вас напасть")
    elif b == "второй":
        print ("Вы не смогли справиться с пламенем, которым вас окутал монстр. Вы погибли;(")
