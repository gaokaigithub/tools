# tools

运行环境python 3.x


## mytime
get_time() 将2016-11-11转为20161111格式,返回int格式<br>
get_stime() 将20161111转为2016-11-11格式,返回str格式<br>
get_month() 获取每年每月对应的天数，返回字典格式<br>
rezero() 将09格式转换为9<br>
runnian() 判断是否是闰年，返回天数<br>
get_days() 获取两个时间点相差的天数
## deal.py
监测v2ex交易版块的小爬虫，根据帖子的id号大小来判断是否有更新，然后再看title里有没有自己感兴趣的关键词。
