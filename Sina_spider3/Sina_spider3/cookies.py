# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------

import base64
import os
import requests
import json
import logging

logger = logging.getLogger(__name__)

"""
    输入你的微博账号和密码，可去淘宝买，一元5个。
    建议买几十个，实际生产建议100+，微博反爬得厉害，太频繁了会出现302转移。
"""
myWeiBo = [
    ('gaiji690yunhe@163.com', 'XVv2p6kW9k700v4'),
    ('qiao6570492yata@163.com', '3v91DQ30UhIJim'),
]


def getCookie(account, password):
    """ 获取一个账号的Cookie """
    loginURL = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)"
    username = base64.b64encode(account.encode("utf-8")).decode("utf-8")
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    session = requests.Session()
    r = session.post(loginURL, data=postData)
    jsonStr = r.content.decode("gbk")
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        logger.warning("Get Cookie Success!( Account:%s )" % account)
        cookie = session.cookies.get_dict()
        return json.dumps(cookie)
    else:
        logger.warning("Failed!( Reason:%s )" % info["reason"])
        return ""


def initCookie(rconn, spiderName):
    """ 获取所有账号的Cookies，存入Redis。如果Redis已有该账号的Cookie，则不再获取。 """
    for weibo in myWeiBo:
        if rconn.get("%s:Cookies:%s--%s" % (spiderName, weibo[0], weibo[1])) is None:  # 'SinaSpider:Cookies:账号--密码'，为None即不存在。
            cookie = getCookie(weibo[0], weibo[1])
            if len(cookie) > 0:
                rconn.set("%s:Cookies:%s--%s" % (spiderName, weibo[0], weibo[1]), cookie)
    cookieNum = "".join(rconn.keys()).count("SinaSpider:Cookies")
    logger.warning("The num of the cookies is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning('Stopping...')
        os.system("pause")


def updateCookie(accountText, rconn, spiderName):
    """ 更新一个账号的Cookie """
    account = accountText.split("--")[0]
    password = accountText.split("--")[1]
    cookie = getCookie(account, password)
    if len(cookie) > 0:
        logger.warning("The cookie of %s has been updated successfully!" % account)
        rconn.set("%s:Cookies:%s" % (spiderName, accountText), cookie)
    else:
        logger.warning("The cookie of %s updated failed! Remove it!" % accountText)
        removeCookie(accountText, rconn, spiderName)


def removeCookie(accountText, rconn, spiderName):
    """ 删除某个账号的Cookie """
    rconn.delete("%s:Cookies:%s" % (spiderName, accountText))
    cookieNum = "".join(rconn.keys()).count("SinaSpider:Cookies")
    logger.warning("The num of the cookies left is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning('Stopping...')
        os.system("pause")
