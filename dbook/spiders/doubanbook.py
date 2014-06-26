from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from dbook.items import DbookItem
from scrapy import log

class DoubanbookSpider(CrawlSpider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['http://book.douban.com/tag/']

    rules = [
        Rule(SgmlLinkExtractor(allow=r'/subject/\d+/?$'),callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=r'/tag/[^/]+/?$'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'/tag/$'), follow=True),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.css('#wrapper')
        i = DbookItem()
        i['link'] = response.url
        i['title'] = sites.css('h1::text').extract()
        i['author'] = sites.xpath('//div[@id="info"]\
                                    /span[1]/a/text()').extract()
        i['desc'] = sites.css('#link-report .intro p::text').extract()
        i['rate'] = sites.css('#interest_sectl \
                                .rating_wrap .rating_num::text').extract()
        i['votes'] = sites.xpath('//div[@id="interest_sectl"]\
                                /div/p[2]/span/a/span/text()')
        log.msg(repr(i).decode("unicode-escape") + '\n', level=log.INFO)
        return i
