#!/usr/bin/env python

import requests
import sys
from pathlib import *
from lxml import etree
from time import sleep
from lxml.html import fromstring, tostring
from html.parser import HTMLParser
# import http.cookiejar

#获取指定问题的答案页面
def get_answer(qurl):

    user_agent = 'Mozilla/5.0 (Windows NT 100.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent':user_agent}

    response = requests.get(qurl, headers=header)
    #保存页面供调试
    save_page(response)

    selector = etree.HTML(response.text)
    # answer = selector.xpath('//div[@class="ContentItem AnswerItem"]/div[@class="RichContent RichContent--unescapable"]/div[@class="RichContent-inner"]/span[1]/text')
    answerElement = selector.xpath('//div[@class="ContentItem AnswerItem"]/div[@class="RichContent RichContent--unescapable"]/div[@class="RichContent-inner"]/span[1]/p')
    answer = ''
    text = ''

    for i in range(len(answerElement)):  
        if isinstance(answerElement[i], etree._Element):
            
            for node in answerElement[i].itertext():
                print(node.strip())
                text += node.strip()
    answer = text
    
    return answer

#获取页面的所有问题和答案链接
def get_question_link(url):

    user_agent = 'Mozilla/5.0 (Windows NT 100.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    cookie = 'tgw_l7_route=37b99ae961afc12480906144dc172172; Expires=Sun, Path=/'
    #设置cookie不起作用?
    header = {'user-agent':user_agent, 'Cookie':cookie}

    try:
        
        response = requests.get(url, headers=header)  
            
        print(f'return code:{response.status_code}')
        print(f"response:{response.text}")

        selector = etree.HTML(response.text)

        #Question list
        question = selector.xpath('//div[@class="HotItem-content"]/a/h2/text()')
        print(f'question:{question}')

        #Question link
        qurl = selector.xpath('//div[@class="HotItem-content"]/a/@href')
        print(f'qurl:{qurl}')

        info = dict(zip(question,qurl))

        for i in info:
            print(f'问题：{i}, 链接:{info[i]}')
            get_answer(info[i])
            # sleep(5)

    except requests.exceptions.ConnectTimeout as e:
        print('request over time')

#保存内容到文件
def save_file(filename,answerList):
    with open(filename, "w+") as ret:
        for line in answerList:
            ret.write(line)

#保存页面到文件
def save_page(response):
    p = Path(__file__)
    # print(f'path:{p}')

    pyfile_path = p.resolve().parent

    html_path = pyfile_path.joinpath('html')

    if not html_path.is_dir():
        Path.mkdir(html_path)
    page = html_path.joinpath('douban.html')

    try:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(response.text)
    except FileNotFoundError as e:
        print(f'file can not be open,{e}')
    except IOError as e:
        print(f'error when write file,{e}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 思路：先抓取主页面上fashion排行的前15个问题及答案链接，再进入答案页面获取答案
    # 问题1：设置cookies貌似不生效，始终无法得到15个问题的页面，一直会跳转到登陆页面
    # 问题2：Xpath在页面调试的时候可以正常显示内容，但是通过代码设置得到的结果是None
    # 问题3：保存问题和答案时，用什么数据结构暂存问题和答案对比较合适？List或者Dict？如果数据量比较大时，如何流式处理写文件？
    # 最终只实现了单个页面的答案抓取。。。

    # myurl = 'https://www.zhihu.com/hot?list=fashion'
    # get_question_link(myurl)

    myurl = 'https://www.zhihu.com/question/423879748'
    filename = r"D:\Ellen\Python\Geek\practise\week2\doc\save_zhihu.txt" 

    answer = get_answer(myurl)
    save_file(filename,answer)




