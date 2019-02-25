import os
import requests

from config.settings.base import CHROME_DRIVER
from .models import SearchList
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class KyoboCrawler:
    def __init__(self, title):
        self.title = title

    @classmethod
    def get_title(cls, title):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        chromedriver_dir = os.path.join(CHROME_DRIVER, 'chromedriver')
        driver = webdriver.Chrome(chromedriver_dir, chrome_options=option)
        driver.maximize_window()
        driver.get('http://www.kyobobook.co.kr')
        driver.implicitly_wait(3)

        # 검색창에 제목 입력
        driver.find_element_by_id('searchKeyword').send_keys(title)

        # ENTER
        driver.find_element_by_id('searchKeyword').send_keys(Keys.ENTER)
        driver.implicitly_wait(3)

        # 카테고리 중에서 국내도서 클릭
        driver.find_elements_by_css_selector('div.box_search_category > ul li')[1].click()

        # 책 수량 파악
        book_count = driver.find_elements_by_css_selector('div.box_search_category > ul li')[1].get_attribute(
            'innerHTML')
        soup = BeautifulSoup(book_count, 'lxml')
        count = soup.select_one('small').get_text()
        left = count.replace('(', '')
        right = left.replace(')', '')

        # 검색한 책이 없으면 에러 발생
        if right == '0':
            pass
        else:
            # 페이지 처리 (일회용)
            page_list = driver.find_elements_by_css_selector('div.list_paging ul > li a')

        for index in range(len(page_list)):
            if index == 0:
                page_list[index].click()
            else:
                # 페이지 이동 시 요소 변경으로 "국내 도서 목록"과 "페이지 처리"를 다시 실행
                driver.find_elements_by_css_selector('div.box_search_category > ul li')[1].click()
                value = driver.find_elements_by_css_selector('div.list_paging ul > li a')
                value[index].click()
            driver.implicitly_wait(3)

            # 국내도서 검색결과
            kor_books = driver.find_element_by_class_name('list_search_result').get_attribute('innerHTML')
            soup = BeautifulSoup(kor_books, 'lxml')
            tr_tags = soup.find_all('tr')

            root_url = 'http://www.kyobobook.co.kr'
            result_url_list = []
            for tr in tr_tags:
                # 제목
                title = tr.select_one('td.detail > div.title')
                result = title.get_text()
                result = result.replace('\n', '')
                result_title = result.replace('\t', '')

                # 저자
                author_info = tr.select_one('td.detail > div.author')
                author_info = author_info.get_text(strip=True)
                author_info_list = author_info.split('|')
                author = author_info_list[0]
                publisher = author_info_list[1]
                date = author_info_list[2]

                # URL
                address = title.find('a', href=True)
                sub_url = address['href']
                url = root_url + sub_url

                # DB 작업
                SearchList.objects.get_or_create(title=result_title,
                                                 author=author,
                                                 publisher=publisher,
                                                 date=date,
                                                 url=url)
