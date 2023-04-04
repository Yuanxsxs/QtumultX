import re , pyperclip,time
from urllib.parse import quote
''' pyperclip 为第三方库 使用 pip install pyperclip 进行安装
    
'''
pattern_raw = "^https?:\/\/(raw\.githubusercontent|gist\.githubusercontent|gitlab)\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite))$"
pattern_like_raw ='^https?:\/\/github\.com/(?P<author>.*?)\/.*\/(blob|raw)\/.*\.(conf|snippet|txt|json|js|list|qxrewrite).*'#可转化为raw的似raw非rawurl
def Output(raw,tag = "Yuan's Selfuse Rewrite"):
    '''raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf
       raw = https://gitlab.com/lodepuly/vpn_tool/-/raw/main/Tool/Loon/Rule/OpenAI.list
    '''
    
    resarch = re.search(pattern_raw,raw)#必须是raw
    if resarch == None:#当输入的不是raw时
        resarch = re.search(pattern_like_raw,raw)#判断是不是类raw链接
        if resarch == None:#当url为非 类raw链接时
            print('无法识别此url!')
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
            txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}"]}}'''
        if suffix in ['txt','list']:
            txt = f'''{{"filter_remote":["{raw}?raw=true,tag={tag},force-policy={resarch.group('tag')}"]}}'''
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