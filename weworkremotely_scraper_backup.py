import requests
from bs4 import BeautifulSoup


response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")

# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")

pages = soup.find("div", class_="pagination").find_all("span", class_="page")

for index in range(len(pages)) :
    page_num = index+1
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={page_num}"
    response = requests.get(url)
    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

    all_jobs = []
    for job in jobs:
        title = job.find("span", class_="title")

        company, position, region  = job.find_all("span", class_="company")[0:3]
        link = job.find_all("a")[-1].get("href")
        
        job_data = {
            "title" : title.text,
            "company" : company.text,
            "position" : position.text,
            "region" : region.text,
            "link" : f"https://weworkremotely.com{link}",
        }
        all_jobs.append(job_data);
        
    print(f"pageNo : {page_num}", all_jobs)
