SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/38764)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口
>一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。


## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：NODEJS 7.10.1 及以上版本。
- 已在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/38764)。
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
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。

### 申请短信模板
```
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的client models。
const smsClient = tencentcloud.sms.v20190711.Client

/* 实例化要请求产品(以sms为例)的client对象 */
const client = new smsClient({
  credential: {
  /* 必填：腾讯云账户密钥对secretId，secretKey。
   * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
   * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
   * 以免泄露密钥对危及你的财产安全。
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
    signMethod: "HmacSHA256",
    httpProfile: {
      /* SDK默认使用POST方法。
       * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
      reqMethod: "POST",
      /* SDK有默认的超时时间，非必要请不要进行调整
       * 如有需要请在代码中查阅以获取最新的默认值 */
      reqTimeout: 30,
      /**
       * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
       * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com
       */
      endpoint: "sms.tencentcloudapi.com"
    },
  },
})

/* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
 * 属性可能是基本类型，也可能引用了另一个数据结构
 * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
const params = {
  /* 模板名称 */
  TemplateName: "腾讯云",
  /* 模板内容 */
  TemplateContent: "{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。",
  /* 短信类型：0表示普通短信, 1表示营销短信 */
  SmsType: 0,
  /* 是否国际/港澳台短信：0：表示国内短信; 1：表示国际/港澳台短信 */
  International: 0,
  /* 模板备注：例如申请原因，使用场景等 */
  Remark: "xxx",
}
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.AddSmsTemplate(params, function (err, response) {
  // 请求异常返回，打印异常信息
  if (err) {
    console.log(err)
    return
  }
  // 请求正常返回，打印response对象
  console.log(response)
})
```

### 发送短信

```
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的client models。
const smsClient = tencentcloud.sms.v20190711.Client

/* 实例化要请求产品(以sms为例)的client对象 */
const client = new smsClient({
  credential: {
  /* 必填：腾讯云账户密钥对secretId，secretKey。
   * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
   * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
   * 以免泄露密钥对危及你的财产安全。
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
    signMethod: "HmacSHA256",
    httpProfile: {
      /* SDK默认使用POST方法。
       * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
      reqMethod: "POST",
      /* SDK有默认的超时时间，非必要请不要进行调整
       * 如有需要请在代码中查阅以获取最新的默认值 */
      reqTimeout: 30,
      /**
       * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
       * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com
       */
      endpoint: "sms.tencentcloudapi.com"
    },
  },
})

/* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
 * 属性可能是基本类型，也可能引用了另一个数据结构
 * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
const params = {
  /* 短信应用ID: 短信SdkAppid在 [短信控制台] 添加应用后生成的实际SdkAppid，示例如1400006666 */
  SmsSdkAppid: "1400787878",
  /* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看 */
  Sign: "xxx",
  /* 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper] */
  ExtendCode: "",
  /* 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper] */
  SenderId: "",
  /* 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
  SessionContext: "",
  /* 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
   * 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号*/
  PhoneNumberSet: ["+8613711112222"],
  /* 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看 */
  TemplateID: "449739",
  /* 模板参数: 若无模板参数，则设置为空*/
  TemplateParamSet: ["666"],
}
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.SendSms(params, function (err, response) {
  // 请求异常返回，打印异常信息
  if (err) {
    console.log(err)
    return
  }
  // 请求正常返回，打印response对象
  console.log(response)
})
```

### 拉取回执状态

```
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的client models。
const smsClient = tencentcloud.sms.v20190711.Client

/* 实例化要请求产品(以sms为例)的client对象 */
const client = new smsClient({
  credential: {
  /* 必填：腾讯云账户密钥对secretId，secretKey。
   * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
   * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
   * 以免泄露密钥对危及你的财产安全。
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
    signMethod: "HmacSHA256",
    httpProfile: {
      /* SDK默认使用POST方法。
       * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
      reqMethod: "POST",
      /* SDK有默认的超时时间，非必要请不要进行调整
       * 如有需要请在代码中查阅以获取最新的默认值 */
      reqTimeout: 30,
      /**
       * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
        * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com
       */
      endpoint: "sms.tencentcloudapi.com"
    },
  },
})

/* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
 * 属性可能是基本类型，也可能引用了另一个数据结构
 * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
const params = {
  // 短信应用ID: 短信SdkAppid在 [短信控制台] 添加应用后生成的实际SdkAppid，示例如1400006666
  SmsSdkAppid: "1400787878",
  // 拉取最大条数，最多100条
  Limit: 10,
}
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.PullSmsSendStatus(params, function (err, response) {
  // 请求异常返回，打印异常信息
  if (err) {
    console.log(err)
    return
  }
  // 请求正常返回，打印response对象
  console.log(response)
})
```

### 统计短信发送数据

```
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的client models。
const smsClient = tencentcloud.sms.v20190711.Client

/* 实例化要请求产品(以sms为例)的client对象 */
const client = new smsClient({
  credential: {
  /* 必填：腾讯云账户密钥对secretId，secretKey。
   * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
   * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
   * 以免泄露密钥对危及你的财产安全。
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
    signMethod: "HmacSHA256",
    httpProfile: {
      /* SDK默认使用POST方法。
       * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
      reqMethod: "POST",
      /* SDK有默认的超时时间，非必要请不要进行调整
       * 如有需要请在代码中查阅以获取最新的默认值 */
      reqTimeout: 30,
      /**
       * SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
       * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com
       */
      endpoint: "sms.tencentcloudapi.com"
    },
  },
})

/* 请求参数，根据调用的接口和实际情况，可以进一步设置请求参数
 * 属性可能是基本类型，也可能引用了另一个数据结构
 * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
const params = {
  /* 短信应用ID: 短信SdkAppid在 [短信控制台] 添加应用后生成的实际SdkAppid，示例如1400006666 */
  SmsSdkAppid: "1400787878",
  /* 拉取最大条数，最多100条 */
  Limit: 10,
  /* 偏移量，目前固定设置为0 */
  Offset: 0,
  /* 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时 */
  StartDateTime: 2019122400,
  /* 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
   * 注：EndDataTime 必须大于 StartDateTime*/
  EndDataTime: 2019122523,
}
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.SendStatusStatistics(params, function (err, response) {
  // 请求异常返回，打印异常信息
  if (err) {
    console.log(err)
    return
  }
  // 请求正常返回，打印response对象
  console.log(response)
})
```

## 常见问题
<dx-accordion>
::: 代理设置
如有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用，抛出连接超时的异常现象。
:::
</dx-accordion>
