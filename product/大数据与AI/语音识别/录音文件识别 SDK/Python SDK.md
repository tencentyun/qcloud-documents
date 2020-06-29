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

#音频 URL 方式
try: 
    #此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "TC3-HMAC-SHA256"  
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 
    req = models.CreateRecTaskRequest()
    params = {"EngineModelType":"16k_0","ChannelNum":1,"ResTextFormat":0,"SourceType":0,"Url":"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav"}
    req._deserialize(params)
    resp = client.CreateRecTask(req) 
    print(resp.to_json_string()) 
    #windows 系统使用下面一行替换上面一行
    #print(resp.to_json_string().decode('UTF-8').encode('GBK') )

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

#本地音频方式
try: 
    #此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "TC3-HMAC-SHA256"  
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 


    #读取文件以及 base64
    fwave = open('./test.wav', mode='r')
    data = str(fwave.read())
    dataLen = len(data)
    base64Wav = base64.b64encode(data)

    req = models.CreateRecTaskRequest()
    params = {"EngineModelType":"16k_0","ChannelNum":1,"ResTextFormat":0,"SourceType":1,"Data":base64Wav,"DataLen":dataLen}
    req._deserialize(params)
    resp = client.CreateRecTask(req) 
    print(resp.to_json_string()) 
    #windows 系统使用下面一行替换上面一行
    #print(resp.to_json_string().decode('UTF-8').encode('GBK') )

except TencentCloudSDKException as err: 
    print(err) 

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
