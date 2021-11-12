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
Spouštění souboru ```main.py``` v přík. řádku požadujeme dva povinné argumenty.
```
main.py <odkaz územního celku> <výsledný soubor>
```
Následně se vým stáhnou výsledky jako soubor s příponou ```.csv```

# Ukázka projektu
Výsledky hlasování pro okres České Budějovice

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101
2. argument: Data.csv

# Průběh stahovaní
```
Iam donwloading data from this 
I am saving, to file Data.csv
I am ending this program
```
