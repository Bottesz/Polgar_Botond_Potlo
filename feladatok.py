import random

def elso():
    nev=" "
    while nev == "" or (nev[0] != 'A' and nev[0] != 'a'):
        nev = input("Adj meg egy 'A' betűvel kezdődő nevet: ")
        if nev == "" or (nev[0] != 'A' and nev[0] != 'a'):
            print("Hiba: A névnek 'A' betűvel kell kezdődnie!")



def hany5oszt_egyikfel():
   
    szamok = []
    for i in range(5):
        szam = random.randint(30, 50)
        szamok.append(szam)
        i+=1
    return szamok



def hany5oszt_masikfel(szamok):
    oszthato_db = 0
    for szam in szamok:
        if szam % 5 == 0:
            oszthato_db += 1
    return oszthato_db



def harmadik(text,N):
    if N > len(text):
        print("Nincs N. karakter!")
    else:
        print(f"A szöveg {N}. karaktere {text[N-2]} -  {text[N-2].upper() *3}")



def feladat4():
    szamok = []
    szam = int(input("Adj meg egy számot (0 a kilépéshez): "))  
    while szam != 0:
        szamok.append(szam)
        szam = int(input("Adj meg egy számot (0 a kilépéshez): "))
    return szamok



def kitalalos_jatek():
    f_tipp = 0
    gep_tipp=random.randint(10, 100)
    
    
    
    while f_tipp != gep_tipp:
        f_tipp:int=int(input("Adj meg egy szamot 10 - 100 között: "))
        if f_tipp > 10 and f_tipp < 100:
            print("A számnak 10 és 100 között kell lennie.")
            if f_tipp < gep_tipp:
                print("A tipped kisebb mint a gépé")
            elif f_tipp > gep_tipp:
                print("A tipped nagyobb mint a gépé ")
            else:
                print("Eltaláltad a gép tippjét! :D")
    return gep_tipp


