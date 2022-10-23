# Наредба return

def крај(n, c):
    """Исписује завршне цифре броја N уназад док се не дође до цифре C.

    >>> крај(34567, 5)
    7
    6
    5
    """
    while n > 0:
        poslednja, n = n % 10, n // 10
        print(poslednja)
        if c == poslednja:
            return None

def претрага(f):
    """Враћа најмањи природан број x за који је f(x) тачно."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def претрага(f):
    """Враћа најмањи природан број x за који је f(x) тачно."""
    x = 0
    while not f(x):
        x += 1
    return x

def квадрат(x):
    return x * x

def трострук(x):
    return 3 * x

def инверзија(f):
    """Враћа функцију g(y) која враћа x такво да је f(x) == y, односно g(f(x)) -> x.

    >>> корен = инверзија(квадрат)
    >>> корен(16)
    4
    >>> инверзија(трострук)(15)
    5
    """
    return lambda y: претрага(lambda x: f(x) == y)


def if_(u, t, n):
    if u:
        return t
    else:
        return n

from math import sqrt

def реални_корен(x):
    """Враћа реални део квадратног корена од x.

    >>> реални_корен(4)
    2.0
    >>> реални_корен(-4)
    0.0
    """
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
    # if_(x > 0, sqrt(x), 0.0)

# Управљачки изрази

def има велики_корен(x):
    """Враћа да ли x има велики квадратни корен.

    >>> велики_корен(1000)
    True
    >>> велики_корен(100)
    False
    >>> велики_корен(0)
    False
    >>> велики_корен(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

def разумно(n):
    """Да ли је N довољно мало да се 1/N може представити?

    >>> разумно(100)
    True
    >>> разумно(0)
    True
    >>> разумно(-100)
    True
    >>> разумно(10 ** 1000)
    False
    """
    return n == 0 or 1/n != 0.0

# Грешке & трагови

def f(x):
    return g(x - 1)

def g(y):
    return abs(h(y) - h(1 / y))  # избрисати заграду

def h(z):
    return z * z  # избрисати return

print(f(12))  # избрисати 2
