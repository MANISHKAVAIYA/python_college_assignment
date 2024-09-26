import urllib.request

url = 'https://stackoverflow.com'

# Mimicking a browser request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(req)
webContent = response.read()

with open('webpage.html', 'wb') as file:
    file.write(webContent)

print("Webpage saved as 'webpage.html'.")
