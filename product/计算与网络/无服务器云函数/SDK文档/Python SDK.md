## 开发准备

安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey，SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 开发环境

Python 2.7 或者 3.6 版本

### 通过 pip 安装（推荐）

您可以通过 pip 安装方式将腾讯云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip 官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 安装。 通过 pip 方式安装请在命令行中执行以下命令：
```
pip install tencentcloud-sdk-python
```

### 通过源码包安装

前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python)下载最新代码，解压后运行以下命令：
```
$ cd tencentcloud-sdk-python
$ python setup.py install
```

## 接口列表

| 接口名称 | 接口功能                            |
| :--- | :------------------------------------ |
| [CreateFunction](https://cloud.tencent.com/document/api/583/18586)   | 创建函数          |
| [DeleteFunction](https://cloud.tencent.com/document/api/583/18585)   | 删除函数        |
| [GetFunction](https://cloud.tencent.com/document/api/583/18584)      | 获取函数详细信息   |
| [GetFunctionLogs](https://cloud.tencent.com/document/api/583/18583)  | 获取函数运行日志   |
| [Invoke](https://cloud.tencent.com/document/api/583/17243)           | 运行函数          |
| [ListFunctions](https://cloud.tencent.com/document/api/583/18582)    | 获取函数列表       |
| [UpdateFunctionCode](https://cloud.tencent.com/document/api/583/18581)  | 更新函数代码    |
| [UpdateFunctionConfiguration](https://cloud.tencent.com/document/api/583/18580)  | 更新函数配置|

## 示例

```
# -*- coding: utf8 -*-
import json
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models
from tencentcloud.scf.v20180416 import scf_client,models



# 对应接口的接口名
action = 'Invoke'

# 接口参数,输入需要调用的函数名，RequestResponse(同步) 和 Event(异步)
action_params = {
    'FunctionName': "test",
	'InvocationType': "Event"
}

print('Start Hello World function')

def main_handler(event, context):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential("用户的secretId", "用户的secretKey")

        # 实例化要请求产品的client对象，以及函数所在的地域
        client = scf_client.ScfClient(cred, "ap-guangzhou")

        # 调用接口，发起请求，并打印返回结果
        ret = client.call(action, action_params)
        
        print(json.loads(ret)["Response"]["Result"]["RetMsg"])

    except TencentCloudSDKException as err:
        print(err)
```

## 打包部署

如果需要在云函数控制台中部署函数，并使用 SDK 调用其他函数，则需要把 tencentcloud 的库和函数代码一起打包成 zip 文件；另外也可以在函数根目录下执行如下如下命令，把 SDK 下载安装到函数目录下。
```
pip install tencentcloud-sdk-python -t .
```

- 注意在控制台创建函数时的执行方法，需要和 zip 文件里的代码文件和执行函数对应。
- 最终生成的 zip 包如果大于50MB，需要通过 COS 上传。
- 云 API 默认限频为每秒20次，如果需要开大并发，可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&step=1) 申请。
