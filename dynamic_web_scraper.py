from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv
from file import save_to_file

def wantedJobsScraper(keyword) :
    jobs_db = []
    print("wantedJobsScraper start")
    with sync_playwright() as playwright:
        chromium = playwright.firefox
        # 브라우저 안보이게 실행 = True
        browser = chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wanted.co.kr/")
        time.sleep(5)

        print("검색버튼 클릭 전")
        
        # 검색버튼 클릭
        #print(page.content())
        page.click("button.Aside_searchButton__Xhqq3")
        time.sleep(3)

        print("검색어를 입력 전", keyword)
        input = page.get_by_placeholder("검색어를 입력해 주세요.")
        input.fill(keyword)

        time.sleep(1)
        print("엔터 전")
        page.keyboard.down("Enter")
        time.sleep(4)

        print("포지션 클릭 전")
        page.click("a#search_tab_position")
        time.sleep(4)

        for i in range(8):
            page.keyboard.down("End")
            time.sleep(4)

        content = page.content()
        # print(content)
        
        time.sleep(3)
        playwright.stop()
        
        soup = BeautifulSoup(content, "html.parser")
        
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        
        for job in jobs :
            title = job.find("strong", class_="JobCard_title__ddkwM")
            company = job.find("span", class_="JobCard_companyName__vZMqJ")
            reward = job.find("span", class_="JobCard_reward__sdyHn")
            link = job.find("a").get("href")
            job_data = {
                "keyword" : keyword,
                "title" : title.text,
                "company" : company.text,
                "reward" : reward.text,
                "link" : f"https://www.wanted.co.kr{link}",
            }
            jobs_db.append(job_data)
        
    
    #print("wantedJobsScraper end ", jobs_db)
    return jobs_db

keywords = [
    "java",
    "react",
    "flutter",
]


for keyword in keywords :
    jobs_db = wantedJobsScraper(keyword)
    save_to_file(keyword, jobs_db)


