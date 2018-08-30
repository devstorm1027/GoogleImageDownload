import scrapy
import re
import urllib.parse
from Scrapy_GoogleImageDownload.items import ImageItem


class GoogleSearch(scrapy.Spider):
    name = 'image_crawler'
    allowed_domains = ['images.google.com']
    search_url = 'https://www.google.com/search?tbm=isch&source=hp&biw=1920&bih=476' \
                 '&q={cel}&ijn={page}&start={count}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/68.0.3440.75 Safari/537.36',
    }

    def start_requests(self):
        with open('celebrities.txt', encoding="ISO-8859-1") as f:
            celebrities = f.readlines()
        celebrities = [x.strip() for x in celebrities]
        for cel in celebrities:
            for i in range(4):
                yield scrapy.Request(
                    url=self.search_url.format(cel=cel, page=i, count=i*100),
                    callback=self.parse,
                    headers=self.headers,
                    meta={'name': cel}
                 )

    def parse(self, response):
        urls = re.findall('"ou":"(.*?)"', response.body_as_unicode())
        for url in urls:
            if 'image?url' in url:
                url = re.search('http(.*)', url.split('image?url')[1], re.DOTALL)
                if url:
                    url = urllib.parse.unquote(url.group(0))
            item = ImageItem()
            item['name'] = response.meta.get('name')
            item['image_urls'] = [url]
            yield item
