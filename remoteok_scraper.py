import requests

url = f"https://remoteok.com/"
response = requests.get(
    url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })

# User-Agent 넣야 status_code 200
# 안넣으면 429
print(response.status_code);