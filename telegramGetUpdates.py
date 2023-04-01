import requests
TOKEN = "5937302183:AAHxqvoy9UjAIVIMlDUp6J7ny6y3D8X9brw"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())