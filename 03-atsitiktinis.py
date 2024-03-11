# 3. Programa prašo įvesti sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo 1 iki n. Sugeneravus atsitiktinį skaičių vartotojui siūloma atspėti kokį skaičių sugeneravo programa. Įvedus spėjamą skaičių (tarkim 75) programa praneša ar sugeneruotas skaičius didesnis ar mažesnis už įvestą skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnis už 75. Atliksite 3 spėjimą...“). Įvedus didesnius skaičius už n ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie spėjimų skaičiaus. Vartotojui atspėjus skaičių - pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo atlikta ir kiek buvo bandymų įvesti netinkamą skaičių. Pabaigus žaidimą – siūloma sužaisti dar kartą.

import random
zaidziam = True
kartai = 0
negalimi = 0

while zaidziam:
    zaidejoSkaicius = int(input("Iveskite sveika teigiama skaiciu: "))
    atsitiktinis = random.randint(1, zaidejoSkaicius)
    while zaidziam:
        spejimas = int(input("Spekite skaiciu: "))
        if 0 < spejimas < atsitiktinis:
            kartai += 1
            print(f'Sugeneruotas skaicius didesnis uz {spejimas}. Atliksite {kartai}-a spejima.')
        elif 0 < spejimas > atsitiktinis:
            kartai += 1
            print(f'Sugeneruotas skaicius mazesnis uz {spejimas}. Atliksite {kartai}-a spejima.')
        elif spejimas == atsitiktinis:
            kartai += 1
            print(f'Teisingas spejimas;\nSpejimu skaicius: {kartai}.\nNegalimu spejimu skaicius: {negalimi}')
            zaidziam = False  
        else:
            print("Negalimas skaicius, bandykite dar karta.")
            negalimi += 1
    if atsitiktinis == spejimas:
        kartoti = input("Kartoti T/N? ")
        if kartoti == "T" or kartoti == "t":
            zaidziam = True
        else:
            zaidziam = False
                
