import requests
from bs4 import BeautifulSoup
import sys
import csv


hostname: str = "https://volby.cz/pls/ps2017nss/"
url = sys.argv[1]
name_of_city = sys.argv[2]

complete_url_array = []
municipal_codes = []
names_of_the_village = []
voter_list = []
issued_envelopes = []
valid_votes = []
list_of_parties = []


def get_data(url_adress):
    global soup, table
    r = requests.get(url_adress)
    status = True
    while status:
        if r.status_code != 200:
            print("Status code is not 200")
        else:
            status = False

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find_all("tr")
    return soup, table


def get_numbers():
    for numbers in table:
        for number in numbers.find_all("td", class_="cislo"):
            municipal_codes.append(number.text)

    return municipal_codes


def get_city(soup):
    table = soup.find_all("tr")
    for cities in table:
        for city in cities.find_all("td", headers="t1sa1 t1sb2"):
            city = city.text
            if (city != "-"):
                names_of_the_village.append(city)
        for city2 in cities.find_all("td", headers="t2sa1 t2sb2"):
            city2 = city2.text
            if (city2 != "-"):
                names_of_the_village.append(city2)
        for city3 in cities.find_all("td", headers="t3sa1 t3sb2"):
            city3 = city3.text
            if (city3 != "-"):
                names_of_the_village.append(city3)
    return names_of_the_village


def get_url_path(tr) -> str:
    return tr.find("a")["href"]


def get_data_for_properties():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all("td", {"class": "cislo"})
    for table in tables:
        path = get_url_path(table)
        complete_url = f"{hostname}{path}"
        complete_url_array.append(complete_url)
    return complete_url_array


def get_other_properties(complete_url_array):
    for i in complete_url_array:
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "html.parser")
        voter = soup.find("td", {"headers": "sa2"}).text
        voter_list.append(voter.replace("xa", "").replace(" ", ""))
        envelopes = soup.find("td", {"headers": "sa5"}).text
        issued_envelopes.append(envelopes.replace(" ", ""))
        votes = soup.find("td", {"headers": "sa6"}).text
        valid_votes.append(votes.replace(" ", ""))
    return voter_list, issued_envelopes, valid_votes


def get_list_of_parties():
    for tr in complete_url_array:
        r = requests.get(tr)
        soup = BeautifulSoup(r.text, "html.parser")
        for fronde in soup.find_all("td", class_="overflow_name"):
            if fronde != "-":
                list_of_parties.append(fronde.text)
        if len(list_of_parties) > 26:
            break
    return list_of_parties



def get_to_csv(list_of_parties):
    csv_colums = ["municipal code", "names of the village", "valid votes",
                  "voter list", "issued envelopes", tuple(list_of_parties)]
    dict_of_data = [{"municipal code": municipal_codes},
                    {"names of the village": names_of_the_village},
                    {"valid votes": valid_votes},
                    {"voter list": voter_list},
                    {"issued envelopes": issued_envelopes},
                    {tuple(list_of_parties): ""}]

    with open("CeskeBudejovice.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = csv_colums)
        writer.writeheader()
        writer.writerows(dict_of_data)


def main():
    if url.startswith("https://volby.cz/pls/ps2017nss/"):
        print("I am donwloading data from this URL", url)
        get_data(url)
        get_numbers()
        get_city(soup)
        get_data_for_properties()
        get_other_properties(complete_url_array)
        print("I am saving, to file ", sys.argv[2])
        get_list_of_parties()
        get_to_csv(list_of_parties[0:25])
        print("I am ending this program")
    else:
        print("Wrong data")


if __name__ == '__main__':
    main()



