import requests, bs4

# res = requests.get('http://nostarch.com')
# print("Status...")
# print(res.raise_for_status())
# noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
# print(str(noStarchSoup))
# print(noStarchSoup.p)
# print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
# print(str(exampleSoup))
# elems = exampleSoup.find_all('p', class_='shan')
# print(elems[0].a)

print(exampleSoup)
newelemens = exampleSoup.select('p.shan a')
print(newelemens)

# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# print(str(elems[0]))
# print(elems[0].attrs)
# print(type(exampleSoup))

# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())