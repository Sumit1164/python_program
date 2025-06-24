import requests
city = input("Enter the name of city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
print(r.text)