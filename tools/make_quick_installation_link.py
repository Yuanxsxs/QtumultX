import re , pyperclip,time,sys
from urllib.parse import quote
''' pyperclip 为第三方库 使用 pip install pyperclip 进行安装
    支持机场订阅,分流订阅,重写订阅,图标订阅的一键导入链接制作
    谁用谁知道真的好用
'''
pattern_raw = "^https?:\/\/(raw\.githubusercontent|gist\.githubusercontent|gitlab)\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite))$"
pattern_like_raw ='^https?:\/\/github\.com/(?P<author>.*?)\/.*\/(blob|raw)\/.*\.(conf|snippet|txt|json|js|list|qxrewrite).*'#可转化为raw的似raw非rawurl

def Output(raw,tag = "Yuan's Selfuse Rewrite",opt_parser = "true",update_interval = "172800"):    
    '''
       添加的资源默认开启资源解析器 资源更新时间为24hours
       raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf
       raw = https://gitlab.com/lodepuly/vpn_tool/-/raw/main/Tool/Loon/Rule/OpenAI.list
    '''

    resarch = re.search(pattern_raw,raw)#必须是raw
    if resarch == None:#当输入的不是raw时
        resarch = re.search(pattern_like_raw,raw)#判断是不是类raw链接
        if resarch == None:#当url为非 类raw链接时
            
            if "subscrib" in raw:#初步判断url是否为 机场订阅
                resarch_s = re.search('^https?:\/\/(.*\.)?(?P<tag>.*?)\..*subscrib',raw)#确认是否为机场
                tag = resarch_s.group('tag')
                raw = f'{raw}#emoji=1&rename=@-{tag}'
                txt = f'''{{"server_remote":["{raw},tag={tag}, update-interval={update_interval},opt-parser={opt_parser}"]}}'''
                url = "https://quantumult.app/x/open-app/add-resource?remote-resource=" + quote(txt,encoding='utf-8')
                return url
            else:
                print('无法识别此url!')
            sys.exit()
        else: #当url为类raw链接时 转化为raw链接
            url = re.sub("github.com","raw.githubusercontent.com",raw)
            raw = re.sub("\/(blob|raw)\/","\/",url)
            
    resarch = re.search(pattern_raw,raw)
    tag = resarch.group('tag') + '-' + resarch.group("author")#显示标签
    suffix =  resarch.group('suffix')#选出后缀来决定添加的资源
    if suffix in ['json'] :#还要分是task 还是 icon 但是现在暂时只考虑icon
        txt = f'''["{raw}"]'''
        url = "https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=" + quote(txt,encoding='utf-8')
    else :
        if suffix in ['conf','snippet']:
            txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}, update-interval={update_interval},opt-parser={opt_parser}"]}}'''
        if suffix in ['txt','list']:
            txt = f'''{{"filter_remote":["{raw}?raw=true,tag={tag},force-policy={resarch.group('tag')}, update-interval={update_interval},opt-parser={opt_parser}"]}}'''
        url = "https://quantumult.app/x/open-app/add-resource?remote-resource=" + quote(txt,encoding='utf-8')
    return url
def main():
    raw = pyperclip.paste()       
    output = Output(raw)
    pyperclip.copy(output)
    print(f'一键安装链接:\n{output}\n已复制!两秒后自动关闭')
    time.sleep(2)
if __name__ == '__main__':
    main()