#!/usr/bin/env/python35
# -*-coding:utf-8-*-
# author:Keekuun

"""
问题：生成一个文件夹，文件夹下面生成100个txt文件，分别命名为1.txt ,2.txt到100.txt,
其中1.txt内容为1到100,2.txt的内容为101到200，以此类推到100.txt的内容为9901到10000。
"""

import os


# 创建文件夹
def create_directory():
    # os.chdir('E:')                                            # 切换到指定目录
    path = r'E:\pycharmfile\exercise'                           # 指定文件根目录
    file_name = '100txt'                                        # 子目录
    target_path = os.path.join(path, file_name)                 # 将子目录放在根目录下面
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    # print(target_path)
    return target_path


# 产生txt文件
def create_txt():
    for i in range(1, 101):
        # 创建100个txt
        txt = '{}.txt'.format(str(i))
        with open(txt, 'w', encoding='utf-8') as f:
            # 写入内容
            for j in range(1, 101):
                f.write(str(j+(i-1)*100)+'\n')


if __name__ == '__main__':
    # 当前工作目录
    print(os.getcwd())
    # 文件要保存的目录
    fpath = create_directory()
    # 切换到目标目录
    os.chdir(fpath)
    # 开始生成txt文件
    create_txt()