import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--headless")

# enter path var

#webdriver_path = "C:\chromedriver.exe"

def optional_scrawl(username:str='instagram'):
    
    url = "https://www.instagram.com/{username}/"


    driver = webdriver.Chrome()


    driver.get(url)


    time.sleep(3)


    html = driver.page_source


    driver.quit()


    soup = BeautifulSoup(html, 'html.parser')
    print([html])

    posts = soup.find_all('article')


    with open('instagram_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Caption', 'username', 'Image'])

        for post in posts:
            
            #caption_element = post.find('div', class_='caption')
            #date_element = post.find('div', class_='date')
            captions_=[]
            image=[]
            for data_ in post.find_all('img'):
                try:
                    captions_.append(data_['alt'])
                    image.append(data_['src'])
                except:
                    continue

            writer.writerow([" ".join(captions_), username, ",".join(image)])

    return 'Success'
