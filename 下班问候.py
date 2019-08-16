from wxpy import *

import requests

from datetime import datetime

import time

from apscheduler.schedulers.blocking import BlockingScheduler  # 定时框架

bot = Bot()


# bot = Bot(console_qr=2, cache_path='botoo.pkl') #这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为bot=Bot()

def offwork_goodbye():
	# 获取金山词霸每日一句，英文和翻译

	url = "http://open.iciba.com/dsapi/"

	r = requests.get(url)

	content = r.json()['content']

	translation = r.json()['translation']

	str = '每日一句: \n' + content + '\n' + translation + '\n'

	return str

my_friends = [ensure_one(bot.search('王文豪Ken')),
			  bot.friends().search('李享')[0],
			  bot.friends().search('梨可启')[0],
			  bot.friends().search('詹显畅')[0],
			  bot.friends().search('胡耿')[0],
			  bot.friends().search('谈泽洲')[0],
			  bot.friends().search('赵蓉娟')[0],
			  ]
print(my_friends)


# 发送函数
def send_message():
	for friend in my_friends:
		friend.send("下午好！天气炎热，提防高温，祝您身体健康！")
		friend.send(offwork_goodbye())
		bot.file_helper.send('发送完毕')


# 定时器

print('start')

#定时操作
sched = BlockingScheduler()
sched.add_job(send_message,'cron', day_of_week='mon-fri',hour =17,minute = 5)#设定发送的时间
sched.start()
send_message()  # 执行程序时直接发送
from wxpy import *

import requests

from datetime import datetime

import time

from apscheduler.schedulers.blocking import BlockingScheduler  # 定时框架

bot = Bot()


# bot = Bot(console_qr=2, cache_path='botoo.pkl') #这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为bot=Bot()

def offwork_goodbye():
	# 获取金山词霸每日一句，英文和翻译

	url = "http://open.iciba.com/dsapi/"

	r = requests.get(url)

	content = r.json()['content']

	translation = r.json()['translation']

	str = '每日一句: \n' + content + '\n' + translation + '\n'

	return str

my_friends = [ensure_one(bot.search('王文豪Ken')),
			  bot.friends().search('李享')[0],
			  bot.friends().search('梨可启')[0],
			  bot.friends().search('詹显畅')[0],
			  bot.friends().search('胡耿')[0],
			  bot.friends().search('谈泽洲')[0],
			  bot.friends().search('赵蓉娟')[0],
			  ]
print(my_friends)


# 发送函数
def send_message():
	for friend in my_friends:
		friend.send("下午好！天气炎热，提防高温，祝您身体健康！")
		friend.send(offwork_goodbye())
		bot.file_helper.send('发送完毕')


# 定时器

print('start')

#定时操作
sched = BlockingScheduler()
sched.add_job(send_message,'cron', day_of_week='mon-fri',hour =17,minute = 5)#设定发送的时间
sched.start()
send_message()  # 执行程序时直接发送
