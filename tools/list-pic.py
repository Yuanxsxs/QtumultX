import os 
from operate_picture import pixel,gainpath
if __name__ == '__main__':
    folder = gainpath(folder_flag=True)#获取多张图片所在的文件夹路径
    if folder == '':
        print('尚未选择文件！')
        exit()
    pic_list = os.listdir(folder)#获取folder下所有文件的名字并返回一个列表

    for item in pic_list:
        pixel(f'{folder}/{item}')