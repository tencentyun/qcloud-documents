## 接入准备
### SDK获取
一句话识别 PHP SDK 获取，请参考：[PHP SDK 依赖环境及获取安装 ](https://cloud.tencent.com/document/sdk/PHP)。

### 接入须知
开发者在调用前请先查看一句话语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37308)，了解接口的**使用要求**和**使用步骤**。

## 快速接入

以下分别是通过**语音 URL** 和**本地语音上传**请求方式的 demo，来帮助用户快速接入。

+ **通过语音 URL 方式请求**

```
<?php
require_once './tencentcloud-sdk-php/TCloudAutoLoader.php';  
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Asr\V20190614\AsrClient;
use TencentCloud\Asr\V20190614\Models\SentenceRecognitionRequest;

//通过语音URL方式调用
try {
    //重要：<Your SecretId>、<Your SecretKey>需要替换成用户自己的账号信息
    //请参考接口说明中的使用步骤1进行获取。 
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new SentenceRecognitionRequest();
    
    $params = '{"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k_zh","SourceType":0,"Url":"https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav","VoiceFormat":"wav","UsrAudioKey":"session-123"}';
    $req->fromJsonString($params);


    $resp = $client->SentenceRecognition($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

+ **通过本地语音上传方式请求**

```
<?php
require_once './tencentcloud-sdk-php/TCloudAutoLoader.php';
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Asr\V20190614\AsrClient;
use TencentCloud\Asr\V20190614\Models\SentenceRecognitionRequest;
    
//通过本地语音上传方式调用
try {
    //重要：<Your SecretId>、<Your SecretKey>需要替换成用户自己的账号信息
    //请参考接口说明中的使用步骤1进行获取。 
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new SentenceRecognitionRequest();
    
    $params = '{"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k_zh","SourceType":1,"Url":"","VoiceFormat":"wav","UsrAudioKey":"session-123"}';
    $req->fromJsonString($params);
    $data = file_get_contents('./test.wav');
    $encodeData = base64_encode($data);
    $req->Data = $encodeData;
    $req->DataLen = strlen($data);

    $resp = $client->SentenceRecognition($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```
