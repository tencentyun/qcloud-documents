## 接入准备
### SDK获取
一句话语音识别 PHP SDK 安装及相关环境说明 [PHP SDK 安装及相关环境说明>>](https://cloud.tencent.com/document/sdk/PHP)

### 接入须知
开发者在调用前请先查看一句话语音识别的[ 接口说明]()，了解接口的**使用要求**和**使用步骤**。
## 快速接入

以下分别是通过**语音URL**和**本地语音上传**请求方式的demo，来帮助客户快速接入。

+ **通过语音URL方式请求**

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
    //重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    //请参考接口说明中的使用步骤1进行获取。 
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new SentenceRecognitionRequest();
    
    $params = '{"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k","SourceType":0,"Url":"http://ttsgz-1255628450.cos.ap-guangzhou.myqcloud.com/20190813/cbf318cd-273e-4b7c-bab0-50a1885c9b96.wav","VoiceFormat":"wav","UsrAudioKey":"session-123"}';
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
    //重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    //请参考接口说明中的使用步骤1进行获取。 
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new SentenceRecognitionRequest();
    
    $params = '{"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k","SourceType":1,"Url":"","VoiceFormat":"wav","UsrAudioKey":"session-123"}';
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
