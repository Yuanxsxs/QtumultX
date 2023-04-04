import re
from make_quick_installation_link import Output
from urllib.parse import quote
'''
用来把readme文件中的raw值 替换为 一键导入qx链接
'''
def subFunc(search):
    f = search.group()
    n = Output(f)
    print(f'{f}\n变成\n{n}')
    return n
if __name__ == '__main__':
    file = "./icon/readme.md"
    with open(file,"r",encoding="utf-8") as f:
        cont = f.read()

    pattern = re.compile('https?:\/\/(raw\.|gist\.)?(githubusercontent|github)\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*?)\.(?P<suffix>(conf|snippet|txt|json|js|list|qxrewrite))')
    cont = re.sub(pattern, subFunc ,cont)

    with open(file,"w",encoding="utf-8") as f:
        f.write(cont)