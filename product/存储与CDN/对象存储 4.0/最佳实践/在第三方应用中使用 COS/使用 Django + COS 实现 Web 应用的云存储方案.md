## 简介

[Django](https://www.djangoproject.com/) 是一个基于 Python 的开源 Web 应用框架，它的出现极大地简化了 Web 应用的开发过程。为了更好地满足现代 Web 应用的需求，Django 提供了很多扩展功能，其中包括云存储。

本文主要介绍如何使用 COS 插件实现远程附件功能，将 Django 应用的数据存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。


## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器（Cloud Virtual Machine，CVM）。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。


## 环境依赖

- Python 版本：大于等于3.8版本。
- Django 版本：大于等于2.2，小于3.3版本。


## 实践步骤


### 创建 COS 存储桶

1. 创建一个访问权限为**公有读私有写**的存储桶，存储桶的地域建议与运行 Django 的 CVM 地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
2. 在存储桶列表中找到刚刚创建的存储桶，并获取存储桶名称，例如 examplebucket-1250000000。


### 创建 Django

1. 前往 [PyCharm 官网](https://www.jetbrains.com.cn/en-us/pycharm/download/#section=windows)，并按照您所使用的系统选择对应的 PyCharm 版本。
2. 安装后打开 PyCharm，单击 NEW project 或者 create project，选择下面的 Django。
![](https://qcloudimg.tencent-cloud.cn/raw/837c3002f792d21b3783b21a3b522029.png)
3. 创建后，在您的目录下找到并打开 setting.py 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/1a83cc7bdc6be7434d01129c4be8498b.png)
将以下代码复制粘贴进去，并按照参数说明进行 COS 服务配置：
```
DEFAULT_FILE_STORAGE = "django_cos_storage.TencentCOSStorage"

TENCENTCOS_STORAGE = {
    "BUCKET": "xxx",
    "CONFIG": {
        "Region": "ap-guangzhou",
        "SecretId": "xxxx",
        "SecretKey": "xxxx",
    }
}
```
参数说明如下：
<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
   <tr>
      <td>Bucket</td>
      <td>创建存储桶时自定义的名称，例如 examplebucket-1250000000。</td>
   </tr>
   <tr>
      <td>Region</td>
      <td>创建存储桶时所选择的地域。</td>
   </tr>
   <tr>
      <td>SecretId</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。详情请参见 <a href="https://cloud.tencent.com/document/product/598/37140">子账号访问密钥管理</a>。</td>
   </tr>
   <tr>
      <td>SecretKey</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。详情请参见 <a href="https://cloud.tencent.com/document/product/598/37140">子账号访问密钥管理</a>。</td>
   </tr>
</table>



### 下载和配置 COS 插件

1. 前往 [Github](https://github.com/Tencent-Cloud-Plugins/tencentcloud-django-plugin-cos/archive/refs/heads/master.zip) 下载 COS 插件。下载后将 django_cos_storage 这个目录解压到 django 项目的目录下。
>?如需查看其插件信息，打开 terminal，输入 `pip freeze`，即可查看其模块信息。
2. 在 django_cos_storage 目录下创建一个 py 文件，例如 COSStorage.py。
![](https://qcloudimg.tencent-cloud.cn/raw/ace76b7266a81ddf589f2a99bf5938ca.png)
将以下代码复制粘贴进去：
```
from .storage import TencentCOSStorage
from functools import wraps

def  decorator(cls):

    instance = None
    @wraps(cls)
    def inner(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance=cls(*args,**kwargs)
        return  instance
    return inner

@decorator
class QFStorage:
    def __init__(self):
        pass
        self.storage =TencentCOSStorage()
        self.bucket =self.storage.bucket
        self.client =self.storage.client

    #上传对象
    def upload_file(self, Key, LocalFilePath, PartSize=1, MAXThread=5, EnableMD5=False):
        #
        try:
            response =self.client.upload_file(
                Bucket=self.bucket,
                Key=Key,
                LocalFilePath=LocalFilePath,
                PartSize=PartSize,
                MAXThread=MAXThread,
                EnableMD5=EnableMD5
            )
            return response
        except Exception as e:
            print('上传对象失败，error:',e)
            return None
```
3. 打开 app_cos 目录下的 views.py。
![](https://qcloudimg.tencent-cloud.cn/raw/7347d6d27e3859ba32d55ab75336dcbc.png)
将以下代码复制粘贴进去：
```
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django_cos_storage.COSStorage import QFStorage
from django.conf import settings


#上传对象

def upload_file_view(request):
    response=QFStorage().upload_file(
        Key='1.png',
        LocalFilePath=settings.BASE_DIR  /  'cessu/1.png'
    )

    if response:
        return HttpResponse('上传文件成功！')
    return HttpResponse('上传文件失败')
		
```
>!这里示例中 `cessu/1.png` 表示创建文件夹 cessu，然后将图片1.png 上传到 cessu 文件夹中。上传成功后，您可以在 COS 存储桶的 cessu 文件夹中找到图片1.png。

4. 在 djangoProject2 目录下找到并打开 urls.py。
![](https://qcloudimg.tencent-cloud.cn/raw/3c840d7cfba7de0f6fdc37f4f35fbd2d.png)
将代码复制粘贴进去：
```
from django.contrib import admin
from django.urls import path
from app_cos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
      
      path('upload_file/', upload_file_view),
      
]
```
5. 在 terminal 中输入 `python manage.py createsuperuser`，按照提示输入账号密码即可。
![](https://qcloudimg.tencent-cloud.cn/raw/c5f225fc5fff6f51e012c56214d34141.png)
6. 然后在 terminal 中输入 `python .\manage.py runserver` 运行。
![](https://qcloudimg.tencent-cloud.cn/raw/a9e65cd3a570e878b8233087e2009bde.png)
7. 打开网站`http://127.0.0.1:8000/admin/`，并输入刚才设置的账号密码即可完成登录。
![](https://qcloudimg.tencent-cloud.cn/raw/59400f143c74e5f6ccf27711f584121d.png)
>!若打开网站提示报错如下：
![](https://qcloudimg.tencent-cloud.cn/raw/570ee2254073f730691f5bc6f2449339.png)
返回 pycharm，重新打开 terminal，依次输入如下：
```
python manage.py makemigrations
python manage.py migrate
```
最后在 terminal 中输入 `python .\manage.py runserver` 运行，然后打开 `http://127.0.0.1:8000/admin/` 即可。


### 验证 Django 附件存储到 COS

1. 访问 `http://127.0.0.1:8000/upload_file`，完成上传文件操作。当提示如下图所示，则表示上传成功。
![](https://qcloudimg.tencent-cloud.cn/raw/149cbb07018a6c1c60e9dc0ac2e5f2cd.png)
2. 登录 COS 控制台，选择之前创建的存储桶，在 cessu 路径下即可看到已上传的图片。



## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！


