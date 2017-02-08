##**Sina_Spider1: 《[新浪微博爬虫分享（一天可抓取 1300 万条数据）](http://blog.csdn.net/bone_ace/article/details/50903178)》**##
##**Sina_Spider2: 《[新浪微博分布式爬虫分享](http://blog.csdn.net/bone_ace/article/details/50904718)》**##
##**Sina_Spider3: 《[新浪微博爬虫分享（2016年12月01日更新）](http://blog.csdn.net/bone_ace/article/details/53379904)》**##
<p>
<p>
Sina_Spider1为单机版本。<p>
Sina_Spider2在Sina_Spider1的基础上基于scrapy_redis模块实现分布式。<p>
Sina_Spider3增加了Cookie池的维护，优化了种子队列和去重队列。<p>
<br>
三个版本的详细介绍请看各自的博客。
遇到什么问题请尽量留言，方便后来遇到同样问题的同学查看。也可加一下QQ交流群：<a target="_blank" href="//shang.qq.com/wpa/qunwpa?idkey=a3e1d79f8c7e12b9db5ac680375d7174a91384f288d3ba16e1781c2587872560"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="微博爬虫交流群" title="微博爬虫交流群"></a>。
<p><p>
 -------------------
20161215更新：
<br>
有人反映说爬虫一直显示爬了0页，没有抓到数据。
<br>
1、把settings.py里面的LOG_LEVEL = 'INFO'一行注释掉，使用默认的"DEBUG"日志模式，运行程序可查看是否正常请求网页。
<br>
2、注意程序是有去重功能的，所以要清空数据重新跑的话一定要把redis的去重队列删掉，否则起始ID被记录为已爬的话也会出现抓取为空的现象。清空redis数据 运行cleanRedis.py即可。
<br>
3、另外，微博开始对IP有限制了，如果爬的快 可能会出现403，大规模抓取的话需要加上代理池。
<p>
