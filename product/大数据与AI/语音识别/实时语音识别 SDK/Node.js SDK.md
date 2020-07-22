## 接入准备
### SDK获取
实时语音识别 Node.js SDK 以及 Demo 的下载地址： [Node.js SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/realtime/nodejs_realtime_asr_sdk_v1.zip) 
### 接入须知
开发者在调用前请先查看实时语音识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37138)，了解接口的**使用要求**和**使用步骤**。
### 开发环境
- **环境依赖**
该接口支持 Node.js 7.10.1 及以上版本。
- **安装 SDK**
下载文件后解压缩，添加文件到代码编辑器（WebStorm、VSCode或其他编辑器），在 nodejs_realtime_asr_sdk_v1 文件夹下执行`npm install`命令安装依赖。

## 快速接入
demo 文件夹下：localRecordFile.js 为整个文件的识别请求 demo，oneFragmentation.js 为某个分片的识别请求demo。
1. 通过下面的实时语音识别请求中的两种接入方式的 demo 或是运行 demo文件夹 下的js文件快速请求，进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取 AppID、SecretId、SecretKey，并在代码中对应位置配置好用户需要的参数。
2. 然后通过运行 demo文件夹 下的 js 文件 或 在项目中使用以下的 demo，来快速获取识别结果。


### 实时语音识别请求

#### 整个文件识别请求
``` js
const fs = require("fs");
const path = require('path');

//引入 SDK 和相关模块
//将 require 中路径替换为项目中 SDK 的真实路径
const tencentcloud = require("../../nodejs_realtime_asr_sdk_v1");
const Asr = tencentcloud.asrRealtime;
const Config = tencentcloud.config;


//Config实例的三个参数分别为 SecretId, SecretKey, appId。请前往控制台获取后修改下方参数
let config = new Config("Your SecretId","Your SecretKey",1200000000);


//设置接口需要参数，具体请参考 实时语音识别接口说明
let query = {
  engineModelType : '16k_0',
  resultTextFormat : 0,
  resType : 0,
  voiceFormat : 1,
  cutLength : 50000,
}
//创建调用实例
const asrReq = new Asr(config, query);

//调用方式1:识别整个文件
//需要将"本地文件地址"替换为用户需要识别的文件地址，例：'./test.wav'
let filePath = path.resolve('本地录音文件地址');
let data = fs.readFileSync(filePath);

//发送识别请求，sendVoice函数最后一个参数为文件分片请求返回时触发的回调，可根据业务修改
//error为请求错误，response为请求响应，data为请求结果
asrReq.sendVoice(data, (error, response, data) => {
  if(error){
    console.log(error);
    return;
  }
  console.log(data);
});
```
#### 分片识别请求

``` js
const fs = require("fs");
const path = require('path');

//引入 SDK 和相关模块
//将 require 中路径替换为项目中 SDK 的真实路径
const tencentcloud = require("../../nodejs_realtime_asr_sdk_v1");
const Asr = tencentcloud.asrRealtime;
const Config = tencentcloud.config;


//Config实例的三个参数分别为 SecretId, SecretKey, appId。请前往控制台获取后修改下方参数
let config = new Config("Your SecretId","Your SecretKey",1200000000);



//设置接口需要参数，具体请参考 实时语音识别接口说明
let query = {
  engineModelType : '16k_0',
  resultTextFormat : 0,
  resType : 0,
  voiceFormat : 1,
  cutLength : 50000,
}
//创建调用实例
const asrReq = new Asr(config, query);


//调用方式2:识别某个分片，test.wav 为示例分片
//发送请求时需要用户自行维护3个变量：voiceId：创建后保持不变； seq：递增； endFlag：前面为0，发送尾部分片的请求时设置为1
//需要将"本地文件地址"替换为用户需要识别的文件地址，例：'./test.wav'
let filePathTestOne = path.resolve('本地文件地址');
let dataTest = fs.readFileSync(filePathTestOne);
let vioceId = asrReq.randStr(16);
let seq = 0;
let endFlag = 1;

//发送识别请求，sendRequest 函数最后一个参数为请求返回时触发的回调，可根据业务修改
asrReq.sendRequest(dataTest, vioceId, seq, endFlag, (error, response, data) => {
  if(error){
    console.log(error);
    return;
  }
  console.log(data);
});
```
