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

def addfriend(driver):
    addcount = 0
    delcount = 0
    driver.get('https://www.facebook.com/friends/requests/?fcref=none&outgoing=1')
    #잠시 멈춤
    sleep(3)
    driver.find_element_by_tag_name('body').click()

    morevis = True
    while morevis:
        mp = driver.find_elements_by_class_name("uiMorePager")
        for mpp in mp:
            count=0
            more = driver.find_element_by_tag_name("a")
            if(more.is_displayed()):
                more.click()
                count += 1
        if count < 1:
            morevis = False
        sleep(1)

    driver.execute_script("window.scrollTo(0,0);")
    noman = 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/c24.0.80.80/p80x80/10354686_10150'\
            '004552801856_220367501106153455_n.jpg?oh=c4b1e4a41838397ed114ba76a8ede76d&oe=5911'\
            '6416'
    nowoman = 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/c24.0.80.80/p80x80/1379841_10150'\
                '004552801901_469209496895221757_n.jpg?oh=edc15ac56d32c9e77fc9eed25b29cded&oe=5'\
                '9233A72'
    apps = driver.find_elements_by_class_name("ruUserBox")
    for a in apps :
        img = a.find_element_by_tag_name("img")
        #get user name
        stdiv = a.find_element_by_tag_name("div")
        nddiv = stdiv.find_elements_by_tag_name("div")
        count = 0
        for a in nddiv:
            count += 1
            if count>0:
                rddiv = a.find_elements_by_tag_name("div")
        count = 0
        for a in rddiv:
            if count == 0:
                atext = a.find_element_by_tag_name("a")
                name = atext.text
        #end get user name
        src = img.get_attribute("src")
        
        deldiv = a.find_elements_by_class_name("ruResponseButtons")
        if eq(noman, src) or eq(nowoman, src) and delb.is_displayed() or not isHangul(name[0]):
            deldiv[0].click()
            sleep(0.5)
            layerbox = driver.find_elements_by_class_name("uiContextualLayerBelowLeft")
            layerbox1 = layerbox.find_element_by_tag_name("div")
            layerbox2 = layerbox1.find_element_by_tag_name("div")
            layerbox3 = layerbox2.find_element_by_tag_name("div")
            manydiv = layerbox3.find_elements_by_tag_name("div")
            getul = manydiv[3].find_element_by_tag_name("ul")
            getli = getul.find_elements.by_tag_name("li")
            cuttag = getli[4].find_element_by_tag_name("a")
            cuttag.click()
            delcount += 1
            
driver=webdriver.Chrome('chromedriver.exe')

driver.set_window_size(1280, 1000)
 
#로그인 화면 접속
driver.get('https://www.facebook.com/')
 
#아이디 입력
username = driver.find_element_by_id("email")
username.send_keys("iselltoo@taijoo.com")

#비밀번호 입력
password = driver.find_element_by_id("pass")
password.send_keys("mc77887788")


#로그인 제출
driver.find_element_by_id("loginbutton").click()
#잠시 멈춤
sleep(1)

addfriend(driver)
