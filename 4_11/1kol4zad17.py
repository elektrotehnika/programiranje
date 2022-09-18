def skraceniNov(niz, duzina):
     try:
          assert isinstance(niz, list) and isinstance(duzina, int) and duzina >= 0
     except AssertionError:
          raise TypeError("Argumenti nisu validni")
     novi = []
     for i in niz:
          if len(i) < duzina:
               novi.append(i)
     return novi          
