### <h3 id="step1">步骤1：环境部署</h3>
`cloudapi.js` 是 Node.js 版的云 API 调用实例，自行安装 Node.js 运行环境。将 `cloudapi.js` 中的 SecretId 和 SecretKey，替换成您的腾讯云帐号下的 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 信息。

**cloudapi.js 示例代码如下：**
```
var express = require('express');
var router = express.Router();
var uuid = require('uuid');
// 导入对应产品模块的client models。
var tencentcloud = require('tencentcloud-sdk-nodejs');
const gsClient = tencentcloud.gs.v20191118.Client;
const gsModels = tencentcloud.gs.v20191118.Models;
const Credential = tencentcloud.common.Credential;
const ClientProfile = tencentcloud.common.ClientProfile;
const HttpProfile = tencentcloud.common.HttpProfile;

// 腾讯云API密钥
var secretId = 'your secretId';
var secretKey = 'your secretKey';

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
    clientInfo.Appid = clientInfo.Appid || 12345678;
    clientInfo.RequestID = uuid.v4();
    clientInfo.Action = 'TrylockWorker';

    // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    //let cred = new Credential("secretId", "secretKey");
    // 可以直接指定，也可以使用环境变量提供账号信息（需要先设置）
    let cred = new Credential(secretId, secretKey);

    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    let httpProfile = new HttpProfile();
    httpProfile.reqMethod = "POST";
    httpProfile.reqTimeout = 30;
    httpProfile.endpoint = "gs.tencentcloudapi.com";

    // 实例化一个client选项，可选的，没有特殊需求可以跳过。
    let clientProfile = new ClientProfile();
    clientProfile.signMethod = "HmacSHA256";
    clientProfile.httpProfile = httpProfile;

    var client = new gsClient(cred, "ap-guangzhou", clientProfile);
    // 实例化一个请求对象,并填充参数
    let apireq = new gsModels.TrylockWorkerRequest();
    // 传入json参数
    apireq.from_json_string(JSON.stringify(clientInfo));

    try{
        // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
        client.TrylockWorker(apireq, function(err, response) {
            // 请求异常返回，打印异常信息
            if (err) {
                console.log(err);
                res.json({code:-1, data: err});
                return;
            }
            // 请求正常返回，打印response对象
            console.log(response.to_json_string());
            res.json({code:0, data: JSON.parse(response.to_json_string())});
        });
    } catch (e) {
        res.json({code:-1, data: e});
    }
});

router.post('/get_signature', jsonParser, function(req, res, next) {
    var clientInfo = req.body;
    clientInfo.Appid = clientInfo.Appid || 12345678;
    clientInfo.RequestID = uuid.v4();
    clientInfo.Action = 'CreateSession';

    // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    //let cred = new Credential("secretId", "secretKey");
    // 可以直接指定，也可以使用环境变量提供账号信息（需要先设置）
    let cred = new Credential(secretId, secretKey);

    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    let httpProfile = new HttpProfile();
    httpProfile.reqMethod = "POST";
    httpProfile.reqTimeout = 30;
    httpProfile.endpoint = "gs.tencentcloudapi.com";

    // 实例化一个client选项，可选的，没有特殊需求可以跳过。
    let clientProfile = new ClientProfile();
    clientProfile.signMethod = "HmacSHA256";
    clientProfile.httpProfile = httpProfile;

    var client = new gsClient(cred, "ap-guangzhou", clientProfile);
    // 实例化一个请求对象,并填充参数
    let apireq = new gsModels.CreateSessionRequest();
    // 传入json参数
    apireq.from_json_string(JSON.stringify(clientInfo));

    try{
        // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
        client.CreateSession(apireq, function(err, response) {
            // 请求异常返回，打印异常信息
            if (err) {
                console.log(err);
                res.json({code:-1, data: err});
                return;
            }
            // 请求正常返回，打印response对象
            //console.log(response.to_json_string());
            res.json({code:0, data: JSON.parse(response.to_json_string())});
        });
    } catch (e) {
        res.json({code:-1, data: e});
    }
});

router.post('/stopgame', jsonParser, function(req, res, next) {
    var clientInfo = req.body;
    clientInfo.Appid = clientInfo.Appid || 12345678;
    clientInfo.RequestID = uuid.v4();
    clientInfo.Action = 'StopGame';

    // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    //let cred = new Credential("secretId", "secretKey");
    // 可以直接指定，也可以使用环境变量提供账号信息（需要先设置）
    let cred = new Credential(secretId, secretKey);

    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    let httpProfile = new HttpProfile();
    httpProfile.reqMethod = "POST";
    httpProfile.reqTimeout = 30;
    httpProfile.endpoint = "gs.tencentcloudapi.com";

    // 实例化一个client选项，可选的，没有特殊需求可以跳过。
    let clientProfile = new ClientProfile();
    clientProfile.signMethod = "HmacSHA256";
    clientProfile.httpProfile = httpProfile;

    var client = new gsClient(cred, "ap-guangzhou", clientProfile);
    // 实例化一个请求对象,并填充参数
    let apireq = new gsModels.StopGameRequest();
    // 传入json参数
    apireq.from_json_string(JSON.stringify(clientInfo));

    try{
        // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
        client.StopGame(apireq, function(err, response) {
            // 请求异常返回，打印异常信息
            if (err) {
                console.log(err);
                res.json({code:-1, data: err});
                return;
            }
            // 请求正常返回，打印response对象
            //console.log(response.to_json_string());
            res.json({code:0, data: JSON.parse(response.to_json_string())});
        });
    } catch (e) {
        res.json({code:-1, data: e});
    }
});


module.exports = router;

```
### <h3 id="step2">步骤2：创建 express 项目</h3>
使用 express-generator 初始化一个 express 项目。
```
    express myproj
    npm i
```

### <h3 id="step3">步骤3：安装依赖库</h3>
```
    npm install --save express tencentcloud tencentcloud-sdk-nodejs
```
### <h3 id="step4">步骤4：调用云 API</h3>
参考示例代码编写 [cloudapi.js](#step1)，修改 app.js，在后面加入一行。
```
    app.use('/cloudapi', require('./cloudapi.js'));
```
### <h3 id="step5">步骤5：运行服务</h3>
```
    npm run
```
### <h3 id="step6">步骤6：启动云游戏</h3>
网页端发送 JSON 格式的 POST 请求 `http://127.0.0.1:3000/cloudapi/get_signature` 接口，返回值里获取 ServerSession 字段，调用 [TCGSDK.start(ServerSession)](https://cloud.tencent.com/document/product/1162/46134#tcgsdk.start(serversession)) 接口启动云游戏。

