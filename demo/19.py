def str_repr_демо():
    from fractions import Fraction
    половина = Fraction(1, 2)
    половина
    print(половина)
    str(половина)
    repr(половина)

    н = 'здраво свима'
    str(н)
    repr(н)
    "'здраво свима'"
    repr(repr(repr(н)))
    eval(eval(eval(repr(repr(repr(н))))))
    # Грешке: eval('здраво свима')

# Имплементација општих нисковних функција

class Вук:
    """Вук.

    >>> вучко = Вук()
    >>> вучко
    Вук()
    >>> print(вучко)
    вук
    >>> print(str(вучко))
    вук
    >>> print(repr(вучко))
    Вук()
    >>> print(вучко.__repr__())
    вучко
    >>> print(вучко.__str__())
    вук вучко
    >>> print(str_(вучко))
    вук
    >>> print(repr_(вучко))
    Вук()
    """
    def __init__(self):
        self.__repr__ = lambda: 'вучко' # атрибут инстанце
        self.__str__ = lambda: 'вук вучко'

    def __repr__(self): # атрибут класе
        return 'Вук()'

    def __str__(self):
        return 'вук'

def print_вук():
    вучко = Вук()
    print(вучко)
    print(str(вучко))
    print(repr(вучко))
    print(вучко.__repr__())
    print(вучко.__str__())

def repr_(x):
    н = type(x).__repr__(x)
    if not isinstance(н, str):
        raise TypeError
    return н

def str_(x):
    н = type(x).__str__(x)
    if not isinstance(н, str):
        raise TypeError
    return н

def fниска_демо():
    """f-ниске демо.

    >>> f'2 + 2 = 2 + 2'
    '2 + 2 = 2 + 2'
    >>> f'2 + 2 = {2 + 2}'
    '2 + 2 = 4'
    >>> '2 + 2 = {2 + 2}'
    '2 + 2 = {2 + 2}'
    >>> f'2 + 2 = {abs(2 + 2)}'
    '2 + 2 = 4'
    >>> abs = float
    >>> f'2 + 2 = {abs(2 + 2)}'
    '2 + 2 = 4.0'
    >>> f'2 + 2 = {(lambda x: x + x)(2)}'
    '2 + 2 = 4'

    >>> from fractions import Fraction
    >>> половина = Fraction(1, 2)
    >>> половина
    Fraction(1, 2)
    >>> print(половина)
    1/2
    >>> f'половина од половине је {половина * половина}.'
    'половина од половине је 1/4.'

    >>> н = [9, 8, 7]
    >>> f'због {н.pop()} {н.pop()} {н}'
    'због 7 8 [9]'
    """


# Разломљени бројеви
from math import gcd

class Разломак:
    """Разломљени број.

    >>> р = Разломак(9, 15)
    >>> р
    Разломак(9, 15)
    >>> print(р)
    9/15

    >>> Разломак(1, 3) + Разломак(1, 6)
    Разломак(1, 2)
    >>> р + 1
    Разломак(8, 5)
    >>> 1 + р
    Разломак(8, 5)
    >>> 1.4 + р
    2.0
    """
    def __init__(self, б, и):
        self.бројилац = б
        self.именилац = и

    def __repr__(self):
        return 'Разломак({0}, {1})'.format(self.бројилац, self.именилац)

    def __str__(self):
        return '{0}/{1}'.format(self.бројилац, self.именилац)

    def __add__(self, други):
        if isinstance(други, Разломак):
            б = self.бројилац * други.именилац + self.именилац * други.бројилац
            и = self.именилац * други.именилац
        elif isinstance(други, int):
            б = self.бројилац + self.именилац * други
            и = self.именилац
        else:
            return float(self) + други
        нзд = gcd(б, и)
        р = Разломак(б // нзд, и // нзд)
        return р

    __radd__ = __add__

    def __float__(self):
        return self.бројилац / self.именилац
