import requests
import bs4

url = input("Inserisci il sito: ")  # Sito target
res = requests.get(url)

soup = bs4.BeautifulSoup(res.content, "html.parser")
results = soup.findAll(
    "div", class_="SmallCard-module_item-key-data__fcbjY"
)  # Correzione qui

if results:
    with open("testo.txt", "a") as file:
        for result in results:
            file.write(result.text + "\n")  # Scrivi il testo su una nuova riga
else:
    print("Elemento non trovato")
