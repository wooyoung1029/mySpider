## 项目信息
网络爬虫
参考地址： https://www.runoob.com/w3cnote/scrapy-detail.html

## windows下安装 Scrapy
1.首先下载scrapy的whl包：http://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载Scrapy‑1.3.3‑py2.py3‑none‑any.whl

2.没有安装过wheel库的请先安装pip install wheel

3.scrapy依赖twiste，进入http://www.lfd.uci.edu/~gohlke/pythonlibs/ 找到适合的版本，下载Twisted‑17.1.0‑cp36‑cp36m‑win_amd64.whl

4.scrapy依赖lxml包，pip install lxml

5.在下载存放的目录下安装pip install Twisted-17.1.0-cp36-cp36m-win_amd64.whl 

6.在下载存放的目录下安装pip install Scrapy-1.3.3-py2.py3-none-any.whl

7.验证，输入scrapy -h，显示版本号，即成功！

## 异常处理
pip install win32api
