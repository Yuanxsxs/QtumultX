import re,json,os
import requests,pyperclip
from operate_picture import specialprint as sprint
from make_quick_installation_link import Output as mqil_out
from make_icon_json_l import author_self,file_name_remote_self,branch_self
# url = input('请输入仓库链接(仅含有png的网页面):')
url = "https://github.com/Centralmatrix3/Scripts-Rules/tree/Master/Matrix-icon/Color"
''' Example : https://github.com/Centralmatrix3/Scripts-Rules/tree/Master/Matrix-icon/Color'''
_re = re.search('^https?:\/\/github.com\/(?P<author>.*?)\/(?P<repo>.*)\/tree\/(?P<branch>.*?)\/(?P<path>.*)',url)
auth = _re.group('author') #作者
title = re.search('.*\/(?P<title>.*?)$',_re.group('path')).group('title')#标题
path = f'./Icon/{auth}/' + _re.group('path') 
file = path + '/' + title + '.json'
raw = re.sub('tree/','',re.sub('github.com','raw.githubusercontent.com',url))

def dumpjson(path,cont,info = '文件录入成功',encodeing='utf-8'):
    '''将cont(cont 为 list 或 dict )转化为json并写入文件
    info 为提示词
    '''
    with open(path,'w',encoding=encodeing) as f:
        cont_str = json.dumps(cont, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        f.write(cont_str)
    print(info)

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print ("---  new folder...  ---")
		print ("---  OK  ---")
 
	else:
		print ("---  There is this folder!  ---")
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
    except Exception  as e:
        print(f'连接超时请重试！{e}')
    content=re.findall('(?<= title=").*?PNG|(?<= title=").*?png',res.content.decode('utf-8'))
    print(len(content),content)
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
    mkdir(path=path)
    dumpjson(path=file,cont=quanXicon)
    sprint(f'订阅文件已生成,\n作者:{auth},\n描述:{description}\n保存在\'{os.getcwd()}\{file}\'')
    sprint('请自行将该文件上传到GitHub并获取到相应raw得到订阅链接,导入qx即大功告成!')
main(url,title = title,description=f'Made by {auth}')
jsonraw = f'https://raw.githubusercontent.com/{author_self}/{file_name_remote_self}/{branch_self}/{re.search("./(?P<file>.*)",file).group("file")}'
print(jsonraw)
output = mqil_out(jsonraw)
pyperclip.copy(output)
print(f'一键安装链接:\n{output}\n已复制!两秒后自动关闭\n先 git push!\n先 git push!\n先 git push!')