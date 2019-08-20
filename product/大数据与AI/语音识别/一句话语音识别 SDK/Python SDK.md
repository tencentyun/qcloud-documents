## 接入准备
### SDK获取
一句话语音识别 Python SDK 安装及相关环境说明 [Python SDK 安装及相关环境说明>>](https://cloud.tencent.com/document/sdk/Python)

### 接入须知
开发者在调用前请先查看一句话语音识别的[ 接口说明]()，了解接口的**使用要求**和**使用步骤**。

##  快速接入
以下分别是通过**语音URL**和**本地语音上传**请求方式的demo，来帮助客户快速接入。

+ **通过语音URL方式请求**

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.asr.v20190614 import asr_client, models 
import base64

//通过语音URL方式调用
try: 
    #重要：Your SecretId、Your SecretKey需要替换成客户自己的账号信息
    #请参考接口说明中的使用步骤1进行获取。 
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 

    #发送请求
    req = models.SentenceRecognitionRequest()
    params = {"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k","SourceType":0,"Url":"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav","VoiceFormat":"wav","UsrAudioKey":"session-123"}
    req._deserialize(params)
    resp = client.SentenceRecognition(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 
```

+ **通过本地语音上传方式请求**

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.asr.v20190614 import asr_client, models 
import base64

//通过本地语音上传方式调用    
try: 
    
    #重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    #请参考接口说明中的使用步骤1进行获取。 
    cred = credential.Credential("Your SecretId", "Your SecretKey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile) 

    #读取文件以及base64
    fwave = open('./test.wav', mode='r')
    data = str(fwave.read())
    dataLen = len(data)
    base64Wav = base64.b64encode(data)

    #发送请求
    req = models.SentenceRecognitionRequest()
    params = {"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k","SourceType":1,"Url":"","VoiceFormat":"wav","UsrAudioKey":"session-123", "Data":base64Wav, "DataLen":dataLen}
    req._deserialize(params)
    resp = client.SentenceRecognition(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 
```
