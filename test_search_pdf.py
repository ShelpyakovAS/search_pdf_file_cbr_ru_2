from selenium.webdriver.common.by import By
import pytest
import requests
import io
from lxml import etree
from conftest import search_url_links


@pytest.mark.parametrize('link', search_url_links())
def test_search_pdf_by_selenium(browser, link):
    browser.get(link)
    links_have_href = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
    for link in links_have_href:
        href = link.get_attribute("href")
        if '.pdf' in href:
            with open('selen_result.txt', 'a') as f:
                f.write(href+'\n')
            f.close()


@pytest.mark.parametrize('link', search_url_links())
def test_search_pdf_by_requests(link):
    data = requests.get(link).text
    parser = etree.HTMLParser()
    tree = etree.parse(io.StringIO(data), parser)
    for im in tree.xpath('//a'):
        if im.get('href'):
            if '.pdf' in im.get('href'):
                with open('re_result.txt', 'a') as f:
                    if 'http' not in im.get('href'):
                        f.write('https://www.cbr.ru' + im.get('href') + '\n')
                    else:
                        f.write(im.get('href') + '\n')
                f.close()