import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

search_query = 'zep'.replace(' ', '+')
base_url = 'https://www.amazon.in/s?k={0}'.format(search_query)

def get_Amazon(prod_name):
    search_query = prod_name.replace(' ', '+')
    base_url = 'https://www.amazon.com/s?k={0}'.format(search_query)
    items = []
    for i in range(1,2):
        print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
        response = requests.get(base_url + '&page={0}'.format(i), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
        for result in results:
            product_name = result.h2.text
            try:
                rating = result.find('i', {'class': 'a-icon'}).text
                try:
                    rating_count = result.find_all('span', {'aria-label': True})[1].text
                except:
                    rating_count="NA"
            except AttributeError:
                continue
            try:
                price1 = result.find('span', {'class': 'a-price-whole'}).text
                price2 = result.find('span', {'class': 'a-price-fraction'}).text
                price = price1 + price2
                product_url = 'https://amazon.com' + result.h2.a['href']
                product_img = result.div.img['src']
                price_actual = result.find('span',{'class':'a-offscreen'}).text
                auther = result.find('a',{'class':'a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style'}).text
                date = result.find('span',{'class':'a-size-base a-color-secondary a-text-normal'}).text
                items.append([product_name, rating, rating_count, price, product_url,product_img,date,auther,price_actual])
            except AttributeError:
                continue
    return items

