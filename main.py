import requests
import bs4

# URL della prima pagina
base_url = "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1"

# Variabile per tenere traccia delle pagine
page = 1

while True:
    # Costruisci l'URL completo con il numero di pagina
    url = f"{base_url}&o={page}"

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
        print("Nessun risultato trovato su pagina", page)
        break  # Esci dal ciclo se non ci sono più risultati

    page += 1
