'''
Find the tutorial for this file on youtube --
https://www.youtube.com/watch?v=3xQTJi2tqgk
'''

import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA"

r = requests.get(url)

# r.content contains all the information available at the url in html format

soup = BeautifulSoup(r.content)

# Now we have all html data within our class object

# find_all("a") method finds all links with anchor tag in it on the page (i.e. </a> tags)

links = soup.find_all("a")

# here we print all links with the anchor tag, specifically the hyperlinks or href for each link on the page

# link.get("tag") finds all references to the given tag argument (if wanted body tags use "b")

# prints all the different links

for link in soup.find_all("a"):
    print link.get("href")

# link.text shows text for each individual link on the page

# prints all text associated with tag

for link in soup.find_all("a"):
    print link.text

# To make this look better, we can add in the hyperlinks

# We now can print the link text and the link itself

for link in soup.find_all("a"):
    print link.text, link.get("href")

# Alternatively, we can use string formating to get the same result with actual html in the output

for link in links:
    # if "http" in link.get("href"): conditional here would ensure None or errors would not be printed
    # probably would be best to do try or except since can give problems in things non-interable
    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


# Here we are searching for all data with the div tag
g_data = soup.find_all("div", {"class": "info"})
