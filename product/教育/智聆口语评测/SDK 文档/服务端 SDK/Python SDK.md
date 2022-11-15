## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。支持单词、句子和段落模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。
Tencent Cound API 3.0 SDK，封装了腾讯云的 SDK，通过集成 SDK，可以快速接入相关产品功能，如智聆口语评测，数学作业批改，英文作文批改。本文档介绍 [智聆口语评测](https://cloud.tencent.com/document/product/884/19309) 相关说明。

## 流程图
流程图请参见 [服务模式](https://cloud.tencent.com/document/product/884/33697)。 

## SDK 集成准备
1. 获取密钥
SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在 访问管理 > 访问密钥 > [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取该凭证。
>! 密钥属于敏感信息，正式密钥仅可在调试使用，线上环境情况下，为了防止他人盗取，推荐使用 [临时签名](https://cloud.tencent.com/document/product/884/31888#SecretKey)，具体请参考 [签名](https://cloud.tencent.com/document/product/884/31888#SecretKey) 相关内容。
>
![](https://qcloudimg.tencent-cloud.cn/raw/c0d190c71c0a47a54e5dbf4b1c6ce150.png)
2. 设备准备
准备一台电脑。


## SDK DEMO 使用流程
1. 安装依赖环境
安装 Python 2.7, 3.6-3.9 版本。
2. 获取安装
	- 通过 pip 安装：
通过 pip 方式安装或更新，在命令行执行以下命令：
```
pip install --upgrade tencentcloud-sdk-python
```
	- 通过下载 SDK 安装：
从 github 下载 [tencentcloud-sdk-python](https://github.com/TencentCloud/tencentcloud-sdk-python)。或者在终端输入 git 命令：
```
git clone https://github.com/TencentCloud/tencentcloud-sdk-python.git
```
如果无法使用 git 或不清楚如何使用，可以单击 [这里](https://github.com/TencentCloud/tencentcloud-sdk-python/archive/refs/heads/master.zip) 下载。
进入项目后运行 setup.py 进行安装：
```
cd tencentcloud-sdk-python
python setup.py install
```

3. 运行项目
进入 examples/soe/v20180903/init_oral_process.py，填入 SecretId 和 SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/298987df5c9ff3efc9c5238724546bf5.png)
填入请求参数，参考 [InitOralProcess](https://cloud.tencent.com/document/product/884/19319)，运行项目，进行评测。
![](https://qcloudimg.tencent-cloud.cn/raw/2fbfb05ad792fc0204880aef25b5a5cc.png)
获取评测结果，参考 [数据结构](https://cloud.tencent.com/document/product/884/19320)。


## SDK 使用方法
### 临时密钥（推荐）
客户端为了密钥安全性，需要考虑在服务端使用临时密钥，对密钥进行加密处理。python 临时密钥参考如下（填入密钥信息使用）：
```
# -*- coding: utf-8 -*-
# 获取联合身份临时访问凭证（https://cloud.tencent.com/document/api/598/13896）
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sts.v20180813 import sts_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "sts.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile
    client = sts_client.StsClient(cred, "ap-beijing", clientProfile)

    req = models.GetFederationTokenRequest()
    req.Name = "soe"
    req.Policy = "{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\",\"action\": [\"soe:TransmitOralProcessWithInit\"],\"resource\": \"*\"}}"

    # 请求服务，获取结果
    resp = client.GetFederationToken(req)
    json_resp = resp.to_json_string()

    # 输出json格式的字符串回包
    print(json_resp)

except TencentCloudSDKException as err:
    print(err)
```

### 内部签名（推荐）
#### 发音数据传输接口附带初始化过程(推荐)
[TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口使用示例。
采用语音输入模式：流式分片。
```
# -*- coding: utf-8 -*-
# 发音数据传输接口附带初始化过程（https://cloud.tencent.com/document/product/884/32605）
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.soe.v20180724 import soe_client, models
import base64
import uuid

try:
    file = ""  # 音频文件路径地址
    slice_num = 10 * 1024  # 分片大小， 1 * 1024即为1k
    SessionId = str(uuid.uuid1())  # 使用uuid作为请求SessionId

    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile
    client = soe_client.SoeClient(cred, "", clientProfile)

    # 读取音频文件
    with open(file, "rb") as f:
        content = f.read()
        content_len = len(content)

    # 分片数量计算
    pkg_num = content_len / slice_num + (content_len % slice_num != 0)
    # 开始分片并传输
    cur_pos = 0
    for j in range(int(pkg_num)):
        if j == int(pkg_num) - 1:
            send_content = content[cur_pos: content_len]
            cur_pos = content_len
            IsEnd = 1
        else:
            send_content = content[cur_pos: cur_pos + slice_num]
            cur_pos += slice_num
            IsEnd = 0
        base64_data = base64.b64encode(send_content).decode()

        # 请求参数赋值
        req = models.TransmitOralProcessWithInitRequest()
        req.SeqId = j + 1 
        req.IsEnd = IsEnd
        req.VoiceFileType = 3
        req.VoiceEncodeType = 1
        req.UserVoiceData = base64_data
        req.RefText = "red"
        req.WorkMode = 0
        req.EvalMode = 1
        req.ScoreCoeff = 1
        req.SessionId = SessionId
        # req.SoeAppId = ""
        req.StorageMode = 0
        req.SentenceInfoEnabled = 0
        req.ServerType = 0
        req.IsAsync = 0
        req.IsQuery = 0
        req.TextMode = 0

        # 请求服务，获取结果
        resp = client.TransmitOralProcessWithInit(req)
        json_resp = resp.to_json_string()

        # 输出json格式的字符串回包
        print(json_resp)

except TencentCloudSDKException as err:
    print(err)
```



#### 发音评估初始化和发音数据传输接口
[InitOralProcess](https://cloud.tencent.com/document/api/884/19319) 和 [TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318) 组合使用示例。
采用语音输入模式：一次性评估。
```
# -*- coding: utf-8 -*-
import base64

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.soe.v20180724 import soe_client, models
import uuid

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True  # 保持活动状态

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()  # 客户端配置文件
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True  # 未签署的有效负载
    clientProfile.httpProfile = httpProfile  # http选项
    client = soe_client.SoeClient(cred, "", clientProfile)  # 连接soe的连接

    # 发音评估初始化（https://cloud.tencent.com/document/product/884/19319）
    SessionId = str(uuid.uuid1())  # 使用uuid
    file = ""  # 音频文件路径地址

    # 请求参数赋值
    req = models.InitOralProcessRequest()  # 连接soe的评测初始化模块
    req.SessionId = SessionId
    req.RefText = "captain"
    req.WorkMode = 1
    req.EvalMode = 1
    req.ScoreCoeff = 1
    req.ServerType = 0
    req.IsAsync = 0
    req.TextMode = 0
    req.IsLongLifeSession = 0
    # 请求服务，获取结果
    resp = client.InitOralProcess(req)
    json_resp = resp.to_json_string()

    # 输出json格式的字符串回包
    print(json_resp)

    # 发音数据传输接口(https://cloud.tencent.com/document/api/884/19318)
    # 读取音频文件
    with open(file, "rb") as f:
        base64_data = base64.b64encode(f.read()).decode()
    tranreq = models.TransmitOralProcessRequest()
    tranreq.SeqId = 1
    tranreq.IsEnd = 1
    tranreq.VoiceFileType = 3
    tranreq.VoiceEncodeType = 1
    tranreq.UserVoiceData = base64_data
    tranreq.SessionId = SessionId
    tranreq.IsLongLifeSession = 1
    # req.SoeAppId = ""
    tranreq.IsQuery = 0

    # 请求服务，获取结果
    tranresp = client.TransmitOralProcess(tranreq)
    json_resp = tranresp.to_json_string()

    # 输出json格式的字符串回包
    print(json_resp)

except TencentCloudSDKException as err:
    print(err)
```



#### 关键词评测
[KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 接口使用示例。
采用语音输入模式：流式分片。
```
# -*- coding: utf-8 -*-
# 关键词评测（https://cloud.tencent.com/document/product/884/35587）
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.soe.v20180724 import soe_client, models
import base64
import uuid

try:
    file = ""  # 音频文件路径地址
    slice_num = 1 * 1024  # 分片大小， 1 * 1024即为1k
    SessionId = str(uuid.uuid1())  # 使用uuid作为请求SessionId

    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile
    client = soe_client.SoeClient(cred, "", clientProfile)

    # 读取音频文件
    with open(file, "rb") as f:
        content = f.read()
        content_len = len(content)

    # 分片数量计算
    pkg_num = content_len / slice_num + (content_len % slice_num != 0)
    # 开始分片并传输
    cur_pos = 0
    for j in range(int(pkg_num)):
        if j == int(pkg_num) - 1:
            send_content = content[cur_pos: content_len]
            cur_pos = content_len
            IsEnd = 1
        else:
            send_content = content[cur_pos: cur_pos + slice_num]
            cur_pos += slice_num
            IsEnd = 0
        base64_data = base64.b64encode(send_content).decode()

        req = models.KeywordEvaluateRequest()
        req.SeqId = j + 1
        req.IsEnd = IsEnd
        req.VoiceFileType = 3
        req.VoiceEncodeType = 1
        req.UserVoiceData = base64_data
        req.SessionId = SessionId
        # req.SoeAppId = ""
        req.IsQuery = 0
        req.Keywords = [
            {
                "RefText": 'red',
                "EvalMode": 0,
                "ServerType": 0,
                "TextMode": 0
            },
            {
                "RefText": '红色',
                "EvalMode": 1,
                "ServerType": 1,
                "TextMode": 0
            }
        ]
        # 请求服务，获取结果
        resp = client.KeywordEvaluate(req)
        json_resp = resp.to_json_string()

        # 输出json格式的字符串回包
        print(json_resp)

except TencentCloudSDKException as err:
    print(err)

```


### 外部签名（不推荐）
使用 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口演示。
1. 生成 curl。
```
# -*- coding: utf-8 -*-
import base64
import hashlib, hmac, json, os, sys, time
from datetime import datetime

# 密钥参数
secret_id = ""
secret_key = ""

# 评测参数，参考发音数据传输接口附带初始化过程（https://cloud.tencent.com/document/product/884/32605）
service = "soe"
host = "soe.tencentcloudapi.com"
endpoint = "https://" + host
region = "ap-guangzhou"
action = "TransmitOralProcessWithInit"
version = "2018-07-24"
algorithm = "TC3-HMAC-SHA256"
timestamp = int(time.time())
# timestamp = 1551113065
date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")

# ************* 步骤 1：拼接规范请求串 *************
http_request_method = "POST"
canonical_uri = "/"
canonical_querystring = ""
ct = "application/json; charset=utf-8"
payload = "{\"SeqId\": 1, \"IsEnd\": 1, \"VoiceFileType\": 3, \"VoiceEncodeType\": 1, \"UserVoiceData\": \"//MoxAALuN4gAUkwAYQh1xWKzZAAMDZPRAKCRiYoJEEP/c4jHPJk0zAGA02ghGPERnaPZARHP8f+BkQQ/CqjfIxQLhkl2RAz//MoxAwPgNqoAZp4ADtQSTWOF1F+AEmTEImdt6jsb6WhXxTCvtkfiVUSLYdfX7hHvulYVqRfAZ+XOecxF//ph/+HbmNezSs8//MoxAkO4Oq4y9pQACMIy2HqbczDokotX71inxey/+udQMhypprA6IdjTWZWb0/QeaAFihx9/dr6NrdmgLOhat/++GIFmkGq//MoxAgOOO7UAHvKcD4u3EwOF9XNMK99Nu9Malj/0ERAqKi6tqYOCnGMAYuPg4il3/+fNB4QBhqZkYLEFC36InsC0mtHtEHf//MoxAoNYPLQAIPScBN69jsHpVNf/FFkPLf/UQ5X6QoAgm+QLisHkaUGoJEMFc///21mX2f9aRil/+KtwSkZ0XEtUWAzE23n//MoxA8Q4OrAAHvecHuoXU9pmuMRsAAl5kxR+iGa25Xy5K5DZndk+5GjFi4ruA3Po3Y////6CJMIhNvYgUhIGXFlFdljblAF//MoxAYOOLcWXmrSTqAB3RCZhvPpqgorarEywEZfpMLiImr/EbP9oFSJ/tRkmWkyCqSB7////ZGIiBim4gD60h/bQ8PAPWCj//MoxAgNMK7dlGveTCGa8yD4Mq/3dFs2/HPQW1XSttIJyKLf22MNsUyxqRmPUuHgi0b////9eQ9wkusmAPBsncNhPkwKoUqn//MoxA4MyK7IAGteTC6OJRT0Ugvx6Ur7OCiUV3r9HnSoYlWVg6oBkf////vLEFNRFMnV8nAFvQwtRZv2MBA4/bybO662jmbd//MoxBUMWNrIAGvMcOK8QpNEgWIosuBaLtuJf9k8M////7UF2StBPfNK6hDgnRvqAyTP/SiQH8hU31/HJqzWg1N61Y0lmoYI//MoxB4NINbEAGvQcGCCb5XfJDJD///1PwmCwKnlG36HrNEa6iqFSihJgRArUoxkzNS9Nr7hnHzGj4peHNfx0dx3LDJ2SFjN//MoxCQMcMrEAIvMcFl0ir////A6xOIktb+mtyEzawnALISGYieXWnFQ5AFCGKxU3XkVteSTc2uUS0oUBAWA0eU+W/t/9QVD//MoxC0NKMa8KmIEcEDQPB2WBqDVr/8/52mU2Dx0NTL1rqQqpzzbAf/0iBIOu37LJ1HPQzcM7dkKXYXETT9ZXqET//UHZbrV//MoxDMMkN6QUNJEcCkoBAN01mbKkI1yPAyqjxXtZltKeAxYa4aAqf+eSGHFlLlKD6m2O9vnhi9qmO////s/+lVRTMnty4ke//MoxDsM0Dp4H1kQABcA/8JwUE/8ciCyT/8YceY5ETf/8RgchQJAcBKf/5OGEHIPMwJQTP//83QGHJdyTGHHmQP///yTJceB//MoxEIXmxqkAYdoAdL49B6EoTBLB4BaP////wtAwA80jQvqY+XDQvrKtXQiaPYkjALhtQTGjWUR4g9zGdfMjohS5vsRp3Xo//MoxB4UcuLQAYcoAb+onWzt9f+RhpFP7qevrbvcyIFMkVE+uYqgxxbzTrFaiZ27KGnYnMR+UYQwfHKYo78ih2r+1cO1qvRa//MoxAcNkp68AYIoAHv6P9ef7/qHBTqpfQWY1u230+YsSHE+2/2RH7SlnoAx0+tLJ/r6CcvMYWMVd9n66oKbdTGxwbruYXOO//MoxAsOchKQAYI4ACXC5rVY5PHD9jnod+arRqj5hL80xXnzl9f+sgPH/uPP/+3lHRircOlTv5Fm0l+qx+zHquq7CjCgJhQE//MoxAwNqSGQA8MQAEkzN/+hjPq1W//qygIlAICFKAnvBpZ0sWPCV1WCpU6DQ87/Ue6vyUGiwNVMQU1FMy45OS41VVVVVVVV\", \"SessionId\": \"test_1432543\", \"RefText\": \"bick sdfad\", \"WorkMode\": 1, \"EvalMode\": 1, \"ScoreCoeff\": 1}"
canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
signed_headers = "content-type;host"
hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
canonical_request = (http_request_method + "\n" +
                     canonical_uri + "\n" +
                     canonical_querystring + "\n" +
                     canonical_headers + "\n" +
                     signed_headers + "\n" +
                     hashed_request_payload)
print(canonical_request)

# ************* 步骤 2：拼接待签名字符串 *************
credential_scope = date + "/" + service + "/" + "tc3_request"
hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
string_to_sign = (algorithm + "\n" +
                  str(timestamp) + "\n" +
                  credential_scope + "\n" +
                  hashed_canonical_request)
print(string_to_sign)


# ************* 步骤 3：计算签名 *************
# 计算签名摘要函数
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
secret_service = sign(secret_date, service)
secret_signing = sign(secret_service, "tc3_request")
signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
print(signature)

# ************* 步骤 4：拼接 Authorization *************
authorization = (algorithm + " " +
                 "Credential=" + secret_id + "/" + credential_scope + ", " +
                 "SignedHeaders=" + signed_headers + ", " +
                 "Signature=" + signature)
print(authorization)

print('curl -X POST ' + endpoint
      + ' -H "Authorization: ' + authorization + '"'
      + ' -H "Content-Type: application/json; charset=utf-8"'
      + ' -H "Host: ' + host + '"'
      + ' -H "X-TC-Action: ' + action + '"'
      + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
      + ' -H "X-TC-Version: ' + version + '"'
      + ' -H "X-TC-Region: ' + region + '"'
      + " -d '" + payload + "'")
```

2. 根据签名信息，使用 requests 进行调用。
```
import requests

headers = {
    "Authorization": authorization,
    "Content-Type": "application/json; charset=utf-8",
    "Host": host,
    "X-TC-Action": action,
    "X-TC-Timestamp": str(timestamp),
    "X-TC-Version": version,
    "X-TC-Region": region
}

response = requests.post(url=endpoint, headers=headers, data=payload)

print(response.text)
```

## 参数说明
### 请求参数说明

| 接口名称 | 接口功能 | 
|---------|---------|
| [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 	| 发音数据传输接口附带初始化过程（常用实践）| 
| [InitOralProcess](https://cloud.tencent.com/document/api/884/19319)	| 发音评估初始化| 
| [KeywordEvaluate](https://cloud.tencent.com/document/api/884/35587) 	| 关键词评测| 
|[TransmitOralProcess](https://cloud.tencent.com/document/api/884/19318)	|发音数据传输接口|

### 返回结果说明
参考 API 文档 [数据结构](https://cloud.tencent.com/document/api/884/19320)。

## 错误码
参考 API 文档 [错误码](https://cloud.tencent.com/document/api/884/30658)。

## 常见问题
参考 [常见问题](https://cloud.tencent.com/document/product/884/32593)。 

## 附录
Web SDK 和 Python SDK 交互使用。使用 flask 框架演示。
使用依赖：
```
tencentcloud-sdk-python
flask
flask_cors
gevent
```

### TransInitUrl 接口
```
import json
from flask import Flask, request, render_template
from flask_cors import CORS
from gevent import pywsgi

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

app = Flask(__name__)

CORS(app)  # 允许跨域


@app.route("/TransInitUrl", methods=["POST"])
def TransInitUrl():
    request_json = request.json

    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential("", "")

        # 实例化一个http选项，可选的，没有特殊需求可以跳过。
        httpProfile = HttpProfile()
        httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
        httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
        httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

        # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
        clientProfile.unsignedPayload = True
        clientProfile.httpProfile = httpProfile

        from tencentcloud.soe.v20180724 import soe_client, models
        client = soe_client.SoeClient(cred, "", clientProfile)

        req = models.TransmitOralProcessWithInitRequest()
        req.SeqId = request_json['SeqId']
        req.IsEnd = request_json['IsEnd']
        req.VoiceFileType = request_json['VoiceFileType']
        req.VoiceEncodeType = request_json['VoiceEncodeType']
        req.UserVoiceData = request_json['UserVoiceData']
        req.RefText = request_json['RefText']
        req.WorkMode = request_json['WorkMode']
        req.EvalMode = request_json['EvalMode']
        req.ScoreCoeff = request_json['ScoreCoeff']
        req.SessionId = request_json['SessionId']
        req.ServerType = request_json['ServerType']
        req.TextMode = request_json['TextMode']

        # 请求服务，获取结果
        resp = client.TransmitOralProcessWithInit(req)
        json_resp = resp.to_json_string()

        json_load = json.loads(json_resp)
        # SDK 封装了返回结果。此处需要加上Response
        new_dict = {
        "Response": json_load
        }
        json_dumps = json.dumps(new_dict)

        return json_dumps

    except TencentCloudSDKException as err:
        return err

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 9000), app)
    server.serve_forever()
```


### getAuthorization 接口
```
import json
from flask import Flask, request, render_template
from flask_cors import CORS
from gevent import pywsgi

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

app = Flask(__name__)

CORS(app)  # 允许跨域

@app.route("/getAuthorization", methods=["GET"])
def getAuthorization():
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential("", "")

        # 实例化一个http选项，可选的，没有特殊需求可以跳过。
        httpProfile = HttpProfile()
        httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
        httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
        httpProfile.endpoint = "sts.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

        # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
        clientProfile.unsignedPayload = True
        clientProfile.httpProfile = httpProfile

        from tencentcloud.sts.v20180813 import sts_client, models
        client = sts_client.StsClient(cred, "ap-guangzhou", clientProfile)

        req = models.GetFederationTokenRequest()
        req.Name = "soe"
        req.Policy = "{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\",\"action\": [\"soe:TransmitOralProcessWithInit\"],\"resource\": \"*\"}}"
        # req.DurationSeconds = 10
        # 请求服务，获取结果
        resp = client.GetFederationToken(req)
        json_resp = resp.to_json_string()
        json_loads = json.loads(json_resp)
        # json_dumps = json.dumps(json_loads)

        return json_loads

    except TencentCloudSDKException as err:
        return err

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 9000), app)
    server.serve_forever()

```



