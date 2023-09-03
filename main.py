import requests
import bs4

# URL della prima pagina
base_url = "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1"

page = 1
total_results = 0

while True:
    url = f"{base_url}&o={page}"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    results = soup.findAll("div", class_="items__item item-card item-card--small")

    if results:
        with open("testo.txt", "a") as file:
            count = 0
            for r in results:
                file.write("Testo: " + r.text + "\n" + "\n")
                file.write("\n")
                count += 1
                total_results += 1
            print(f"Risultati su pagina {page}: {count}")
    else:
        break
    page += 1

print(f"Totale risultati: {total_results}")
