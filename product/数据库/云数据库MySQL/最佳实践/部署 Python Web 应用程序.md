Django 是一个开放源代码的 Web 应用框架，由 Python 写成。
本教程指导如何部署默认 Django 网站至运行 Python 2.7 的云服务器。

使用的软件环境为：CentOS7.2 | Python2.7 | Django1.11

### 步骤1：登录到云服务器实例
云服务器的购买和访问请参见 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

### 步骤2：安装 Python
在 CentOS 中会默认安装 Python，您可通过`python --version`查看 Python 版本。

### 步骤3：安装 Django
1. 安装 pip。
```
yum install python-pip 
```
2. 更新 pip 包。
```
pip install --upgrade pip
```
2. 通过 pip 安装 Django。
```
pip install Django==1.11
```
3. 查看 Django 版本，测试 Django 是否安装完成。
```
python # 进入python命令行
>>> import django
>>> django.VERSION
```

### 步骤4：安装 MySQLdb 模块
安装 MySQL 的支持模块。
```
yum install python-devel
yum install mysql-devel
yum -y install mysql-devel libxml2 libxml2-dev libxslt* zlib gcc openssl
yum install gcc libffi-devel python-devel openssl-devel
pip install MySQL-python
```

### 步骤5：安装 Apache 服务
1. 在云服务器实例中使用`yum`安装 Apache。
```
yum install httpd -y
```
2. 启动 Apache 服务。
```
service httpd start
```
3. 测试 Apache。
>!此步骤需要您的云服务器在安全组中配置来源为 **all**，端口协议为 **TCP:80** 的入站规则。关于安全组的配置方法请参见 [安全组操作](https://cloud.tencent.com/document/product/213/12452)。
>
在您本地的浏览器中输入`http://xxx.xxx.xxx.xxx/`（其中`xxx.xxx.xxx.xxx`为您的云服务器公网 IP 地址），出现下列画面表示 Apache 启动成功。
![](https://main.qcloudimg.com/raw/a8708d09de9280c730f47eb8289f7c47.png)

### 步骤6：安装 Apache 的 mod_wsgi 拓展作为 Django 的应用容器
1. 安装 httpd-devel。
```
yum install -y httpd-devel
```
2. 安装 mod_wsgi。
```
yum install -y mod_wsgi
```

### 步骤7：创建项目测试 Django 环境
1. 在`/usr/local`下创建测试项目，运行`django-admin.py startproject projectname`来创建一个项目，其中 projectname 为项目名。
```
cd /usr/local
django-admin.py startproject projectname
```
2. 在**项目根目录**中新建文件`django.wsgi`作为 Apache 支持。
```
cd /usr/local/projectname
vim django.wsgi
```
3. 在`django.wsgi`中输入以下内容。
```
import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '.'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectname.settings'
application = get_wsgi_application()
```
4. 添加 Apache 支持，在`httpd.conf`添加如下内容，`httpd.conf`的路径为`/etc/httpd/conf/httpd.conf`。
```
LoadModule wsgi_module modules/mod_wsgi.so
WSGIScriptAlias /python "/usr/local/projectname/django.wsgi"
<Directory "/usr/local/projectname">
    AllowOverride None
    Options None
    Require all granted
</Directory>
<Directory "/usr/local/projectname">
    AllowOverride None
    Options None
    Require all granted
</Directory>
```
5. 创建视图，在**项目目录**`/usr/local/projectname/projectname`下创建`view.py`文件作为访问入口，内容如下。
```
from django.http import HttpResponse
def hello(request):
       return HttpResponse("Hello world ! ")
```
6. 配置 URL，配置**项目目录**`/usr/local/projectname/projectname`下的`urls.py`文件，删除原来的内容，添加内容如下。
```
from django.conf.urls import *
from projectname.view import hello
urlpatterns = [
    url(r'^hello/$',hello),
]
```
7. 修改**项目目录**`/usr/local/projectname/projectname`下的`settings.py`文件。
```
ALLOWED_HOSTS = ['*']
```
8. 重启 Apache 服务。
```
service httpd restart
```
9. 在您本地的浏览器中输入`http://xxx.xxx.xxx.xxx/python/hello`（其中`xxx.xxx.xxx.xxx`为您的云服务器公网 IP 地址），页面出现 “Hello world !” 表示项目环境搭建成功。

### 步骤8：在 Django 中配置 TencentDB（可选）
1. 配置项目目录下的`settings.py`文件。
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root', # TencentDB 账户名
        'PASSWORD': '123456', # TencentDB 账户密码
        'HOST': '0.0.0.0', # TencentDB 内网地址
        'PORT': '3306', # TencentDB 端口
    }
}
```
2. 配置完成后可以使用以下命令测试数据库连接。
```
$python manage.py validate/check
```
3. 测试通过即可进行数据库操作，更多的数据库操作请参见 [模型和数据库](https://docs.djangoproject.com/en/1.11/topics/db/)。
