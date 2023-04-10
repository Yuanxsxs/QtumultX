import os ,tkinter as tk,re ,json,pyperclip
from tkinter import filedialog 
from PIL import Image
from make_quick_installation_link import Output as mqil_out
author           = 'Yuanxsxs'
file_name_remote = 'QtumultX'
branch           = 'master'
def dumpjson(path,cont,info = '文件录入成功',encodeing='utf-8'):
    '''将cont(cont 为 list 或 dict )转化为json并写入文件
    info 为提示词
    '''
    with open(path,'w',encoding=encodeing) as f:
        cont_str = json.dumps(cont, indent=4, separators=(',', ': '),ensure_ascii=False)
        f.write(cont_str)
    print(info)
def gainpath(folder_flag = False):
    '''获取选择文件路径与文件夹路径,默认获取单个文件路径'''
    root = tk.Tk()
    root.withdraw()
    if folder_flag == True:
        print('请选择文件夹路径：')
        Folder = filedialog.askdirectory() #获得选择好的文件夹
        return Folder
    else:
        print('请选择文件路径：')
        File = filedialog.askopenfilename() #获得选择好的文件
        return File
def mkdir(path):
    '''创建新文件夹'''
    folder = os.path.exists(path)

    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print ("---  New folder created  ---")
        print(f'position is:{path}')
    else:
        print("---  The folder is already existed!  ---") 

def pixel(file_in,width = 108,height = 108, format = '.png'):
    '''更改图片像素，file_in为图片的绝对路径'''
    try :
        file = re.search('.*\/(?P<series>.*)\/(?P<FILE>.*?)\.(?P<suffix>png|jpg|PNG|JPG)$',file_in)#取 C:/Users/Yuan/Pictures/1071126863/img/Changed/file_527762.png 中的Changed/file_527762
        file_name = file.group('FILE')
        global folder ,series_name        
        series_name = file.group('series')
        folder = f'./Icon/{series_name}/'
        file_out = folder + file_name + format
        try:
            Image.open(file_in).resize((width, height), Image.Resampling.LANCZOS).save(file_out)
            print(f'图片像素已更改,\n文件保存在\'{file_out}\'')
        except FileNotFoundError:
            mkdir(f'./Icon/{series_name}')
            Image.open(file_in).resize((width, height), Image.Resampling.LANCZOS).save(file_out)
            print(f'图片像素已更改,\n文件保存在\'{file_out}\'')
    except AttributeError as e :
        print(f'无效内容,已跳过！{e}')#有其他格式的文件(不符合正则表达,或其他后缀)
        file_out = None
    return file_out
def main():
    '''批量调整文件夹内的图片'''
    folder_origin = gainpath(folder_flag=True)#获取多张图片所在的文件夹路径
    if folder_origin == '':
        print('尚未选择文件！')
        exit()
    pic_list = os.listdir(folder_origin)#获取folder下所有文件的名字并返回一个列表
    icons = []
    
    for item in pic_list:
        fileout_f = pixel(f'{folder_origin}/{item}')#./Icon/XZKB/54cbcea52ad3b6be.png
        if fileout_f == None:
            continue
        fileout = re.search('\.\/(.*\..*)',fileout_f).group(1)#/Icon/XZKB/54cbcea52ad3b6be.png
        raw = f'https://raw.githubusercontent.com/{author}/{file_name_remote}/{branch}/{fileout}'
        con = {"name": item,"url" : raw }
        icons.append(con)
    description = f'Made by {author}'
    quanXicon = {"name":re.search('.*\/(.*)',folder_origin).group(1),"description":description,"icons":icons}
    dumpjson(f'{folder}/{series_name}.json',quanXicon,'json文件已生成')
    folder_save = re.search('\.\/(.*)\/.*',folder).group(1)
    jsonraw = f'https://raw.githubusercontent.com/{author}/{file_name_remote}/{branch}/{folder_save}/{series_name}.json'
    output = mqil_out(jsonraw)
    pyperclip.copy(output)
    print(f'一键安装链接:\n{output}\n已复制!两秒后自动关闭\n先 git push!\n先 git push!\n先 git push!')
if __name__ == '__main__': 
    main()