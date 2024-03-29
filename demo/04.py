# Факторизација

def прости_чиниоци(n):
    """Исписује просте чиниоце природног броја n у неопадајућем редоследу.

    >>> прости_чиниоци(8)
    2
    2
    2
    >>> прости_чиниоци(9)
    3
    3
    >>> прости_чиниоци(10)
    2
    5
    >>> прости_чиниоци(11)
    11
    >>> прости_чиниоци(12)
    2
    2
    3
    >>> прости_чиниоци(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = најмањи_чинилац(n)
        print(k)
        n = n // k

def најмањи_чинилац(n):
    """Враћа најмањи чинилац броја n већи од 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k

# DRY (Don't Repeat Yourself)

def истаДужина(а, б):
    """Враћа да ли природни бројеви а и б имају исти број цифара.

    >>> истаДужина(50, 70)
    True
    >>> истаДужина(50, 100)
    False
    >>> истаДужина(1000, 100000)
    False
    """
    return цифре(а) == цифре(б)
    # аЦифре = 0
    # while а > 0:
    #     а = а // 10
    #     аЦифре = аЦифре + 1
    # бЦифре = 0
    # while б > 0:
    #     б = б // 10
    #     бЦифре = бЦифре + 1
    # return аЦифре == бЦифре

def цифре(а):
    аЦифре = 0
    while а > 0:
        а = а // 10
        аЦифре = аЦифре + 1
    return аЦифре

# Уопштавање образаца коришћењем аргумената

from math import pi, sqrt

def површинаКвадрата(r):
    """Враћа површину квадрата са страницом дужине R."""
    return r * r

def површинаКруга(r):
    """Враћа површину круга с полупречником дужине R."""
    return r * r * pi

def површинаШестоугла(r):
    """Враћа површину правилног шестоугла са страницом дужине R."""
    return r * r * 3 * sqrt(3) / 2

def површина(r, константаОблика):
    """Враћа површину геометријског облика с мером дужине R."""
    assert r > 0, 'Дужина мора бити позитивна'
    return r * r * константаОблика

def површинаКвадрата(r):
    return површина(r, 1)

def површинаКруга(r):
    return површина(r, pi)

def површинаШестоугла(r):
    return површина(r, 3 * sqrt(3) / 2)

# Функције као аргументи

def збирБројева(n):
    """Збир првих N природних бројева.

    >>> збирБројева(5)
    15
    """
    збир, k = 0, 1
    while k <= n:
        збир, k = збир + k, k + 1
    return збир

def збирКубова(n):
    """Збир првих N кубова природних бројева.

    >>> збирКубова(5)
    225
    """
    збир, k = 0, 1
    while k <= n:
        збир, k = збир + pow(k, 3), k + 1
    return збир

def истоветност(k):
    return k

def куб(k):
    return pow(k, 3)

def сабирање(n, члан):
    """Збир првих N чланова секвенце.

    >>> сабирање(5, куб)
    225
    """
    збир, k = 0, 1
    while k <= n:
        збир, k = збир + члан(k), k + 1
    return збир

from operator import mul

def пиЧлан(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

сабирање(1000000, пиЧлан)

# Локалне дефиниције функција; функције као повратне вредности

def направиСабирач(n):
    """Враћа функцију једног аргумента K чија је повратна вредност K + N.

    >>> додајТри = направиСабирач(3)
    >>> додајТри(4)
    7
    """
    def сабирач(k):
        return k + n
    return сабирач

направиСабирач(2000)(23)
