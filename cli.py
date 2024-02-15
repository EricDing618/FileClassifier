"""
以命令行的形式运行程序（源代码：main.py），可用于查看输出信息。
在您运行或调试源代码文件，并且没有可执行文件时此文件无效。
"""
from os import system,getcwd
import os.path
if os.path.isfile(getcwd()+'\\cli.exe'):
    system('cli.exe')
else:
    print('错误：可执行文件不存在！')
input('按回车键退出本程序...')