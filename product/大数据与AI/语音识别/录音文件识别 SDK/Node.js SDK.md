## 接入准备
### SDK获取
录音文件识别 Node.js SDK 以及 Demo 的下载地址：[Node.js SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/record/nodejs_record_asr_sdk_v3.zip) 
### 接入须知
开发者在调用前请先查看录音文件识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37139)，了解**接口要求**和**接口使用步骤**。
### 开发环境
- **环境依赖**
该接口支持 Node.js 7.10.1 及以上版本。
- **安装 SDK**
下载文件后解压缩，添加文件到代码编辑器（WebStorm、VSCode 或其他编辑器），在`nodejs_record_asr_sdk_v3` 文件夹下执行` npm install `命令安装依赖。

## 快速接入
`demo`文件夹下：`localRecordFileRequest.js` 以及`urlRequest.js` 为录音识别请求 demo，`recognizeResult.js` 为轮询识别结果的 demo。

1. 通过下面的录音文件识别请求中的两种接入方式的 demo 或是直接运行 demo 文件夹下的 js 文件快速请求，进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取 AppID、SecretId、SecretKey，并在代码中对应的位置配置好用户参数。

2. 然后通过运行 demo 文件夹下的 js 文件 或 在项目中使用以下的 demo，来快速获取识别结果。


### 录音识别请求

#### 通过语音 URL 请求
``` js
//将 require 中路径替换为项目中 SDK 的真实路径
const tencentcloud = require("../nodejs_record_asr_sdk_v3");

// 导入对应产品模块的 client models 以及需要用到的模块
const AsrClient = tencentcloud.asr.v20190614.Client;
const models = tencentcloud.asr.v20190614.Models;
const Credential = tencentcloud.common.Credential;
const ClientProfile = tencentcloud.common.ClientProfile;
const HttpProfile = tencentcloud.common.HttpProfile;

// Your SecretId、Your SecretKey 需要替换成客户自己的账号信息
let cred = new Credential("Your SecretId", "Your SecretKey");

let httpProfile = new HttpProfile();
httpProfile.reqMethod = "POST";
httpProfile.reqTimeout = 30;
httpProfile.endpoint = "asr.tencentcloudapi.com";

let clientProfile = new ClientProfile();
clientProfile.httpProfile = httpProfile;
clientProfile.signMethod = "TC3-HMAC-SHA256";
// 实例化要请求产品(asr)的 client 对象
let client = new AsrClient(cred, "", clientProfile);

//通过语音 URL 方式调用 

// 实例化一个请求对象
let req = new models.CreateRecTaskRequest();
// 设置接口需要的参数，参考 接入须知 中 [请求接口说明]
req.EngineModelType = '16k_0';
req.ChannelNum = 1;
req.ResTextFormat = 0;
req.SourceType = 0;
req.Url = 'https://ruskin-1256085166.cos.ap-guangzhou.myqcloud.com/test.wav';

// 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.CreateRecTask(req, function(errMsg, response) {
    if (errMsg) {
        console.log(errMsg);
        return;
    }

    console.log(response.to_json_string());
});
```
#### 通过上传本地录音文件请求

``` js
//将require中路径替换为项目中 SDK 的真实路径
const tencentcloud = require("../nodejs_record_asr_sdk_v3");

// 导入对应产品模块的 client models 以及需要用到的模块
const AsrClient = tencentcloud.asr.v20190614.Client;
const models = tencentcloud.asr.v20190614.Models;
const Credential = tencentcloud.common.Credential;
const ClientProfile = tencentcloud.common.ClientProfile;
const HttpProfile = tencentcloud.common.HttpProfile;

// Your SecretId、Your SecretKey 需要替换成客户自己的账号信息
let cred = new Credential("Your SecretId", "Your SecretKey");

let httpProfile = new HttpProfile();
httpProfile.reqMethod = "POST";
httpProfile.reqTimeout = 30;
httpProfile.endpoint = "asr.tencentcloudapi.com";

let clientProfile = new ClientProfile();
clientProfile.httpProfile = httpProfile;
clientProfile.signMethod = "TC3-HMAC-SHA256";
// 实例化要请求产品(asr)的 client 对象
let client = new AsrClient(cred, "", clientProfile);

//通过本地语音上传方式调用 

const fs = require('fs');
const path = require('path');
//需要将"本地录音文件地址"替换为用户录音文件地址，例：'./test.wav'
let filePath = path.resolve('本地录音文件地址');
let data = fs.readFileSync(filePath);
//将音频文件转为 base64 格式，注意：转为 base64 后数据要小于5MB，否则不能成功请求识别
data = Buffer.from(data).toString('base64'); 
//此数据长度为数据未进行 base64 编码时的数据长度
let dataLen = fs.statSync('本地录音文件地址').size;

// 实例化一个请求对象
let req = new models.CreateRecTaskRequest();
// 设置接口需要的参数，参考 接入须知 中 [请求接口说明]
req.EngineModelType = '16k_0';
req.ChannelNum = 1;
req.ResTextFormat = 0;
req.SourceType = 1;
req.Data = data;
req.DataLen = dataLen;

// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.CreateRecTask(req, function(errMsg, response) {
    if (errMsg) {
        console.log(errMsg);
        return;
    }

    console.log(response.to_json_string());
});
```
### 识别结果查询
#### 录音文件识别结果查询
```js
//调用录音识别结果查询接口
let reqResult = new models.DescribeTaskStatusRequest();
//reqResult.TaskId 为创建识别任务时 response 里的 TaskId 字段
//示例 TaskId 不可用，需要客户替换成可用 TaskId
reqResult.TaskId = 080387961;

client.DescribeTaskStatus(reqResult, function(errMsg, response) {
    if (errMsg) {
        console.log(errMsg);
        return;
    }

    console.log(response.to_json_string());
});
```
