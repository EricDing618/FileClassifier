from os import getcwd, listdir, makedirs
import os.path
from pathlib import Path
from shutil import move, Error
from numpy import delete
from config import *

#核心代码
def classify(pathlist, file=None, notempty=False):
    try:
        while pathlist.size:
            print(pathlist)
            if notempty: #字典不为空
                for item in file: #遍历自定义分类器，file=[(classifier,type),...]
                    index=-1
                    for path in pathlist: #遍历文件路径列表
                        olddir=path.rsplit('\\',1)[0]
                        name=path.rsplit('\\',1)[1]
                        type_='.'+name.rsplit('.',1)[1].lower()
                        index+=1
                        print('Moving:'+path)
                        if type(item[1])==list or tuple: #类型为矩阵
                            print(type_,item[1])
                            if type_ in item[1]: #匹配这一分类
                                newdir=os.path.join(olddir,item[0])
                                if not Path(newdir).is_dir():
                                    makedirs(newdir)
                                move(path,newdir) # 使用 move() 函数
                                print('ok')
                                pathlist = delete(pathlist,index,axis=0) # 更新列表
                                index-=1
                        else: #类型为字符串
                            if type_ == item[1]: #匹配这一分类
                                newdir=os.path.join(olddir,item[0])
                                if Path(newdir).is_dir()==False:
                                    makedirs(newdir)
                                if Path(os.path.join(newdir,name)).is_file():
                                    move(path,os.path.join(newdir,name.rsplit('.',1)[0]+' - 副本'+type_)) # 使用 move() 函数
                                else:
                                    move(path,newdir) # 使用 move() 函数
                                print('ok')
                                pathlist = delete(pathlist,index,axis=0) # 更新列表
                                index-=1
            index=0
            for path in pathlist:
                print('Moving:'+path)
                olddir=path.rsplit('\\',1)[0]
                name=path.rsplit('\\',1)[1]
                type_='.'+name.rsplit('.',1)[1].lower()
                if type_ in Image:
                    newdir=os.path.join(olddir,'图片')
                elif type_ in Video:
                    newdir=os.path.join(olddir,'视频')
                elif type_ in Music:
                    newdir=os.path.join(olddir,'音乐')
                elif type_ in Zip:
                    newdir=os.path.join(olddir,'压缩包')
                elif type_ in SourceFile:
                    newdir=os.path.join(olddir,'源文件')
                elif type_ in Program:
                    newdir=os.path.join(olddir,'二进制文件')
                elif type_ in Text:
                    newdir=os.path.join(olddir,'文档')
                else:
                    newdir=os.path.join(olddir,'其它')
                if not Path(newdir).is_dir():
                    makedirs(newdir)
                if Path(os.path.join(newdir,name)).is_file():
                    move(path,os.path.join(newdir,name.rsplit('.',1)[0]+' - 副本'+type_)) # 使用 move() 函数
                else:
                    move(path,newdir) # 使用 move() 函数
                print('ok')
                pathlist = delete(pathlist,index,axis=0) # 更新列表
    except Error:
        if Path(os.path.join(newdir,name)).is_file():
            pass
        else:
            raise Exception('未知的报错！')