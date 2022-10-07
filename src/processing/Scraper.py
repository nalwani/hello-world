import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        pass

    @staticmethod
    def getWikiTOC(subject):
        print("Scrapping...")

        base_url = "https://en.wikipedia.org/wiki"
        search_url = base_url + "/" + subject

        response = requests.get(url=search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table_of_content = soup.find('div', {'class': "toc"})
        toc_items_raw = table_of_content.find_all('span', {'class': "toctext"})

        toc_items = []
        for item in toc_items_raw:
            print(item.text)
            toc_items.append(item.text)

        return toc_items