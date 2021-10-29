

[](id:step1)
### 步骤1：环境部署
[cloudapi.js](https://cloud.tencent.com/document/product/1162/47523?!editLang=zh&!preview#cloudapi) 是 Node.js 版的云 API 调用实例，自行安装 Node.js 运行环境。将 `cloudapi.js` 中的 SecretId 和 SecretKey，替换成您的腾讯云帐号下的 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 信息。


**cloudapi.js 示例代码如下：**[](id:cloudapi)
<dx-codeblock>
::: JavaScript JavaScript
var express = require('express');
var router = express.Router();
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
    region: "ap-shanghai",// cloud api region, for example: ap-shanghai, ap-guangzhou, ap-chengdu, ap-beijing
    profile: {
        signMethod: "TC3-HMAC-SHA256",// signature algorithm
        httpProfile: {
            reqMethod: "POST",
            reqTimeout: 30,
        },
    },
});

var paramsVerify = (req, res, next) => {
    try {
        if (!req.body || typeof ("") == typeof (req.body)) {
            throw 'request body is null or did not parse as json';
        }

        ["Appid", "Action", "Version", "Region"].forEach((item, _) => {
            if (item in req.body) {
                throw `${item} is not required`;
            }
        });
    } catch (err) {
        res.json({ code: -1, data: err });
        return;
    }
    next();
};

// support forward proxy
var getClientIp = (req) => {
    var ips = req.headers['x-forwarded-for'] ||
        req.headers['x-real-ip'] ||
        req.connection.remoteAddress ||
        req.socket.remoteAddress ||
        req.connection.socket.remoteAddress;
    return ips ? ips.split(',')[0].trim() : "";
};

// API for get client WAN ip
router.get('/get_wan_ip', (req, res, next) => {
    var clientIp = getClientIp(req).replace(/::ffff:/, '');// ipv4-over-ipv6 to ipv4
    var data = JSON.stringify({ cip: clientIp });
    var body = `var returnCitySN = ${data};`;
    res.end(body);
});

// try to lock an instance
router.post('/TrylockWorker', paramsVerify, (req, res, next) => {
    var clientInfo = req.body;

    client.TrylockWorker(clientInfo).then((response) => {
        // normally
        console.log(response);
        res.json({ code: 0, data: response });
    }, (err) => {
        // error
        console.log(err);
        res.json({ code: -1, data: err });
    });
});

// connect to locked instance
router.post('/CreateSession', paramsVerify, (req, res, next) => {
    var clientInfo = req.body;

    client.CreateSession(clientInfo).then((response) => {
        // normally
        console.log(response);
        res.json({ code: 0, data: response });
    }, (err) => {
        // error
        console.log(err);
        res.json({ code: -1, data: err });
    });
});

// release instance
router.post('/StopGame', paramsVerify, (req, res, next) => {
    var clientInfo = req.body;

    client.StopGame(clientInfo).then((response) => {
        // normally
        console.log(response);
        res.json({ code: 0, data: response });
    }, (err) => {
        // error
        console.log(err);
        res.json({ code: -1, data: err });
    });
});


module.exports = router;
:::
</dx-codeblock>


[](id:step2)
### 步骤2：创建 express 项目
使用 `express-generator` 初始化一个 express 项目。
```
express myproj
npm i
```

[](id:step3)
### 步骤3：安装依赖库
```
npm install --save express tencentcloud tencentcloud-sdk-nodejs
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
