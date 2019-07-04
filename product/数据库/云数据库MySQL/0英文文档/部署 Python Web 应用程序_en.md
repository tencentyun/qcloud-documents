Django is a Web application framework for open source code written in Python.
This tutorial shows how to deploy the default Django website to the CVM that Python 2.7 runs on.

Supported software environment: CentOS7.2 | Python2.7  | Django1.11.


### Logging in to CVM Instance
For more information on purchase and access of CVM, please see [Quick Start for Linux CVM](https://cloud.tencent.com/document/product/213/2936).

### Installing Python
Python is installed in CentOS by default. You can view Python version in `"Python" -> "Version"`.

### Installing Django
1. Install pip.
```
yum install python-pip -y
```
2. Install Django by pip.
```
pip install Django
```
3. View Django version to test whether Django is installed.
```
python # Enter the Python command line
>>> import django
>>> django.VERSION
```

### Installing MySQLdb Module
Install the supporting modules of MySQL.
```
yum install python-devel
yum install mysql-devel
pip install MySQL-python
```

### Installing Apache Service
1. Use `yum` to install Apache in the CVM instance.
```
yum install httpd -y
```
2. Start Apache service.
```
service httpd start
```
3. Test Apache.
>**Note:**
In this step, you must configure the source as **all** and the port protocol as **TCP:80** inbound rule for your CVM in the security group. For more information on how to configure the security group, please see [Security Group](https://cloud.tencent.com/document/product/213/5221).

Enter `http://115.xxx.xxx.xxx/` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM). The appearance of the following screen indicates Apahce has started successfully.
![](//mc.qcloudimg.com/static/img/3cde70e76a386b81f96ea9919280269d/image.png)

### Installing Apache's "mod_wsgi" Extension as Application Container for Django
1. Install httpd-devel.
```
yum install -y httpd-devel
```
2. Install mod_wsgi.
```
yum install -y mod_wsgi
```
3. Add the following content in httpd.conf file whose path is `/etc/httpd/conf/httpd.conf`.
```
LoadModule  wsgi_module modules/mod_wsgi.so
```

### Creating a Project to Test Django Environment
1. Create a test project under /usr/local, and run `django-admin.py startproject projectname` to create a project. "projectname" refers to the name of the created project.
```
cd /usr/local
django-admin.py startproject testProject
```
2. Create a new file "django.wsgi" in the project's root directory as Apache support.
```
cd /usr/local/testProject
vim django.wsgi
```
3. Enter the following content in django.wsgi.
```
import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectname.settings'
application = get_wsgi_application()
```
4. Add support in Apache.
```
WSGIScriptAlias /python "/usr/local/testProject/django.wsgi"
```
5. Create a view and view.py file in the project directory as the access entry. Details are shown below:
```
from django.http import HttpResponse
def hello(request):
 return HttpResponse("Hello world ! ")
```
6. Configure the URL and urls.py file in the project directory. Delete the original content and add the following content.
```
from django.conf.urls import *
form testProject.view import hello
urlpatterns = [
    url(r'^hello/$',hello),
]
```
7. Restart Apache service.
```
service httpd restart
```
8. Enter `http://115.xxx.xxx.xxx/python/hello` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM). The appearance of the "Hello world!" page indicates the project environment has been built successfully.

### Configuring CDB in Django (Optional)
1. Configure settings.py file in the project directory.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root', # CDB account name
        'PASSWORD': '123456', # CDB account password
        'HOST': '0.0.0.0', # CDB private IP
        'PORT': '3306', # CDB port
    }
}
```
2. Use the following command to test the database connection after configuration.
```
$python manage.py validate/check
```
3. You can perform operations on the database after it is tested. For more database operations, please see [Models and Databases](https://docs.djangoproject.com/en/1.11/topics/db/).

