import feladatok

print("\n 1. |--- feladat ---| ")
elso_feladat=feladatok.elso()
print(elso_feladat)

print("\n 2.  |--- feladat Elsofele ---| ")
szamok=feladatok.hany5oszt_egyikfel()
print(szamok)


print("\n 2.  |--- feladat Masodikfele ---| ")
masodik_feladat=feladatok.hany5oszt_masikfel(szamok)
print(f"A számok között {masodik_feladat} db 5-mal osztható van!")




print("\n 3.  |--- feladat ---| ")
harmadik_feladat=feladatok.harmadik("Pörgős Bakugán", 2)




print("\n 4.  |--- feladat ---| ")
negyedik_feladat=feladatok.feladat4()
print(f" A felhasznalo {negyedik_feladat} szamot  adott meg")



print("\n 5. |--- feladat ---| ")
otodik_feladat=feladatok.kitalalos_jatek()
print(otodik_feladat)
