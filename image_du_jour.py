import requests
from PIL import Image
from io import BytesIO
api_key = "lqlmxg4mnC5vbrMwt5Tn2oksg34exwXVIawIHkAk"
url = "https://api.nasa.gov/planetary/apod"

response = requests.get(url, params = {"api_key":api_key})
data = response.json()

print("Titre:", data ["title"])
image_url = data["url"]
img_data = requests.get(image_url)
img = Image.open(BytesIO(img_data.content))
img.show()