## 概述

即时通讯是目前最流行的网上通讯方式之一，云上的即时通讯服务也是层出不穷，很多用户会使用即时通讯产品开发实现自己的聊天业务。

对象存储推出的内容安全管理能力，可以帮助用户实现识别即时通讯业务中的安全问题，当发送出来的消息属于违规内容时，则不允许发送。

整体流程如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/0577e5fa1b21886947fbb795b38dd0cc.png)

安全管理主要在步骤3、4、5。
- 步骤3表示发送请求对消息内容进行识别。
- 步骤4表示返回处理结果。
- 步骤5表示根据结果判断是否发送消息或是否撤回、删除消息。

实际聊天效果如下图：
- 发送端
![img](https://main.qcloudimg.com/raw/5bb14cd8a5a044c98a10d18952c31a02.png)
- 接收端
![img](https://main.qcloudimg.com/raw/265483ac6d58db9fee497a89dc748da1.png)


## 准备工作

### 1. 入门一款常用的即时通讯产品

按照以下文档说明完成**登录**、**获取 SDKAppID 及密钥信息**、**创建应用**、**下载 DEMO 源码**、 **配置密钥**、**编译运行（部分平台需要）**操作。

- 通用 Demo 入门教程，请参见 [一分钟跑通 Demo](https://cloud.tencent.com/document/product/269/36838)。
- 通用即时通讯 SDK 和 Demo 源码，请参见 [SDK 下载](https://cloud.tencent.com/document/product/269/36887)。

本文例子使用 Web&H5，修改`GenerateTestUserSig.js`文件配置密钥后，无需编译，可直接访问`dist/index.html`，例如`http://127.0.0.1/timSdkH5Demo/dist/index.html`替换为服务器地址后可以直接访问，`timSdkH5Demo`为代码目录，可按需修改。

登录账号后即可实现聊天功能。以下为发起会话页面：

![img](https://main.qcloudimg.com/raw/54bc11435128816dfb2dfc1b1ed5086d.png)

### 2. 具体配置

（1）每款即时通讯产品都有回调内容的配置，这里需要先进行回调的配置，具体回调参数及说明可以参考 [第三方回调简介](https://cloud.tencent.com/document/product/269/1522)。
（2）回调事件以“单聊消息”为例，选中“发单聊消息之前回调”，会在发送消息前请求回调 URL，一系列判断后返回回调结果。

>? 这一步需要保证的就是，即时通讯产品可实现消息发送，且在发送消息时触发回调URL的请求，回调接口能够接收到请求数据。
>

## 图文消息具体配置

目前准备工作已经做好了，接下来需要考虑的有以下几点：

1. 消息发送时回调接口接收请求参数，确认参数的准确性。
2. 根据不同参数获取到不同消息内容，例如：聊天文本、图片地址等。
3. 对消息内容进行识别，不同的消息类型会调用不同的识别接口，接下来的内容会对不同的消息类型（文本和图片）进行举例说明。
4. 根据安全识别结果给出不同的返回结果，达到消息是否允许发送的效果。

下面举例说明部分会以`Step n`来对应上面各点。

举例说明：

```
开发工具：SCF 云函数 https://console.cloud.tencent.com/scf (不一定非要云函数，服务公网可见即可，否则回调请求失败)
语言：PHP/7.2.2

SDK以及Demo源码（公有云即时通讯产品都可以）：
地址: https://cloud.tencent.com/document/product/269/36887 
本文档例子使用Web&H5: https://github.com/tencentyun/TIMSDK/tree/master/H5

对象存储SDK文档：
PHP SDK地址: https://cloud.tencent.com/document/product/436/12266 (其他语言可见页面左侧栏对应标签)

即时通讯配置项：
单聊消息 >> 发单聊消息之前回调

举例消息类型：
文本、图片
```

#### 步骤1：回调请求参数

相关文档如下：
- [第三方回调简介](https://cloud.tencent.com/document/product/269/1522)
- [回调参数列表](https://cloud.tencent.com/document/product/269/1523)
- [消息格式描述](https://cloud.tencent.com/document/product/269/2720)

发送消息后会请求回调 URL，本例中对`SdkAppid`参数做了简单身份验证，如需要其他复杂验证可自行判断。

```php
<?php

include_once 'commonFunc.php'; // 自定义公用函数，如发送POST、GET请求或做出Response响应等函数的封装
include_once 'imMsg.php'; // 自定义消息审核类，对文本和图片做出审核请求并对审核结果做出是否违规判断
include_once 'cos-php-sdk-v5-master/vendor/autoload.php'; // COS内容审核SDK引入，本例使用PHP的SDK

$content = file_get_contents('php://input'); // 获取POST JSON数据 字符串
$post  = json_decode($content, true); // POST JSON数据 数组

// 对SdkAppid做出简单身份验证
if(!isset($_GET['SdkAppid']) || $_GET['SdkAppid'] != ImMsg::SDK_APPID) {
    imcallback_return(false); // 接口返回结果数据
}
```

```php
/**
 * 函数内列出两种回调结果
 * $send true 允许消息发送；false 禁止消息发送
 */
function imcallback_return($send = true) {
    $retSuccess = array(
        'ErrorCode' => 0, // 0 为允许发言
        'ErrorInfo' => '',
        'ActionStatus' => 'OK'
    );;
    $retErr = array(
        'ErrorCode' => 1, // 1 为拒绝发言
        'ErrorInfo' => 'err',
        'ActionStatus' => 'FAIL'
    );
    $ret = $send === true ? $retSuccess : $retErr;
    ob_clean();
    echo json_encode($ret);
}
```

回调请求示例：

```json
POST /?SdkAppid=123456&CallbackCommand=C2C.CallbackBeforeSendMsg&contenttype=json&ClientIP&OptPlatform HTTP/1.1
Host: www.example.com
文本类型：
{
    "MsgBody": [
        {
            "MsgType": "TIMTextElem", // TIMTextElem 表示消息类型为文本
            "MsgContent": {
                "Text": "asdad" // 文本内容
            }
        }
    ],
    "CallbackCommand": "C2C.CallbackBeforeSendMsg", // C2C.CallbackBeforeSendMsg 发单聊消息之前回调
    "From_Account": "user1",
    "To_Account": "user0",
    "MsgRandom": 123,
    "MsgSeq": 1234567,
    "MsgTime": 1629439393,
    "MsgKey": "1234567_123456_123456789",
    "OnlineOnlyFlag": 0
}

图片类型：
{
    "MsgBody": [
        {
            "MsgType": "TIMImageElem", // TIMImageElem 表示消息类型为图片
            "MsgContent": {
                "UUID": "123456-user1-abcdefghd", 
                "ImageFormat": 3, 
                "ImageInfoArray": [
                    {
                        "Type": 1, //原图
                        "Size": 43599, 
                        "Width": 1156, 
                        "Height": 582, 
                        "URL": "https://cos.ap-shanghai.myqcloud.com/6244-shanghai-007-shared-01-1256635546/2690-1400560394/e078-user1/582eef3bb1e6439cd842ae0bd6a16cae-101935?imageMogr2/"
                    }, 
                    {
                        "Type": 2, //大图
                        "Size": 0, 
                        "Width": 0, 
                        "Height": 0, 
                        "URL": "https://cos.ap-shanghai.myqcloud.com/6244-shanghai-007-shared-01-1256635546/2690-1400560394/e078-user1/582eef3bb1e6439cd842ae0bd6a16cae-101935?imageMogr2/"
                    }, 
                    {
                        "Type": 3, //缩量图
                        "Size": 0, 
                        "Width": 394, 
                        "Height": 198, 
                        "URL": "https://cos.ap-shanghai.myqcloud.com/6244-shanghai-007-shared-01-1256635546/2690-1400560394/e078-user1/582eef3bb1e6439cd842ae0bd6a16cae-101935?imageMogr2/&imageView2/3/w/198/h/198"
                    }
                ]
            }
        }
    ], 
    "CallbackCommand": "C2C.CallbackBeforeSendMsg", 
    "From_Account": "user1", 
    "To_Account": "user0", 
    "MsgRandom": 123, 
    "MsgSeq": 1234567, 
    "MsgTime": 1629357746, 
    "MsgKey": "1234567_123456_123456789", 
    "OnlineOnlyFlag": 0
}
```

回调应答示例：

```http
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 75
{
  "ActionStatus": "OK", 
  "ErrorInfo": "", 
  "ErrorCode": 0 // 1 为拒绝发言；0 为允许发言
}
```

回调 App 后台的超时时间为2秒，且没有重试。如果回调超时，后续处理逻辑与没有配置回调时相同（例如，假设“发送群消息之前回调”超时，消息会正常下发）。

为确保回调成功率，第三方 App 应当尽可能加快回调处理速度，例如先发送回调应答，然后再处理具体业务逻辑。

#### 步骤2：获取消息内容

| 回调类型           | 回调命令字                                                   |
| ------------------ | ------------------------------------------------------------ |
| 发单聊消息之前回调 | [C2C.CallbackBeforeSendMsg](https://cloud.tencent.com/document/product/269/1632) |
| 发单聊消息之后回调 | [C2C.CallbackAfterSendMsg](https://cloud.tencent.com/document/product/269/2716) |

其他回调命令及相关参数见 [回调命令列表](https://cloud.tencent.com/document/product/269/1523)。

| MsgType的值  | 类型     |
| ------------ | -------- |
| TIMTextElem  | 文本消息 |
| TIMImageElem | 图像消息 |

其他消息类别 MsgType 描述及相关参数见 [消息格式描述](https://cloud.tencent.com/document/product/269/2720)。

本例中简单获取了文本内容及图片地址 URL。

```php
$flag = false;
switch($_GET['CallbackCommand']) {
    case 'C2C.CallbackBeforeSendMsg': { // 对发单聊消息之前回调进行封装
        $flag = ImMsg::cmdC2cMsgBefore($post);
        break;
    }
    default: {
        break;
    }
}
imcallback_return($flag);
```

```php
// ImMsg::cmdC2cMsgBefore
public static function cmdC2cMsgBefore($allData) {
    $data = $allData['MsgBody'];
    $flag = true;
    foreach($data as $msgItem) {
        if($msgItem['MsgType'] == 'TIMTextElem') { // 文本类型审核
            // $msgItem['MsgContent']['Text'] 文本内容
            $flag = self::textDetect($msgItem['MsgContent']['Text']); 
        } else if($msgItem['MsgType'] == 'TIMImageElem') { // 图片类型审核
            // $msgItem['MsgContent']['ImageInfoArray'][0]['URL'] 图片URL地址，原图、大图、缩略图三选一
            $flag = self::imgDetect($msgItem['MsgContent']['ImageInfoArray'][0]['URL']);
        }
    }
    return $flag;
}
```

进行到这一步，已经获取到了消息内容，即：

- 文本内容：`$msgItem['MsgContent']['Text']`
- 图片地址：`$msgItem['MsgContent']['ImageInfoArray'][0]['URL']`

接下来对消息内容发送识别请求并获取识别结果。

#### 步骤3：对消息内容进行安全识别，获取识别结果

相关文档如下：:
- [图片安全识别](https://cloud.tencent.com/document/product/436/45434)
- [提交文本安全识别任务](https://cloud.tencent.com/document/product/436/56289)

关于安全，为了开发者更方便、更快速地使用数据万象的基础图片处理和媒体处理功能，以及 CDN 的云闪图片分发功能，我们提供了 SDK，开发者可根据具体需求进行选择，详情请参见对应的快速入门文档。对象存储的 SDK 也集成了数据万象的数据处理功能，若您需要使用其他语言的 SDK，例如 C++ 、JavaScript 等，请参见 [COS SDK 概览](https://cloud.tencent.com/document/product/436/6474)。

(1) 图片安全识别

>? 关于图片安全识别的图片限制说明，请参见 [规则与限制](https://cloud.tencent.com/document/product/460/36620)。
>

以下为 COS PHP SDK 请求示例（sample/getObjectSensitiveContentRecognition.php）：

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //"云 API 密钥 SecretId";
$secretKey = "SECRETKEY"; //"云 API 密钥 SecretKey";
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials' => array(
            'secretId' => $secretId,
            'secretKey' => $secretKey)));
try {
    //图片链接审核
    $imgUrl = 'https://test.jpg';
    $result = $cosClient->getObjectSensitiveContentRecognition(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => '/', // 链接图片资源路径写 / 即可
        'DetectType' => 'porn,ads',//可选参数：porn,ads，可使用多种规则，注意规则间不要加空格
        'DetectUrl' => $imgUrl,
//      'Interval' => 5, // 审核gif时使用 截帧的间隔
//      'MaxFrames' => 5, // 针对 GIF 动图审核的最大截帧数量，需大于0。
//      'BizType' => '', // 审核策略
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

响应结果：

```
GuzzleHttp\Command\Result Object
(
    [RequestId] => asdjahsfkjshfkjsdhfkjshfksjhfj=
    [PornInfo] => Array
        (
            [0] => Array
                (
                    [Code] => 0
                    [Msg] => OK
                    [HitFlag] => 0
                    [Score] => 0
                    [Label] => 
                )

        )

    [AdsInfo] => Array
        (
            [0] => Array
                (
                    [Code] => 0
                    [Msg] => OK
                    [HitFlag] => 0
                    [Score] => 0
                    [Label] => 
                )

        )

    [Key] => /
    [Bucket] => examplebucket-125000000
    [Location] => examplebucket-125000000.cos.ap-guangzhou.myqcloud.com//
)
```

(2) 文本安全识别

以下为 COS PHP SDK 请求示例 （sample/detectText.php）：

```php
  <?php
  
  require dirname(__FILE__) . '/../vendor/autoload.php';
  
  $secretId = "SECRETID"; //"云 API 密钥 SecretId";
  $secretKey = "SECRETKEY"; //"云 API 密钥 SecretKey";
  $region = "ap-beijing"; //设置一个默认的存储桶地域
  $cosClient = new Qcloud\Cos\Client(
      array(
          'region' => $region,
          'schema' => 'https', //协议头部，默认为http
          'credentials'=> array(
              'secretId'  => $secretId ,
              'secretKey' => $secretKey)));
  try {
      // start --------------- 文本内容审核 ----------------- //
      $content = '敏感信息';
      $result = $cosClient->detectText(array(
          'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
          'Input' => array(
              'Content' => base64_encode($content) // 文本需base64_encode
          ),
          'Conf' => array(
              'DetectType' => 'Porn,Ads', //Porn,Ads,Illegal,Abuse类型
              'BizType' => '',
          ),
      ));
      // 请求成功
      print_r($result);
      // end --------------- 文本内容审核 ----------------- //
  
  } catch (\Exception $e) {
      // 请求失败
      echo($e);
  }
```

响应结果：

```
  GuzzleHttp\Command\Result Object
  (
      [RequestId] => asdjsajfaslofjsdofjsoifjsf=
      [ContentType] => application/xml
      [ContentLength] => 1237
      [JobsDetail] => Array
          (
              [Code] => Success
              [Message] => Array
                  (
                  )
  
              [JobId] => asjhdkjahfkjashfkjsdfhkjs
              [State] => Success
              [CreationTime] => 2021-09-09T20:04:05+08:00
              [Content] => 57qm54Ku
              [Result] => 1
              [SectionCount] => 1
              [PornInfo] => Array
                  (
                      [HitFlag] => 1
                      [Count] => 1
                  )

              [AdsInfo] => Array
                  (
                      [HitFlag] => 0
                      [Count] => 0
                  )
  
              [Section] => Array
                  (
                      [0] => Array
                          (
                              [StartByte] => 0
                              [PornInfo] => Array
                                  (
                                      [Code] => 0
                                      [HitFlag] => 1
                                      [Score] => 97
                                      [Keywords] => 敏感词
                                  )
 
                              [AdsInfo] => Array
                                  (
                                      [Code] => 0
                                      [HitFlag] => 0
                                      [Score] => 0
                                      [Keywords] => 
                                  )
  
                          )
  
                  )
  
          )
  
      [Bucket] => examplebucket-1250000000
      [Location] => examplebucket-1250000000.ci.ap-guangzhou.myqcloud.com/text/auditing
  )
```

#### 步骤4：回调请求返回结果

进行到这一步，说明已经对消息内容进行了安全识别并作出了是否违规的判断，接下来就是返回是否违规的结果即可。

在`Step 1`回调应答示例中也提到了，`ErrorCode=1`拒绝发言，`ErrorCode=0`允许发言。

```
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 75
{
  "ActionStatus": "", 
  "ErrorInfo": "", 
  "ErrorCode": 0 // 1 为拒绝发言；0 为允许发言
}
```

在用户侧效果为：

![img](https://main.qcloudimg.com/raw/bae3615c0efdbf87816ce12a1adbf0ff.png)

具体参数及含义或其他应答方式可见 [第三方回调简介](https://cloud.tencent.com/document/product/269/1522) 或同页面左侧其他文档页。

至此，即时通讯发送消息、消息请求回调、消息安全识别、回调应答、消息发送结果，所有步骤均已完成。

## 语音消息安全识别具体配置

以 Android 端的通信 App 为例，进行语音消息安全识别。

Android 端的文本、图片消息和 Web 端请求过程一致，在此不再累述。可参见以下文档：

- [Android SDK 下载](https://cloud.tencent.com/document/product/269/36887)
- [一分钟跑通 Demo](https://cloud.tencent.com/document/product/269/36838)

本测试用例的 Android Demo 下载了 SDK 源码之后直接运行没跑起来，删减了一些代码才跑通，且虚拟机运行起来了之后在实体机上安装失败，过程比较曲折，若 Demo 跑不起来可自行研究文档或咨询 IM 相关技术人员。

语音消息的安全识别流程和文本、图片略有不同，文本、图片是在消息发送前就同步检测，违规不予发送，可以直接给出识别结果，不会存在一定的曝光期，而由于语音消息的特性，短时间无法做出结果响应，会以异步的形式识别，识别完成后以回调的方式发送识别结果，这样就会使得语音消息存在一定的曝光期，曝光期长短视识别的时长而定。流程如下：

1. 用户发送语音消息。
2. 请求回调 URL 接口，获取到语音消息对应的音频文件。
3. 回调接口提交音频安全识别任务，识别音频文件是否存在敏感违规信息。
4. 语音消息发送，不做拦截，聊天对象接收到语音消息。
5. 音频安全识别完成后发送回调结果，根据结果判断是否违规。
6. 若违规直接撤回消息，反之不做任何操作。
7. 流程结束。

下面举例说明部分会以`Step n`来对应上面各点。

#### 步骤1：用户发送消息

![img](https://main.qcloudimg.com/raw/56071d82a288b6169c5145e1e5c271da.jpeg)

#### 步骤2：请求回调 URL 接口，获取到语音消息对应的音频文件

和文本、图片获取方式一样，只不过换成了语音消息，参数略有不同。

```json
{
    "MsgBody": [
        {
           "MsgType": "TIMSoundElem",
           "MsgContent": {
               "Url": "https://1234-5678187359-1253735226.cos.ap-shanghai.myqcloud.com/abc123/c9be9d32c05bfb77b3edafa4312c6c7d", // 语音下载地址
               "Size": 62351, // 语音数据大小，单位：字节。
               "Second": 1, // 语音时长，单位：秒。
            "Download_Flag": 2
           }
        }
    ],
    "CallbackCommand": "C2C.CallbackBeforeSendMsg",
    "From_Account": "user1",
    "To_Account": "user0",
    "MsgRandom": 74363827834904,
    "MsgSeq": 9586798211,
    "MsgTime": 1629873986,
    "MsgKey": "1234567_1234567_1234567", // 该条消息唯一标识
    "OnlineOnlyFlag": 0
}
```

这里`From_Account`、`To_Account`、`MsgKey`三个字段在消息违规撤回时需要用到。

样例代码是对文本、图片安全识别流程`Step 2`获取消息内容的`ImMsg::cmdC2cMsgBefore`做了补充：

```php
public static function cmdC2cMsgBefore($allData) {
    $data = $allData['MsgBody'];
    $flag = true;
    foreach($data as $msgItem) {
        if($msgItem['MsgType'] == 'TIMTextElem') {
            $flag = self::textDetect($msgItem['MsgContent']['Text']);
        } else if($msgItem['MsgType'] == 'TIMImageElem') {
            $flag = self::imgDetect($msgItem['MsgContent']['ImageInfoArray'][0]['URL']);
        } else if($msgItem['MsgType'] == 'TIMSoundElem') {
            // $msgItem['MsgContent']['Url'] 音频文件地址
            self::soundDetectSubmit($msgItem['MsgContent']['Url'], $allData); // 提交检测，先发后审
            $flag = true;
        }
    }
    return $flag;
}
```

这一步获取到了语音对应的音频文件地址，即`$msgItem['MsgContent']['Url']`。

#### 步骤3：提交音频安全识别任务

和文本、图片安全识别基本一致，只是多了一步回调操作，而不是直接返回结果，在音频识别完成后自动调用回调接口，发送识别结果。相关 API 文档可参见 [提交音频安全识别任务](https://cloud.tencent.com/document/product/436/54063)。

使用 COS PHP SDK 请求示例（sample/detectAudio.php），请求中`Callback`为识别完成后的回调 URL，发送识别结果。

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //"云 API 密钥 SecretId";
$secretKey = "SECRETKEY"; //"云 API 密钥 SecretKey";
$region = "ap-beijing"; //设置一个默认的存储桶地域
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
try {
    $result = $cosClient->detectAudio(array(
        'Bucket' => 'examplebucket-125000000', //格式：BucketName-APPID
        'Input' => array(
            'Url' => 'http://example.com/sound01.mp3',
        ),
        'Conf' => array(
            'DetectType' => 'Porn,Ads',
            'Callback' => 'https://example.com/callback',
            'BizType' => '',
        ),
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

响应结果：

```
GuzzleHttp\Command\Result Object
(
    [RequestId] => asdjhakjsdkajshdksajhdkjasd=
    [ContentType] => application/xml
    [ContentLength] => 432
    [JobsDetail] => Array
        (
            [Url] => https://example.com/test.mp3
            [JobId] => asjhdklasdhkajsdhksajhdksjad
            [State] => Submitted
            [CreationTime] => 2021-09-09T20:12:12+08:00
        )

    [Bucket] => examplebucket-125000000
    [Location] => examplebucket-125000000.ci.ap-guangzhou.myqcloud.com/audio/auditing
)
```

#### 步骤4：消息接收方收到消息

这里以先发后审的形式，在安全识别结果出来之前，默认所有语音消息都正常，允许发送。

#### 步骤5：音频安全识别结果

在提交音频安全识别任务后，识别完成会以回调的方式发送识别任务，回调 URL 就是提交检测时`Callback`参数。

结果示例：

```json
{
    "code": 0,
    "message": "success",
    "data": {
        "url": "https:\/\/example.com\/test.mp3",
        "result": 0,
        "forbidden_status": 0,
        "trace_id": "ashdiashdiuahdiahdiahdi",
        "event": "ReviewAudio",
        "porn_info": {
            "hit_flag": 0,
            "score": 0,
            "label": ""
        },
        "ads_info": {
            "hit_flag": 0,
            "score": 0,
            "label": ""
        }
    }
}
```

详细参数及含义见 [查询音频安全识别结果](https://cloud.tencent.com/document/product/436/54064)，主动请求返回的是 XML 格式，回调发送的是 json，但参数含义一致。

#### 步骤6：若违规，则撤回消息

相关文档如下：

- [撤回单聊消息](https://cloud.tencent.com/document/product/269/38980)
- [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)

>! 使用该接口撤回单聊消息后，被撤回的消息不能恢复，请谨慎调用该接口。
>

请求示例：

```http
POST https://console.tim.qq.com/v4/openim/admin_msgwithdraw?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json HTTP/1.1
Content-Type: application/json
<body>

{
    "From_Account": "vinson",
    "To_Account": "dramon",
    "MsgKey": "31906_833502_1572869830"
}
```

响应体：

```json
// 正常应答
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0
}

// 异常应答
{
    "ActionStatus": "FAIL",
    "ErrorInfo": "Fail to Parse json data of body, Please check it",
    "ErrorCode": 90001 // 其他错误码见文档介绍
}
```

代码示例：

```php
public static function withdrawC2cMsg($fromAccount, $toAccount, $msgKey) {
    // 撤回单聊消息
    try {
        $api = new \Tencent\TLSSigAPIv2(self::SDK_APPID, self::SDK_APPID_KEY);
        $userSig = $api->genUserSig(self::USER_ADMIN);
    } catch (Exception $e) {
        return false;
    }
    $random = rand(1, 100000);
    $url = 'https://console.tim.qq.com/v4/openim/admin_msgwithdraw?sdkappid='.self::SDK_APPID.'&identifier='.self::USER_ADMIN.'&usersig='.$userSig.'&random='.$random.'&contenttype=json';
    $data = array(
        'From_Account' => $fromAccount,
        'To_Account' => $toAccount,
        'MsgKey' => $msgKey,
    );
    $headers = array(
        'Content-Type: application/json'
    );
    $res = requestPost($url, json_encode($data), $result, $headers); // 发送POST请求
    if(!$res || ! $result) {
        return false;
    }
    $result = json_decode($result, true);
    if($result['ErrorCode'] == 0) {
        return true; // 撤回成功
    }
    return false;
}
```

以 PHP 为例，在生成 UserSig 时引入`TLSSigAPIv2.php`即可。其他语言见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。

#### 步骤7：违规消息自动撤回，流程结束

![img](https://main.qcloudimg.com/raw/cb65d0f313ac461e2092477145de62b9.png)
