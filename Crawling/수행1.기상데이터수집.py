from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

#가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#기상데이터 수집 사이트 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')



#파일 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())
fname = "{:Weather_%Y_%m_%d_%H_%M.csv}".format(datetime.now())
file = open(dir+'/'+fname, 'w', encoding='utf-8')

#기상데이터 수집
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    time.sleep(1)
    tr1 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a').text
    tr2 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
    tr3 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
    tr4 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
    tr5 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
    tr6 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
    tr7 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
    tr8 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
    tr9 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
    tr10 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
    tr11 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
    tr12 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
    tr13 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text
    tr14 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(14)').text

    file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(tr1, tr2, tr3, tr4,
                                                                    tr5, tr6, tr7, tr8, tr9,
                                                                    tr10, tr11, tr12,
                                                                    tr13, tr14))
file.close()
print('완료...')

# tds = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr:nth-child(1) > td')
#
# for tr in trs:
#     tr1 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a').text
#     for td in tds:
#         tr2 = td.find_element(By.CSS_SELECTOR, 'td').text
#
#     file.write('{},{}'.format(tr1, tr2))
# file.close()
# print('완료...')