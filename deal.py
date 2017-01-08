import requests
from bs4 import BeautifulSoup
import time
import re
import easygui

def want(want_keys,num):
    you_want = {}
    want_nums = []
    url = 'https://www.v2ex.com/?tab=deals'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    bsj = BeautifulSoup(html, 'lxml')
    t_span = bsj.find_all('span', {'class': 'item_title'})
    r = re.compile(r'[0-9]+')
    for t in t_span:
        title = t.find('a').get_text()
        href = t.find('a')['href']
        num_now = r.search(href)
        want_nums.append(num_now.group())
        #查询新发布的帖子并且是包含自己设置的关键词
        if int(num_now.group())>num:
            for want_key in want_keys:
                if want_key in title:
                    want_href = 'https://www.v2ex.com'+href
                    you_want[title] = want_href
                    break
    num_max = int(max(want_nums))
    return you_want,num_max

if __name__ == '__main__':
    num = 300
    n = 1
    while n:
        mine,num_max = want(['iPhone'],num)
        num = num_max
        if len(mine)>1 :
            for i in mine.items():
                print(i)
            if n>1:
                easygui.msgbox(msg='查询到了相关主题帖',title='v2ex帖子提醒')
        else:
            print('耐心等待5min将进行下次查询')
        n = n + 1
        time.sleep(300)










