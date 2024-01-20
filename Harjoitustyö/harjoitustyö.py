sali = ["pieni", "keskik", "iso"]
e_nimi = ["abc", "kissa", "elain"]
ajat = ["15", "18", "20"]

naytokset = {}
"""Elokuvan nimi ja sali, jossa elokuva näytetään."""

vapaat_pieni = [1,2]
vapaat_keski = [1,2,3,4,5]
vapaat_iso = [1,2,3,4,5,6,7,8]
varatut_pieni = []
varatut_keski = []
varatut_iso = []
varaukset = []

def nayta_UIyp():
    """Näyttää yp:n käyttöliittymän"""

    while True:
        print("Valitse toiminto:")
        print("1. Lisää elokuva")
        print("2. Lisää näytösaika")
        print("3. Selaa varauksia")
        print("0. Poistu")
        valinta = int(input("Valintasi: "))

        if valinta == 0:
            break

        elif valinta == 1:
            elokuva = input("Anna elokuvan nimi: ")
            lisaa_elokuva(elokuva)
            print("Elokuva lisätty!")

            tiedosto1 = open("elokuvat.txt", "a", encoding = "utf-8")
            tiedosto1.write(elokuva + "\n")
            tiedosto1.close
        
        elif valinta == 2:
            naytos = input("Anna näytösaika: ")
            lisaa_naytos(naytos)
            print("Näytösaika lisätty!")

            tiedosto2 = open("näytösajat.txt", "a", encoding = "utf-8")
            tiedosto2.write(naytos + "\n")
            tiedosto2.close
        
        elif valinta == 3:
            """Ylläpitäjä voi selata tehtyjä varauksia."""

            tiedosto3 = open("Varaukset.txt", "r", encoding = "utf-8")
            tiedosto3.close()
                
def lisaa_elokuva(elokuva: str):
    """Yp voi lisätä elokuvan"""
    e_nimi.append(elokuva)

def lisaa_naytos(naytos: int):
    """Yp voi lisätä näytösajan"""
    ajat.append(naytos)

def selaa_varauksia(varaus: int) -> list:
    """Näyttää varausten määrän"""
    print(varaukset)

def nayta_UIas():
    """Näyttää asiakkaan käyttöliittymän"""
    varaa_paikka()

def varaa_paikka():
    """Asiakas voi varata paikan"""
    v_elokuva = input("Valitse haluamasi elokuva: ")

    if v_elokuva == "kissa":
        print("Elokuva näytetään pienessä salissa.")
        naytokset["kissa"] = "15", "18", "20"
        print ("Elokuva näytetään seuraavina aikoina:", naytokset["kissa"])

        naytos1 = input("Valitse aika: ")
        paikka1 = input("Valitse haluamasi paikka 1-2: ")

        if paikka1 in varatut_pieni:
            print("Valitettavasti paikka on jo varattu.")
        else:
            varatut_p1 = (naytos1, paikka1)
            varatut_pieni.append(varatut_p1)
            varaukset.append(varatut_p1)

            print("Kiitos varauksestasi, tervetuloa!")

            tiedosto3 = open("Varaukset.txt", "a", encoding = "utf-8")
            tiedosto3.write("Näytös " + naytos1 + ", ")
            tiedosto3.write("Paikka " + paikka1 + "\n")
            tiedosto3.close()

            
    if v_elokuva == "abc":
        print("Elokuva näytetään keskikokoisessa salissa.")
        naytokset["kissa"] = "15", "18", "20"
        print ("Elokuva näytetään seuraavina aikoina:", naytokset["abc"])

        naytos2 = input("Valitse aika: ")
        paikka2 = input("Valitse haluamasi paikka 1-5: ")

        if paikka2 in varatut_keski:
            print("Valitettavasti paikka on jo varattu.")
        else:
            varatut_p2 = (naytos2, paikka2)
            varatut_keski.append(varatut_p2)
            varaukset.append(varatut_p2)

            print("Kiitos varauksestasi, tervetuloa!")

            tiedosto3 = open("Varaukset.txt", "a", encoding = "utf-8")
            tiedosto3.write(naytos2, paikka2 + "\n")
            tiedosto3.close()
        
    if v_elokuva == "elain":
        print("Elokuva näytetään isossa salissa.")
        naytokset["elain"] = "15", "18", "20"
        print ("Elokuva näytetään seuraavina aikoina:", naytokset["naytos"])

        naytos3 = input("Valitse aika: ")
        paikka3 = input("Valitse haluamasi paikka 1-8: ")

        if paikka3 in varatut_iso:
            print("Valitettavasti paikka on jo varattu.")
        
        else:
            varatut_p3 = (naytos3, paikka3)
            varatut_iso.append(varatut_p3)
            varaukset.append(varatut_p2)
            print("Kiitos varauksestasi, tervetuloa!")

            tiedosto3 = open("Varaukset.txt", "a", encoding = "utf-8")
            tiedosto3.write(naytos3, paikka3 + "\n")
            tiedosto3.close()

nayta_UIyp()
nayta_UIas()