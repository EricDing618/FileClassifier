# ✨文件分类器FileClassifier  

![image](show.jpg)  

## 👀工具材料
 - Windows10  
 - Python 3.11.0 64-bit  
 - Visual Studio Code
  
## 👏所需库（包）和工具  
- `os`  
- `shutil`
- `pathlib`
- `json5`  
- `PyQt5`  
- `numpy`
- `pyuic5.exe`(From PyQt5)  
- `pyrcc5.exe`(From PyQt5)  
  
## 📥安装第三方库  
打开`cmd`并输入：  
```shell  
python -m pip install json5 pyqt5 numpy
```  
（注：安装失败可能是因为网络原因或没有将`Python`添加至`PATH`环境变量中）  

## 🎨自定义分类步骤  
1. 打开`settings.json`。  
2. 输入格式：`{类型:后缀}`，如：  
   ```json5  
    {
        //...
        "Python Files":[".py",".pyw"],
        "C Files":[".c",".h"]
    }
    ```  

    **注意：一定要记得在后缀前面加上“.”！**
3. 保存并重新运行主文件`main.py`。

## 💖错误及漏洞
- “无法分类，原因：...”错误提示
1. 可能是`settings.json`配置错误
   1. 使用 **“\\”、“/”、“:”、“*”、“?”、“"”、“<"、“>”和“|”** 这样的非法字符。
   2. `Key`和`Value`的类型错误。
2. 可能是`settings.json`被误删了。
3. 程序**没有足够的权限**访问文件（夹）。
4. 若以上可能都排除可以向仓库添加`issue`。
- “无法打开...！”错误提示
1. 可能是目标文件不存在。
2. 若以上可能排除可以向仓库添加`issue`。
- 桌面文件整理不全  
  这是一个正常的“bug”，因为`用户桌面`和`公用桌面`的文件都会显示在电脑桌面上。
- 其他bug请向仓库添加`issue`。

## 📢提示
- 可以在命令行中运行本程序以获取报错内容。
- 自定义分类越多，整理速度可能会越慢。
- 在移动之前，请再三思考，因为无法恢复成之前的样子。
