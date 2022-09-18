def najveci(niz):
    assert isinstance(niz, list)
    
    niz.sort(reverse=True)
    for i in niz:
        if niz.count(i)%2 != 0:
            return i

niz = [int(i) for i in input().split()]
print(najveci(niz))
