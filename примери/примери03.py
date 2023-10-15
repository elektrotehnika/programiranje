# -*- coding: utf-8 -*-
"""
Вежбе 3 - Примери
"""

"""
Пример 1: Разни примери поворки.
"""
#povorka = ()
#povorka = (1, )
#povorka = (1, "dva", 3.0)

#povorka1 = (1, "dva", 3.0)
#povorka = (povorka1, "cetiri")

#print(type(povorka))
#print(povorka)



"""
Пример 2: Примери операција над поворкама.
"""
#povorka1 = (1, "dva", 3.0)
#povorka2 = ("cetiri",)

#Аритметичке операције
#povorka = povorka1 + povorka2
#povorka = 3*povorka1

#Извлачење делова поворке
#povorka = povorka1[1]
#povorka = povorka1[0:1]
#povorka = povorka1[:]
#povorka = povorka1[::2]
#povorka = povorka1[::-1]

#print(povorka)

#Дужина поворке
#print(len(povorka1))

#Оператори чланства
#print(1 in povorka1)
#print(1 not in povorka1)



"""
Пример 3: Разни примери низова.
"""
#niz = []
#niz = [1]
#niz = [1, "dva", 3.0]

#niz1 = [1, "dva", 3.0]
#niz = [niz1, "cetiri"]

#print(type(niz))
#print(niz)



"""
Пример 4: Примери операција над низовима.
"""
#niz1 = [1, "dva", 3.0]
#niz2 = ["cetiri"]

#Аритметичке операције
#niz = niz1 + niz2
#niz = 3*niz1

#Извлачење делова низа
#niz = niz1[1]
#niz = niz1[0:1]
#niz = niz1[:]
#niz = niz1[::2]
#niz = niz1[::-1]

#print(niz)

#Дужина низа
#print(len(niz1))

#Оператори чланства
#print(1 in niz1)
#print(1 not in niz1)



"""
Пример 5: Понашање прослеђених објеката унутар функције.
"""
#x = 5
#x = (5,)
#x = [5]

def izmeni(x):
    x += 1
    
   
def izmeni_slozeni_objekat(x):
    x[0] += 1
 
    
def izmeni_povorku(x):
    x = x + ("član",)
    print(x)
    
#izmeni(x)
#izmeni_slozeni_objekat(x)
#izmeni_povorku(x)
#print(x)



"""
Пример 6: Промена члана низа; алијас, клонирање.
"""
#niz = [1, 2, 3]
#niz[0] = "jedan"
#niz[1] = "dva"
#niz[2] = "tri"

#x = niz
#x[0] = "jedan"

# = niz[:]
#x[0] = "jedan"

#print(x)
#print(niz)



"""
Пример 7: Коришћење функције append().
"""
#niz = [1, 2, 3]
#niz.append(4)
#niz.append(4, 5, 6)
#niz.append([4, 5, 6])

#print(niz)



"""
Пример 8: Коришћење функције remove().
"""
#niz = [1, 2, 3, 1]
#niz.remove(1)
#niz.remove(4)

#print(niz)



"""
Пример 9: Илустрациjа коришћења наредбе break кроз задатак.

Написати функцију која проверава да ли прослеђена ниска садржи 
макар једну цифру.
"""
"""
Верзија 1:
"""
def cifra_u_niski(niska):
    brojac_iteracija = 0
    cifre = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    while(brojac_iteracija < len(niska)):
        if niska[brojac_iteracija] in cifre:
            print("Niska sadrži makar jednu cifru.")
            break
        brojac_iteracija += 1
    if brojac_iteracija == len(niska):
        print("Niska ne sadrži cifre.")

#niska1 = "2drav0"
#niska2 = "Zdravo"   

#cifra_u_niski(niska1)   
#cifra_u_niski(niska2)  

"""
Верзија 2:
"""
def cifra_u_niski(niska):
    brojac_iteracija = 0
    cifre = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    while(brojac_iteracija < len(niska)):
        if niska[brojac_iteracija] in cifre:
            return True
        brojac_iteracija += 1
    return False

#niska1 = "2drav0"
#niska2 = "Zdravo"   

#print(cifra_u_niski(niska1))   
#print(cifra_u_niski(niska2))



"""
Пример 10: Понављање применом for петље.
"""
#niska = "Zdravo"
#povorka = (1, 2, 3)
#niz = [0, -1, -2]

"""
for i in niska:
    print(i)
"""

"""
for i in povorka:
    print(i)
"""

"""
for i in niz:
    print(i)
"""

"""
for i in range(5):
    print(i)
"""

"""
for i in range(-2):
    print(i)
"""

"""
for i in range(1, 10):
    print(i)
"""

"""
for i in range(-10, -5):
    print(i)
"""

"""
for i in range(10, 100, 10):
    print(i)
"""

"""
for i in range(5, -1, -1):
    print(i)
"""



"""
Пример 11: Илустрациjа коришћења наредбе continue кроз задатак.

Написати функцију која пребројава самогласнике у прослеђеној речи.
"""
"""
Верзија 1: без препознавања слова "р" у функцији самогласника.
"""
def prebroj_samoglasnike(rec):
    samoglasnici = ("a", "e", "i", "o", "u")
    rezultat = 0
    for i in rec.lower():
        if i not in samoglasnici:
            continue
        rezultat += 1
    return rezultat

#print(prebroj_samoglasnike("astal"))
#print(prebroj_samoglasnike("crv"))
#print(prebroj_samoglasnike("Onomatopeja"))

"""
Верзија 2: са препознавањем слова "р" у функцији самогласника.
"""
def prebroj_samoglasnike(rec):
    rec_ms = rec.lower()
    samoglasnici = ("a", "e", "i", "o", "u")
    rezultat = 0
    for i in range(len(rec)):
        if rec_ms[i] not in samoglasnici:
            if i==0 or not (rec_ms[i] == "r" and 
                            rec_ms[i-1] not in samoglasnici and 
                            rec_ms[i+1] not in samoglasnici): 
                continue
        rezultat += 1
    return rezultat

#print(prebroj_samoglasnike("astal"))
#print(prebroj_samoglasnike("crv"))
#print(prebroj_samoglasnike("crvena"))
#print(prebroj_samoglasnike("Onomatopeja"))
#print(prebroj_samoglasnike("OSTRVO"))



"""
Пример 12: Коришћење функције split().
"""
#niska = "Zdravo svima"
#niska = "Zdravo svima, moje ime je Isidora, a prezime Grujić."
#niska = "jabuka#kruska#banana#limun"

#print(niska.split())
#print(niska.split(", "))
#print(niska.split("#"))
#print(niska.split("#", 2))



"""
Пример 13: Коришћење функције map().
"""
#from math import sqrt

#povorka = (1, 4, 9, 16)

#rezultat = map(sqrt, povorka)
#rezultat = list(map(sqrt, povorka))
#rezultat = tuple(map(sqrt, povorka))

#rezultat = list(map(lambda x: 3*x, povorka))

#print(rezultat)

"""
(x1, x2, x3, x4) = map(sqrt, povorka)
print(x1, x2, x3, x4)
"""



"""
Пример 14: Учитавање више променљивих са стандардног улаза.
"""
"""
(x1, x2, x3) = map(int, input("Unesite tri cela broja: ").split())
print(x1, x2, x3)
"""

"""
niz = list(map(int, input("Unesite tri cela broja: ").split()))
print(niz)
"""
