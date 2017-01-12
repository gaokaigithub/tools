import requests
from bs4 import BeautifulSoup
import re
import time
from topic import auto_topic

#用来判断是否是我们需要的帖子以及进行分类
maos = ['京东','天猫','白条','券','立减','支付宝','wx','vx','红包','元','免费','活动','流量','买','话费','淘宝','微信','苏宁','消费','立返']
maosd = {'1':['京东','天猫','白条','券','立减','苏宁','淘宝','消费','立返'],'4':['支付宝','wx','vx','红包','元','免费','活动','流量','买','话费','微信']}
nmaos = ['？','工具','程序','辅助','哪','吗','求','注册','刷单','操作','什么','有没有','如何']

#获取线报屋更新的帖子链接
def get_url5(num):
    info = []
    titles = []
    r = re.compile(r'[0-9]{3,}')
    url = 'http://www.xianbao5.com/forum.php?mod=guide&view=newthread'
    html = requests.get(url).text
    bsj = BeautifulSoup(html,'lxml')
    td = bsj.find('td',{'class':'comeing_channel_threadlist_sub'})
    title = td.find('a').get_text()
    href = td.find('a')['href']
    num_now = int(r.search(href).group())
    #判断是否更新
    if num_now>num:
        for m in maos:
            if m in title:
                titles.append(title)
                md = m
                break
        if len(titles)>0:
            title_now = titles[0]
            for nm in nmaos:
                if nm in title_now:
                    titles.pop()
                    break

        #对帖子进行分类
        if len(titles)>0:
            if md in maosd['1']:
                c = '1'
            else:
                c = '4'
            info.append(c)
            info.append(href)
            info.append(num_now)
    return info

def get_url8(num):
    info = []
    titles = []
    r = re.compile(r'[0-9]{3,}')
    url = 'http://www.zuanke8.com/forum.php?mod=forumdisplay&fid=19&filter=author&orderby=dateline'
    html = requests.get(url).text
    bsj = BeautifulSoup(html, 'lxml')
    tbody = bsj.find_all('tbody')[2]
    th = tbody.find('th')
    a = th.find_all('a')[1]
    title = a.get_text()
    href = a['href']
    num_now = int(r.search(href).group())
    #判断是否更新
    if num_now>num:
        for m in maos:
            if m in title:
                titles.append(title)
                md = m
                break

        if len(titles) > 0:
            title_now = titles[0]
            for nm in nmaos:
                if nm in title_now:
                    titles.pop()
                    break
        #对帖子进行分类
        if len(titles)>0:
            if md in maosd['1']:
                c = '1'
            else:
                c = '4'
            info.append(c)
            info.append(href)
            info.append(num_now)
    return info


def get_topic(url):
    topic = []
    img_dict = {}
    html = requests.get(url).text
    bsj = BeautifulSoup(html, 'lxml')
    div = bsj.find('div', {'class': 't_fsz'})
    if div is not None:
        con = div.find('td')
        ignores = con.find_all('ignore_js_op')
        con2 = div.find('td').get_text()
        title = bsj.find('span', {'id': 'thread_subject'}).get_text()
        con_as = con.find_all('a')

        # 获取帖子里的图片信息
        if len(ignores) > 0:
            for ignore in ignores:
                img = ignore.find('img')
                imgcon = ignore.get_text()
                src = img['file']
                src = '![](%s)' % src
                img_dict[src] = imgcon

        # 替换文本中的链接
        if len(con_as) > 0:
            for con_a in con_as:
                href = con_a['href']
                text = con_a.get_text()
                con2 = con2.replace(text, href)

        # 替换图片为markdown链接
        if len(img_dict) > 0:
            for s in img_dict.keys():
                con2 = con2.replace(img_dict[s], s)

        # 判断是否需要登录访问帖，是的就不获取
        if '游客' not in con2:
            topic.append(title)
            topic.append(con2)
    return topic

if __name__ == '__main__':
    #设置帖子id初始值
    num5 = 300
    num8 = 300
    atop = auto_topic('http://xueyuan.me/api/v1/topics/','xxxxxxxxxxx')

    while True:
        url5_info = get_url5(num5)
        url8_info = get_url8(num8)
        #线报屋帖子
        if len(url5_info)>0:
            num5 = url5_info[-1]
            c5 = url5_info[0]
            url5 = url5_info[1]
            topic = get_topic(url5)
            if len(topic)>0:
                title = topic[0]
                con = topic[1]
                atop.create('1',c5,title,con)
                print('5更新了一条')
        else:
            print('5尚未更新')
        #赚客8帖子
        if len(url8_info)>0:
            num8 = url8_info[-1]
            c8 = url8_info[0]
            url8 = url8_info[1]
            topic = get_topic(url8)
            if len(topic)>0:
                title = topic[0]
                con = topic[1]
                atop.create('1',c8,title,con)
                print('8更新了一条')

        else:
            print('8尚未更新')
        time.sleep(60)



