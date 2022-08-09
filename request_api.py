import requests

r = requests.get("https://www.bbc.co.uk/")

print(r.status_code)
