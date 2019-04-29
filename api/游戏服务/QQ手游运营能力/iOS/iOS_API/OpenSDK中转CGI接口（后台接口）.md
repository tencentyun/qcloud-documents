## 公共接口说明
### CGI 调用方法

- 方法1：`http://proxy.vip.qq.com/cgi-bin/QQConnect.fcgi `
- 方法2：`https://proxy.vip.qq.com/cgi-bin/QQConnect.fcgi`

### 公共请求参数


|参数|	是否必须	|含义|
|-----|-----|-----|
|oauth_consumer_key|	是	|申请 QQ 登录成功后，分配给应用的appid |
|openid	|是	|用户的 ID，与 QQ 号码一一对应。<br> 可通过调用`https://graph.qq.com/oauth2.0/me?access_token=YOUR_ACCESS_TOKEN` 来获取。|
|access_token|	是|	可通过使用 Authorization_Code 来获取。 <br>access_token有 3 个月有效期。|
|cmd	|是	|cgi名称，此字段决定具体的接口功能|
|sign	|是	|签名|
|format|	否	|控制 cgi 的输出格式。<br>目前可选值为 json、jsonp，如果不传则默认为 json|
|callback	|否	|当 format 为 jsonp 时，可通过 callback 参数指定返回时的字符串,如果不传则默认为“_Callback“|

>**注意：**
>所有参数都是放在 QUREY_STRING 中（即 url 的 `?`后以 `&` 作为分隔符），不支持 POST 调用。

### 公共返回参数

|参数|	是否必须	|含义|
|-----|-----|-----|
|ret	|是	|返回值，0 表示成功，非 0 表示错误码|
|msg	|是	|错误描述|
|data	|是	|返回的数据。不同的 cgi，返回不同的格式|

### 签名算法
签名值 sign 是将请求源串以及密钥根据一定签名方法生成的签名值，用来提高传输过程参数的防篡改性。 签名值的生成共有 3 个步骤：构造源请求串、构造待加密串和生成签名值。

#### 使用示例
URL：`http://proxy.vip.qq.com/cgi-bin/QQConnect.fcgi`

请求参数：
```
oauth_consumer_key=100330589
access_token=1821FD577DD45526CA6EA2ADAC685508
openid=29439511BB5D23F36BD09F5B0DF94181
cmd=qc_set_summary_card
card_id=11746
style_id=1
version=7.2.5
platform=2
```
密钥：123456

**请求串参数排序**
 将上面的请求，按照参数名升序排序之后拼接，格式：参数 1 名称参数 1 值参数 2 名称参数2值，示例如下：
```
$access_token$1821FD577DD45526CA6EA2ADAC685508$card_id$11746$cmd$qc_set_summary_card$oauth_consumer_key$100330589$openid$29439511BB5D23F36BD09F5B0DF94181$platform$2$style_id$1$version$7.2.5
```
**构造待加密串**
将上一步中准备好的参数和密钥拼接起来得到待加密串，格式：待加密串=密钥&参数串&密钥：
```
123456$access_token$1821FD577DD45526CA6EA2ADAC685508$card_id$11746$cmd$qc_set_summary_card$oauth_consumer_key$100330589$openid$29439511BB5D23F36BD09F5B0DF94181$platform$2$style_id$1$version$7.2.5123456
```
**生成签名值**
将上一步中拼接之后的待加密串进行md5编码（小写 16 进制字符串）
```
sign=tolower(md5("123456$access_token$1821FD577DD45526CA6EA2ADAC685508$card_id$11746$cmd$qc_set_summary_card$oauth_consumer_key$100330589$openid$29439511BB5D23F36BD09F5B0DF94181$platform$2$style_id$1$version$7.2.5123456"))
```
得到的签名值结果如下：
`a61529eb51852c7bb6fe396bd62dadcd`

**最终得到 HTTP 请求串**
```
http://proxy.vip.qq.com/cgi-bin/QQConnect.fcgi?oauth_consumer_key=100330589&access_token=1821FD577DD45526CA6EA2ADAC685508&openid=29439511BB5D23F36BD09F5B0DF94181&cmd=qc_set_summary_card&sign=a61529eb51852c7bb6fe396bd62dadcd&card_id=11746&style_id=1&version=7.2.5&platform=2
```

## CGI 接口汇总
### 功能描述 
游戏方按照约定上报特定意义的流水。

### 接入流程

1.游戏方与 opensdk 侧约定上报的字段，需要以下数据，经由 opensdk 确认登记后，才可以进行上报。

- 游戏 appid。
- 上报字段，具体见下面“type字段说明”。
- 报的请求量和请求峰值的评估。

2.游戏方有资源推广等导致上报量大幅上涨的情况，需要提前周知 opensdk 进行评估和扩容。
3.如需接入关怀，需要额外进行以下步骤。

- 需要游戏方提前申请好公众号（必须是服务号）。
- 向 opensNNdk 侧提供申请好的公众号，opensdk 侧添加相应的消息模板和权限。
- 提供需要发送关怀消息的场景，opensdk 侧检查场景是否可以实现，并负责录入场景规则。

#### CGI 名字 
`gc_achieve_report`

#### 调用方式
`POST`

#### 输入参数 
输入参数是一个 json 结构。

|参数	|是否必须|含义|
|-----|-----|-----|
|appid	|是	|游戏 appid|
|param	|是	|是一个 json 字符串, 结构见下面说明|

```
http://proxy.vip.qq.com/cgi-bin/QQConnect.fcgi?oauth_consumer_key=100330589&access_token=1821FD577DD45526CA6EA2ADAC685508&openid=29439511BB5D23F36BD09F5B0DF94181&cmd=gc_achieve_report&sign=ca3ba525d78fe5c883833dc8e8119021&param={"total":2,"list":[{"type":12,"data":"1","bcover":0,"expires":0},{"type":26,"data":"123","bcover":0,"expires":0},{"type":27,"data":"456","bcover":0,"expires":0},{"type":28,"data":"476","bcover":1,"expires":1510109015}]}
```
#### json 结构

|参数 |是否必须	|类型	|含义|
|-----|-----|-----|-----|
| total	|是	|number	|数量，list 数组元素个数|
|  List	|是	|vector	|流水内容 |
| type	|是	|number	|流水类型，由opensdk统一分配，详细说明见下表|
|data	|是	|String|	流水值|
| bcover	|是	|number	|是否覆盖， 0：不覆盖, 1：覆盖|
| expires	|是	|number	|0:不过期, 非 0:过期的时间点（unix 时间戳）|

#### type 字段说明（必填 type）
type12、26、27、28 是必填的字段，所有流水上报必须夹带上报。

|type	|bcover	|expire	|描述	|
|-----|-----|-----|-----|
|12	|bcover=1	|expire=0	|平台类型:iOS(0)，安卓(1)	|
|26	|bcover=1	|expire=0	|大区信息:手 Q(1)，微信(2)|
|27	|bcover=1	|expire=0	|区服 ID	|
|28	|bcover=1	|expire=0	|角色 ID	|

#### type 字段说明（常用 type）
常用 type 是选取的比较公用的字段，游戏方可以选择性上报，如果有其他字段，需要约定 type 值后进行上报。

常用 type 是选取的比较公用的字段，游戏方可以选择性上报，如果有其他字段，需要约定 type 值后进行上报。

| type	| bcover	| expire	| 描述 |  备注  |
|---------|---------|---------|---------|---------|
| 1	| bcover=1	| expire=0	| 等级	|  |
| 2	| bcover=1	| expire=0	| 金钱（钻石、金币、点卷）	| |
| 3	| bcover=1	| 与游戏结算时间一致	| 流水得分	| |
| 8	| bcover=1	| expire=0	| 角色 ID	 | | 
| 17	| bcover=1	| expire=0	| 战力	| 变化时上报 |
| 25	| bcover=1	| expire=0	| 用户注册时间	| | 
| 29	| bcover=1	| expire=0	| 角色名称	| 创建角色时上报，且每条流水上报时同时上报此项 |
| 43	| bcover=1	| expire=0	| 累积充值金额	| 累计充值金额变动时进行上报 |
| 44	| bcover=1	| expire=0	| 单笔充值金额	| 有充值发生时进行上报 |
| 45	| bcover=1	| expire=0	| 游戏内玩家VIP等级	| 变化时上报、登出上报 |
| 46	| bcover=1	| expire=0	| 充值时间	| 有充值发生时进行上报 |
| 46	| bcover=1	| expire=0	| 充值时间	| 有充值发生时进行上报 |
| 6000	| bcover=1	| expire=0	| 当天累计游戏时长	| 上报格式：unix 时间戳（单位必须为：秒）周期上报，每 5 分钟上报一次，上报用户当日的累计游戏时长。（例：用户前 5 分钟在线 1 分钟，上报一次 1 分钟；下一个5分钟在线 2 分钟，则上报一次 3 分钟。）|


#### 输出示例
```
{
"ret":0,        //中转cgi返回码
"msg":"ok",     //中转cgi返回信息
"data": 
　　{
    	"ret":0,      //0-成功，其他-失败
    	"msg":"xx",   //错误描述
　　}
}
```

