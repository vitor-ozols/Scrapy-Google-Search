import time
import scrapy
from urllib.parse import unquote


def black_list_chars(str_to_check):

    bl_chars = ['\\', '/', '%', '&', '#', '*', "(", ")", "<", ">",
                ',', '"', "'", ";", "?", "!", 'bootstrap', "=", "https",
                '[', ']']

    check = True
    for bl in bl_chars:
        if bl in str_to_check:
            check = False
            break
    return check


class MsSpider(scrapy.Spider):

    name = 'ms'
    reader = open(r'../to_search.txt', 'r', encoding="utf8").read().split('\n')
    start_urls = [f"https://www.google.com/search?q={str(i).replace(' ','+')}" for i in reader]

    def parse(self, response, **kwargs):

        for r in response.xpath('//a[@data-ved]//@href'):
            url = r.extract()
            g_url = (response.url).split('=')[-1]

            if 'https://' in url:
                yield scrapy.Request(url,
                                     callback=self.parse_html,
                                     meta={'g_url':g_url})

    def parse_html(self, response):
        time.sleep(0.5)
        g_url = unquote(response.meta.get('g_url'))

        for text in response.xpath('//text()'):
            t = text.extract()
            if '@' in t and "." in t and black_list_chars(t) == True:
                yield {
                    'g_url': g_url,
                    'url': response.url,
                    'mail': t
                }

        for href in response.xpath('//@href'):
            h = href.extract()
            if '@' in h and '.' in h and black_list_chars(h) == True:
                yield {
                    'g_url': g_url,
                    'url': response.url,
                    'mail': (str(h.replace('mailto:',"")))
                }
