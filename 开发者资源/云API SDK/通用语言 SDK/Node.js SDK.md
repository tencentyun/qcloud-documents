## 简介
* 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。
* 本文以 Node.js SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。
* 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/document/sdk/Description)，后续会支持其他云产品接入。

## 依赖环境

* Node.js 7.10.1版本及以上。
* 获取安全凭证。安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/78145f9e6a830a188304991552a5c614.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**
* 获取调用地址。调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。具体调用地址可参考对应产品的 [API 文档](https://cloud.tencent.com/document/api)。



## 安装 SDK

通过 npm 获取安装是使用 Node.js SDK 的推荐方法，npm 是 Node.js 的包管理工具。关于 npm 详细可参考 [npm 官网](https://www.npmjs.com/)。 

1. 在命令行中执行以下命令，安装 Node.js SDK。
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考下文示例。 


## 使用 SDK

### 示例1：查询可用区

以 [查询可用区](https://cloud.tencent.com/document/product/213/15728) 接口为例，创建`HelloWorld.js`文件并写入以下代码（运行时，需要将 secretId、secretKey 替换为真实值）：

```js
const tencentcloud = require("tencentcloud-sdk-nodejs");

const CvmClient = tencentcloud.cvm.v20170312.Client;
const models = tencentcloud.cvm.v20170312.Models;

const Credential = tencentcloud.common.Credential;

let cred = new Credential("secretId", "secretKey");

let client = new CvmClient(cred, "ap-shanghai");

let req = new models.DescribeZonesRequest();

client.DescribeZones(req, function(err, response) {
    if (err) {
        console.log(err);
        return;
	}
	console.log(response.to_json_string());
});
```

在命令行中进入`HelloWorld.js`文件所在目录，执行以下命令，即可获取所需内容。
```
node HelloWorld.js
```



### 示例2：查询实例列表

以 [查询实例列表](https://cloud.tencent.com/document/product/213/15707) 接口为例，创建`HelloWorld.js`文件并写入以下代码：

```js
const tencentcloud = require("tencentcloud-sdk-nodejs");

// 导入对应产品模块的client models。
const CvmClient = tencentcloud.cvm.v20170312.Client;
const models = tencentcloud.cvm.v20170312.Models;

const Credential = tencentcloud.common.Credential;
const ClientProfile = tencentcloud.common.ClientProfile;
const HttpProfile = tencentcloud.common.HttpProfile;


// 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
//let cred = new Credential("secretId", "secretKey");
// 可以直接指定，也可以使用环境变量提供账号信息（需要先设置）
let cred = new Credential(process.env.TENCENTCLOUD_SECRET_ID, process.env.TENCENTCLOUD_SECRET_KEY);

// 实例化一个 http 选项，可选的，没有特殊需求可以跳过。
let httpProfile = new HttpProfile();
httpProfile.reqMethod = "POST";
httpProfile.reqTimeout = 30;
httpProfile.endpoint = "cvm.ap-shanghai.tencentcloudapi.com";

// 实例化一个 client 选项，可选的，没有特殊需求可以跳过。
let clientProfile = new ClientProfile();
clientProfile.signMethod = "HmacSHA256";
clientProfile.httpProfile = httpProfile;

// 实例化要请求产品 (以 cvm 为例) 的 client 对象。clientProfile 可选。
let client = new CvmClient(cred, "ap-shanghai", clientProfile);

// 实例化一个请求对象,并填充参数
let req = new models.DescribeInstancesRequest();
let filters = {
	Filters: [
	    {
	        Name: "zone",
	        Values: ["ap-shanghai-1", "ap-shanghai-2"]
	    },
	    {
	        Name: "instance-charge-type",
	        Values: ["POSTPAID_BY_HOUR"]
	    }
	]
};
// 传入 json 参数
req.from_json_string(JSON.stringify(filters));

// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeInstances(req, function(err, response) {
    // 请求异常返回，打印异常信息
    if (err) {
        console.log(err);
        return;
    }
    // 请求正常返回，打印 response 对象
    console.log(response.to_json_string());
});
```

在命令行中进入`HelloWorld.js`文件所在目录，执行以下命令，即可获取所需内容。
```
node HelloWorld.js
```

### 更多示例

您可以在 [github](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 中的`examples`目录下获取更多详细的示例。


## 相关配置

### 代理

若在代理的环境下使用 SDK 进行接口调用，则需设置系统环境变量`https_proxy`，否则可能出现无法正常调用，抛出连接超时异常的现象。





