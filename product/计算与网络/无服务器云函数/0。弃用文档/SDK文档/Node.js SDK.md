## 开发准备
安装 Node.js SDK 前，需要先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey， SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 开发环境
Node.js 8.9 版本

### 通过 npm 安装
通过 npm 获取安装是使用 NODEJS SDK 的推荐方法，npm 是 Node.js 的包管理工具。关于 npm 详细可参考 [npm 官网](https://www.npmjs.com/) 。
1. 执行以下安装命令：
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，请参考下面的示例。

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，请参考下面的示例。

## 接口列表
| 接口名称 | 接口功能                            |
| :--- | :------------------------------------ |
| [CreateFunction](https://cloud.tencent.com/document/api/583/18586)   | 创建函数          |
| [DeleteFunction](https://cloud.tencent.com/document/api/583/18585)   | 删除函数          |
| [GetFunction](https://cloud.tencent.com/document/api/583/18584)      | 获取函数详细信息   |
| [GetFunctionLogs](https://cloud.tencent.com/document/api/583/18583)  | 获取函数运行日志   |
| [Invoke](https://cloud.tencent.com/document/api/583/17243)           | 运行函数          |
| [ListFunctions](https://cloud.tencent.com/document/api/583/18582)    | 获取函数列表       |
| [UpdateFunctionCode](https://cloud.tencent.com/document/api/583/18581)  | 更新函数代码    |
| [UpdateFunctionConfiguration](https://cloud.tencent.com/document/api/583/18580)  | 更新函数配置|

## 示例
```
'use strict';

const tencentcloud = require("/var/user/tencentcloud-sdk-nodejs");
const Credential = tencentcloud.common.Credential;

// 导入对应产品模块的client models。
const ScfClient = tencentcloud.scf.v20180416.Client;
const models = tencentcloud.scf.v20180416.Models;

exports.main_handler = (event, context, callback) => {
    console.log("Hello World")
    console.log(event)
    // console.log(context)
    callback(null, event); 

    // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    let cred = new Credential("AKIxxxxxxPDpqj3C", "75rxxxxxxyJSODrMkx");

     // 实例化要请求产品的client对象，以及函数所在的地域
    let client = new ScfClient(cred, "ap-shanghai");


    // 实例化一个请求对象,获取函数列表
    console.log("Start ListFunctions")
    let req = new models.ListFunctionsRequest();
    // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
    client.ListFunctions(req, function(err, response) {
        // 请求异常返回，打印异常信息
        if (err) {
          console.log(err);
         return;
        }
        // 请求正常返回，打印response对象
        console.log(response.to_json_string());
    });

    // 实例化一个请求对象,调用invoke()
    console.log("Start Invoke")
    let request = new models.InvokeRequest();
    // 接口参数,输入需要调用的函数名，RequestResponse(同步) 和 Event(异步)
    let params = '{"FunctionName":"test_python", "InvocationType":"RequestResponse"}'
    request.from_json_string(params);  
    // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
    client.Invoke(request, function(err, response) {
        // 请求异常返回，打印异常信息
        if (err) {
          console.log(err);
         return;
        }
        // 请求正常返回，打印response对象
        console.log(response.to_json_string());
    },"test_python","RequestResponse");

};

```
## 打包部署
如果需要在云函数控制台中部署函数，并使用 SDK 调用其他函数，则需要把 tencentcloud 的库和函数代码一起打包成 zip 文件。

- 注意在控制台创建函数时的执行方法，需要和 zip 文件里的代码文件和执行函数对应。
- 最终生成的 zip 包如果大于50MB，需要通过 COS 上传。
- 云 API 默认限频为每秒20次，如需提升并发上限，可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&step=1) 申请。

## 相关信息
您也可以使用腾讯云云函数 SDK（Tencentserverless SDK），该 SDK 集成云函数业务流接口，简化云函数的调用方法，使您无需再进行公有云 API 接口的封装。详情请参见 [函数间调用 SDK](https://cloud.tencent.com/document/product/583/37316)。
