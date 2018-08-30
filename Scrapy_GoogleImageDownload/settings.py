from scrapy.settings.default_settings import ITEM_PIPELINES
from scrapy.pipelines.images import ImagesPipeline
BOT_NAME = 'Scrapy_GoogleImageDownload'

SPIDER_MODULES = ['Scrapy_GoogleImageDownload.spiders']
NEWSPIDER_MODULE = 'Scrapy_GoogleImageDownload.spiders'


ROBOTSTXT_OBEY = False

IMAGES_STORE = 'images'

DEPTH_PRIORITY = 1
CONCURRENT_REQUESTS = 250
MEDIA_ALLOW_REDIRECTS = True
DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
   'Scrapy_GoogleImageDownload.pipelines.MyImagePipeline': 1,
}
IMAGES_RESULT_FIELD = 'images'

