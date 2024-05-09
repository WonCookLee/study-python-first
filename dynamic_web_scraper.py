from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

with sync_playwright() as playwright:
    chromium = playwright.chromium
    # 브라우저 안보이게 실행 = True
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wanted.co.kr/")
    time.sleep(3)

    # 검색버튼 클릭
    page.click("button.Aside_searchButton__Xhqq3")
    time.sleep(1)

    input = page.get_by_placeholder("검색어를 입력해 주세요.")
    input.fill("java")

    page.keyboard.down("Enter")
    time.sleep(4)

    page.click("a#search_tab_position")
    time.sleep(4)

    for i in range(8):
        page.keyboard.down("End")
        time.sleep(3)

    content = page.content()
    # print(content)
    
    time.sleep(3)
    playwright.stop()
    
    soup = BeautifulSoup(content, "html.parser")
    
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    jobs_db = []
    for job in jobs :
        title = job.find("strong", class_="JobCard_title__ddkwM")
        company = job.find("span", class_="JobCard_companyName__vZMqJ")
        reward = job.find("span", class_="JobCard_reward__sdyHn")
        link = job.find("a").get("href")
        job_data = {
            "title" : title.text,
            "company" : company.text,
            "reward" : reward.text,
            "link" : f"https://www.wanted.co.kr{link}",
        }
        jobs_db.append(job_data)
    
    file = open("java_jobs.csv", "w", encoding="utf-8", newline = "")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "reward", "link"])
    
    for job_data in jobs_db :
        writer.writerow(job_data.values())