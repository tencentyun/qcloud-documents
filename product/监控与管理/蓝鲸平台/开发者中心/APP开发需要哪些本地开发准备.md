开发前准备包括：安装python、Mysql等开发环境的配置； APP开发样例下载；配置host。
##1.开发环境配置
1)安装python

2)安装Mysql

3)安装 setuptools-0.6c11.win32-py2.7.exe和MySQL-python-1.2.3.win32-py2.7.exe

4)安装python库，包括django1.3、south、httplib2等

5)安装本地开发工具，windows环境下推荐使用Eclipse进行代码开发、使用TortoiseSVN管理SVN

##2.从svn中检出（checkout）代码
1)将APP从SVN仓库中检出到本地目录中

2)将APP样例的代码拷贝到到APP本地目录中

3)配置修改：

A.config/settings_develop.py 文件中DATABASES 项中：填写本地数据库的相关信息

B.本地使用Eclipse开发时，工程的启动端口默认为8000，如使用其他端口在config/settings_develop.py 文件中S_URL 项中：修改工程的启动端口

![图1](https://mccdn.qcloud.com/img562079eb430d6.png)
##3.host配置
在hosts中配置```127.0.0.1 app.o.qcloud.com```

1)windows下host配置

C:\Windows\System32\drivers\etc\hosts文件中添加```127.0.0.1 app.o.qcloud.com```

2)linux下host配置

/etc/hosts 文件中添加```127.0.0.1 app.o.qcloud.com```
