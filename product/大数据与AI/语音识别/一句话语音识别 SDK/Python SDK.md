## 接入准备
### SDK获取
一句话识别 Python SDK 获取，请参考：[Python SDK 依赖环境及获取安装说明 ](https://cloud.tencent.com/document/sdk/Python)。
### 接入须知
开发者在调用前请先查看一句话语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的**使用要求**和**使用步骤**。

##  快速接入
以下分别是通过**语音 URL** 和**本地语音上传**请求方式的 demo，来帮助用户快速接入。  

+ **通过语音 URL 方式请求**

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
    #发送请求
    req = models.SentenceRecognitionRequest()
    params = {"ProjectId":0,"SubServiceType":2,"SourceType":0,"UsrAudioKey":"session-123"}
    req._deserialize(params)
    req.EngSerViceType = "16k_zh"
    req.VoiceFormat = "wav"
    req.Url = "https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav"
    resp = client.SentenceRecognition(req) 
    print(resp.to_json_string()) 

    #windows 如果是 GBK 编码则用下面 print 语句替换上面 print 语句
    #print(resp.to_json_string().decode('UTF-8').encode('GBK') )

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
    #发送请求
    req = models.SentenceRecognitionRequest()
    params = {"ProjectId":0,"SubServiceType":2,"SourceType":1,"UsrAudioKey":"session-123"}
    req._deserialize(params)
    req.DataLen = len(content)
    req.Data = content
    req.EngSerViceType = "16k_zh"
    req.VoiceFormat = "wav"
    resp = client.SentenceRecognition(req) 
    print(resp.to_json_string()) 

    #windows 如果是 GBK 编码则用下面 print 语句替换上面 print 语句
    #print(resp.to_json_string().decode('UTF-8').encode('GBK') )

except TencentCloudSDKException as err: 
    print(err) 
```
