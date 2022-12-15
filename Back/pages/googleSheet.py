import http.client
from bs4 import BeautifulSoup



# conn = http.client.HTTPSConnection("https://www.google.com/maps/place/", 8080)
# res = conn.request("HEAD","/brasil,20551")
# print(res)


# import http.client
#
# from pip._vendor import requests
#
# conn = http.client.HTTPSConnection("www.google.com")
# conn.request("GET", "/maps/place/brasil,20551")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)
# data1 = r1.read()  # This will return entire content.
# # The following example demonstrates reading data in chunks.
# conn.request("GET", "/maps/place/brasil,20551")
# r1 = conn.getresponse()
# while chunk := r1.read(200):
#     print(repr(chunk))
#
# # Example of an invalid request
# conn = http.client.HTTPSConnection("www.google.com")
# conn.request("GET", "/maps/place/brasil,20551")
# r2 = conn.getresponse()
# print(r2.status, r2.reason)
# data2 = r2.read()
# conn.close()
#
# url = "http://www.google.com/maps/place/brasil,20551"
# headers = {'Accept-Encoding': 'identity'}
# r = requests.get(url, headers=headers)
# print(dict(r.headers))
#
#
#
#
# resp = requests.get("http://www.google.com/maps/place/brasil,20551")
#
#
# html = resp.text
#
# # parse the HTML
# soup = BeautifulSoup(html, "html.parser")
#
# # print the HTML as text
# print(soup.body.get_text().strip())


import pgeocode

nomi = pgeocode.Nominatim('pt')
print(nomi.query_postal_code("20551"))

