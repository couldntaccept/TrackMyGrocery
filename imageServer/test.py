import requests

# image = '/Users/yu/Downloads/datess.jpeg'
image = "/Users/yu/Downloads/IMG_9442.JPG"

url = 'http://192.168.31.48:8080/ocr'
files = {'media': open(image, 'rb')}
# data = { "item_id" : "1"}
resp = requests.post(url, files=files)
print(resp.text)
