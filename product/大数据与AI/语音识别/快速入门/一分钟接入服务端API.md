## 操作场景
本文将为您介绍如何使用 API 3.0 Explorer 在线调试语音识别相关接口，并快速将该接口对应的腾讯云开发者工具套件（SDK）集成到本地项目中。

## 操作步骤
### 开通语音识别服务
在调用语音识别相关接口前，您需要进入 [语音识别控制台](https://console.cloud.tencent.com/asr)，进行实名认证和人脸认证，认证完成后，阅读《用户协议》后勾选“我已阅读并同意《用户协议》”，然后单击【立即开通】，即可一键开通**录音文件识别、实时语音识别、一句话识别、录音文件识别极速版、语音流异步识别服务接口**，如需开通营业执照核验或增值税发票核验功能，可前往官网页服务介绍页申请开通，审核通过后即可使用该服务。 
![](https://main.qcloudimg.com/raw/284e58e4eaed33b3ea9e290b0872f920.png)

服务开通成功后，您将获得各项服务对应的免费调用额度，可在 [资源包管理页](https://console.cloud.tencent.com/asr/resourcebundle) 查看。同时您也可以在 [语音识别购买页](https://buy.cloud.tencent.com/asr) 中购买对应语音识别服务的资源包，若免费额度以及资源包调用次数耗尽，接口计费将自动转为后付费方式按月/日进行结算，具体计费标准可以查看语音识别的 [计费概述](https://cloud.tencent.com/document/product/1093/35686)。

### 调试语音识别接口
语音识别服务开通成功后，进入语音识别 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=asr&Version=2019-06-14&Action=CreateAsyncRecognitionTask&SignVersion=) 在线接口调试页面，选择需要调用的接口，并填写**输入参数**。输入参数在 API 3.0 Explorer 界面的“参数说明”选项卡中可以查看对应接口输入参数的具体含义。
>?平台将对登录用户提供临时 Access Key，以便进行调试。

![](https://main.qcloudimg.com/raw/32372679d9f39b46009ec5eaebb302d5.png)

填写**输入参数**后，选择“代码生成”选项卡，可以看到自动生成的不同编程语言代码（可支持 Java、Python、Node.js、PHP、GO、.NET、C++ 语言），生成代码中的部分字段信息和填写内容是关联的，如需调整传入参数，可在左侧修改参数值后重新生成代码。
![](https://main.qcloudimg.com/raw/d2c7cdbf68df6d975bf538babb70b0ba.png)
选择“在线调用”选项卡，单击【发送请求】可进行真实请求，供您调试、参考。
![](https://main.qcloudimg.com/raw/2822cfaacc45d821ea57375409740ace.png)

### 集成语音识别 SDK
确认本地依赖环境满足以下条件：

| 编程环境 | SDK 集成要求 |
|---------|---------|
| Node.js | 需要 NODEJS 10.0.0 版本及以上 |
| Python | 需要 Python 2.7、3.6至3.9版本 |
| Java | 需要 JDK 7 版本及以上 |
| Go | 需要 Go 1.9 版本及以上（如使用 go mod 需要 Go 1.14） |
| .Net | 需要 .NET Framework 4.5+ 或者 .NET Core 2.1 |
| PHP | 需要 PHP 5.6.0 版本及以上 |
| C++ | 需要 C++ 11 或更高版本的编译器 GCC 4.8 或以上版本。暂时仅支持 Linux 环境，不支持 Windows 环境 |
| Ruby | 需要 Ruby 2.3 及以上版本 |

安装与本地依赖环境对应的腾讯云语音识别 SDK，下面将以 Node.js 为例说明 SDK 安装、使用的方法，其他语言的 SDK 使用方法请参考 [腾讯云 SDK 使用手册](https://cloud.tencent.com/document/sdk)。

#### 通过 npm 安装（推荐）
通过 npm 获取安装是使用 NODEJS SDK 的推荐方法，npm 是 NODEJS 的包管理工具。关于 npm 详细可参考 [npm 官网](https://www.npmjs.com/)。
1. 执行以下安装命令：
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考示例。
3. 如上引用方式会将腾讯云所有产品 sdk 下载到本地，可以将 `tencentcloud-sdk-nodejs` 换成 `tencentcloud-sdk-nodejs-cvm/cbs/vpc` 等，即可引用特定产品的 sdk，代码中可将 `require("tencentcloud-sdk-nodejs")` 改为 `require("tencentcloud-sdk-nodejs-cvm/cbs/vpc")`，其余不变，可参考示例，可大大节省存储空间。

#### 通过源码包安装
1. 前往 [GitHub 代码托管地址](https://github.com/TencentCloud/tencentcloud-sdk-nodejs) 或者 [快速下载地址](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/archive/refs/heads/master.zip)，下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，可参考示例。

### 示例
SDK 安装完成后，可在您的项目代码中引用 API 3.0 Explorer 自动生成的代码， 以 Node.js 为例，简易 demo 示例如下：

```
const tencentcloud = require("tencentcloud-sdk-nodejs")

// 导入对应产品模块的 client models。
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
// 实例化要请求产品(以 cvm 为例)的 client 对象
const client = new CvmClient(clientConfig)
// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones().then(
  (data) => {
    console.log(data)
  },
  (err) => {
    console.error("error", err)
  }
)
```

在支持 typescript 项目中，采用如下方式调用：

```
import * as tencentcloud from "tencentcloud-sdk-nodejs"

// 导入对应产品模块的 client models。
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
// 实例化要请求产品(以 cvm 为例)的 client 对象
const client = new CvmClient(clientConfig)
// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones().then(
  (data) => {
    console.log(data)
  },
  (err) => {
    console.error("error", err)
  }
)
```
实例化 Client 的入参支持 clientConfig 数据结构和说明，详请可参见 [ClientConfig](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/common/interface.ts)。

