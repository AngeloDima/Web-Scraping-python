import requests
import bs4

# Lista degli URL da visitare
urls = [
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1",
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1&o=2",
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1&o=3",
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1&o=4",
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1&o=5",
    "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1&o=6",
]

for url in urls:
    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.content, "html.parser")
    results = soup.findAll("div", class_="items__item item-card item-card--small")

    if results:
        with open("testo.txt", "a") as file:
            for r in results:
                file.write(r.text + "\n")

                link = r.find("a")
                if link:
                    href = link.get("href")
                    file.write("Link: " + href + "\n")
                    file.write("\n")
    else:
        print("ERRORE per l'URL:", url)

print("Operazione completata.")
