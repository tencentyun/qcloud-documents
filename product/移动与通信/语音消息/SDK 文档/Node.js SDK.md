SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [语音消息 API](https://cloud.tencent.com/document/product/1128/51569)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#SendTtsVoice)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。



## 前提条件

- 已开通语音消息服务，具体操作请参见 [快速入门](https://cloud.tencent.com/document/product/1128/37343)。
- 已准备依赖环境：NODEJS 10.0.0 版本及以上。
- 已在访问管理控制台 >**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 语音消息的调用地址为`vms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/1128/51569)。
- 下载 SDK 源码请访问 [Node.js SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)。

## 安装 SDK
### 通过 npm 安装（推荐）
[npm](https://www.npmjs.com/) 是 Node.js 的包管理工具。

1. 执行以下安装命令。
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考 [示例代码](#example)。

### 通过源码包安装
1. 前往 [GitHub 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 或 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-nodejs/tencentcloud-sdk-nodejs.zip)，下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，可参考 [示例代码](#example)。

## 示例代码[](id:example)
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vms&Version=2020-09-02&Action=SendCodeVoice) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。示例代码如下所示。

### 发送语音验证码

```
const tencentcloud = require("tencentcloud-sdk-nodejs");

// 导入 VMS 模块的 client models
const vmsClient = tencentcloud.vms.v20200902.Client;

/* 实例化要请求 VMS 的 client 对象 */
const client = new vmsClient({
    credential: {
    /* 必填：腾讯云账户密钥对secretId，secretKey。
     * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
     * 您也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
     * 以免泄露密钥对危及您的财产安全。
     * CAM密匙查询: https://console.cloud.tencent.com/cam/capi */
      secretId: process.env.secretId,
      secretKey: process.env.secretKey,
    },
    /* 必填：地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
    region: "ap-guangzhou",
    /* 非必填:
     * 客户端配置对象，可以指定超时时间等配置 */
    profile: {
      /* SDK默认用TC3-HMAC-SHA256进行签名，非必要请不要修改这个字段 */
      signMethod: "TC3-HMAC-SHA256",
      httpProfile: {
        /* SDK默认使用POST方法。
         * 如果您一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
        reqMethod: "POST",
        /* SDK有默认的超时时间，非必要请不要进行调整
         * 如有需要请在代码中查阅以获取最新的默认值 */
        reqTimeout: 30,
        /**
         * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务
         * 则必须手动指定域名，例如vms的上海金融区域名： vms.ap-shanghai-fsi.tencentcloudapi.com
         */
        endpoint: "vms.tencentcloudapi.com"
      },
    },
  });
  
  /* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
   * 属性可能是基本类型，也可能引用了另一个数据结构
   * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 
   * 帮助链接：
   * 语音消息控制台：https://console.cloud.tencent.com/vms
   * vms helper：https://cloud.tencent.com/document/product/1128/37720
   */
  const params = {
    /* 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是" */
    CodeMessage: "1234",
    /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
     * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号
     */
    CalledNumber: "+8613711112222",
    /* 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666 */
    VoiceSdkAppid: "1400006666",
    /* 播放次数，可选，最多3次，默认2次 */
    PlayTimes: 2,
    /* 用户的 session 内容，腾讯 server 回包中会原样返回 */
    SessionContext: "xxxx",
  };
  // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
  client.SendCodeVoice(params, function (err, response) {
    // 请求异常返回，打印异常信息
    if (err) {
      console.log(err);
      return;
    }
    // 请求正常返回，打印response对象
    console.log(response);
  })
```

### 指定模版发送语音通知[](id:SendTtsVoice)

```
const tencentcloud = require("tencentcloud-sdk-nodejs");

// 导入 VMS 模块的 client models
const vmsClient = tencentcloud.vms.v20200902.Client;

/* 实例化要请求 VMS 的 client 对象 */
const client = new vmsClient({
    credential: {
    /* 必填：腾讯云账户密钥对secretId，secretKey。
     * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
     * 您也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
     * 以免泄露密钥对危及您的财产安全。
     * CAM密匙查询: https://console.cloud.tencent.com/cam/capi */
      secretId: process.env.secretId,
      secretKey: process.env.secretKey,
    },
    /* 必填：地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
    region: "ap-guangzhou",
    /* 非必填:
     * 客户端配置对象，可以指定超时时间等配置 */
    profile: {
      /* SDK默认用TC3-HMAC-SHA256进行签名，非必要请不要修改这个字段 */
      signMethod: "TC3-HMAC-SHA256",
      httpProfile: {
        /* SDK默认使用POST方法。
         * 如果您一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
        reqMethod: "POST",
        /* SDK有默认的超时时间，非必要请不要进行调整
         * 如有需要请在代码中查阅以获取最新的默认值 */
        reqTimeout: 30,
        /**
         * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务
         * 则必须手动指定域名，例如vms的上海金融区域名： vms.ap-shanghai-fsi.tencentcloudapi.com
         */
        endpoint: "vms.tencentcloudapi.com"
      },
    },
  });
  
  /* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
   * 属性可能是基本类型，也可能引用了另一个数据结构
   * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 
   * 帮助链接：
   * 语音消息控制台：https://console.cloud.tencent.com/vms
   * vms helper：https://cloud.tencent.com/document/product/1128/37720
   */
  const params = {
    // 模板 ID，必须填写在控制台审核通过的模板 ID，可登录 [语音消息控制台] 查看模板 ID
    TemplateId: "4356",
    TemplateParamSet: ["7652"],
    /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
     * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号
     */
    CalledNumber: "+8613711112222",
    /* 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666 */
    VoiceSdkAppid: "1400006666",
    /* 播放次数，可选，最多3次，默认2次 */
    PlayTimes: 2,
    /* 用户的 session 内容，腾讯 server 回包中会原样返回 */
    SessionContext: "xxxx",
  };
  // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
  client.SendTtsVoice(params, function (err, response) {
    // 请求异常返回，打印异常信息
    if (err) {
      console.log(err);
      return;
    }
    // 请求正常返回，打印response对象
    console.log(response);
  })
```
