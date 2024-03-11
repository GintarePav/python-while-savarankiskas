# 1. Suprogramuokite programinę įrangą kavos aparatui. Pradinė kavos kaina įvedama klaviatūra. Kaina nurodoma eurais (tarkim 2.20). Nurodžius kavos kainą, prašoma mesti monetą. Kavos aparatas priima 10, 20, 50 centų arba 1, 2 eurus (klaviatūra įvedamas skaičius 10 arba 20 arba 50 arba 1 arba 2) Įmetus tinkamą monetą (tarkim 1), parodomas pranešimas, kiek liko sumokėti (tarkim 1.20) ir prašoma mesti monetą dar. Įmetus tinkamą monetą (tarkim 2), kavos aparatas išveda pranešimą: Grąža (tarkim 80 centų arba tarkim 1.20 euro) ir palinkima „Skanios kavos“.

# Įmetus netinkamą monetą (tarkim 58 ), išvedamas pranešimas „Netinkama moneta. Meskite dar kartą“. Suskaičiuoti ir išvesti pabaigoje, kiek buvo bandymų įmesti „padirbtą“ monetą ir kiek kartų buvo metama „tikra“ moneta

kavosKaina = float(input("Kokia kavos kaina? "))
padirbtosMonetos = 0
tikrosMonetos = 0

while kavosKaina > 0:
    moneta = int(input("Imeskite moneta. "))
    # Validuojamos monetos ir skaiciuojamos padirbtos:
    while moneta != 1 and moneta != 2 and moneta != 10 and moneta != 20 and moneta != 50:
        padirbtosMonetos += 1
        print("Netinkama moneta. Meskite dar karta.")
        moneta = int(input("Imeskite moneta. "))
    # Konvertuojama i centus ir skaiciuojamos tikros monetos:
    if moneta >= 10:
        moneta /= 100
        tikrosMonetos += 1
    else:
        tikrosMonetos += 1
    # Apskaiciuojamas kavos apmokejimas
    if kavosKaina >= moneta:
        kavosKaina = round(kavosKaina - moneta, 2)
        print(f'Liko sumoketi {kavosKaina} eur.')
    else:
        moneta -= kavosKaina
        print(f'Graza: {moneta} eur.')
        kavosKaina = 0    
print("Skanios kavos!")
print(f'Bandymai naudoti padirbtą monetą: {padirbtosMonetos};\nPanaudotos tikros monetos: {tikrosMonetos}.')