import tkinter as tk
from tkinter import Widget, filedialog
from PIL import Image
import re,os
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    resized_image.save(file_out)
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
        file_name ,others = re.findall('.*/(.*?)\.(png|jpg|PNG|JPG)$',file_in)[0]#取 C:/Users/Yuan/Pictures/1071126863/img/Changed/file_527762.png 中的Changed/file_527762
        file_path = re.findall('.*/',file_in)[0] # 取 C:/Users/Yuan/Pictures/1071126863/img/Changed/file_527762.png 中的C:/Users/Yuan/Pictures/1071126863/img/Changed/
        file_out = file_path + 'Changed/' + file_name + format
        try:
            Image.open(file_in).resize((width, height), Image.Resampling.LANCZOS).save(file_out)
            print(f'图片像素已更改,\n文件保存在\'{file_out}\'')
        except FileNotFoundError:
            mkdir(f'{file_path}changed')
            Image.open(file_in).resize((width, height), Image.Resampling.LANCZOS).save(file_out)
            print(f'图片像素已更改,\n文件保存在\'{file_out}\'')
    except :
        print('内置文件夹，已跳过！')
        pass

if __name__ == '__main__':
    file = gainpath()
    if file == '':
        print('尚未选择！')
        exit()
    try:
        width = int(input('请输入图片宽度：'))
        height = int(input('请输入图片高度：'))
        pixel(file,width,height)
    except:
        pixel(file)
    

