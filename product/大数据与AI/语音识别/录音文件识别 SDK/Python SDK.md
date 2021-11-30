## 接入准备
### SDK获取
录音文件语音识别 Python SDK 获取，请参考： [Python SDK 安装及相关环境说明](https://cloud.tencent.com/document/sdk/Python)

### 接入须知
开发者在调用前请先查看录音文件语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37823)，了解接口的**使用要求**和**使用步骤**。

##  快速接入
以下分别是通过**语音 URL**和**本地语音上传**请求方式的 demo，以及**轮询接口**查询识别结果，来帮助客户快速接入。

1. 通过下面的录音文件识别请求中的两种接入方式的 demo快速请求，进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取 AppID、SecretId、SecretKey，并在代码中对应的位置配置好用户参数。
2. 然后在项目中使用以下的 demo，来快速获取识别结果。  


- **通过语音 URL 方式请求**

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.asr.v20190614 import asr_client, models 
import base64
import io 
import sys 
if sys.version_info[0] == 3:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#采用 URL 方式请求
try: 
    #重要，此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息，获取方法：
        #https://cloud.tencent.com/product/asr/getting-started
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "TC3-HMAC-SHA256"  
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 

    req = models.CreateRecTaskRequest()
    params = {"ChannelNum":1,"ResTextFormat":0,"SourceType":0}
    req._deserialize(params)
    req.EngineModelType = "16k_zh"
    req.Url = "https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav"
    resp = client.CreateRecTask(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 
```

- **通过本地语音上传方式请求**

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.asr.v20190614 import asr_client, models 
import base64
import io 
import sys 
if sys.version_info[0] == 3:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#本地文件方式请求
try: 
    #重要，此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息，获取方法：
        #https://cloud.tencent.com/product/asr/getting-started
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "TC3-HMAC-SHA256"  
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 
    #读取文件以及 base64
    #此处可以下载测试音频 https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav
    with open('./test16k.wav', "rb") as f:
        if sys.version_info[0] == 2:
            content = base64.b64encode(f.read())
        else:
            content = base64.b64encode(f.read()).decode('utf-8')

    req = models.CreateRecTaskRequest()
    params = {"ChannelNum":1,"ResTextFormat":0,"SourceType":1}
    req._deserialize(params)
    req.EngineModelType = "16k_zh"
    req.Data = content
    resp = client.CreateRecTask(req) 
    print(resp.to_json_string())

except TencentCloudSDKException as err: 
    print(err) 
```

- **查询录音文件识别结果**

```
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.asr.v20190614 import asr_client, models 
try: 
    #此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 

    req = models.DescribeTaskStatusRequest()
    params = '{"TaskId":123456}'
    req.from_json_string(params)

    resp = client.DescribeTaskStatus(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 
```
