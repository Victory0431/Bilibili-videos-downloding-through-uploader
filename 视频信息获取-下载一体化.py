import os
import time
import easygui
import requests
import datetime
from fake_useragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
path1 = os.getcwd()
ua = UserAgent()
programme = {}
programmeinfo = []
count = 0
length = 0
sec = 0
s=requests.session()
cookie = "_uuid=E71ACACD-B901-DB63-17D1-13BB0E6BA68E68793infoc; buvid3=F465EB7B-2D4A-4763-AEB5-3ADFF263B50818567infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(u)ml|~uJkR0J'uYuu)u|~|l; buvid_fp=F465EB7B-2D4A-4763-AEB5-3ADFF263B50818567infoc; buvid_fp_plain=F465EB7B-2D4A-4763-AEB5-3ADFF263B50818567infoc; LIVE_BUVID=AUTO9316153846806950; CURRENT_BLACKGAP=1; PVID=1; CURRENT_QUALITY=80; fingerprint=952d4dacefe9b75fc4adeac2e2217f42; sid=6ubiym6u; bfe_id=61a513175dc1ae8854a560f6b82b37af"
t1 = datetime.datetime.now()
mid = easygui.enterbox(title = '请输入up主的id',msg = '主页链接后面的号码\n 例：https://space.bilibili.com/66607740')#'66607740'#'485599712'

def forname(title):
    title = list(title)
    for i in title:
        if i == '*' or i == '?' or i == '\\' or i == '/' or i == '|' or i == '<' or i == '>' or i == ':' or i == '"':
            title[title.index(i)] = '-'
        else:
            pass
    return ''.join(title)
    
if os.path.exists('源文档\\' + mid):
        pass
else:
    os.makedirs(path1 + '\源文档\\' + mid) #001此处是递归创建目录，复数语法(位置莫名其妙，于是指定path1)
    
for page in range(1,100):
    headers= {'authority': 'api.bilibili.com', 'method': 'GET',
              'path': '/x/space/arc/search?mid='+mid+'&ps=30&tid=0&pn=2&keyword=&order=pubdate&jsonp=jsonp',
              'scheme': 'https', 'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'zh-CN,zh;q=0.9',
              'cookie': cookie, 'dnt': '1', 'origin': 'https://space.bilibili.com',
              'referer': 'https://space.bilibili.com/'+mid+'/video?tid=0&page=2&keyword=&order=pubdate',
              'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
              'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site',
              'user-agent': ua.random
              }
    url = 'https://api.bilibili.com/x/space/arc/search?mid='+mid+'&ps=30&tid=0&pn=' + str(page) + '&keyword=&order=pubdate&jsonp=jsonp'  
    pathy = path1 + '\\源文档\\'+ mid + '\\' + mid +'--' + str(page) + '.txt'
    if os.path.exists(pathy):
        print('第'+ str(page)+ '页已存在')
        with open(pathy,'r',encoding = 'utf-8')as f:
            vv = f.read()
        false = 'fa'
        true = '1'
        arc = eval(vv)
        ai = arc['data']['list']['vlist']
    else:
        rs=s.get(url,headers=headers,verify=False)
        ui = rs.text
        with open(pathy,'w',encoding = 'utf-8') as f:
                f.write(ui)
        #print(str(page))
    
        #print(len(ui))
        false = 'fa'
        true = '1'
        arc = eval(ui)
        ai = arc['data']['list']['vlist']
        
    for i in ai:
        print(str(count) + '\t' + i['bvid'] + '\t'+ i['length'] + '\t' + i['title'])
        length += int(i['length'].split(':')[0])
        sec += int(i['length'].split(':')[1])
        programme[str(count)] = [i['bvid'],i['title']]
        programmeinfo.append(i)
        count += 1
        
    print('         ->->-找到视频 '+ str(len(ai)) + '个->->-')
    
    if len(ai)<30:
        author = ai[0]['author']
        print('以上就是' + author + '的全部内容')
        break
length += sec//60
print(author + '总共发布视频'+str(len(programme))+'个,共'+str(length)+'分钟，约合'+str(length/60)+'小时')
with open(mid + '视频集合.txt','w',encoding = 'utf-8') as f:
                f.write(str(programmeinfo))

bv = []
al = False
print('请输入想要下载的序号，以空格分隔，若要下载全部，请输入 all ')
s = input('>>>')
if s == 'all':
    al = True
    print('即将下载全部视频')
else:
    li = s.split(' ')
    for i in li:
        try:
            nn = int(i)
        except:
            continue
        else:
            bv.append(nn)

print(bv)

num = 0
#ai = eval(con)

#author = ai[0]['author']

if os.path.exists(author):
    save_dir = path1 + '\\' + author
    pass
elif os.path.exists(mid):
    save_dir = path1 + '\\' + mid
    pass
else:
    try:
        os.mkdir(author)
    except:
        os.mkdir(mid)
        save_dir = path1 + '\\' + mid
    else:
        save_dir = path1 + '\\' + author

fall = []  

if al:
    ai = programmeinfo
    t1 = datetime.datetime.now()
    for i in range(0,len(ai)):
        bvid = ai[i]['bvid']            #'BV1Q64y1e7mQ'
        title = ai[i]['title']
        title = forname(title)
        if os.path.exists(save_dir + '\\' + title + '.mp4'):
            print(title + '已存在')
        else:
            v_url = 'https://www.bilibili.com/video/'+bvid
            tem_cmd = "you-get" +" " +v_url + "  -o "+save_dir
            print(str(num) + ' ' + title)
            end = False
            ch = 1
            while not end:
                result = os.system(tem_cmd)
                if result == 0:
                    t2 = datetime.datetime.now()
                    print(title + ' 下载成功！')
                    print('用时：' + str(t2-t1))
                    t1 = t2
                    num += 1
                    end = True
                else:
                    if ch < 4:
                        print(str(i) + ' ERROR!!!!')
                        print('第'+str(ch)+'次重试中...')
                        ch += 1
                        continue
                    else:
                        print('重试失败，请关闭程序，稍后再试，即将开始下一个')
                        fall.append(title)
        
else:
    ai = programme
    t1 = datetime.datetime.now()
    for i in bv:
        bvid = ai[str(i)][0]            #'BV1Q64y1e7mQ'
        title = ai[str(i)][1]
        title = forname(title)
        if os.path.exists(save_dir + '\\' + title + '.mp4'):
            print(title + '已存在')
        else:
            v_url = 'https://www.bilibili.com/video/'+bvid
            tem_cmd = "you-get" +" " +v_url + "  -o "+save_dir
            print(str(num) + ' ' + title)
            end = False
            ch = 1
            while not end:
                result = os.system(tem_cmd )
                if result == 0:
                    t2 = datetime.datetime.now()
                    print(title + ' 下载成功！')
                    print('用时：' + str(t2-t1))
                    t1 = t2
                    num += 1
                    end = True
                else:
                    if ch < 4:
                        print(str(i) + ' ERROR!!!!')
                        print('第'+str(ch)+'次重试中...')
                        ch += 1
                        continue
                    else:
                        print('重试失败，请关闭程序，稍后再试，即将开始下一个')
                        fall.append(title)














