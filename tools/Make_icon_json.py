import re,json
import requests
url = input('请输入仓库链接(png所在的页面):')
title = re.findall('.*/(.*?)$',url)[0]#标题
file = re.sub('/','_',title) +'.json'
auth = re.search('(?<=com/).*?(?=/)',url).group()#作者
raw = re.sub('tree/','',re.sub('github.com','raw.githubusercontent.com',url))
def main(url,title = 'QxIcon',description='Collect by Yuanxsxs'):
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Connection': 'close',
    }
    try :
        res=requests.get(url,headers=headers,timeout= 5)
    except :
        print('连接超时请重试！')
    content=re.findall('(?<= title=").*?PNG|(?<= title=").*?png',res.content.decode('utf-8'))
    # print(len(content),content)
    quanXicon = {
        "name":title,
        "description":description,
        "icons":[]
    }
    for item in content:
        con = {
            "name": item,
            "url" : raw + '/' + item
        }
        quanXicon['icons'].append(con)
    with open(f'Icon/{file}','w') as f:
        content = json.dumps(quanXicon,indent=1,separators=(',',':'))
        f.write(content)
    print(f'订阅文件已生成,\n作者:{auth},\n描述:{description}')
main(url,title = title,description=f'Made by {auth}')