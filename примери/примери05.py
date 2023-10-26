skup = {1,2,3}
niz= [1,2,3]
povorka=(1,2,3)

"""
for i in skup:
    print(i)
print("*------------------------------------------------*")
for i in niz:
    print(i)
print("*------------------------------------------------*")
for i in povorka:
    print(i)
"""



"""
print(niz+niz)
print(povorka+povorka)
#print(skup+skup)
skup2={4,5,6}
print(skup.union(skup2))
print(skup.intersection(skup2))
print(skup.difference(skup2))
#postoji i intersection i difference
print("*------------------------------------------------*")
print(niz*2)
print(povorka*2)
#print(skup*2)
"""



"""
print(niz[2])
print(povorka[2])
#print(skup[2])
print("*------------------------------------------------*")

#niz[2]=4
#povorka[2]=4
#skup[2]=4


niz.append(4)
#povorka nema ovakvu funkciju
povorka=povorka+(4,)
skup.add(4)
print(niz)
print(povorka)
print(skup)
print("*------------------------------------------------*")
"""



"""
niz.append(4)
#povorka nema ovakvu funkciju
povorka=povorka+(4,)
skup.add(4)
print(niz)
print(povorka)
print(skup)
skup.remove(4)
print(skup)
print("*------------------------------------------------*")
"""



"""
#nisu u redu
print("*------------------------------------------------*")
skup1=set([1,2,3,4])
skup2=set([2,3,4,1])
skup3 = set(('a', 'a', 'b', 'b', 'c'))   # od povorki
skup4 = set('anaconda')                  # od stringa
skup5 = {1, 1, 'anaconda', 'anaconda', 8.6, (1, 2, 3), None} #True
#skup5 = {1, 1, 'anaconda', 'anaconda', 8.6, (1, 2, 3), None, [1,2,3]}
#moguce je generisati skup na osnovu POJEDINACNIH CLANOVA NIZA, ali sam niz ne moze biti clan skupa!

print('Skup1:', skup1)
print('Skup2:', skup2)
print('Skup3:', skup3)
print('Skup4:', skup4)
print('Skup5:', skup5)

print("*------------------------------------------------*")
"""



"""
string="stringaaaaai"
skup=set(string)
for karakter in skup:
    if niz.count(karakter) > 1:
        print(karakter)

niz=[1,2,3,5,4]
print(niz.index(max(niz)))
print(sorted(niz))


niz=["lazar","rec","a"]
print(sorted(niz))
print(sorted(niz,key=len))
print(sorted(niz,key=len,reverse=True))
print(niz.sort(key=len,reverse=True))
niz.sort(key=len,reverse=True)
print(niz)
"""