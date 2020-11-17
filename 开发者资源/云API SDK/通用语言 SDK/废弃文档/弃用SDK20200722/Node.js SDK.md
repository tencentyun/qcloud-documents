本文主要介绍适用于 Node.js 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 Node.js 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。

## 依赖环境

- Node.js 7.10.1 版本及以上。
- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

### 通过 npm 安装（推荐）
[npm](https://www.npmjs.com/) 是 Node.js 的包管理工具。

1. 中国大陆地区的用户可以使用国内镜像源提高下载速度，例如：
```
npm config set registry https://mirrors.tencent.com/npm/
```
2. 执行以下安装命令：
```
npm install tencentcloud-sdk-nodejs --save
```
3. 在您的代码中引用对应模块代码，可参考 [示例](#example)。

### 通过源码包安装
1. 前往 [GitHub 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-nodejs/tencentcloud-sdk-nodejs.zip)，下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，可参考 [示例](#example)。

<span id="example"></span>
## 示例
本文以云服务器查询可用区接口为例，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/tree/master/examples)。

```js
const tencentcloud = require("../../../../tencentcloud-sdk-nodejs");

// 导入对应产品模块的 client models
const CvmClient = tencentcloud.cvm.v20170312.Client;
const models = tencentcloud.cvm.v20170312.Models;

const Credential = tencentcloud.common.Credential;

// 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
let cred = new Credential("secretId", "secretKey");

// 实例化要请求产品（以 CVM 为例）的 client 对象
let client = new CvmClient(cred, "ap-shanghai");

// 实例化一个请求对象
let req = new models.DescribeZonesRequest();

// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones(req, function(errMsg, response) {
    // 请求异常返回，打印异常信息
    if (errMsg) {
        console.log(errMsg);
        return;
    }
    // 请求正常返回，打印 response 对象
    console.log(response.to_json_string());
});
```


## 旧版 SDK
我们推荐使用新版 Node.js SDK，如果需要使用旧版 SDK，请前往 [GitHub 仓库](https://github.com/CFETeam/qcloudapi-sdk) 下载。
