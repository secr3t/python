# -*- coding: utf-8 -*-
from selenium import webdriver
from operator import eq
from random import randint
from time import sleep
import os
#shutdown 용

#1번 반복 for i in range(1, 2)

def isHangul(ch): #주어진 문자가 한글인지 아닌지 리턴해주는 함수
    JAMO_START_LETTER = 44032
    JAMO_END_LETTER = 55203
    return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER

driver=webdriver.Chrome('chromedriver.exe')

driver.set_window_size(1280, 1000)
 
#로그인 화면 접속
driver.get('https://www.facebook.com/')
 
#아이디 입력
username = driver.find_element_by_id("email")
username.send_keys("i.sell.too.tv@gmail.com")

#비밀번호 입력
password = driver.find_element_by_id("pass")
password.send_keys("mc77887788")

addcount = 0
delcount = 0
#로그인 제출
driver.find_element_by_id("loginbutton").click()
#잠시 멈춤
sleep(1)
for i in range(1, 11):
    driver.get('https://www.facebook.com/find-friends/browser/')
    #잠시 멈춤
    sleep(3)
    driver.execute_script("document.getElementsByClassName('uiLayer')[0].style.display = 'none';")
    for i in range(1,20):
        driver.execute_script("window.scrollTo(0,0);window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
    driver.execute_script("window.scrollTo(0,0);")


    #친구의 사진을 가져와서 그 사진에 적혀있는 이름을 출력하고 삭제버튼을 클릭

    noman = 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/c24.0.80.80/p80x80/10354686_10150'\
            '004552801856_220367501106153455_n.jpg?oh=c4b1e4a41838397ed114ba76a8ede76d&oe=5911'\
            '6416'

    nowoman = 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/c24.0.80.80/p80x80/1379841_10150'\
                '004552801901_469209496895221757_n.jpg?oh=edc15ac56d32c9e77fc9eed25b29cded&oe=5'\
                '9233A72'
    #이미지 소스 주소를 판별해서 프로필 사진이 없는사진인지 판별한다.
    #프로필 사진이 없는 사람들의 친구추가버튼 삭제버튼이 있는div를 target으로 설정
    #class로 검색을 하였기 때문에 <list>deldiv를 순환하면서 a태그(삭제버튼)click


    apps = driver.find_elements_by_class_name("friendBrowserListUnit")
    for a in apps :
        img = a.find_element_by_tag_name("img")
        alt = img.get_attribute("alt")
        src = img.get_attribute("src")
        deldiv = a.find_elements_by_class_name("friendBrowserAddAsFriend")
        for b in deldiv:
            delb = b.find_element_by_tag_name("a")

        if eq(noman, src) or eq(nowoman, src) and delb.is_displayed() or not isHangul(alt[0]):
            delb.click()
            print("삭제"+"\t\t" + alt)
            delcount += 1
    driver.execute_script("window.scrollTo(0,0);")
    #삭제를 완료한 후에 다시 맨 위로 이동

    apps = driver.find_elements_by_class_name("friendBrowserListUnit")
    for a in apps :
        img = a.find_element_by_tag_name("img")
        alt = img.get_attribute("alt")
        src = img.get_attribute("src")
        deldiv = a.find_elements_by_class_name("friendBrowserAddAsFriend")
        for b in deldiv:
                addb = b.find_element_by_class_name("addButton")
        if(addb.is_displayed()):
            
            nowid=a.get_attribute("id")

            try:
                addb.click()
            except:
                driver.execute_script("window.scrollBy(0,-85);")
                try:
                    addb.click()
                except:
                    driver.find_element_by_tag_name('body').click()
            
            print("친구추가"+"\t" + alt)
            addcount = addcount + 1
            sleep(2)
            layers = driver.find_elements_by_class_name("uiLayer")
            if len(layers) != 0:
                for a in layers :
                    if a.is_displayed():
                        try :
                            driver.find_elements_by_class_name('layerConfirm')[0].click() 
                        except:
                            driver.find_elements_by_class_name('layerCancel')[0].click()
                            addcount = addcount - 1
            sleep(randint(1,2))
            #driver.execute_script("window.scrollBy(0,85);")
        del a
print("친구 추가한 수" + str(addcount))
print("친구 삭제한 수" + str(delcount))
