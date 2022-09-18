def zbirCifaraBroja(broj):
     #rekurzivno resenje
     assert isinstance(broj, int)
     if broj < 0:
          broj = -broj
     if broj < 10:
          return broj
     return broj%10 + zbirCifaraBroja(broj//10)

def zbirCifaraBroja2(broj):
     #iterativno resenje
     zbir = 0
     broj = abs(broj)
     while broj>0:
          zbir += broj%10
          broj = broj//10
     return zbir

broj = int(input())
print(zbirCifaraBroja2(broj))
     
