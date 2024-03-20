import requests
from bs4 import BeautifulSoup

proxy = {
    "http": "127.0.0.1:8080"
}

class CSRF_Manage:
    @staticmethod
    def get_token(session:requests.Session, url:str):
        response = session.get(url, proxies=proxy)
        soup = BeautifulSoup(response.text, 'html.parser')
        user_token = soup.find("input", {"name": "user_token"})
        return user_token["value"]