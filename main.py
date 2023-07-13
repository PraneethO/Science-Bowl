import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import scraper

directory = 'INPUT'

for filename in os.listdir(directory):
    if filename.endswith(".TXT"):
      scraper.sort_file(filename)
    else:
        print('Input file must be a text document.')


folder_location = 'INPUT_HERE'

# connect to website and get list of all pdfs
url = "https://science.osti.gov/wdts/nsb/Regional-Competitions/Resources/MS-Sample-Questions"
response = requests.get(url)
soup= BeautifulSoup(response.text,"html.parser")  

for link in soup.select("a[href$='.pdf']"):
  filename = os.path.join(folder_location,link['href'].split('/')[-1])
  with open(filename, 'wb') as f:
    f.write(requests.get(urljoin(url,link['href'])).content)









