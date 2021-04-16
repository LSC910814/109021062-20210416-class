import requests as reqs
import sys
from bs4 import BeautifulSoup

req=reqs.get(
    "https://search.books.com.tw/search/query/key/{0}/cat/all")

def generate_search(url, keyword):
    urls = url.format(keyword)
        return url

def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding ="utf8"
        soup = BeatifulSoup(r.text."lxml")
    else:
        print("HTTP request error!!")
        soup = None 
        return soup

if (__name__ == "__main__"):
    if len(sys.argv)>1:
        url = generate_search_key(URL,"Java")
        print(get_resource(url).text)