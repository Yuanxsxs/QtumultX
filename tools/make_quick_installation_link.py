import re , pyperclip
from urllib.parse import quote
''' pyperclip 为第三方库 使用 pip install pyperclip 进行安装
    
'''
def Output(raw,tag = "Yuan's Selfuse Rewrite"):
    '''raw = https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/Crack/Ego_reader.conf'''
    
    set = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(conf|snippet|txt|json|js)$",raw)
    tag = set.group('tag') + '-' + set.group("author")
    txt = f'''{{"rewrite_remote":["{raw}?raw=true,tag={tag}"]}}'''
    cont_enquoted = quote(txt,encoding='utf-8')
    
    url = "https://api.boxjs.app/quanx/add-resource?remote-resource=" + cont_enquoted
    return url
def main():
    raw = pyperclip.paste()
    research = re.search("^https?:\/\/raw\.githubusercontent\.com\/(?P<author>.*?)\/.*\/(?P<tag>.*)\.(conf|snippet|txt|json|js)$",raw)
    # print(research)
    if research == None:
        '''https://github.com/Yuanxsxs/QtumultX/blob/master/Rewrite/AD_block/Cuttfish/StartUp.conf'''
        url = re.search('^https?:\/\/github\.com/(?P<author>.*?)\/.*\/blob\/.*\.(conf|snippet|txt|json|js)$',raw).group()
        
        if url ==  None:
            raw = input('请复制正确的raw链接并输入在下方:\n')
        else:
            print('虽然不是正确的raw,但问题不大.')
            url = re.sub("github.com","raw.githubusercontent.com",url)
            raw = re.sub("\/blob","",url)
        # print(raw)        
    output = Output(raw)
    pyperclip.copy(output)
    print(f'一键安装链接:\n{output}\n已复制!')
if __name__ == '__main__':
    main()