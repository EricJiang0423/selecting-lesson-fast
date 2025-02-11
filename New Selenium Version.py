#!/usr/bin/env python
# coding: utf-8

import selenium 
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("http://210.28.81.11/")
driver.maximize_window()
verificationcode=input()
Username='2120210988'
#教务系统账户
password='Jiang525566!'
#教务系统密码

driver.find_element("xpath",'//*[@id="txtSecretCode"]').send_keys(verificationcode)
driver.find_element("xpath",'//*[@id="txtUserName"]').send_keys(Username)
driver.find_element("xpath",'//*[@id="TextBox2"]').send_keys(password)
driver.find_element("xpath",'//*[@id="Button1"]').click()

def mainpage(driver=driver,User=Username):
    driver.get("http://210.28.81.11/xs_main.aspx?xh="+User)
    move = driver.find_element("xpath",'//*[@id="navxl"]/li[2]/a/span')
    ActionChains(driver).move_to_element(move).perform()#悬浮鼠标，拉出选项卡
    driver.find_element("xpath",'//*[@id="navxl"]/li[2]/ul/li[1]/a').click()#通识
    #driver.find_element_by_xpath('//*[@id="headDiv"]/ul/li[2]/ul/li[2]/a').click()#专业任意专限
    #driver.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[3]/a').click()#创新、外语
    driver.switch_to.frame(driver.find_element("xpath",'//*[@id="iframeautoheight"]')) #进入iframe中,很重要，否则会找不到提交
    Select(driver.find_element(by=By.ID,value='kj')).select_by_value('板块（3）')  #记得修改板块！！！！
    #import warnings
    #warnings.filterwarnings("ignore")


def alert_is_present(driver):
    try:
        alert = driver.switch_to.alert
        alert.text
        return alert
    except:
        return False

#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页
#driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl3_xk"]').click()
#element = driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl3_xk"]')
#driver.execute_script("arguments[0].click();", element)


def loop(driver=driver):
    try:
        element = driver.find_element("xpath",'//*[@id="kcmcGrid_xk_6"]') #修改要选的课
    except:
        time.sleep(1)
        mainpage(driver)
        loop(driver=driver)
    driver.execute_script("arguments[0].click();", element)
    driver.find_element("xpath",'//*[@id="Button1"]').click()#提交
    #alert = driver.switch_to.alert
    if alert_is_present(driver):
        driver.switch_to.alert.accept()
# main task
while True:
    mainpage()
    for i in range(1000):
        loop(driver)

alert = driver.switch_to.alert
driver.switch_to.alert.accept()



get_ipython().run_cell_magic('time', '', 'driver.find_element_by_xpath(\'//*[@id="kcmcGrid__ctl8_xk"]\').click()\ndriver.find_element_by_xpath(\'//*[@id="Button1"]\').click()#提交  \nalert = driver.switch_to.alert\ndriver.switch_to.alert.accept()')


#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页


#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnPrePage"]').click()#上一页


#driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl2_xk"]').click()


#driver.find_element_by_xpath('//*[@id="Button1"]').click()#提交

#driver.find_element_by_xpath('//*[@id="dpkcmcGrid_btnNextPage"]').click()#下一页

driver.switch_to.default_content()#返回主页面框架

#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

ActionChains(driver).send_keys(Keys.ENTER).perform()#回车键