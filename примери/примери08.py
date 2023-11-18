# -*- coding: utf-8 -*-
"""
Вежбе 8 - Примери 
"""

"""
Пример 1 - Синтакса речника
"""

meseci = {1: 'januar',
          2: 'februar',
          3: 'mart',
          4: 'april',
          5: 'maj',
          6: 'jun',
          7: 'jul',
          8: 'avgust',
          9: 'septembar',
          'januar': 1,
          'februar': 2,
          'mart': 3,
          'april': 4,
          'maj': 5,
          'jun': 6,
          'jul': 7,
          'avgust': 8,
          'septembar': 9}

#print(meseci[3])
#print(meseci['jul'])
#print(meseci.get(5))
#print(meseci.get('avgust'))



"""
Пример 2 - Пример додавања нових елемената у речник.
"""

meseci[10] = 'oktobar'
#print(meseci[10])
meseci['oktobar'] = 10
#print(meseci['oktobar'])



"""
Пример 3 - Начини за брисање елемената из речника.
"""
# први начин
del meseci[10]

# други начин
meseci.pop('oktobar')

# Брисање последњег додатог елемента
meseci.popitem()

#print(meseci)



"""
Пример 4 - Пример излиставања кључева и вредности датог речника.
"""

#print(meseci.keys())
#print(meseci.values())
#print(meseci.items())



"""
Пример 5 - Пример провере да ли се одређена вредност кључа налази у речнику.
"""

"""
if 4 in meseci:
    print("Dati ključ se nalazi u rečniku.")
"""


"""
Пример 6 - Пример проласка кроз кључеве речника.
"""
# први начин
"""
for kljuc in meseci:
    #print(meseci[kljuc])
    print(kljuc)
"""

# други начин
"""
for kljuc in meseci.keys():
    print(meseci[kljuc])
    #print(kljuc)
"""



"""
Пример 7 - Начини за промену вредности за дати кључ у уређеном пару <кључ, вредност>.
"""
# први начин
"""
meseci[2] = 'decembar'
print(meseci[2])
"""

# други начин
"""
meseci.update({2: 'februar'})
print(meseci[2])


dani_u_nedelji = {
    1:"ponedeljak",
    2:"utorak",
    3:"sreda",
    4:"cetvrtak",
    5:"petak",
    6:"subota",
    7:"nedelja"
}

meseci.update(dani_u_nedelji)
print(meseci)
"""


"""
Пример 8 - Начини копирања речника.
"""
# први начин

#meseciKopija = meseci.copy()
#print(meseciKopija)


# други начин

#meseciKopija2 = dict(meseci)
#print(meseciKopija2)




"""
Пример 9 - Пример брисања садржаја речника.
"""
#meseciKopija.clear()
#print(meseciKopija)



"""
Пример 10 - Брисање речника.
"""
#del meseciKopija2
#print(meseciKopija2)



"""
Пример 11 - Пример речника чији су кључеви сложени типови података.
"""

mojRecnik = {(1,1): 'jedanaest',
             (1,2): 'dvanaest',
             (1,3): 'trinaest',
             (1,4): 'četrnaest',
             (1,5): 'petnaest',
             (1,6): 'šesnaest',
             (1,7): 'sedamnaest',
             (1,8): 'osamnaest',
             (1,9): 'devetnaest',
             (2,0): 'dvadeset'}



"""
Пример 12 - Пример угнеждених речника.
"""
prviMesec = {'redniBroj': 1,
             'naziv': 'januar'}

drugiMesec = {'redniBroj': 2,
              'naziv': 'februar'}

treciMesec = {'redniBroj': 3,
              'naziv': 'mart'}


ugnezdeniMeseci = {'prviMesec': prviMesec,
          'drugiMesec': drugiMesec,
          'treciMesec': treciMesec}

#print(ugnezdeniMeseci)
#print(ugnezdeniMeseci['drugiMesec']['naziv'])



"""
Пример 13

Унос на стандардном улазу састоjи се из два реда. У оба реда
прослеђуjе се уређени пар (x, y), у формату x <размак> y. Од
учитаних уређених парова направити речник, тако да су x кључеви, а y
њима припадаjуће вредности. Сматрати да су и кључеви и вредности 
по типу ниске.
"""
"""
#ucitaniRecnik = dict()
ucitaniRecnik = {}

prviRed = input().split()
ucitaniRecnik[prviRed[0]] = prviRed[1]

drugiRed = input().split()
ucitaniRecnik[drugiRed[0]] = drugiRed[1]

print(ucitaniRecnik)
"""



"""
Број редова за унос података са стандардног улаза није познат.
У овом случају, број редова за учитавање података се обично учитава у првом реду.
"""

"""
n = int(input())
ucitaniRecnik = dict()
for _ in range(n):
    kljuc, vrednost = input().split()
    ucitaniRecnik[kljuc] = vrednost

print(ucitaniRecnik)
"""


"""
Пример 14: Пример са матрицом.
"""

br_vrsta, br_kolona = map(int, input().split())
matrica=[]
for i in range(br_vrsta):
    vrsta=list(map(int,input().split()))
    matrica.append(vrsta)
#print(matrica)

for i in range(br_vrsta):
    for j in range(br_kolona):
        print(matrica[i][j], end=" ") #"{:3d}".format(matrica[i][j])
    #print()
    print("\n")


#for vrsta in matrica:
#   print (" ".join(map(str,vrsta)))