def isprepletaneRekurzivno(niska1, niska2):
     assert isinstance(niska1, str) and isinstance(niska2,str)
     if len(niska1) == 0:
          return niska2
     if len(niska2) == 0:
          return niska1
     return niska2[0] + niska1[0] + isprepletaneRekurzivno(niska1[1:], niska2[1:])
