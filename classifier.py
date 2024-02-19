#导入所需要的库（包）
from os import makedirs
import os.path
from pathlib import Path
from shutil import move, Error
from numpy import delete
from config import *

#判断名称的合法性
def NameIsBad(string:str) -> bool:
    a=0
    BadWords=[
            '\\',
            '/',
            ':',
            '*',
            '?',
            '"',
            '<',
            '>',
            '|'
        ]
    for i in string:
        if i in BadWords:
            a=1
            break
    return bool(a)

#核心代码
def classify(patharray, file=None, 
             notempty=False):
    """
    classify:整个项目的核心函数
    patharray:装文件路径的numpy.array()
    file:设置自定义分类的文件，默认为./settings.json
    notempty:自定义文件是否不为空
    """
    try:
        #print(patharray)
        while patharray.size:
            if notempty: #字典不为空
                for item in file: #遍历自定义分类器，file=[(classifier,type),...]
                    if NameIsBad(item[0]):
                        item[0]='' 
                    classifytype=item[1]
                    index=-1
                    for path in patharray: #遍历文件路径列表
                        olddir=path.rsplit('\\',1)[0]
                        name=path.rsplit('\\',1)[1]
                        type_='.'+name.rsplit('.',1)[-1].lower() if '.' in name else ''
                        index+=1
                        if ((type(classifytype)==list or type(classifytype)==tuple) and type_ in classifytype) or (type(classifytype)==str and type_ == classifytype): #匹配这一分类
                            print('Moving:'+path)
                            #print(type_,classifytype)
                            newdir=os.path.join(olddir,item[0]) if item[0] != '' else os.path.join(olddir,'其它')
                            if Path(newdir).is_dir()==False:
                                makedirs(newdir)
                            if Path(os.path.join(newdir,name)).is_file():
                                move(path,os.path.join(newdir,name.rsplit('.',1)[0]+' - 副本'+type_)) # 使用 move() 函数
                            else:
                                move(path,newdir) # 使用 move() 函数
                            print('ok')
                            patharray = delete(patharray,index,axis=0) # 更新列表
                            index-=1
            
            #剩余部分
            index=-1
            for path in patharray:
                print('Moving:'+path)
                olddir=path.rsplit('\\',1)[0]
                name=path.rsplit('\\',1)[1]
                type_='.'+name.rsplit('.',1)[-1] if '.' in name else ''
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
                    newdir=os.path.join(olddir,'程序')
                elif type_ in Text:
                    newdir=os.path.join(olddir,'文档')
                elif type_ in ShortCut:
                    newdir=os.path.join(olddir,'快捷方式')
                else:
                    newdir=os.path.join(olddir,'其它')
                if Path(newdir).is_dir()==False:
                    makedirs(newdir)
                if Path(os.path.join(newdir,name)).is_file():
                    move(path,os.path.join(newdir,name.rsplit('.',1)[0]+' - 副本'+type_)) # 使用 move() 函数
                else:
                    move(path,newdir) # 使用 move() 函数
                print('ok')
                patharray = delete(patharray,index,axis=0) # 更新列表
            #print(patharray)
    except Error:
        if Path(os.path.join(newdir,name)).is_file():
            pass
        else:
            raise Exception('未知的报错！')
        
if __name__=='__main__':
    print(NameIsBad('aaa'))
    print(NameIsBad('aaa?'))