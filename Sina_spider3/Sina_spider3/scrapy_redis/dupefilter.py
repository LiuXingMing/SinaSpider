import time
import re

from scrapy.dupefilters import BaseDupeFilter

from . import connection


class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplication filter"""

    def __init__(self, server, key):
        """Initialize duplication filter

        Parameters
        ----------
        server : Redis instance
        key : str
            Where to store fingerprints
        """
        self.server = server
        self.key = key

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings_filter(settings)
        key = "dupefilter:%s" % int(time.time())
        return cls(server, key)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):
        uid = re.findall('(\d+)/info', request.url)
        if uid:
            uid = int(uid[0])
            isExist = self.server.getbit(self.key + str(uid / 4000000000), uid % 4000000000)
            if isExist == 1:
                return True
            else:
                self.server.setbit(self.key + str(uid / 4000000000), uid % 4000000000, 1)
                return False

    def close(self, reason):
        """Delete data on close. Called by scrapy's scheduler"""
        self.clear()

    def clear(self):
        """Clears fingerprints data"""
        self.server.delete(self.key)
