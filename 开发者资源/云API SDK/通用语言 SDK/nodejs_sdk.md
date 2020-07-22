## 简介

- 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。
- SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。本文以 NODEJS SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。首次使用 NODEJS SDK 3.0 的简单示例见下文，您可通过本文快速获取腾讯云 NODEJS SDK 3.0 并开始进行调用。
- 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/product)，后续会支持其他云产品接入。


## 步骤1：搭建所需环境

### 配置语言环境

#### 1. 下载安装

>!支持 NODEJS 7.10.1 版本及以上。

1.  [NODEJS 官网]( https://nodejs.org/en/ ) 下载安装包，本文以 node-v12.18.0-x64.msi 版本为例。
2. 双击`node-v12.18.0-x64.msi`，打开安装窗口：
	1. 单击【Next】。
![](https://main.qcloudimg.com/raw/c5d56f40ff0020c226a555f6fdaf97c2.png)
	2. 勾选后，单击【Next】。
![](https://main.qcloudimg.com/raw/a98a08ae174f6cb37362bf8ced1d1d40.png)
	3. 选择安装目录，单击【Next】。
![](https://main.qcloudimg.com/raw/53b0fb3d36248ee2279c859925ab3bc9.png) 
	4. 选择安装项，本文选择默认，单击【Next】。
![](https://main.qcloudimg.com/raw/46f45b756797ead72991489518484497.png) 
	5. 根据个人情况进行勾选，本文默认不勾选，单击【Next】。
![](https://main.qcloudimg.com/raw/d0c671869eebc7aa43741b19f31e8134.png) 
	6. 单击【Install】，开始安装。
![](https://main.qcloudimg.com/raw/a02e41efca53cbe62695ca42c7b7ed6c.png) 
	7. 等待安装完成，单击【Finish】完成安装。
![](https://main.qcloudimg.com/raw/418cfd6e49999167c7fdb82f9fd8abd4.png)
3. 安装完成后，按 **Win+R** 打开运行窗口，输入 cmd 并单击【确定】，打开“命令行窗口”，输入命令查看 Nodejs 版本。
```bash
node -V
npm -v
```
返回结果如下图所示，即表明已成功安装 node-v12.18.0。
![](https://main.qcloudimg.com/raw/58d407701b8993ca6ae527634eb2f1db.png)

#### 2. 配置 npm 全局模块缓存

1. 配置 npm 的全局模块存放路径以及缓存 cache：
在 Nodejs 的安装主目录中新建文件夹：“node_cache”和“node_global”（本文的安装路径是`F:\saftware\language\nodejs`）。 
![](https://main.qcloudimg.com/raw/f05a49034d8c5b463792c0212aa60e50.png)
2. 在命令窗口执行命令，使设置生效：
```js
# 输入命令
npm config set prefix "F:\saftware\language\nodejs\node_global"
npm config set cache "F:\saftware\language\nodejs\node_cache"
# 查看默认全局模块存放路径
npm list -g
```
![](https://main.qcloudimg.com/raw/fb7f3caf9bf578d5fe27f58b544d39ac.png) 

#### 3. 配置环境变量

配置环境变量：【我的电脑】>【属性】>【高级系统设置】>【环境变量】>【系统变量】。
<img src="https://main.qcloudimg.com/raw/0946c8544324227a4ba405b0fe4a97ee.png" width="600"><span/>
- 新建变量名：NODE_HOME，变量值：安装路径主目录。
![](https://main.qcloudimg.com/raw/be5f3c192822efb7cd3985fdc4c78ad7.png)
- 新建变量名：NODE_PATH，变量值：存放全局包的路径。
![](https://main.qcloudimg.com/raw/102249823860fdb04985d5976117bb60.png)   
- 配置【Path】：将系统设置的`F:\saftware\language\nodejs\`路径，改为 %NODE_HOME%，并且新增上文所建的 node_global 路径。
![](https://main.qcloudimg.com/raw/cce0919f6f02a9a9460c0e950b4f9428.png) 

#### 4. 配置镜像源（加速下载）

中国大陆地区的用户可以使用国内镜像源提高下载速度。

命令窗口执行：
```
npm config set registry https://mirrors.tencent.com/npm/

# 查看是否设置成功
npm config get registry
```

配置完后，安装个 module 进行测试：

```
# -g 是全局安装的意思 
npm install express -g
```

>!如果安装时不加 -g 参数，模块就会默认安装在当前路径下。
![](https://main.qcloudimg.com/raw/b1e2dc9501ac6ff661532a4f4782f0f5.png) 



### 产品开通

登录 [腾讯云控制台](https://console.cloud.tencent.com/) 并开通需使用产品，您可通过控制台进行搜索。如下图所示：
![](https://main.qcloudimg.com/raw/af625557f35ff329afecf7eceb06bc29.png)


### 获取凭证

安全凭证包含 SecretId 及 SecretKey 两部分。SecretId 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，即可进行获取，如下图所示：
![](https://main.qcloudimg.com/raw/0b064499a40369f8f57a3aea88455a9c.png)
>!**您的安全凭证代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。**

### 获取调用地址

调用地址（endpoint）一般形式为`*.tencentcloudapi.com`，产品的调用地址有一定区别，详情请参见各产品下的“请求结构”文档。例如，云服务器的调用地址为`cvm.tencentcloudapi.com`。




## 步骤2：安装 SDK

通过 npm 获取安装是使用 NODEJS SDK 的推荐方法，npm 是 NODEJS 的包管理工具。关于 npm 详细可参考 [npm 官网](https://www.npmjs.com/)。 

1. 在命令行中执行以下命令，安装 NODEJS SDK。
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考下文示例。 


## 步骤3：使用 SDK

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



