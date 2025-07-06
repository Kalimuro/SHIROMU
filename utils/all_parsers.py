from utils.imports import *


def doxbin_parser(url):
    if requests.get(url).status_code == 404:
        print('Ничего не найдено')

    else:
        siilka = requests.get(url)
        soup = BeautifulSoup(siilka.text, 'html.parser')
        dox = soup.find_all('div')
        for text1 in dox:
            print(text1.text)



