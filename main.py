import requests
import re
from datetime import datetime as dt
from bs4 import BeautifulSoup
from Application.salary import calculate_salary
from Application.db.people import get_employees


def scrap (url: str):
  response = requests.get(url)
  text = response.text
  soup = BeautifulSoup(text, 'html.parser')
  amended_text = str(soup.find(class_="morelangs"))
  print('На сайте Мультитран следующие словари относятся к "популярным":')
  for i in re.finditer('([A-Z])\w+\‑([A-Z])\w+', amended_text):
    result = i.group(0)
    print(result)


if __name__ == '__main__':
  scrap('https://www.multitran.com/')
  print(dt.today().strftime('\n%b.%d.%Y'))
  calculate_salary()
  get_employees()
