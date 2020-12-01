## 简介

- 欢迎使用腾讯云开发者工具套件（SDK），Node.js SDK 4.0 是云 API 3.0 平台的配套工具。新版 SDK 4.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同，接口调用方式相同，错误码和返回包格式相同等优点。
- 本文以 Node.js SDK 4.0 为例，介绍首次使用开发工具包和简单示例。方便 Node.js 开发者调试和接入腾讯云产品 API，让您快速获取腾讯云 Node.js SDK 并开始调用。
- 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

- Node.js 10.0.0 版本及以上。
- 从 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应产品。
- 获取安全凭证。安全凭证包括 SecretID 和 SecretKey 两个部分。SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。请前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/83c7610394b1a0423d1601ea7e956594.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，SecretKey 必须严格保管，避免泄露。**
- 获取调用地址。调用地址（endpoint）一般形式为`\*.tencentcloudapi.com`，产品的调用地址有一定区别，如云服务器 CVM 的调用地址为 `cvm.tencentcloudapi.com`，具体调用地址可参见对应产品的 [API文档](https://cloud.tencent.com/document/api)。

## 安装 SDK

### 方式一：通过 Npm 安装

通过 npm 获取安装是使用 Node.js SDK 的推荐方法，npm 是 Node.js 的包管理工具。关于 npm 详细介绍可参见 [ npm 官网](https://www.npmjs.com/) 。

1. 执行以下安装命令：
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考下文使用 SDK 示例。

### 方式二：通过源码包安装

1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，如下 SDK 示例。

## 使用 SDK
### 示例

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

>! 运行时，需要将 secretId、secretKey 替换为真实值。

在支持 typescript 项目中，采用如下方式调用：

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

实例化`Client` 的入参支持 `clientConfig` 数据结构和说明 详见 [ClientConfig](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/common/interface.ts)。

### 更多示例

更丰富的使用 demo，请在[`examples`](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/tree/master/examples)目录中寻找。

## 相关配置

### 代理
如有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用，抛出连接超时的异常现象。

## 旧版 SDK
我们推荐使用新版 Node.js SDK，如果一定要使用旧版 SDK，请前往 [GitHub 仓库下载](https://github.com/CFETeam/qcloudapi-sdk) 。
