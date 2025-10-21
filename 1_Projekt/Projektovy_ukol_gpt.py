# Task manager – začátečnická verze pro konzoli

def hlavni_menu():
    """Vypíše hlavní menu a vrátí volbu uživatele jako číslo 1–4."""
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    volba = input("Vyberte možnost (1-4): ").strip()
    return volba

def pridat_ukol(ukoly):
    """
    Zeptá se na název a popis a přidá úkol do seznamu 'ukoly'.
    Každý úkol je slovník {'nazev': ..., 'popis': ...}.
    """
    print("\nZadejte název úkolu:")
    nazev = input("> ").strip()
    print("Zadejte popis úkolu:")
    popis = input("> ").strip()

    # Minimální validace: název nesmí být prázdný
    if not nazev:
        print("Úkol nebyl přidán: název nesmí být prázdný.")
        return

    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}''{popis}' byl přidán.")

def zobrazit_ukoly(ukoly):
    """Vypíše všechny úkoly v očíslovaném seznamu, nebo info, že je prázdný."""
    print("\nSeznam úkolů:")
    if not ukoly:
        print("(Žádné úkoly nebyly zatím přidány.)")
        return

    for i, u in enumerate(ukoly, start=1):
        print(f"{i}. {u['nazev']} - {u['popis']}")

def odstranit_ukol(ukoly):
    """
    Zobrazí seznam úkolů a umožní odstranit vybraný úkol podle čísla.
    Při chybné volbě uživatele upozorní a nic nemaže.
    """
    if not ukoly:
        print("\nSeznam úkolů je prázdný, není co odstraňovat.")
        return

    zobrazit_ukoly(ukoly)
    volba = input("\nZadejte číslo úkolu, který chcete odstranit: ").strip()

    if not volba.isdigit():
        print("Neplatná volba: prosím zadejte číslo.")
        return

    idx = int(volba)
    if 1 <= idx <= len(ukoly):
        odstraneny = ukoly.pop(idx - 1)
        print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
    else:
        print("Neplatné číslo: takový úkol neexistuje.")

def main():
    ukoly = []
    while True:
        volba = hlavni_menu()

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            odstranit_ukol(ukoly)
        elif volba == "4":
            print("\nKonec programu.")
            break
        else:
            print("Neplatná volba. Zadejte číslo 1–4.")

if __name__ == "__main__":
    main()
