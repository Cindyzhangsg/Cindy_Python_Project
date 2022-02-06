import requests
dest_url = "https:// www.google.com/search"
d = {"tbm isch&q": "violins"}
resp = requests.get(dest_url, params = d)
print(resp.url)
print(resp.text[:200])