# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'],\
                                        settings['MONGODB_PORT'])
        db = connection[settings['MONGO_DB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        items = set()
        for i in item:
            if i in items:
                raise DropItem("Duplicated item %s" % i["title"])
                log.msg("Duplicated item %s has been destroyed" % i['title'],
                        level = log.DEBUG)
            else:
                items.add(i)
                new_book = [{
                    "link":i["link"],
                    "title":i["title"],
                    "author":i["author"],
                    "desc":i["desc"],
                    "rate":i["rate"],
                    "votes":i["votes"]
                }]
                self.collection.insert(new_book)
                log.msg("Book %s has added" % i["title"], level=log.DEBUG)
                return item
