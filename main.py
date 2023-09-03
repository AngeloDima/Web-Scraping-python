import requests
import bs4

url = input("Inserisci il sito: ")  # Sito target
res = requests.get(url)

soup = bs4.BeautifulSoup(res.content, "html.parser")
results = soup.findAll("div", class_="SmallCard-module_item-key-data__fcbjY")

maxCount = 3

if results:
    with open("testo.txt", "a") as file:
        count = 0
        for result in results:
            file.write(result.text + "\n" + "\n")  # Scrivi il testo su una nuova riga
            # Limite risultati
            count += 1
            if count >= maxCount:
                break


else:
    print("Elemento non trovato")
