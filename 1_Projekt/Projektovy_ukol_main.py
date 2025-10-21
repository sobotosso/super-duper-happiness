from Projektovy_ukol_utils import hlavni_menu, pridat_ukol, zobrazit_ukoly

while True:
    volba = hlavni_menu()
    if volba == 1:
        pridat_ukol()
    elif volba == 2:
        zobrazit_ukoly()

