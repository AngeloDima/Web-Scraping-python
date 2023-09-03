import requests
import bs4
import json

# URL della prima pagina
base_url = "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1"

page = 1
total_results = 0
data = []

while True:
    url = f"{base_url}&o={page}"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    results = soup.findAll("div", class_="items__item item-card item-card--small")

    if results:
        count = 0
        for r in results:
            item_data = {}
            item_data["Testo"] = r.text
            a = r.find("a")
            if a:
                href = a.get("href")
                item_data["Link"] = href
            data.append(item_data)
            count += 1
            total_results += 1
        print(f"Risultati su pagina {page}: {count}")
    else:
        break
    page += 1

print(f"Totale risultati: {total_results}")

# Converti i dati in formato JSON come testo
json_data = json.dumps(data, indent=4)

# Stampa il JSON
print(json_data)
