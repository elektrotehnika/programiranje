recenica = input()
broj_slova = 0
broj_cifara = 0
for karakter in recenica:
    if karakter.isalpha():
        broj_slova += 1
    if karakter.isdigit():
        broj_cifara += 1
print(broj_slova)
print(broj_cifara)
