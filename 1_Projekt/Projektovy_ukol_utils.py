seznam_ukolu = []

def hlavni_menu():
    print("Správce úkolů - Hlavni menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    volba = input("Vyberte možnost (1-4): ")

    if volba >= "1" and volba <= "4":
        return int(volba)
    else:
        print("Neplatná volba. Zadejte číslo 1–4.")

def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ")
        popis_ukolu = input("Zadejte popis úkolu: ")
        if not popis_ukolu or not nazev_ukolu:
            print("Popis a název úkolu nesmí být prázdné!")
            continue

        seznam_ukolu.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
        print(f"Úkoly '{nazev_ukolu}' '{popis_ukolu}' byl přidán.")
        break  # po úspěchu se vracíme do hlavního menu

def zobrazit_ukoly():
    if not seznam_ukolu:
        print("Žádné úkoly nejsou uloženy.")
        return

    print("Seznam úkolů:")
    for i, u in enumerate(seznam_ukolu, start=1):
        print(f"{i}. {u['nazev']} - {u['popis']}")


