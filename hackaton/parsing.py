import csv
import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup






# def main():
    # star = datetime.now()
    # notebooks_url = 'https://www.eldorado.ru/c/noutbuki/'


if __name__ == "__name__":