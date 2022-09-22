## 概述
腾讯云智聆口语评测（Smart Oral Evaluation，SOE）是腾讯云推出的语音评测产品，是基于口语类教育培训场景和腾讯云的语音处理技术，应用特征提取、声学模型和语音识别算法，为儿童和成人提供高准确度的口语发音评测。腾讯云智聆口语评测支持单词和句子模式的评测，多维度反馈口语表现，可广泛应用于中文及英语口语类教学中。   

本 SDK 为智聆口语测评的 Web 版本，封装了对智聆口语测评网络 API 的 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/api/884/32605) 接口调用及本地音频文件处理，并提供简单的录音功能，使用者可以专注于从业务切入，方便简洁地进行二次开发。

本文档只对 Web SDK 进行描述，详细的网络 API 说明请参见 [API 文档](https://cloud.tencent.com/document/product/884/19309)。

## 流程图
![](https://qcloudimg.tencent-cloud.cn/raw/151ac834387d41c3b841c5a63b2d07a5.png)

## SDK 集成准备
### 获取密钥
在首次使用插件之前，请前往 [访问管理](https://console.cloud.tencent.com/capi) 申请安全凭证。 安全凭证包括 SecretId 和 SecretKey：
- SecretId 用于标识 API 调用者身份。
- SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。

>! 用户必须要严格保管安全凭证，避免泄露。
>
有了安全凭证 SecretId 和 SecretKey 后，可以生成鉴权凭证来使用 Web SDK： 后端获取授权凭证请参考[服务端 SDK](https://cloud.tencent.com/document/product/884/78785)。
![](https://qcloudimg.tencent-cloud.cn/raw/5479ee8b864859845a11679ddb5c06bf.png)

## SDK DEMO 使用流程
### Demo 调试
使用浏览器打开 [这里](https://test-v.campus.qq.com/aiedu/soe/demo/index-client.html)。 

### 填入密钥
填入 SecretId 和 SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/7c277ee697287c7cc83b7237bcd5970a.png)
### 开始评测
单击**开始录音**或**外部文件**，即可开始评测。


## SDK 使用方法
[使用示例](https://test-v.campus.qq.com/aiedu/soe/demo/soe_websdk_develop.html)。
### SDK 引入
在您的 Web 页面中添加如下 Web SDK 依赖：
```
<script src="https://aiedu.qcloud.com/soe/TencentSOE-0.1.4.js"></script>
```
### 标签页建立
在请求体中设置触发按钮和请求参数（由于请求参数有默认值，这里暂不展示）：
```
<div>
    <button id="start">start</button>
    <button id="stop">stop</button>
    <button id="upload">upload</button>
    <br>
    <span id="result"></span>
</div>
```

### 事件触发
获取标签按钮，触发点击事件
```
let startbtn = document.querySelector("#start")
    let stopbtn = document.querySelector("#stop")
    let uploadbtn = document.querySelector("#upload")
    let result = document.querySelector("#result")
    startbtn.onclick = function () {}
```

### 创建 TencentSOE 对象
#### 方式一（不推荐）：前端使用固定密钥（SecretId和SecretKey）计算授权凭证
该方式适用于前端调试，若使用此方式，请避免泄露密钥。
```
startbtn.onclick = function () {
    let recorder = new TencentSOE({
      SecretId: 'your secretid',
      SecretKey: 'your secretkey',
      success() {
        recorder.start({});
      },
      error(err) {
        console.log(err);
      }
    });
}
```

#### 方式二（推荐）：使用 getAuthorization 接收临时密钥
需要使用服务端 SDK， [获取联合身份临时访问凭证](https://cloud.tencent.com/document/product/1312/48195)，提供回调函数的 url。
```
startbtn.onclick = function () {
    let recorder = new TencentSOE({
      getAuthorization(callback) {
        let url = ''; // 服务端获取临时密钥地址
        $.get(url, function (data) {
          callback({
            Token: data.Credentials.Token,
            TmpSecretId: data.Credentials.TmpSecretId,
            TmpSecretKey: data.Credentials.TmpSecretKey,
            ExpiredTime: data.ExpiredTime
          });
        });
      },
      success() {
        recorder.start({});
      },
      error(err) {
        console.log(err);
      }
    });
}
```
智聆口语评测 [获取联合身份临时访问凭证](https://cloud.tencent.com/document/product/1312/48195) 请求参数参考：
```
Name = "soe",
Policy = "{\"version\": \"2.0\",\"statement\": {\"effect\": \"allow\",\"action\": [\"soe:TransmitOralProcessWithInit\"],\"resource\": \"*\"}}"
```
Node.js 版本获取联合身份临时访问凭证代码示例：
```
// token.js
import * as tencentcloud from 'tencentcloud-sdk-nodejs';

export const getToken = () => {
  return new Promise(async (resolve, reject) => {
    const StsClient = tencentcloud.sts.v20180813.Client;
    const clientConfig = {
      // 腾讯云认证信息
      credential: {
        secretId: 'your secretid',
        secretKey: 'your secretkey',
      },
      // 产品地域
      region: 'ap-guangzhou',
      // 可选配置实例
      profile: {
        signMethod: 'HmacSHA256', // 签名方法
        httpProfile: {
          reqMethod: 'POST', // 请求方法
          reqTimeout: 30, // 请求超时时间，默认60s
          endpoint: 'sts.tencentcloudapi.com'
        },
      },
    };
    const client = new StsClient(clientConfig);
    const policy = {
      version: '2.0',
      statement: {
        effect: 'allow',
        action: ['soe:TransmitOralProcessWithInit'],
        resource: '*'
      }
    };
    const params = {
      Name: 'soe',
      Policy: encodeURIComponent(JSON.stringify(policy))
    };
    client.GetFederationToken(params).then((res) => {
      resolve(res);
    }, (err) => {
      reject(err);
    })
  });
};
```

#### 方式三（推荐）：使用 TransInitUrl
通过传递评测参数给服务端 SDK 接收进行评测，返回评测结果。
```
startbtn.onclick = function () {
    let recorder = new TencentSOE({
      TransInitUrl: '',服务端获取评测结果地址
      success() {
        recorder.start({});
      },
      error(err) {
        console.log(err);
      }
    });
}
```

### 调用方法
创建对象 TencentSOE 后，在 success（）内调用方法进行录音评测。
#### 开始录音
```
let recorder = new TencentSOE({
    SecretId: '',
    SecretKey: '',
    success() {
        recorder.start({
            RefText: 'about',
            error: function (err) {
                console.log(err);
            },
            complete: function () {
                console.log('录音超过1分钟未停止触发此回调')
            },
            success: function (res) {
                console.log(res);
                result.innerHTML = JSON.stringify(res); //展示结果
            }
        });
    }
})
```

#### 停止录音
```
let recorder = new TencentSOE({
    SecretId: '',
    SecretKey: '',
    success() {
        stopbtn.onclick = function () {
            recorder.stop({
                success(res) {
                    // 输出测评结果
                    console.log(res); //打印结果
                    result.innerHTML = JSON.stringify(res); //展示结果
                },
                error(err) {
                    console.log(err);
                }
            });
        }
    }
})
```
#### 本地上传文件测评
```
uploadbtn.onclick = function () {
        let recorder = new TencentSOE({
            SecretId: '',
            SecretKey: '',
            success() {
                recorder.uploadLocalFile({
                    RefText: 'about',
                    load() {
                        console.log('文件加载完成');
                    },
                    success(res) {
                        console.log(res); // 输出测评结果
                        result.innerHTML = JSON.stringify(res);
                    },
                    error(err) {
                        console.log('err', err);
                    }
                });
            }
        })
    }
```

#### 重置参数
```
let recorder = new TencentSOE({
    SecretId: '',
    SecretKey: '',
    success() {
        recorder.reset({
          WorkMode: 1
        });
    }
})
```


## 参数说明
### TencentSOE 说明

|      参数         |  类型     |  说明    |  是否必填 | 默认值 |
|     :---:        | :---:    | :---    | :----: | :----  |
| SecretId         | String   | 用户 SecretId | 否| 无 |
| SecretKey        | String   | 用户 SecretKey | 否 | 无 |
| getAuthorization | function | 获取临时密钥接口 | 否 | 无 |
| TransInitUrl     | String   | 发音数据传输附带初始化接口地址 | 否 | 无 |
| success          | function | 创建成功回调 | 否 | 无 |
| error            | function | 创建失败回调 | 否 | 无 |

### 评测参数说明
评测参数有默认值，需要按需填写。可以在 TencentSOE 里面使用，也可以在 reset 里面使用。参数来源 [TransmitOralProcessWithInit](https://cloud.tencent.com/document/product/884/32605)。

|      参数         |  类型     |  说明    |  是否必填 | 默认值 |
|     :---:        | :---:    | :---    | :----: | :----  |
| WorkMode         | Integer  | 上传方式：语音输入模式，0流式分片（微信端无效），1非流式一次性评估 | 否 | 0 |
| EvalMode         | Integer  | 0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式 | 否 | 0 |
| ScoreCoeff       | Float    | 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数<br>用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段 | 否 | 3.5 |
| SoeAppId         | String   | 业务应用 ID，与账号应用 APPID 无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在 [腾讯云智聆口语评测](https://console.cloud.tencent.com/soe/index/setting_en)  的**应用管理**下新建。 | 否 | 无 |
| ServerType       | Integer  | 评估语言，0：英文，1：中文 | 否 | 0 |
| TextMode         | Integer  | 输入文本模式，0: 普通文本，1: 音素结构文本 | 否 | 0 |

### SecretId 参数说明
在 [访问关管理控制台](https://console.cloud.tencent.com/cam/capi)，新建密钥，获取使用。密钥属于敏感信息，所以需要通过临时密钥或服务端请求。

### getAuthorization 回调函数说明

| 属性名        |  参数描述                                     | 类型    | 必填 |
| :---        | :---                                        | :----  | :--- |
| Token        |  获取回来的临时密钥的 Token           | String | 是   |
| TmpSecretId  |  获取回来的临时密钥的 TmpSecretId，用于前端计算签名  | String | 是   |
| TmpSecretKey |  获取回来的临时密钥的 TmpSecretKey，用于前端计算签名 | String | 是   |
| ExpiredTime  |  获取回来的临时密钥的 ExpiredTime，过期时间        | String | 是   |

### TransInitUrl 参数说明
接口方法为 POST，需要对前端传来的参数进行签名，再调用云 API 的 TransmitOralProcessWithInit （发音数据传输接口附带初始化过程）接口，返回的数据格式不必再做封装，透传云 API 返回的数据即可，成功返回：`{"Response":{"RequestId": "xxx"...}}`，
失败返回：`{"Response":{"RequestId":"xxx","Error":{"xxx":"xxx"}...}}`，详情请参见 [Tencent Cloud API 3.0 SDK](https://cloud.tencent.com/document/product/884/78785)。

## 错误码
|   code   | 错误说明                  |
|  :---:   | :---                    |
| 10000    | 参数格式错误              |
| 10001    | 当前浏览器不支持录音功能     |
| 10002    | 未开启麦克风访问权限        |
| 10003    | 未提供发音评估初始化接口     |
| 10004    | 未提供发音数据传输接口接口   |
| 10005    | 未提供测评文本             |
| 10006    | 上传文件必须是 mp3 类型       |
| 10007    | 未引入微信 JS-SDK          |
| 10008    | 用户拒绝用户拒绝授权录音     |
| 10009    | 上传文件必须是mp3类型       |
| 10010    | 网络异常                  |
| 10011    | TransInitUrl 接口不正确     |
| 10012    | MediaUrl 接口不正确         |
| 10013    | 录音失败，请重新录音         |
| 10020    | 接口错误，具体看返回信息      |

## 常见问题
### undefined is not an object (evaluating 'u.start')
每次调用 recoder.start 都需要初始化。

### code：10010，网络异常
1. 检查网络状态。
2. 线上版本迭代，本地存储老版本不可以使用。重新从线上获取即可。
3. web sdk 有对音频做转码，如果使用 TransInitUrl 接口，服务端不需要使用音频转码。

### code: 10002, msg: "未开启麦克风访问权限"
需要使用 HTTPS 协议。


## 平台和兼容性
| 操作系统平台	  | 浏览器/webview                  | 版本要求 | 备注|
|  :---:      | :---                           | :---   | :--- |
| iOS         | Safari ( 只支持 Safari )         | 11.1.2 | -|
| Android     | TBS （微信和手机 QQ 的默认 webview）  | 43600  | 微信和手机 QQ 默认内置的浏览器内核为 [TBS](https://x5.tencent.com/)。|
| Android     | Chrome                         | 60+    |- |
| Mac         | Chrome                         | 47+    | -|
| Mac         | Safari                         | 11+    |- |
| Windows(PC) | Chrome                         | 52+    | -|
| Windows(PC) | QQ 浏览器                        | 10.2   | -|
| 微信端       | 微信默认 webview                  | 无     | 需引入微信 JS-SDK。|

>!非本地环境必须使用 HTTPS 协议。
