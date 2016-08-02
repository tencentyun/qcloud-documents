## 1 功能说明 

1. Node.js Server SDK将调用RESTAPI的底层操作封装成js库，并以接口类的方式暴露给开发者，具体参见lib文件夹下TimRestApi.js ；
2. 提供TimRestApiGear.js示例工具，可直接访问RestAPI；
3. 提供压力测试工具TimSendGroupMsgPressTest.js，可测试在群内发送消息时，客户端接收消息能力。

## 2 Node.js Server SDK集成 

支持[独立模式](/doc/product/269/独立模式)。

### 2.1 API集成示例代码（独立模式） 

该示例代码是TimRestApiGear.js的简化版本，详情可直接参考TimRestApiGear.js。
```
var TimRestAPI = require('/path/lib/TimRestApi.js');
// 设置REST API调用基本参数
var config = {
    sdkAppid: '1400001111',
    identifier: 'admin',
    accountType: '106',
    version: '201512300000',
    privateKey: '/path/private.pem',
    expireAfter: 30 * 24 * 3600,
};

// 创建api对象
var api = new TimRestAPI(config);

// 调用api的成员函数，实现REST API的调用，以下单发消息，群组内发送文本消息为示例：
// 单发消息
api.init(function(err, data) {
    if (err) {
        // deal error
        console.log(err);
        return;
    }
    var reqBody = {
        "To_Account": "86-18688732391",
        //消息接收者
        "From_Account": "86-18602833226",
        //消息发送者
        "MsgRandom": 123,
        //消息随机数
        "MsgBody": [{
            "MsgType": "TIMTextElem",
            //文本消息类型
            "MsgContent": {
                "Text": "hello" //具体文本消息
            }
        }]
    }
    api.request("openim", "sendmsg", reqBody,
    function(err, data) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(data);
    })
});

// 群组内发送消息
api.init(function(err, data) {
    if (err) {
        // deal error
        console.log(err);
        return;
    }
    var reqBody = {
        GroupId: "UserDefinedGroupId",
        MsgBody: [{
            MsgType: "TIMTextElem",
            From_Account: "86-18602833226",
            MsgContent: {
                Text: "hello"
            }
        }]
    };
    api.request("group_open_http_svc", "send_group_msg", reqBody,
    function(err, data) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(data);
    })
});
```

## 3 群内发送消息压力测试脚本使用说明 
在互动直播场景，消息量比较大时，由于弹幕等渲染操作，客户端可能会承受比较大的压力，建议在上线之前，用此工具来测试客户端性能。
使用方法：执行node TimSendGroupMsgPressTest.js 可看到压测脚本工具访问命令(用法)。
注意事项：压测前需要确保群组存在，并且群内人数尽可能少，减少其他因素影响。 

## 4 SDK下载 

您可通过如下两种方式下载： 
1. [直接点击下载](http://share.weiyun.com/3bf4fd92fa71cb61f3117f5740af016f)； 
2. 到[github](https://github.com/tencentyun/imsdk_restapi-nodejs-sdk)下载。

