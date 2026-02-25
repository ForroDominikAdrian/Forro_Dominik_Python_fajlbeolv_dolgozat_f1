"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

direct = dict()
lst = []
with open("beolvasando_adatok/f1.txt","r",encoding="UTF-8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        elemek = sor.strip().split(";")
        gyozelem = int(elemek[2])
        futam = int(elemek[3])
        direct = dict(nev = elemek[0],csapat = elemek[1], gyozelmek = gyozelem,futamok = futam)
        lst.append(direct)

def futamok(lst,melyik):
    legtobb = 0
    legt = ""
    legkevesebb = 10000
    legk = ""
    for i in range(len(lst)):
        if legtobb < lst[i]["gyozelmek"]:
            legtobb = lst[i]["gyozelmek"]
            legt = lst[i]["nev"]
        if legkevesebb > lst[i]["gyozelmek"]:
            legkevesebb = lst[i]["gyozelmek"]
            legk = lst[i]["nev"]
    if melyik == True:
        return legt
    if melyik == False:
        return legk

def futamsz(lst,melyik):
    legtobb = 0
    legt = ""
    avrg = 0
    for i in range(len(lst)):
        if legtobb < lst[i]["futamok"]:
            legtobb = lst[i]["futamok"]
            legt = lst[i]["nev"]
        avrg += lst[i]["futamok"]
    if melyik == True:
        return legt
    else:
        return round(avrg / len(lst), 2)


def csapat(lst):
    idk = []
    thisdict = {}
    for i in range(len(lst)):
            gyozelmek = lst[i]["gyozelmek"]
            if lst[i]["csapat"] in thisdict:
                thisdict[lst[i]["csapat"]] += gyozelmek
            else:
                thisdict[lst[i]["csapat"]] = gyozelmek
        
    return max(thisdict, key=thisdict.get)



print(lst)
print(f"1. A beolvasott fájlban összesen {len(lst)} versenyző szerepel.")
print(f"2. A legtöbb futamot nyert versenyző: {futamok(lst,True)}")
print(f"3. A legkevesebb futamot nyert versenyző: {futamok(lst,False)}")
print(f"4. A legtöbb futamot teljesített versenyző: {futamsz(lst,True)}")
print(f"5. Az átlagos futamszám: {futamsz(lst,False)}")
print(f"***A legtöbb futamgyőzelmet szerző csapat: {csapat(lst)}")