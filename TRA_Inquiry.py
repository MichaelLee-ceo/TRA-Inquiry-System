from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd

#hide browser
op = Options()
op.add_argument('--headless')
browser = webdriver.Chrome(options=op)
#url = 'http://140.138.155.188:888/login.aspx'      testUrl - 1

while True:
    os.system('cls')
    print("Welcome to TRA Inquiry System\n")

    choice = eval(input("1.查詢\n2.退出\n?"))

    if choice == 2:
        break

    url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime'      #testUrl - 2
    browser.get(url)

    #date
    date = input("\n出發日期(xxxx/xx/xx): ")
    browser.find_element_by_id('rideDate').send_keys(date)
    #startStation
    arrival = input("\n出發站: ")
    browser.find_element_by_id('startStation').send_keys(arrival)
    #endStation
    departure = input("到達站: ")
    browser.find_element_by_id('endStation').send_keys(departure)
    #seat
    seat = input("全部 / 對號 / 非對號: ")
    if seat == "全部":
        pass
    elif seat == "對號":
        browser.find_element_by_xpath('//label[@for="trainTypeList2"]').click()
    elif seat == "非對號":
        browser.find_element_by_xpath('//label[@for="trainTypeList3"]').click()
    #inquiry
    browser.find_element_by_name('query').click()

    #data = pd.read_html(browser.page_source)

    #buffer = []

    #data[0][['車種車次', '出發時間', '抵達時間', '行駛時間']].to_csv('D:/trainInquiry.csv', encoding='utf_8_sig')
    print('\n')

    #for i in range(1, data[0].shape[0], 4):
        #print(data[0].loc[:,['車種車次', '出發時間', '抵達時間']])
        #buffer.append(data[0].loc[i][0][6:])

    #pandaBuffer = pd.DataFrame(buffer)
    #pandaBuffer.to_csv('D:/trainInquiry.csv', encoding='utf_8_sig')

    type = browser.find_elements_by_class_name('train-type').find_element_by_tag_name('a')
    print(type.text)


    print(len(type))

    print("\n查詢完成!")
    input("請按任意鍵以繼續")

browser.quit()
