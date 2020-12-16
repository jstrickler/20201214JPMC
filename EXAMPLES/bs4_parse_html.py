#!/usr/bin/python
import bs4
import requests

# with open('../DATA/craigslist.html', 'r') as CL:
#     soup = bs4.BeautifulSoup(CL, 'lxml')

URL = "https://washingtondc.craigslist.org/"
response = requests.get(URL)
html = response.content.decode()
soup = bs4.BeautifulSoup(html, 'lxml')

for input_tag in soup.findAll('input'):
    print("{0} ({1})".format(
        input_tag.get('name', "*NO NAME*"),
        input_tag.get('type', '*NO TYPE*')
    ))
print('-' * 60)


search_form = soup.find(id="search")
print(search_form)
for option in search_form.findAll('option'):
    print(option.get("value"), option.getText())

