# 简介

欢迎使用腾讯云开发者工具套件（SDK），NODEJS SDK 4.0 是云 API 3.0 平台的配套工具。目前已经支持 cvm、vpc、cbs 等产品，后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 NODEJS 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 NODEJS 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 NODEJS SDK 并开始调用。

# 依赖环境

1. NODEJS 10.0.0 版本及以上
2. 从腾讯云控制台 开通相应产品
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为\*.tencentcloudapi.com，如 CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

# 获取安装

安装 NODEJS SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey， SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

## 通过 Npm 安装

通过 npm 获取安装是使用 NODEJS SDK 的推荐方法，npm 是 NODEJS 的包管理工具。关于 npm 详细可参考[ npm 官网](https://www.npmjs.com/) 。

1. 执行以下安装命令：
   > npm install tencentcloud-sdk-nodejs --save
2. 在您的代码中引用对应模块代码，可参考示例。

## 通过源码包安装

1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，可参考示例。

# 示例

```js
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的client models。
const CvmClient = tencentcloud.cvm.v20170312.Client

const clientConfig = {
  // 腾讯云认证信息
  credential: {
    secretId: "secretId",
    secretKey: "secretKey",
  },
  // 产品地域
  region: "ap-shanghai",
  // 可选配置实例
  profile: {
    signMethod: "HmacSHA256", // 签名方法
    httpProfile: {
      reqMethod: "POST", // 请求方法
      reqTimeout: 30, // 请求超时时间，默认60s
    },
  },
}
// 实例化要请求产品(以cvm为例)的client对象
const client = new CvmClient(clientConfig)
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones().then(
  (data) => {
    console.log(data)
  },
  (err) => {
    console.error("error", err)
  }
)
```

在支持 typescript 项目中，采用如下方式调用

```js
import * as tencentcloud from "tencentcloud-sdk-nodejs"

// 导入对应产品模块的client models。
const CvmClient = tencentcloud.cvm.v20170312.Client

const clientConfig = {
  // 腾讯云认证信息
  credential: {
    secretId: "secretId",
    secretKey: "secretKey",
  },
  // 产品地域
  region: "ap-shanghai",
  // 可选配置实例
  profile: {
    signMethod: "HmacSHA256", // 签名方法
    httpProfile: {
      reqMethod: "POST", // 请求方法
      reqTimeout: 30, // 请求超时时间，默认60s
    },
  },
}
// 实例化要请求产品(以cvm为例)的client对象
const client = new CvmClient(clientConfig)
// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones().then(
  (data) => {
    console.log(data)
  },
  (err) => {
    console.error("error", err)
  }
)
```

实例化`Client` 的入参支持 `clientConfig` 数据结构和说明 详见 [ClientConfig](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/common/interface.ts)

## 更多示例

更丰富的使用 demo 请在 examples 目录中寻找。

# 相关配置

## 代理

如果是有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用，抛出连接超时的异常。

# 旧版 SDK

我们推荐使用新版 NODEJS SDK，如果一定要用旧版 SDK，请前往[github 仓库](https://github.com/CFETeam/qcloudapi-sdk)下载。
