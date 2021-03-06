import requests
import sys
import csv

from bs4 import BeautifulSoup


def get_municipal_codes(table, municipal_codes) -> list:
    for numbers in table:
        for number in numbers.find_all("td", class_="cislo"):
            municipal_codes.append(number.text)

    return municipal_codes


def get_city(table, names_of_the_village) -> list:
    for cities in table:
        for city in cities.find_all("td", headers="t1sa1 t1sb2"):
            if city != "-":
                names_of_the_village.append(city.text)
        for city2 in cities.find_all("td", headers="t2sa1 t2sb2"):
            if city2 != "-":
                names_of_the_village.append(city2.text)
        for city3 in cities.find_all("td", headers="t3sa1 t3sb2"):
            if city3 != "-":
                names_of_the_village.append(city3.text)
    return names_of_the_village


def get_url_path(tr) -> str:
    return tr.find("a")["href"]


def get_data_for_properties(soup, complete_url_array, hostname) -> list:
    tables = soup.find_all("td", {"class": "cislo"})
    for table in tables:
        path = get_url_path(table)
        complete_url = f"{hostname}{path}"
        complete_url_array.append(complete_url)
    return complete_url_array


def get_other_properties(complete_url_array, voter_list, valid_votes, issued_envelopes) -> tuple:
    for i in complete_url_array:
        r = requests.get(i)
        # request on other pages
        parser = BeautifulSoup(r.text, "html.parser")
        voter = parser.find("td", {"headers": "sa2"}).text
        voter_list.append(voter.replace("xa", "").replace(" ", ""))
        envelopes = parser.find("td", {"headers": "sa5"}).text
        issued_envelopes.append(envelopes.replace(" ", ""))
        votes = parser.find("td", {"headers": "sa6"}).text
        valid_votes.append(votes.replace(" ", ""))
    return voter_list, issued_envelopes, valid_votes


def get_list_of_parties(soup, list_of_parties) -> list:
    for fronde in soup.find_all("td", class_="overflow_name"):
        if fronde != "-":
            list_of_parties.append(fronde.text)
        if len(list_of_parties) > 26:
            break
    return list_of_parties


def get_all_data_to_table(name_of_city, municipal_codes, names_of_the_village, voter_list,
                          issued_envelopes, valid_votes, list_of_parties):
    csv_colums = ["municipal code", "names of the village", "valid votes",
                  "voter list", "issued envelopes", tuple(list_of_parties)]

    with open(str(name_of_city), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_colums)
        for item in zip(municipal_codes, names_of_the_village, valid_votes,
                        voter_list, issued_envelopes):
            writer.writerow(item)


def main():
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

    r = requests.get(url)
    if r.status_code != 200:
        print("Status code is not 200")

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find_all("tr")

    if url.startswith("https://volby.cz/pls/ps2017nss/"):
        print("I am donwloading data from this URL", url)
        get_municipal_codes(table, municipal_codes)
        get_city(table, names_of_the_village)
        get_data_for_properties(soup, complete_url_array, hostname)
        get_other_properties(complete_url_array, voter_list, valid_votes, issued_envelopes)
        print("I am saving, to file ", sys.argv[2])
        get_list_of_parties(soup, list_of_parties)
        get_all_data_to_table(name_of_city, municipal_codes, names_of_the_village, voter_list,
                              issued_envelopes, valid_votes, list_of_parties[0:25])
        print("I am ending this program")
    else:
        print("Wrong data")


if __name__ == '__main__':
    main()
    

