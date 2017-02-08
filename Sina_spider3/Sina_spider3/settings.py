# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

BOT_NAME = ['Sina_spider3']

SPIDER_MODULES = ['Sina_spider3.spiders']
NEWSPIDER_MODULE = 'Sina_spider3.spiders'

DOWNLOADER_MIDDLEWARES = {
    "Sina_spider3.middleware.UserAgentMiddleware": 401,
    "Sina_spider3.middleware.CookiesMiddleware": 402,
}
ITEM_PIPELINES = {
    "Sina_spider3.pipelines.MongoDBPipeline": 403,
}

SCHEDULER = 'Sina_spider3.scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'Sina_spider3.scrapy_redis.queue.SpiderSimpleQueue'

# 种子队列的信息
REDIE_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0

DOWNLOAD_DELAY = 10  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 1  # 默认为16
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
