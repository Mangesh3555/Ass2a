##https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

#Step 1: Inspect Your Data Source
#Step 2: Scrape HTML Content From a Page
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#print(page.text)

#Step 3: Parse HTML Code With Beautiful Soup
soup = BeautifulSoup(page.content, "html.parser")

#Find Elements by ID
results = soup.find(id="ResultsContainer")
#print(results.prettify())

#Find Elements by HTML Class Name
job_elements = results.find_all("div", class_="card-content")

#Extract Text From HTML Elements
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

  #  print(title_element)
  #  print(company_element)
  #  print(location_element)
  #  print()
    
  #  print(title_element.text)
  #  print(company_element.text)
  #  print(location_element.text)
  #  print()

    print("Title of Job =",title_element.text.strip())
    print("Company Name =",company_element.text.strip())
    print("Location of Job =",location_element.text.strip())
    print()

#Find Elements by Class Name and Text Content
#python_jobs = results.find_all("h2", string="Python")
#print(python_jobs)

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print("Number of Jobs in Python =", len(python_jobs))
#print(len(python_jobs))


    
