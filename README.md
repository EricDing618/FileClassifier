# ✨文件分类器FileClassifier  
## 👀工具材料
 - Windows10  
 - Python 3.11.0 64-bit  
 - Visual Studio Code
  
## 👏所需库（包）和工具  
- `os`  
- `json5`  
- `PyQt5`  
- `pyuic5.exe`(From PyQt5)  
- `pyrcc5.exe`(From PyQt5)  
  
## 📥安装第三方库  
打开`cmd`并输入：  
```shell  
python -m pip install json5 pyqt5 
```  
（注：安装失败可能是因为网络原因或没有将`Python`添加至`PATH`环境变量中）  

## 🎨自定义分类步骤  
1. 打开`settings.json`。  
2. 输入格式：`{类型:后缀}`，如：  
   ```json5  
    {
        "Python Files":[".py",".pyw"],
        "C Files":[".c",".h"]
    }
    ```  
    **注意：一定要记得在后缀前面加上“.”！**
3. 保存并重新运行主文件`main.py`。  
