import requests

url = "http://craphound.com/images/1006884_2adf8fc7.jpg"

response = requests.get(url)

if response.status_code == 200:

    with open("D:\\sample.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully!")
else:
    print("Failed to retrieve the image.")
