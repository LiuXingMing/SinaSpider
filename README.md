**Sina_Spider1: 《[新浪微博爬虫分享（一天可抓取 1300 万条数据）](http://blog.csdn.net/bone_ace/article/details/50903178)》**
<br> **Sina_Spider2: 《[新浪微博分布式爬虫分享](http://blog.csdn.net/bone_ace/article/details/50904718)》**
<br> **Sina_Spider3: 《[新浪微博爬虫分享（2016年12月01日更新）](http://blog.csdn.net/bone_ace/article/details/53379904)》**
<br>
<br>
Sina_Spider1为单机版本。<br>
Sina_Spider2在Sina_Spider1的基础上基于scrapy_redis模块实现分布式。<br>
Sina_Spider3增加了Cookie池的维护，优化了种子队列和去重队列。<br>
<br>
三个版本的详细介绍请看各自的博客。
遇到什么问题请尽量留言，方便后来遇到同样问题的同学查看。也可加一下QQ交流群：<a target="_blank" href="//shang.qq.com/wpa/qunwpa?idkey=a3e1d79f8c7e12b9db5ac680375d7174a91384f288d3ba16e1781c2587872560"><img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="微博爬虫交流群" title="微博爬虫交流群"></a>。
<br><br><br><br>
 --------------------------------------------------------------------------
<br>
20161215更新：
<br>
有人反映说爬虫一直显示爬了0页，没有抓到数据。
<br>
1、把settings.py里面的LOG_LEVEL = 'INFO'一行注释掉，使用默认的"DEBUG"日志模式，运行程序可查看是否正常请求网页。
<br>
2、注意程序是有去重功能的，所以要清空数据重新跑的话一定要把redis的去重队列删掉，否则起始ID被记录为已爬的话也会出现抓取为空的现象。清空redis数据 运行cleanRedis.py即可。
<br>
3、另外，微博开始对IP有限制了，如果爬的快 可能会出现403，大规模抓取的话需要加上代理池。
<br><br><br><br>
 ---------------------------------------------------------------------------
<br>
20170323更新：
<br>微博从昨天下午三点多开始做了一些改动，原本免验证码获取Cookie的途径已经不能用了。以前为了免验证码登录，到处找途径，可能最近爬的人多了，给封了。
<br>那么就直面验证码吧，走正常流程登录，才没那么容易被封。此次更新主要在于Cookie的获取途径，其他地方和往常一样（修改了cookies.py，新增了yumdama.py）。
<br>加了验证码，难度和复杂程度都提高了一点，对于没有编程经验的同学可能会有一些难度。
<br>验证码处理主要有两种：手动输入和打码平台自动填写（手动输入配置简单，打码平台输入适合大规模抓取）。
<br><br>手动方式流程：
<br>
1、下载PhantomJS.exe，放在python的安装路径（适合Windows系统，Linux请找百度）。
<br>
2、运行launch.py启动爬虫，中途会要求输入验证码，查看项目路径下新生成的aa.png，输入验证码 回车，即可。
<br>
<br>打码方式流程：
<br>
1、下载PhantomJS.exe，放在python的安装路径。
<br>
2、安装Python模块PIL（请自行百度，可能道路比较坎坷）
<br>
3、验证码打码：我使用的是 http://www.yundama.com/ （真的不是打广告..），将username、password、appkey填入yumdama.py（正确率挺高，weibo.cn正常的验证码是4位字符，1元可以识别200个）。
<br>
4、cookies.py中设置IDENTIFY=2，运行launch.py启动爬虫即可。
<br><br>
<br>
