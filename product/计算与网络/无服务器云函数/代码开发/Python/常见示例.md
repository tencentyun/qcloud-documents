常见示例中包含了 Python 环境下可以试用的相关代码片段，您可以根据需要选择尝试。示例均基于 Python 3.6 环境提供。

您可从 github 项目 [scf-python-code-snippet](https://github.com/awesome-scf/scf-python-code-snippet) 中获取相关代码片段并直接部署。

## 环境变量读取

本示例提供了获取全部环境变量列表，或单一环境变量值的方法。

```
# -*- coding: utf8 -*-
import os
		
def main_handler(event, context):
      print(os.environ)
      print(os.environ.get("SCF_RUNTIME"))
      return("Hello World")
```

## 本地时间格式化输出

本示例提供了时间格式化输出方法，按指定格式进行日期和时间输出。

SCF 环境默认是 UTC 时间，如果期望按北京时间输出，可以为函数添加 `TZ=Asia/Shanghai` 环境变量。

```
# -*- coding: utf8 -*-
import time
		
def main_handler(event, context):
      print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))   
      return("Hello World")
```

## 函数访问 MySQL 数据库

本示例使用了 PyMySQL 库来进行数据库连接，在项目目录下需要执行 `pip3 install PyMySQL -t .` 命令完成依赖库安装。

在使用本示例时：

* 需要注意函数网络配置，将函数网络配置到 MySQL 数据库所在的 VPC 中，确保网络可达。
* 根据数据库具体情况，修改代码中的数据库连接 IP、用户名、密码、数据库名等信息。


```
# -*- coding: utf8 -*-
import pymysql

def main_handler(event, context):
        
       # 打开数据库连接
       db = pymysql.connect(host="host ip",port=3306,user="user",password="password",database="db name")
    
       # 使用 cursor() 方法创建一个游标对象 cursor
       cursor = db.cursor()
    
       # 使用 execute()  方法执行 SQL 查询 
       cursor.execute("SELECT VERSION()")
    
       # 使用 fetchone() 方法获取单条数据.
       data = cursor.fetchone()
    
       print ("Database version : %s " % data)
    
       # 关闭数据库连接
       db.close()
    
```

## 函数内发起网络连接

本示例使用了 requests 库在函数内发起网络连接，获取页面信息。可以通过在项目目录下执行 `pip3 install requests -t .` 命令完成依赖库安装。

```
# -*- coding: utf8 -*-
import requests
	

def main_handler(event, context):
      addr = "https://cloud.tencent.com"    
      resp = requests.get(addr)
      print(resp)
      print(resp.text)
      return resp.status_code

```


## 函数 + API 网关返回网页

通过配置 API 网关触发器并启用集成响应，可以实现 API 网关 URL 访问时获取 html 页面。

```
# -*- coding: utf8 -*-
import time

def main_handler(event, context):
      resp = {
          "isBase64Encoded": False,
          "statusCode": 200,
          "headers": {"Content-Type":"text/html"},
          "body": "<html><body><h1>Hello</h1><p>Hello World.</p></body></html>"
      }  
      return resp
```

## 函数 + API 网关返回图片

通过配置 API 网关触发器并启用集成响应，可以实现 API 网关 URL 访问时获取到二进制图片文件。


```
# -*- coding: utf8 -*-
import base64

def main_handler(event, context):
       with open("tencent_cloud_logo.png","rb") as f:
           data = f.read()
       base64_data = base64.b64encode(data)    
       base64_str = base64_data.decode('utf-8')
       resp = {
           "isBase64Encoded": True,
           "statusCode": 200,
           "headers": {"Content-Type":"image/png"},
           "body": base64_str
       }
       return resp
```

