## 1. 接口描述
接口请求域名：`iask.qq.com`
本接口（pushTemplateMsg）用于推送模板消息。调用协议为 HTTPS POST 请求，content-type 为 application/JSON。

 ## 2. 请求参数
| 参数名称    | 参数类型 | 是否必填 | 参数说明                                       |
| :---------- | :------- | :------- | ---------------------------------------------- |
| appId       | String   | 是       | 应用 ID，可在 IASK 应用管理界面获取                |
| oaId        | String   | 是       | 应用授权给 IASK 的公众号 ID                       |
| openId      | Int      | 是       | 接收者 openid                                   |
| templateId  | String   | 是       | 模板 ID                                         |
| url         | String   | 否       | 模板跳转链接                                   |
| timestamp   | Int      | 是       | 时间戳，单位秒                                 |
| sign        | String   | 是       | 调用签名，根据接口调用参数及应用 SecretKey 生成 |
| miniprogram | JSON     | 否       | 放置在 post body 中，详见 [示例1](#miniprogram)      |
| data        | JSON     | 是       | 放置在 post body 中，详见 [示例2](#data )                   |
 
 
 ## 3. 响应参数
 |参数名称	|参数类型	|参数说明|
 |---------|---------|------|
 |code	   |   Int	|code 码，0为正常，非0为异常|
 |data	   |  String	|返回过滤后的文本|
 |msg	   |  String	|返回消息|

 ## 4. 接入流程
 4.1 用户从 IASK 的应用获取 APPID 及 SecretKey；
 4.2 确认除 sign 参数外各参数的值（不需要考虑`postbody`里面的参数）；
 4.3 生成 sign 参数，将 APPID、oaID、openID、templateID、timestamp 参数按升序排列组合成字符串得到`&appId=x&openId=x&templateId=x&timestamp=x`；在字符串头部加上  SecretKey 得到`x&appId=x&openId=x&templateId=x&timestamp=x`。对此字符串做 MD5处理得到签名参数 sign。

 sign 参数生成示例（PHP）：
 ```
$secret_key = xxx;  //IASK 应用配置里面的 SecretKey
$params = [
    'appId' => 'xx'
    'openId' => 'xx'
    'timestamp' => 1525339871, 
    'oaId' => 'xx', 
    'templateId' => 'xx',
];
ksort($params);
foreach ($params as $key => $value) {
    $secret_key.= '&' . $key . '=' . $value;
}
$sign = md5($secret_key);
 ```

 ## 5. 示例
 ### 请求示例
 ```
iask.qq.com/aics/open/pushTemplateMsg?
appId=be043fdb5e7d23041f0436a27ae3777d
&oaId=wxc300f0df2a16da43
&openId=ogud103JWOxWQmSKy2DR-NE6NTD4
&templateId=Jpdhk-mCTam7fQjbObwBgZW54g2ij8cjja7NYo_b8YU
&url=http://www.qq.com&timestamp=111&sign=xxx
```

示例1（miniprogram）：<span id="miniprogram"></span>
 ```
 {
"appid":"xiaochengxuappid12345",   //小程序 APPID
"pagepath":"index?foo=bar"    //小程序具体页面地址
}
```

示例2（data）：<span id="data"></span>
 ```
 {
        "first": {
            "value":"工单处理进度通知",
            "color":"#173177"
        },
        "keyword1":{
            "value":"xxxx",
            "color":"#173177"
        },
        "keyword2": {
            "value":"xxx",
            "color":"#173177"
},
        "keyword3": {
            "value":"xxx",
            "color":"#173177"
        },
        "remark":{
            "value":"请点击查看详情！",
            "color":"#173177"
        }
    }
``` 

 ### 响应示例

 ```
 {
    "code": 0,
    "data": {
        "errcode": 0,			//推送模板消息接口返回 code 码
        "errmsg": "ok",		//推送模板消息接口返回 msg
        "msgid": 496146255857205248	//推送模板消息接口返回 msgId
    },
    "msg": "success"
}
 ```
