# pip install requests

import requests


response = requests.get("https://www.cursbnr.ro/")
print(response)
print(response.status_code)
print(response.text)

with open("curs.html", "w") as fwriter:
    fwriter.write(response.text)
