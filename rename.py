# -*- coding: UTF-8 -*-
import os

#获得文件夹下文件名列表
path=r"C:\wing"
path=unicode(path,"utf8")
file_list=os.listdir(path)

#选择要重命名的文件夹路径
os.chdir(path)

for file in file_list:
    os.rename(file,file.replace("Lesson","wh"))
