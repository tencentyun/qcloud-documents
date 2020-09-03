## 接入准备
### SDK获取
录音文件语音识别 PHP SDK 获取，请参考： [PHP SDK 安装及相关环境说明](https://cloud.tencent.com/document/sdk/PHP)。

### 接入须知
开发者在调用前请先查看录音文件语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37823)，了解接口的**使用要求**和**使用步骤**。
## 快速接入

以下分别是通过**语音 URL** 和**本地语音上传**请求方式的 demo，来帮助客户快速接入。
1. 通过下面的录音文件识别请求中的两种接入方式的 demo快速请求，进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取 AppID、SecretId、SecretKey，并在代码中对应的位置配置好用户参数。
2. 然后在项目中使用以下的 demo，来快速获取识别结果。


- **通过语音 URL 方式请求**

```
<?php
require_once './tencentcloud-sdk-php/TCloudAutoLoader.php';  
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Asr\V20190614\AsrClient;
use TencentCloud\Asr\V20190614\Models\CreateRecTaskRequest;
//通过音频 URL 方式请求
try {
    //此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new CreateRecTaskRequest();
    
    $params = '{"EngineModelType":"16k_zh","ChannelNum":1,"ResTextFormat":0,"SourceType":0,"Url":"https://asr-audio-1300466766.cos.ap-nanjing.myqcloud.com/test16k.wav"}';
    $req->fromJsonString($params);

    $resp = $client->CreateRecTask($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

- **通过本地语音上传方式请求**

```
<?php
require_once './tencentcloud-sdk-php/TCloudAutoLoader.php';
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Asr\V20190614\AsrClient;
use TencentCloud\Asr\V20190614\Models\CreateRecTaskRequest;
//通过本地音频方式请求
try {
    //此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $clientProfile->setSignMethod("TC3-HMAC-SHA256");  
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new CreateRecTaskRequest();
    
    $params = '{"EngineModelType":"16k_zh","ChannelNum":1,"ResTextFormat":0,"SourceType":1}';
    $req->fromJsonString($params);
    $data = file_get_contents('./test.wav');
    $encodeData = base64_encode($data);
    $req->Data = $encodeData;
    $req->DataLen = strlen($data);

    $resp = $client->CreateRecTask($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```

- **查询识别结果**

```
<?php
require_once '../../../TCloudAutoLoader.php';
use TencentCloud\Common\Credential;
use TencentCloud\Common\Profile\ClientProfile;
use TencentCloud\Common\Profile\HttpProfile;
use TencentCloud\Common\Exception\TencentCloudSDKException;
use TencentCloud\Asr\V20190614\AsrClient;
use TencentCloud\Asr\V20190614\Models\DescribeTaskStatusRequest;
try {
    //此处<Your SecretId><Your SecretKey>需要替换成客户自己的账号信息
    $cred = new Credential("Your SecretId", "Your SecretKey");
    $httpProfile = new HttpProfile();
    $httpProfile->setEndpoint("asr.tencentcloudapi.com");
      
    $clientProfile = new ClientProfile();
    $clientProfile->setHttpProfile($httpProfile);
    $client = new AsrClient($cred, "ap-shanghai", $clientProfile);

    $req = new DescribeTaskStatusRequest();
    
    $params = '{"TaskId":123456}';
    $req->fromJsonString($params);


    $resp = $client->DescribeTaskStatus($req);

    print_r($resp->toJsonString());
}
catch(TencentCloudSDKException $e) {
    echo $e;
}
```
