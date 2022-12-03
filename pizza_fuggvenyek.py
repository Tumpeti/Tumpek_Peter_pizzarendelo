pizza_fajtak = []
pizza_meretek = []
pizza_feltetek = []
pizza_arak = []
oldalhossz = 50

def program_indito():
    diszites("*")


def szovekiiras(szoveg, diszites=" "):
    jel_oldalankent = int((oldalhossz - len(szoveg))/2)
    print(jel_oldalankent*diszites + szoveg + jel_oldalankent*diszites)


def menuvalaszto():
    print("Kérem válasszon az alábbi menüpontok közül!\n- 1 - Rendelésfelvétel\n- 2 - Rendelés áttekintése")
    menu_szama = input()
    return int(menu_szama)


def menuindito(menuszam):
    if menuszam == 1:
        rendelesfelvetel()
    elif menuszam == 2:
        rendeles_kiirasa()


def diszites(jel=" "):
    print(oldalhossz * jel)

def fajta_bekero():
    fajta = input("Milyen típusú pizzát szeretne? sa/go/so ")
    return fajta


def meret_bekero():
    meret = input("Mekkora pizzát szeretne? ki/no/na ")
    return meret


def feltet_bekero():
    feltet = input("Kér extra feltétet? igen/nem ")
    return feltet


def rendelesfelvetel():
    i = 0
    while input("Kíván pizzarendelést leadni?\n") != "nem":
        pizza_fajtak.append(fajta_bekero())
        pizza_arak.append(arszamitas(i))
        i += 1
    menuindito(menuvalaszto())


def rendeles_kiirasa():
    print(pizza_arak)
    print(pizza_fajtak)
    print(pizza_meretek)
    print(pizza_feltetek)
    menuindito(menuvalaszto())


def arszamitas(i):
    ar = 0
    if pizza_fajtak[i] == "sa":
        ar = 1000
    elif pizza_fajtak[i] == "go":
        ar = 1100
    elif pizza_fajtak[i] == "so":
        ar = 1200
    pizza_meretek.append(meret_bekero())
    if pizza_meretek[i] == "ki":
        ar = ar * 0.9
    elif pizza_meretek[i] == "no":
        ar = ar * 1
    elif pizza_meretek[i] == "na":
        ar = ar * 1.1
    pizza_feltetek.append(feltet_bekero())
    if pizza_feltetek[i] == "igen":
        ar += 50
    return ar


