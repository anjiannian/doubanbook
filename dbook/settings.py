# Scrapy settings for dbook project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dbook'

SPIDER_MODULES = ['dbook.spiders']
NEWSPIDER_MODULE = 'dbook.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dbook (+http://www.yourdomain.com)'
#DOWNLOADER_MIDDLEWARES = {
    #'misc.middleware.CustomHttpProxyMiddleware': 400,
    #'misc.middleware.CustomUserAgentMiddleware': 401,
#}

ITREM_PIPELINES={
    'dbook.pipelines.MongoDBPipeline':300
}

LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 \
     (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = False

MONGODB_SERVER = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DB = 'douban'
MONGODB_COLLECTION = 'book'
