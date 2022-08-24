import os 
from operate_picture import pixel,gainpath,specialprint as sprint
'''操作多张图片的脚本'''
if __name__ == '__main__':
    folder = gainpath(folder_flag=True)#获取多张图片所在的文件夹路径
    if folder == '':
        print('尚未选择文件！')
        exit()
    pic_list = os.listdir(folder)#获取folder下所有文件的名字并返回一个列表

    for item in pic_list:
        pixel(f'{folder}/{item}')
    sprint('请将生成的changed文件夹重命名并上传到GitHub,\n接着复制该文件夹在GitHub上的链接,\n接着打开Make_icon_json,\n输入复制的链接.')