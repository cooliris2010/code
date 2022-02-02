from bs4 import BeautifulSoup
import requests 

url ="https://www.newegg.com/p/0BA-00AG-00008?quicklink=true"

results = requests.get(url)
print(results.text)

#save it in a file 
doc= BeautifulSoup(results.text,"html.parser")

prices= doc.find_all(text="$")

parent = prices[0].parent

strong = parent.find("strong")

print(strong.string)