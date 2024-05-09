import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", id="category-2").find_all("li")[1:-1]

# print(jobs)

all_jobs = []
for job in jobs:
    title = job.find("span", class_="title")

    company, position, region  = job.find_all("span", class_="company")[0:3]
    
    job_data = {
        "title" : title.text,
        "company" : company.text,
        "position" : position.text,
        "region" : region.text,
    }
    all_jobs.append(job_data);
    
print(all_jobs)
    