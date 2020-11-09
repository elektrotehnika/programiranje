def isprepletane(str1,str2):
     rez = ''
     for i in range(min(len(str1),len(str2))):
          rez+=str1[i]+str2[i]
     rez+=str1[i+1:]+str2[i+1:]    
     return rez

prva = input()
druga = input()
print(isprepletane(prva, druga))
