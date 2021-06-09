[](id:step1)

### 步骤1：环境部署

`cloudapi.js` 是 Node.js 版的云 API 调用实例，自行安装 Node.js 运行环境。将 `cloudapi.js` 中的 SecretId 和 SecretKey，替换成您的腾讯云帐号下的 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 信息。

**cloudapi.js 示例代码如下：**
<dx-codeblock>
::: JavaScript JavaScript
var express = require('express');
var router = express.Router();
var uuid = require('uuid');
// 导入对应产品模块的client models。
var tencentcloud = require('tencentcloud-sdk-nodejs');
const GsClient = tencentcloud.gs.v20191118.Client;

// 腾讯云API密钥，可以在控制台创建, https://console.cloud.tencent.com/cam/capi
var secretId = 'your secretId';
var secretKey = 'your secretKey';

// 实例化要请求产品的client对象。profile可选。
const client = new GsClient({
    credential: {
      secretId,
      secretKey,
    },
    region: "ap-shanghai",// 调用区域，可以就近改为ap-guangzhou、ap-chengdu、ap-beijing
    profile: {
      signMethod: "TC3-HMAC-SHA256",// 签名算法
      httpProfile: {
        reqMethod: "POST",
        reqTimeout: 30,// 请求超时
      },
    },
})

var jsonParser = function(req, res, next) {
    var arr = '';
    req.on('data', buff => {
        arr += buff;
    });
    req.on('end', _ => {
        req.body = JSON.parse(arr);
        next();
    });
}

var rawParser = function(req, res, next) {
    var arr = '';
    req.on('data', buff => {
        arr += buff;
    });
    req.on('end', () => {
        req.body = arr;
        next();
    });
}

var getClientIp = function(req) {
    return req.headers['x-forwarded-for'] ||
        req.headers['x-real-ip'] || 
        req.connection.remoteAddress ||
        req.socket.remoteAddress ||
        req.connection.socket.remoteAddress;
}

router.get('/get_wan_ip', function(req, res, next){
    var clientIp = getClientIp(req).replace(/::ffff:/, '');
    var data = JSON.stringify({cip: clientIp});
    var body = `var returnCitySN = ${data};`;
    res.end(body);
});

router.post('/try_lock', jsonParser, function(req, res, next){
    var clientInfo = req.body;
    clientInfo.RequestID = uuid.v4();

    client.TrylockWorker(clientInfo).then((response) => {
        // 请求正常返回，打印response对象
        console.log(response);
        res.json({code:0, data: response});
    },
    (err) => {
        console.log(err);
        res.json({code:-1, data: err});
    });

});

router.post('/get_signature', jsonParser, function(req, res, next) {
    var clientInfo = req.body;
    clientInfo.RequestID = uuid.v4();

    client.CreateSession(clientInfo).then((response) => {
        // 请求正常返回，打印response对象
        console.log(response);
        res.json({code:0, data: response});
    },
    (err) => {
        console.log(err);
        res.json({code:-1, data: err});
    });

});

router.post('/stopgame', jsonParser, function(req, res, next) {
    var clientInfo = req.body;
    clientInfo.RequestID = uuid.v4();

    client.StopGame(clientInfo).then((response) => {
        // 请求正常返回，打印response对象
        console.log(response);
        res.json({code:0, data: response});
    },
    (err) => {
        console.log(err);
        res.json({code:-1, data: err});
    });

});


module.exports = router;
:::
</dx-codeblock>



[](id:step2)

### 步骤2：创建 express 项目

使用 express-generator 初始化一个 express 项目。

```
    express myproj
    npm i
```

[](id:step3)

### 步骤3：安装依赖库

```
		npm install --save express tencentcloud tencentcloud-sdk-nodejs uuid
```

[](id:step4)

### 步骤4：调用云 API

参考示例代码编写 [cloudapi.js](#step1)，修改 `app.js`，在后面加入一行。

```
    app.use('/cloudapi', require('./cloudapi.js'));
```

[](id:step5)

### 步骤5：运行服务

```
    npm run
```

[](id:step6)

### 步骤6：启动云游戏

网页端发送 `try_lock` 请求，锁定机器成功后，再调用 `get_signature`，返回值获得 ServerSession 字段，然后调用 [TCGSDK.start(ServerSession)](https://cloud.tencent.com/document/product/1162/46134#tcgsdk.start(serversession)) 接口启动云游戏。

