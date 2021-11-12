# Engeto-py-3-projekt
Třetí projekt na Python Akademii od Engeta

# Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v Roce 2017 Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101)

# Instalce knihoven
Knihovny které jsou použit v kódu jsou uložené v souboru requiremnets.txt Pro instalaci doporučuji použít nové virtuální prostředí a s naistalovaným manažerem spustit následovně:
```
$ pip3 --version                    # overim verzi manazeru
$ pip3 install - r requirements.txt # nainstalujeme knihovny
```
# Spouštění projektu 
Spouštění souboru ```election-scraper.py``` v přík. řádku požadujeme dva povinné argumenty.
```
python election-scraper <odkaz územního celku> <výsledný soubor>
```
Následně se vým stáhnou výsledky jako soubor s příponou ```.csv```

# Ukázka projektu
Výsledky hlasování pro okres Prostějov

