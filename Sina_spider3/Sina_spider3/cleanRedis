# encoding=utf-8
# ------------------------------------------
#   作用：清空Redis数据，重新跑数据时用。
#   日期：2016-12-15
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

import settings
import redis

if __name__ == '__main__':
    try:
        rconn = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)
    except Exception:
        rconn = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT)

    try:
        rconn_filter = redis.Redis(settings.FILTER_HOST, settings.FILTER_PORT, settings.FILTER_DB)
    except Exception:
        try:
            rconn_filter = redis.Redis(settings.FILTER_HOST, settings.FILTER_PORT)
        except Exception:
            rconn_filter = None

    if rconn:
        if 'SinaSpider:requests' in rconn.keys():
            rconn.delete('SinaSpider:requests')

    if rconn_filter:
        if 'SinaSpider:dupefilter0' in rconn.keys():
            rconn.delete('SinaSpider:dupefilter0')
        if 'SinaSpider:dupefilter1' in rconn.keys():
            rconn.delete('SinaSpider:dupefilter1')

    print 'Finish!'
