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
        self.items_seen = set()
        if item["link"] in self.items_seen:
            raise DropItem("Duplicated item %s" % item)
            log.msg("Duplicated item %s has been destroyed" % item['title'],
                    level = log.DEBUG)
        else:
            self.items_seen.add(item["link"])
            new_book = [{
                "link":item["link"],
                "title":item["title"],
                "author":item["author"],
                "desc":item["desc"],
                "rate":item["rate"],
                "votes":item["votes"]
            }]
            self.collection.insert(new_book)
            log.msg("Book %s has added" % item["title"], level=log.DEBUG)
            return item
