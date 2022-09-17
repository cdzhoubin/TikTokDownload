#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:__init__.py
@Date       :2022/07/29 23:20:56
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:20:56 : Init
2022/08/16 18:34:27 : Add moudle Log
-------------------------------------------------
'''

import re
import os
import json
import time
import logging
import requests
import platform
import argparse
import configparser

from lxml import etree

from .Log import Log
from .Lives import Lives
from .Check import CheckInfo
from .Config import Config
from .Command import Command
from .Profile import Profile
from .Download import Download
from .Images import Images

# 日志记录
log = Log()

headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }

def replaceT(obj):
        """替换文案非法字符

        Args:
            obj (_type_): 传入对象

        Returns:
            new: 处理后的内容
        """
        if len(obj) > 80:
            obj = obj[:80]
        # '/ \ : * ? " < > |'
        reSub = r"[\/\\n\:\*\?\"\<\>\|]"
        new = []
        if type(obj) == list:
            for i in obj:
                # 替换为下划线
                retest = re.sub(reSub, "_", i)
                new.append(retest)
        elif type(obj) == str:
            new = eval(repr(obj).replace('\\', '_').replace('/','_').replace(':','_').replace('*','_').replace('?','_').replace('<','_').replace('>','_').replace('|','_').replace('"','_'))
            # 替换为下划线
            # new = re.sub(reSub, "_", obj, 0, re.MULTILINE)
        return new

print('''
  ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗
  ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
     ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
     ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
     ''')

print("#" * 120)
print(
        """
                                                TikTokDownload V1.3.0
        使用说明：
                1、本程序目前支持命令行调用和配置文件操作，GUI预览版本已经发布
                2、命令行操作方法：1）将本程序路径添加到环境变量
                                2）控制台输入 TikTokMulti -u https://v.douyin.com/jqwLHjF/

                3、配置文件操作方法：1）运行软件前先打开目录下 conf.ini 文件配置用户主页和音乐下载模式
                                2）按照控制台输出信息操作

                4、如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起
                5、GUI预览版本现已发布，操作更简单 https://github.com/Johnserf-Seed/TikTokDownload/tags 下载

        注意：  目前已经支持app内分享短链和web端长链识别。
        """
    )
print("#" * 120)
print('\r')

if (platform.system() == 'Windows'):
    sprit = '\\'
    # 💻
    print('[   💻   ]:Windows平台')
elif (platform.system() == 'Linux'):
    sprit = '/'
    # 🐧
    print('[   🐧   ]:Linux平台')
else:
    sprit = '/'
    # 🍎
    print('[   🍎   ]:MacOS平台')