# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

import pymongo
from items import InformationItem, TweetsItem, RelationshipsItem


class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Sina"]
        self.Information = db["Information"]
        self.Tweets = db["Tweets"]
        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, RelationshipsItem):
            try:
                self.Relationships.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, TweetsItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, InformationItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        return item
