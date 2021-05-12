import requests
from bs4 import BeautifulSoup


def get_quote():
    user_url = input("Input the URL: \n")
    correct_url = 'http://api.quotable.io/quotes/-4WQ_JwFWI'

    try:
        r = requests.get(user_url)
        print(r.json()['content'])

        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup.prettify())

        return r

    except:
        print("Invalid quote resource!")


get_quote()
