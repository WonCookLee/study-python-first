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

all_jobs = []

def set_job(jobs):
    for job in jobs:
        title = job.find("h2").text
        company = job.find("h3").text
        region = job.find("div", class_="location").text
        url = job.find("a")["href"]

        job_data = {
            "title": title,
            "company": company,
            "region": region,
            "link": f"https://remoteok.com{url}"
        }
        all_jobs.append(job_data) 

def get_jobs(keyword):
    print(f"Scrapping {keyword}...")
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("table", id= "jobsboard").find_all("td", class_="company position company_and_position")[1:]

    set_job(jobs)
    return all_jobs