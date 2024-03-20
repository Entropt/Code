import re
from new_utils import *

login_url = "http://localhost:4280/login.php"

proxy = {
    "http": "127.0.0.1:8080"
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "http://localhost:4280/login.php",
    "DNT": "1",
    "Origin": "http://localhost:4280",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

passwd = open('pass.txt', 'r').read().split('\n')

session = requests.Session() 
credentials = {
    "username": "admin",
    "password": "password",
    "Login": "Login",
    "user_token": CSRF_Manage.get_token(session, login_url)
}

header["Cookie"] = "PHPSESSID=" + session.cookies.get("PHPSESSID", domain=".localhost") + "; security=impossible"

response = session.post(url=login_url, proxies=proxy, headers=header, data=credentials, allow_redirects=False)

cookie_header = response.headers['Set-Cookie']

phpsessid = cookie_header[10:42]

print(cookie_header)

print(phpsessid)

header["Cookie"] = "PHPSESSID=" + phpsessid + "; security=impossible"

new_response = session.get(url="http://localhost:4280/vulnerabilities/brute/", proxies=proxy, headers=header)

print(new_response.text)

