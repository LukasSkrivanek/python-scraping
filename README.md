# Engeto-py-3-projekt
Třetí projekt na Python Akademii od Engeta

# Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v Roce 2017 Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101)

# Instalce knihoven
Knihovny které jsou použit v kódu jsou uložené v souboru requiremnets.txt Pro instalaci doporučuji použít nové virtuální prostředí a s naistalovaným manažerem spustit následovně:
```
$ pip3 --version                    # overim verzi manazeru
$ pip3 install - r requirements.txt # nainstalujeme knihovny
```
# Spouštění projektu 
Spouštění souboru ```main.py``` v přík. řádku 
```
main.py 
```
Následně se nám stáhnou výsledky jako soubor s příponou ```.csv```

# Ukázka projektu
Výsledky hlasování pro okres České Budějovice

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101
2. argument: Data.csv

# Průběh stahovaní
```
I am donwloading data from this 
I am saving, to file Data.csv
I am ending this program
```
# Částečný výstup
```
,municipal_code,names of the village,valid votes,voter list,issued nevelopes,"('Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální', 'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 'Strana Práv Občanů')"
0,535826,Adamov,472,682,473,
1,536156,Bečice,63,82,63,
2,544272,Borek,914,1 215,923,
```
