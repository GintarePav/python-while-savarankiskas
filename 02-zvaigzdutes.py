# 2. Įvedamas bet koks skaičius. Parašykite programą, kuri tą skaičių pavaizduotu žvaigždutėmis pradedant vienetais.

skaicius = int(input("Iveskite skaiciu: "))
skaitmuo = 0

while skaicius > 0:
    skaitmuo = skaicius % 10
    zvaigzdutes = "*" * skaitmuo
    print(zvaigzdutes)
    skaicius //= 10
