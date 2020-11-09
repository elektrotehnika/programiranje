def zbirCifaraNiske(niska):
     assert isinstance(niska, str)
     suma = 0
     for i in niska:
          if i.isdigit():
               suma += int(i)
     return suma

niska = input()
print(zbirCifaraNiske(niska))
          
