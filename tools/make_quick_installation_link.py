import re , pyperclip,time
from urllib.parse import quote
''' pyperclip 为第三方库 使用 pip install pyperclip 进行安装
    
'''
def Output(raw,tag = "Yuan's Selfuse Rewrite"):
    '''raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf'''
    
    resarch = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(?P<suffix>(conf|snippet|txt|json|js|list))$",raw)
    
    tag = resarch.group('tag') + '-' + resarch.group("author")#显示标签
    suffix =  resarch.group('suffix')#选出后缀来决定添加的资源
    if suffix in ['json'] :#还要分是task 还是 icon 但是现在暂时只考虑icon
        txt = f'''["{raw}"]'''
        url = "https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=" + quote(txt,encoding='utf-8')
    else :
        if suffix in ['conf','snippet']:
            txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}"]}}'''
        if suffix in ['txt','list']:
            txt = f'''{{"filter_remote":["{raw}?raw=true,tag={tag}"]}}'''
        url = "https://quantumult.app/x/open-app/add-resource?remote-resource=" + quote(txt,encoding='utf-8')
    return url
def main():
    raw = pyperclip.paste()
    research = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(conf|snippet|txt|json|js|list)$",raw)
    # print(research)
    if research == None:
        '''https://github.com/Yuanxsxs/QtumultX/(blob|raw)/master/Rewrite/AD_block/Cuttfish/StartUp.conf'''
        url = re.search('^https?:\/\/github\.com/(?P<author>.*?)\/.*\/(blob|raw)\/.*\.(conf|snippet|txt|json|js|list)$',raw)
        if url ==  None:
            raw = input('请复制正确的raw链接并输入在下方:\n')
        else:
            url = url.group()
            print('虽然不是正确的raw,但问题不大.')
            url = re.sub("github.com","raw.githubusercontent.com",url)
            raw = re.sub("\/(blob|raw)\/","\/",url)
        # print(raw)        
    output = Output(raw)
    pyperclip.copy(output)
    print(f'一键安装链接:\n{output}\n已复制!两秒后自动关闭')
    time.sleep(2)
if __name__ == '__main__':
    main()