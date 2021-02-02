import requests
import sys

from bs4 import BeautifulSoup


class MyError(Exception):
    """Class of user-defined exception to handle abnormal cases of requests to site."""

    def __init__(self, text):
        self.txt = text


def get_events():
    """Function performs printing of closest events from site python.org"""

    # setting output for result
    stdout = sys.stdout

    # target link
    link = 'https://www.python.org/'

    # truing to get response from link
    try:
        response = requests.get(link)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # getting html data
    if response.status_code == 200:
        content = response.content
    else:
        raise MyError("Service unavailable now. Please try again later")

    # working with html data
    soup = BeautifulSoup(content, 'html.parser')
    target_div = soup.find("div", {"class": "shrubbery"})
    target_menu = target_div.find("ul", {"class": "menu"})

    # printing out received data
    print('Ближайшие события Python Software Foundation:')
    for item in target_menu.children:
        try:
            stdout.write(item.text + '\n')
        except AttributeError:
            continue


if __name__ == '__main__':
    get_events()
