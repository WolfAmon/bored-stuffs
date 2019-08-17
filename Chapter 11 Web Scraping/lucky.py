# ! python 3

import requests, sys, webbrowser, bs4

custom_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }

print('googling...' + ' '.join(sys.argv[1:]))
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]), headers=custom_header)
res.raise_for_status()
# print(res.status_code)
# print(res.url)
# print(res.headers)
# print(res.encoding)
# print(res.text)

# file = open('lucky.html', 'wb')

# for chunk in res.iter_content(100000):
#     file.write(chunk)

# file.close()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(soup)
# print(soup.prettify())
# TODO: Open a browser tab for each result.

linkElems = soup.select('.rc .r')
for i in range(len(linkElems)):
    print(linkElems[i].select_one("a").get("href"))
	# webbrowser.open(linkElems[i].select_one("a").get("href"))