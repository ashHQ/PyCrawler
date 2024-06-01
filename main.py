from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f'Requests failed {url}')
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)
        
        # print(urls)
        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, url)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass















url = input("Enter the url you want to Scrape. ")
keyword = input("Enter the keyboard you want to search for in the url provided. ")
spider_urls(url, keyword)