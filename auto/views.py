# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.decorators import api_view
#
# from .models import Auto
# from .serializers import PostSerializer
#
# class ListPost(generics.ListCreateAPIView):
#     queryset = Auto.objects.all()
#     serializer_class = PostSerializer
#
#
# class DetailPost(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Auto.objects.all()
#     serializer_class = PostSerializer
from django.views import View
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from datetime import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.utils import six

class ticketing(View):
    #인터파크 로그인

   def post(self, request):
        data = dict(six.iterlists(request.POST))
        log_url = data['site'][0]
        # path = "/Users/tyflow/Downloads/chromedriver"
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")
        # driver = webdriver.Chrome(path, chrome_options=options)
        path = "/Users/tyflow/Downloads/chromedriver"
        driver = webdriver.Chrome(path)
        driver.get(log_url)

        log_id = data['id'][0]
        log_pw = data['pw'][0]
        log = driver.find_element_by_id("userId")
        log.send_keys(log_id)
        log = driver.find_element_by_id("userPwd")
        log.send_keys(log_pw)
        log.send_keys(Keys.RETURN)

        time.sleep(2)

        ticket_url = data['url'][0]
        driver.get(ticket_url)
        time.sleep(2)
        driver.find_elements_by_xpath(data['xpath'][0])[0].click()

        # driver.switch_to_window(driver.window_handles[1])
        # driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])
        # driver.find_element_by_xpath('//*[@id="CellPlayDate"]').click()
        # print('날짜선택')
        # driver.switch_to_window(driver.window_handles[1])
        # time.sleep(2)
        # driver.find_elements_by_xpath('//*[@id="LargeNextBtnImage"]')[0].click()
        # print('다음단계')
        # print(driver.find_elements_by_xpath('//*[@id="SID1"]'))
        # # test = driver.find_element_by_xpath('//*[@id="CellPlayDate"]')
        # # print(test.text)
        # # req = driver.page_source
        # # soup = BeautifulSoup(req, 'html.parser')
        # # print(soup)
        # # driver.find_element_by_xpath('//*[@id="CellPlayDate"]')[0].click()
        # # while True:
        # #     if str(datetime.datetime.today())[11:16] == '14:31':
        # #         driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[4]/div/div[2]/div/div[2]/div[5]/a')[0].click()
        # #         break

        return HttpResponse("Post 요청을 잘받았다")
