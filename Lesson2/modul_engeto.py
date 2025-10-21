import math
def soucet(a, b):
    return a + b

def rozdil(a, b):
    return a - b

#funkce ktera pozdravi studenty Engetu zdar
def pozdrav_engeto_studenty():
    print("Engetu zdar!")

#funkce ktera se rozlouci se studenty Engetu konec
def rozlouceni_engeto_studenty():
    print("Engetu konec!")

#specialni Engeto funkce pro objem koule
def objem_koule(polomer):
    objem = (4/3) * math.pi * (polomer ** 3)
    return objem