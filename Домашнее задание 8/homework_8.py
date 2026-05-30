import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()

valutes = data["Valute"]

max_value = -1
max_name = ""

for code, info in valutes.items():
    name = info["Name"]
    value = info["Value"]
    
    if value > max_value:
        max_value = value
        max_name = name

print(max_name)