from urllib.parse import quote
import requests
import re

def sina_news(company):
	company = quote(company, encoding='GBK')
	url = 'https://search.sina.com.cn/?q=' + company + '&range=title&c=news&sort=time'
	res = requests.get(url).text
	title = '<h2>.*?>(.*?)</a>'
	date = '<span class="fgray_time">(.*?)</span>'
	link = '<h2><a href="(.*?)"'
	result_content = re.findall (title, res, re.S)
	result_date = re.findall (date, res, re.S)
	result_link = re.findall(link, res, re.S)

	for i in range(0,len(result_content)):
		result_content[i] = re.sub('<.*?>', '', result_content[i])
		result_date[i] = re.sub('<.*?>', '', result_date[i])
		result_link[i] = re.sub('<.*?>', '', result_link[i])
		result_content[i] = result_content[i].strip()
		result_date[i] = result_date[i].strip()
		result_link[i] = result_link[i].strip()
		print(str(i+1) + '.' + result_content[i] + '   ' + result_date[i] + '    ' + result_link[i])
multi_company = ['国泰君安','中信','广发','申万','方正']
for i in multi_company:
	print(i)
	sina_news(i)