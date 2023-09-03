import requests
import bs4

url = "https://www.subito.it/annunci-italia/vendita/moto-e-scooter/?q=yamaha+r1"
res = requests.get(url)

soup = bs4.BeautifulSoup(res.content, "html.parser")
results = soup.findAll("div", class_="items__item item-card item-card--small")

maxResult = 2

if results:
    with open("testo.txt", "a") as file:
        count = 0
        for result in results:
            file.write(result.text + "\n")

            link = result.find("a")
            if link:
                href = link.get("href")
                file.write("Link: " + href + "\n")
            file.write("\n")
            count += 1
            if count >= maxResult:
                break
else:
    print("Elemento non trovato")
