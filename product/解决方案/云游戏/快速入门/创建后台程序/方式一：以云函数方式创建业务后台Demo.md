本文主要讲解如何以云函数方式创建业务后台 Demo，通过快速创建云游戏业务 server 的方式完成云游能力接入。
云函数创建方式有2种，开发者可根据自身需求选用：
- [导入云函数](#upload)：基于云游戏提供的 ZIP 文件，导入即可（没有特殊需求推荐使用）。
- [新建云函数](#create)：基于云游戏提供的工程源码，进行 server 开发，二次开发自由度较高。

[](id:upload)
## 导入云函数

1. 访问 [函数服务控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，单击**新建**进入函数创建页。
2. 选择创建方式为“**自定义创建**”，函数类型为“**Web函数**”，部署方式为“**代码部署**”，运行环境为“**Nodejs12.16**”。
3. 在**函数代码**中选择提交方法为“**本地上传zip包**”，单击**上传**，上传云游戏提供的 [ZIP 文件](https://demo-1304469412.cos.ap-guangzhou.myqcloud.com/express_demo-1630920466.zip)，单击**完成**即可完成导入函数操作。
![](https://qcloudimg.tencent-cloud.cn/raw/95d2010dbf05e20d384e1546de9820dd.png)
4. 在**函数管理 > 函数代码** 中打开 `app.js` 文件。`app.js` 文件里定义了2个客户业务后台接口，分别为启动云端游戏（StartCloudGame）和退出云端游戏（StopCloudGame），并通过调用 [云渲染后端 API](https://cloud.tencent.com/document/product/1162/40729) 实现业务逻辑。
>! 需将 `app.js` 文件中的 secretId 和 secretKey 替换为您购买腾讯云游戏的账号的 [API 密钥](https://console.cloud.tencent.com/cam/capi)。
![](https://qcloudimg.tencent-cloud.cn/raw/485873e133b63e2e32b4784e4e0fa1c9.png)
5. 打开**自动安装依赖**，单击**部署**。部署运行云函数后，可以在云函数页面上查看云函数的“访问路径”，构造“测试模版”，进行接口测试。
![](https://qcloudimg.tencent-cloud.cn/raw/d931b6caf5c912a1f8c963fb5af4a92a.png)
6. 记录下后台接口的 server，在构建客户端程序的时候会要用到。
>? server 地址示例：`service-test-xxxxxxxxxx.gz.apigw.tencentcs.com/release`。

[](id:create)
## 新建云函数
1. 访问 [函数服务控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，单击**新建**进入函数创建页。
2. 选择创建方式为 **模板创建** > **Express 框架模版**，单击**下一步**。单击**完成**创建函数，进入函数详情页。
3. 进入**函数管理 > 函数代码**，修改工程中 `package.json` 文件的 dependencies 内容为：
```
......
"dependencies": {
    "body-parser": "^1.19.0",
    "express": "^4.17.1",
    "tencentcloud": "^3.0.1",
    "tencentcloud-sdk-nodejs": "^4.0.195"
  }
```
4. 修改工程中 `app.js` 文件内容为：
```
const express = require('express');
const path = require('path');
const app = express();

// Web 类型云函数，只能监听 9000 端口
app.listen(9000, () => {
  console.log(`Server start on http://localhost:9000`);
});

// parse application/json
var bodyParser = require('body-parser')
var jsonParser = bodyParser.json()
app.use(jsonParser)

// import client models
var tencentcloud = require('tencentcloud-sdk-nodejs');
const GsClient = tencentcloud.gs.v20191118.Client;

// tencent cloud api secret id and key, could be found here: https://console.cloud.tencent.com/cam/capi
var secretId = 'your secretId';
var secretKey = 'your secretKey';

// tencent cloud api client profile
const client = new GsClient({
  credential: {
   secretId,
   secretKey,
  },
  region: "ap-guangzhou",// api region, for example: ap-shanghai, ap-guangzhou, ap-chengdu, ap-beijing
  profile: {
   signMethod: "TC3-HMAC-SHA256",// signature algorithm
   httpProfile: {
    reqMethod: "POST",
    reqTimeout: 30,
   },
  },
});

// 定义接口：启动云端游戏。参数示例{"UserId":"cp4321","GameId":"game-nf771d1e","ClientSession":"xxx"}
app.post('/StartCloudGame', (req, res) => {
  var reqBody = req.body;
  console.log("reqBody=", reqBody);
  
  // step1: 尝试锁定机器
  var trylockWorkerParams = JSON.parse(JSON.stringify(reqBody))
  delete trylockWorkerParams.ClientSession;
  console.log("trylockWorkerParams=", trylockWorkerParams); // 示例{"UserId":"cp4321","GameId":"game-nf771d1e"}
  client.TrylockWorker(trylockWorkerParams).then(
    (response) => {
      console.log("TrylockWorker success res=", response);

      // step2: 创建会话
      client.CreateSession(reqBody).then(
        (response) => {
          console.log("CreateSession success res=", response);
          res.json({code:0, data:response});
        },
        (err) => {
          console.error("CreateSession fail res=", err);
          res.json({code:-2, data:err});
        }
      );
    },
    (err) => {
      console.error("TrylockWorker fail res=", err);
      res.json({code:-1, data:err});
    }
  );
});

// 定义接口：退出云端游戏。参数示例{"UserId":"cp4321"}
app.post('/StopCloudGame', (req, res) => {
  var reqBody = req.body;
  console.log("reqBody=", reqBody); 
  client.StopGame(reqBody).then(
    (response) => {
      console.log("response=", response);
      res.json({code:0, data:response});
    },
    (err) => {
      console.error("response=", err);
      res.json({code:-1, data:err});
    }
  );
});
```
`app.js` 文件里定义了2个客户业务后台接口：启动云端游戏（StartCloudGame）和退出云端游戏（StopCloudGame），并通过调用 [云渲染后端 API](https://cloud.tencent.com/document/product/1162/40729) 实现业务逻辑。
>! 需将 `app.js` 文件中的 secretId 和 secretKey 替换为您购买腾讯云游戏的账号的 [API 密钥](https://console.cloud.tencent.com/cam/capi)。
>![](https://qcloudimg.tencent-cloud.cn/raw/485873e133b63e2e32b4784e4e0fa1c9.png)     
>
>5.  打开**自动安装依赖**，单击**部署**。部署运行云函数后，可以在云函数页面上查看云函数的“访问路径”，构造“测试模版”，进行接口测试。
>![](https://qcloudimg.tencent-cloud.cn/raw/d931b6caf5c912a1f8c963fb5af4a92a.png)
6. 记录下后台接口的 server，在构建客户端程序的时候会要用到。
>? server 地址示例：`service-test-xxxxxxxxxx.gz.apigw.tencentcs.com/release`。



