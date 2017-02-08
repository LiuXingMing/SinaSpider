# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

import os
import random
import redis
import json
import logging
from user_agents import agents
from cookies import initCookie, updateCookie, removeCookie
from scrapy.exceptions import IgnoreRequest
from scrapy.utils.response import response_status_message
from scrapy.downloadermiddlewares.retry import RetryMiddleware

logger = logging.getLogger(__name__)


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(RetryMiddleware):
    """ 维护Cookie """

    def __init__(self, settings, crawler):
        RetryMiddleware.__init__(self, settings)
        self.rconn = settings.get("RCONN", redis.Redis(crawler.settings.get('REDIS_HOST', 'localhsot'), crawler.settings.get('REDIS_PORT', 6379)))
        initCookie(self.rconn, crawler.spider.name)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings, crawler)

    def process_request(self, request, spider):
        redisKeys = self.rconn.keys()
        while len(redisKeys) > 0:
            elem = random.choice(redisKeys)
            if "SinaSpider:Cookies" in elem:
                cookie = json.loads(self.rconn.get(elem))
                request.cookies = cookie
                request.meta["accountText"] = elem.split("Cookies:")[-1]
                break
            else:
                redisKeys.remove(elem)

    def process_response(self, request, response, spider):
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers["location"]
                if "login.weibo" in redirect_url or "login.sina" in redirect_url:  # Cookie失效
                    logger.warning("One Cookie need to be updating...")
                    updateCookie(request.meta['accountText'], self.rconn, spider.name)
                elif "weibo.cn/security" in redirect_url:  # 账号被限
                    logger.warning("One Account is locked! Remove it!")
                    removeCookie(request.meta["accountText"], self.rconn, spider.name)
                elif "weibo.cn/pub" in redirect_url:
                    logger.warning(
                        "Redirect to 'http://weibo.cn/pub'!( Account:%s )" % request.meta["accountText"].split("--")[0])
                reason = response_status_message(response.status)
                return self._retry(request, reason, spider) or response  # 重试
            except Exception, e:
                raise IgnoreRequest
        elif response.status in [403, 414]:
            logger.error("%s! Stopping..." % response.status)
            os.system("pause")
        else:
            return response
