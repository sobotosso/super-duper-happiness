# #Pozdrav
# print("Ahojte z Python kurzu pokracovani")

# #Vypis vaha
# vaha = 5.98
# print("Vaha je", vaha, "kg")

#print(bool(11!=11))

#=======================================================

#cyklus for
# for i in range(10):
#     print(f"Pozor nehoda!")
# print("Tělo cyklu")

#cyklus while
# correct_password = "tajneheslo"
# user_input = input("Zadejte heslo: ")

# while user_input != correct_password:
#     print("Nesprávné heslo, zkuste to znovu.")
#     user_input = input("Zadejte heslo: ")

# print("Přihlášení úspěšné.")

#=======================================================

#Podminky
# vek_uzivatele = 143

# if vek_uzivatele >0 and vek_uzivatele < 18:
#     print("Kofola")
# elif vek_uzivatele >=18 and vek_uzivatele < 64:
#     print("Nazdravi")
# elif vek_uzivatele >=64 and vek_uzivatele < 140:
#     print("Pozor, pijte s rozumem!")
# else:
#     print("Chyba, spatne zadany vek!")



# vek_uzivatele = ("cože?")

# if not isinstance(vek_uzivatele, int):
#     print("Hodnota musí být číslo")
# else:
#     if vek_uzivatele > 0 and vek_uzivatele < 18:
#         print("Kofola")
#     elif vek_uzivatele >= 18 and vek_uzivatele < 64:
#         print("Nazdravi")
#     elif vek_uzivatele >= 64 and vek_uzivatele < 140:
#         print("Pozor, pijte s rozumem!")
#     else:
#         print("Chyba, spatne zadany vek!")

#=======================================================

#Funkce obvod trojuhelniku


# def obvod_trojuhelniku(strana_a, strana_b, strana_c):
#     obvod = strana_a + strana_b + strana_c
#     return obvod

# #Zadani: a=45, b=56, c=150
# print(obvod_trojuhelniku(45, 56, 150))

# #Obsah čtverce
# def obsah_ctverce(strana_a, strana_b):
#     obsah = strana_a * strana_b
#     return obsah

# #Zadani: a=10, b=20
# print (obsah_ctverce(10, 20))

# #Funkce pozdrav Engeto studenty
# def pozdrav_engeto_studenty():
#     print("Ahojte Engeto studenti!")

# pozdrav_engeto_studenty()

#=======================================================

import math
import datetime
import random, modul_engeto

# #z modulu math použij druhá odmocnina
# print(math.sqrt(16))

# #z modulu datetime použij aktuální čas
# aktualni_cas = datetime.datetime.now()
# print(aktualni_cas)

# print(random.choice(["voda", "mineralni voda", "nic"]))

#=======================================================

#použití funkce z vlastního modulu
# print(modul_engeto.soucet(50, 5))

#funkce ktera pozdravi studenty Engetu zdar
modul_engeto.pozdrav_engeto_studenty()

# #funkce ktera se rozlouci se studenty Engetu konec
modul_engeto.rozlouceni_engeto_studenty()

# #specialni Engeto funkce pro objem koule
modul_engeto.objem_koule(5)
print(modul_engeto.objem_koule(5))









