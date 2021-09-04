# Bilibili-videos-downloding-through-uploader
B站up主视频下载。输入up主id，获取其所有视频。然后选择全部下载，或者选择性下载。
使用了you-get库，python调用了os执行cmd代码
使用from you-get import common 结果报错，说是没有attribe 'buffer'
我去common源码，把那行代码注释掉，结果运行正常。
