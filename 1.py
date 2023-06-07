import requests
import os
from urllib.parse import urlsplit, unquote_plus

# id = '5eb87ce4ffd86e000604b337'
# response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}/")
#
# #for i in response.json()['links']['flickr']['original']:
# print(os.path.splitext(urlsplit("http://example.com/image.png#about_python").path)[1])

# response = requests.get('https://api.nasa.gov/planetary/apod',
#                         params={'api_key': 'OkZFKyc9IH4w7J6qnMJaceaIE5B17MFyLATPVlyf'})
# print(response.url)
#
#
# def get_file_permission(file_url):
#     return os.path.splitext(urlsplit(file_url).path)[1]
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=OkZFKyc9IH4w7J6qnMJaceaIE5B17MFyLATPVlyf')

print(response.content)
# for i,j in enumerate(response):
#     print(j.content())
#     # image_name = f'nasa_apod_{i}{get_file_permission(j)}'
#     # with open(f'./images/{image_name}', 'wb') as file:
#     #     file.write(response.content)
