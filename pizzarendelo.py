"""
Pizzarendelő alkalmazás

A felhasználótól addig kérje be a rendeléseket, amíg a @ jelet nem ütjük le!
Minden rendelés során a  program kérje be, hogy:
1. sajtos, gombás, vagy sonkás pizzát kér-e?
2. mekkora a pizza mérete:
        kicsi   -  ára az ár 90%-a
        normál  - ára az ár 100%-a
        nagy    – ára az ár 110%-a

3.  kér e feltétet.

Alapárak:
A plusz feltét 50 Ft.
Normál sajtos pizza alapára 1000 Ft
Normál gombás pizza alapára 1100 Ft
Normál sonkás pizza alapára 1200 Ft


Tároljuk a felvett rendeléseket megfelelő listákba!  tipus, meret, feltet
Végezzük el minden rendelés esetében az ár kiszámítását is! esetleg ezt is tárolhatjuk egy listában! ar

A rendelések felvétele után készítsünk statisztikát!
1. Melyik típusú (név alapján)  pizzából hány darab fogyott?
2. Melyik pizzából fogyott a legtöbb?
3. Mekkora volt a bevétel?
4. Hányszor kértek extra feltétet?
5. A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet?
6. … ami még eszetekbe jut.
7 + menü indítása ahol lehet választani, hogy rendelést adunk le, vagy adatokat, statisztikákat nézünk

"""
import pizza_fuggvenyek

"""
pizzarendelo():

1 rendelés: 
be: sajtos
be: normál
be: nem kér feltétet
be: kér-e még? -> rendelés itt végződik

sok rendelés
adatszerkezet: 3db lista:
tipus=[]
meret=[]
feltet=[]
ar=[] -> indexek alapján árszámoló függvénynek átadjuk az értékeket
a listáknak globálisnak kell lennie

függvények:

rendelesfelvetel():
a listákat feltöltjük adatokkal


arszamitas():


rendeleskiiras():


statisztika1(): 2, 3 4 stb....


ne legyenek kódismétlések, azokat ki kell szervezni függvénybe
"""
pizza_fuggvenyek.diszites(" ")
pizza_fuggvenyek.diszites("*")
pizza_fuggvenyek.szovekiiras("Üdvözlöm a pizzarendelő alkalmazásban!"," ")
pizza_fuggvenyek.diszites("*")
pizza_fuggvenyek.diszites()
pizza_fuggvenyek.menuindito(pizza_fuggvenyek.menuvalaszto())





