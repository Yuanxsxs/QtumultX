import re , pyperclip
from urllib.parse import quote
''' pyperclip 为第三方库 使用 pip install pyperclip 进行安装
    
'''
def Output(raw,tag = "Yuan's Selfuse Rewrite"):
    '''raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf'''
    
    set = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.[(conf)|(snnipet)|(txt)]",raw)
    tag = set.group('tag') + '-' + set.group("author")
    txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}"]}}'''
    cont_enquoted = quote(txt,encoding='utf-8')
    
    url = "https://api.boxjs.app/quanx/add-resource?remote-resource=" + cont_enquoted
    return url
def main():
    raw = pyperclip.paste()
    research = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.[(conf)|(snnipet)|(txt)]",raw)
    if research == None:
        raw = input('请复制正确的raw链接并输入在下方:\n')
    output = Output(raw)
    pyperclip.copy(output)
    print(f'{output}\n已复制!')
if __name__ == '__main__':
    main()