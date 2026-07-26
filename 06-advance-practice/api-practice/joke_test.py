import requests

try:
    response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json", timeout=7)
    if response.status_code == 200:
        data = response.json()
        print(data['joke'])
    else:
        print("API Issuse - Try Again!")
except requests.exceptions.RequestException:
    print("Internet/Server Issue - Try Again!")
