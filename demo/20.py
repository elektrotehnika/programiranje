class Листа:
    """Уланчана листа.

    >>> с = Листа(3, Листа(4, Листа(5)))
    >>> с
    Листа(3, Листа(4, Листа(5)))
    >>> print(с)
    <3 4 5>
    >>> с.први
    3
    >>> с.остатак
    Листа(4, Листа(5))
    >>> с.остатак.први
    4
    >>> с.остатак.први = 7
    >>> с
    Листа(3, Листа(7, Листа(5)))
    >>> с.први = 6
    >>> с.остатак.остатак = Листа.празно
    >>> с
    Листа(6, Листа(7))
    >>> print(с)
    <6 7>
    >>> print(с.остатак)
    <7>
    >>> т = Листа(1, Листа(Листа(2, Листа(3)), Листа(4)))
    >>> т
    Листа(1, Листа(Листа(2, Листа(3)), Листа(4)))
    >>> print(т)
    <1 <2 3> 4>
    """
    празно = ()

    def __init__(self, први, остатак=празно):
        assert остатак is Листа.празно or isinstance(остатак, Листа)
        self.први = први
        self.остатак = остатак

    def __repr__(self):
        if self.остатак:
            остатак_repr = ', ' + repr(self.остатак)
        else:
            остатак_repr = ''
        return 'Листа(' + repr(self.први) + остатак_repr + ')'

    def __str__(self):
        ниска = '<'
        while self.остатак is not Листа.празно:
            ниска += str(self.први) + ' '
            self = self.остатак
        return ниска + str(self.први) + '>'


квадрат, непаран = lambda x: x * x, lambda x: x % 2 == 1
list(map(квадрат, filter(непаран, range(1, 6))))  # [1, 9, 25]


def range_листа(почетак, крај):
    """Враћа уланчану Листу која садржи узастопне целе бројеве од почетка до краја.

    >>> range_листа(3, 6)
    Листа(3, Листа(4, Листа(5)))
    """
    if почетак >= крај:
        return Листа.празно
    else:
        return Листа(почетак, range_листа(почетак + 1, крај))


def map_листа(f, с):
    """Враћа уланчану Листу која садржи f(x) за свако x у Листи с.

    >>> map_листа(квадрат, range_листа(3, 6))
    Листа(9, Листа(16, Листа(25)))
    """
    if с is Листа.празно:
        return с
    else:
        return Листа(f(с.први), map_листа(f, с.остатак))


def filter_листа(f, с):
    """Враћа уланчану Листу која садржи само чланове x из уланчане Листе с за које је f(x) тачно.

    >>> filter_листа(непаран, range_листа(3, 6))
    Листа(3, Листа(5))
    """
    if с is Листа.празно:
        return с
    филтриран_остатак = filter_листа(f, с.остатак)
    if f(с.први):
        return Листа(с.први, филтриран_остатак)
    else:
        return филтриран_остатак


map_листа(квадрат, filter_листа(непаран, range_листа(1, 6)))  # Листа(1, Листа(9, Листа(25)))


# Стабла

class Стабло:
    """Стабло је ознака и низ грана."""
    def __init__(self, ознака, гране=[]):
        self.ознака = ознака
        for грана in гране:
            assert isinstance(грана, Стабло)
        self.гране = list(гране)

    def __repr__(self):
        if self.гране:
            грана_str = ', ' + repr(self.гране)
        else:
            грана_str = ''
        return 'Стабло({0}{1})'.format(repr(self.ознака), грана_str)

    def __str__(self):
        return '\n'.join(self.увучено())

    def увучено(self):
        редови = []
        for грана in self.гране:
            for ред in грана.увучено():
                редови.append('  ' + ред)
        return [str(self.ознака)] + редови

    def да_ли_је_лист(self):
        return not self.гране


def фиб_стабло(n):
    """Фибоначијево стабло.

    >>> print(фиб_стабло(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Стабло(n)
    else:
        лево = фиб_стабло(n-2)
        десно = фиб_стабло(n-1)
        фиб_n = лево.ознака + десно.ознака
        return Стабло(фиб_n, [лево, десно])


def листови(стабло):
    """Враћа низ ознака свих листова у задатом стаблу.

    >>> листови(фиб_стабло(4))
    [0, 1, 1, 0, 1]
    """
    if стабло.да_ли_је_лист():
        return [стабло.ознака]
    else:
        return sum([листови(г) for г in стабло.гране], [])


def висина(стабло):
    """Враћа висину стабла."""
    if стабло.да_ли_је_лист():
        return 0
    else:
        return 1 + max([висина(г) for г in стабло.гране])


def орежи(с, к):
    """Орезује сва подстабла чија је ознака корена једнака к.

    >>> с = фиб_стабло(5)
    >>> орежи(с, 1)
    >>> print(с)
    5
      2
      3
        2
    """
    с.гране = [г for г in с.гране if г.ознака != к]
    for г in с.гране:
        орежи(г, к)
