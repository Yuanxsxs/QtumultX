import re
from make_quick_installation_link import Output
from urllib.parse import quote
'''
用来把readme文件中的raw值 替换为 一键导入qx链接
'''
def Output(url,tag = "Yuan's Selfuse Rewrite"):
    '''raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf'''
    

    rawre = re.search("^https?:\/\/(raw|gist)\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite)).*",url)   
    if rawre == None:#条件成立时 该链接不是raw 不成立时为raw
        urlre = re.search('^https?:\/\/github\.com/(?P<author>.*?)\/.*\/(blob|raw)\/.*\.(conf|snippet|txt|json|js|list|qxrewrite).*',url)
        if urlre ==  None:
            print(f"无法识别该{url}")
            exit()
        else:
            url = urlre.group()
            url = re.sub("github.com","raw.githubusercontent.com",url)
            url = re.sub("\/(blob|raw)\/","\/",url)
    rawre = re.search("^https?:\/\/(raw|gist)\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite)).*",url)
    raw = url
    tag = rawre.group('tag') + '-' + rawre.group("author")#显示标签
    suffix =  rawre.group('suffix')#选出后缀来决定添加的资源
    if suffix in ['json'] :#还要分是task 还是 icon 但是现在暂时只考虑icon
        txt = f'''["{raw}"]'''
        url = "https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=" + quote(txt,encoding='utf-8')
    else :
        if suffix in ['conf','snippet','qxrewrite','js']:
            txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}"]}}'''
        if suffix in ['txt','list']:
            txt = f'''{{"filter_remote":["{raw}?raw=true,tag={tag}"]}}'''
        quick_install_url = "https://quantumult.app/x/open-app/add-resource?remote-resource=" + quote(txt,encoding='utf-8')
    return quick_install_url
def subFunc(search):
    f = search.group()
    n = Output(f)
    print(f'{f}\n变成\n{n}')
    return n
if __name__ == '__main__':
    with open("README.md","r",encoding="utf-8") as f:
        cont = f.read()

    pattern = re.compile('https?:\/\/(raw\.|gist\.)?(githubusercontent|github)\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*?)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite))')
    cont = re.sub(pattern, subFunc ,cont)

    with open("README.md","w",encoding="utf-8") as f:
        f.write(cont)