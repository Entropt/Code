from new_utils import *

login_url = "http://localhost:4280/login.php"

header = {
    "Referer": "http://localhost:4280/login.php"
}

session = requests.Session() 

# First login into DVWA
def initial_login():
    
    # Default username and password of DVWA
    credentials = {
        "username": "admin",
        "password": "password",
        "Login": "Login",
        "user_token": CSRF_Manage.get_token(session, login_url, header)
    }

    header["Cookie"] = "PHPSESSID=" + session.cookies.get("PHPSESSID", domain=".localhost") + "; security=impossible"

    # POST the credentials and not allow to redirect to take the PHPSESSID from response
    response = session.post(url=login_url, proxies=proxy, headers=header, data=credentials, allow_redirects=False)

    cookie_header = response.headers['Set-Cookie']
    phpsessid = cookie_header[10:42]
    header["Cookie"] = "PHPSESSID=" + phpsessid + "; security=impossible"