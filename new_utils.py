import requests
from bs4 import BeautifulSoup

proxy = {
    "http": "127.0.0.1:8080"
}

class CSRF_Manage:
    
    # Take the user_token in any website
    @staticmethod
    def get_token(session:requests.Session, url:str, header):
        response = session.get(url, proxies=proxy, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        user_token = soup.find("input", {"name": "user_token"})
        return user_token["value"]