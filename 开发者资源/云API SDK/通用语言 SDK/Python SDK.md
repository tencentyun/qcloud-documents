## 简介
* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。
* 本文以 Python SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* Python 2.7，3.6至3.9版本。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/78145f9e6a830a188304991552a5c614.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。



## 安装 SDK
可通过 pip 安装方式将腾讯云 Python SDK 安装至您的项目中。若您的项目环境未安装 pip，请前往 [pip 官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 完成安装。
在命令行中执行以下命令，安装 Python SDK。

```python
pip install tencentcloud-sdk-python
```
>! 若同时具备 python2 及 python3 环境，则需使用 pip3 命令进行安装。

中国大陆地区的用户可以使用国内镜像源提高下载速度。如果仅使用国内源，则可使用`-i`参数指定。示例如下：
```python
# 以腾讯源为例 
# 源地址后为所要安装的包：tencentcloud-sdk-python
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
```


## 使用 SDK

### 示例1：查询可用区
以 [查询可用区](https://cloud.tencent.com/document/product/213/15728) 接口为例，创建`HelloWorld.py`文件并写入以下代码：
```python
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的 client models。
from tencentcloud.cvm.v20170312 import cvm_client, models

# 导入可选配置项
from tencentcloud.common.profile import client_profile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")
    
    # 实例化要请求产品 (以 cvm 为例) 的 client 对象
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过 client 对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出 json 格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
```
在命令行中进入`HelloWorld.py`文件所在目录，执行以下命令，即可获取所需内容。
```
python HelloWorld.py
```



### 示例2：查询实例列表
以 [查询实例列表](https://cloud.tencent.com/document/product/213/15707) 接口为例，创建`HelloWorld.py`文件并写入以下代码：
```python
# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的 client models。
from tencentcloud.cvm.v20170312 import cvm_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey, 此处还需注意密钥对的保密
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个 http 选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "GET"  # get 请求 (默认为 post 请求)
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒 (默认60秒)
    httpProfile.endpoint = "cvm.ap-shanghai.tencentcloudapi.com"  # 指定接入地域域名 (默认就近接入)

    # 实例化一个 client 选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"  # 指定展示英文（默认为中文）
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品 (以 cvm 为例) 的 client 对象，clientProfile 是可选的。
    client = cvm_client.CvmClient(cred, "ap-shanghai", clientProfile)

    # 实例化一个 cvm 实例信息查询请求对象,每个接口都会对应一个 request 对象。
    req = models.DescribeInstancesRequest()

    # 填充请求参数,这里 request 对象的成员变量即对应接口的入参。
    # 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义。
    respFilter = models.Filter()  # 创建 Filter 对象, 以 zone 的维度来查询 cvm 实例。
    respFilter.Name = "zone"
    respFilter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
    req.Filters = [respFilter]  # Filters 是成员为 Filter 对象的列表

    # 这里还支持以标准 json 格式的 string 来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    params = '''{
        "Filters": [
            {
                "Name": "zone",
                "Values": ["ap-shanghai-1", "ap-shanghai-2"]
            }
        ]
    }'''
    req.from_json_string(params)

    # 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的。
    # 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应。
    resp = client.DescribeInstances(req)

    # 输出 json 格式的字符串回包
    print(resp.to_json_string(indent=2))

    # 也可以取出单个值。
    # 您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义。
    print(resp.TotalCount)

except TencentCloudSDKException as err:
    print(err)
```
在命令行中进入`HelloWorld.py`文件所在目录，执行以下命令，即可获取所需内容。
```
python HelloWorld.py
```


### 更多示例
您可以在 [github](https://github.com/tencentcloud/tencentcloud-sdk-python) 中的`examples`目录下获取更多详细的示例。




## 相关配置

### 代理

如果是有代理的环境下，可通过以下两种方式设置代理：

- 在初始化 HttpProfile 时指定 proxy，参考 [example](https://github.com/TencentCloud/tencentcloud-sdk-python/blob/master/examples/cvm/v20170312/describe_zones.py)。
- 需要设置系统环境变量`https_proxy`。

否则可能无法正常调用，抛出连接超时的异常。

## 常见问题
### 证书问题

在 Mac 操作系统安装 Python 3.6 或以上版本时，可能会遇到证书错误：`Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).`。

这是因为在 Mac 操作系统下，Python 不再使用系统默认的证书，且本身也不提供证书。在进行 HTTPS 请求时，需要使用`certifi`库提供的证书，但 SDK 不支持指定，所以只能使用`sudo "/Applications/Python 3.6/Install Certificates.command"`命令安装证书才能解决此问题。

虽然 Python 2 版本不应该有上述问题，但在个别用户环境上可能也会存在类似的情况，同样可以通过`sudo /Applications/Python 2.7/Install Certificates.command`解决。



