import requests
import sys

from bs4 import BeautifulSoup

# setting output for result
stdout = sys.stdout

# target link
link = 'https://www.python.org/'

# getting html data
response = requests.get(link)
content = response.content

# working with html data
soup = BeautifulSoup(content, 'html.parser')
target_div = soup.find("div", {"class": "shrubbery"})
target_menu = target_div.find("ul", {"class": "menu"})

print('Ближайшие события Python Software Foundation:')
for item in target_menu.children:
    try:
        stdout.write(item.text + '\n')
    except AttributeError:
        continue
