print ("Pozor, náledí!")

# funkce pro řetězce
# pokud má SMS > 160 znaků -> 2 SMS uctujeme
SMS = "Dobrou noc!"
print (len(SMS))

# jaky znak je první znak v SMS
print(SMS[8])

# jaky je posledni znak v SMS
print(SMS[-1])

# lowerCase
user_name = "SteFFaan007"
print(user_name.lower())

print(11%5)

a = 2
b = 3
print(a * b)

# uzivatelsky vstup
# funkce input()
print("Vítejte!\nKolik je Vám let?")
vek_navstevnika_hospody = input()
print("Váš věk je: " + vek_navstevnika_hospody)

# datovy typ seznam
akciove_zbozi = ["jablka", "banany", "hrusky"]
print(akciove_zbozi)


# funkce pro datovy typ seznam
# dosly nam banany, musime tento produkt sahnout z nabidky
# funkce ve vypisu odebere banany
akciove_zbozi.remove("banany")
print(akciove_zbozi)


# aktualizovat , pridat nove zbozi
# funkce ve vypisu prida mandarinky
akciove_zbozi.append("mandarinky")
print(akciove_zbozi)

# ktere je zbozi na prvnim miste v nasem seznamu?
print(akciove_zbozi[0])

uzivatel = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "vek": 30
}

# funkce pro datovy typ slovnik
print(uzivatel["jmeno"])

# pridani noveho klice a hodnoty
uzivatel["je_pojisten_EU"] = True
print(uzivatel)
