from wxpy import *

import requests

from datetime import datetime

import time

from apscheduler.schedulers.blocking import BlockingScheduler #定时框架

bot = Bot()

# bot = Bot(console_qr=2, cache_path='botoo.pkl') #这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为bot=Bot()

def get_news1():

    # 获取金山词霸每日一句，英文和翻译

    url = "http://open.iciba.com/dsapi/"

    r = requests.get(url)

    content = r.json()['content']

    translation= r.json()['translation']

    return content, translation

my_friends = [ensure_one(bot.search('王文豪Ken')),
              bot.friends().search('i')[0],
              bot.friends().search('凡哥')[0]
              ]
print(my_friends)

#发送函数

def send_message():


    for friend in my_friends:
        friend.send(get_news1())
    #-------------------------------------


    #给单个好友发送消息-----------------
    #friend.send(get_news1())
    #发送成功通知我

    bot.file_helper.send(get_news1())

    bot.file_helper.send('发送完毕')

#定时器

print('start')

#定时操作
#sched = BlockingScheduler()
#sched.add_job(send_message,'cron', day_of_week='mon-fri',hour =17,minute = 0)#设定发送的时间
#sched.start()
send_message()#执行程序时直接发送
