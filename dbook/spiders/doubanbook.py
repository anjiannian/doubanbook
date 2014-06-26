from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from dbook.items import DbookItem
#from scrapy import log

class DoubanbookSpider(CrawlSpider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['http://book.douban.com/tag/']

    rules = [
         Rule(SgmlLinkExtractor(allow=("/subject/\d+/?$")), callback='parse_item'),
         Rule(SgmlLinkExtractor(allow=("/tag/[^/]+/?$", )), follow=True),
         Rule(SgmlLinkExtractor(allow=("/tag/$", )), follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/subject/\d+/?$')),callback='parse_item'),
        #Rule(SgmlLinkExtractor(allow=(r'/tag/[^/]+/?$')), follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'/tag/$')), follow=True),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        site = sel.css('#wrapper')
        item = DbookItem()
        item['link'] = response.url
        item['title'] = site.css('h1::text').extract()
        item['author'] = site.xpath('//div[@id="info"]/span[1]/a/text()').extract()
        item['desc'] = site.css('#link-report .intro p::text').extract()
        item['rate'] = site.css('#interest_sectl .rating_wrap .rating_num::text').extract()
        item['votes'] = site.xpath('//div[@id="interest_sectl"]/div/p[2]/span/a/span/text()')
        print repr(item).decode("unicode-escape") + '\n'
        return item
