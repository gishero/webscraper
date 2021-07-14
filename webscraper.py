# from os import link
import requests
from bs4 import BeautifulSoup

# create csv file
filename = 'jobs.csv'
f = open(filename, "w")
# write headers
headers = "title,date\n"
f.write(headers)

# get webpage from url
url = 'https://au.indeed.com/jobs?q=mechatronics+graduate&l=Melbourne+VIC'
result = requests.get(url)


src = result.content
# create bs4 construct
soup = BeautifulSoup(src, 'lxml')
# container with all the job ads on the page
containers = soup.find_all("div",{"class": "slider_container"})

for container in containers:
    # css path for the job title
    job = container.select('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading4.color-text-primary.singleLineTitle.tapItem-gutter > h2 > span')[0].text.strip()
    
    f.write(job + "\n")

# close file after finish
f.close