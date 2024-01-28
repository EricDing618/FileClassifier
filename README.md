# ✨文件分类器FileClassifier  
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

## 💖错误解决
- “无法分类，原因：...”错误提示
  1. 可能是`settings.json`配置错误。
  2. 可能是`settings.json`被误删了。
  3. 若以上两种都排除可以向仓库添加`issue`。
- “无法打开...！”错误提示
  1. 可能是目标文件不存在。
  2. 若以上可能排除可以向仓库添加`issue`。
- 其他bug请向仓库添加`issue`。
