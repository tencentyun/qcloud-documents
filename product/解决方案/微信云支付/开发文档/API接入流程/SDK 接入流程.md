## 微信云支付 SDK
SDK 支持 C/C++/C#/Java。SDK 说明请参见 [SDK](https://cloud.tencent.com/document/product/569/9806)。

## 接入场景
本文为您介绍收银机+扫码枪场景的接入流程，在收银机上实现腾讯云支付功能，当用扫码枪扫码顾客微信支付或支付宝付款码，收银机调用云支付的 API 发起刷卡支付。
 ![](https://main.qcloudimg.com/raw/b65326c9bca7b8d557d81669e08f1ecc.jpg)

## 接入流程
### 服务商/子商户入驻流程
**前提条件**
登录 [腾讯云官网](https://cloud.tencent.com/) PC 端录入服务商、子商户、门店，详细操作请参见 [配置服务商](https://cloud.tencent.com/document/product/569/9796)、[配置子商户](https://cloud.tencent.com/document/product/569/9795)、[配置门店](https://cloud.tencent.com/document/product/569/9797)。
 **入驻流程**
 ![服务商/子商户入驻流程图](https://main.qcloudimg.com/raw/1d6b66c6c4ef61022510c7abbb8ff9ca.png)
>?流程图中的 out_mch_id、out_sub_mch_id、out_shop_id、decive_id、staff_id、子商户订单前缀、认证 key、私钥在调用刷卡支付时需用到。

- **获取云支付服务商账号**
登录 [云支付控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcpay)，选择**服务商账户管理**，在服务商账号列表可查看云支付服务商账号。
2. **获取云支付子商户账号**
登录 [云支付控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcpay)，选择**子商户管理**，在子商户账号列表可查看云支付子商户账号。
3. **获取订单号前缀**
在子商户详情页有两个订单前缀，推荐使用纯数字的8位订单前缀，便于机具扫订单条码退款时很容易扫上。 
4. **获取门店全局 ID、设备 ID（设备编号）、店员 ID（店员编号）**
![](https://main.qcloudimg.com/raw/ca0ffcd1f125d9fecfb33f672141ac63.png)
5. **获取认证密钥和签名私钥**
配置子商户时，保存到本地的“认证密码”和“签名私钥”。

### SDK API 接入流程
#### 刷卡支付接入流程（顾客被扫）
![](https://main.qcloudimg.com/raw/9acbd65f38d1036275c5667768bb47d8.png)
- 初始化 SDK 时，commonconf 配置的 micro_pay_query_order_count 和 micro_pay_query_order_interval 两个参数，分别为刷卡支付后查询结果次数和间隔，默认次数是25次、时间间隔是6s，即一共会持续查询150s看是否有支付结果。
用户如果需要调整次数和间隔时间太，可在初始化时设置这两个参数的值。
2. 提交刷卡支付时，out_trade_no 为云支付分配的子商户订单前缀+商户自己定义的部分。子商户订单前缀可在云支付控制台的子商户页面获取。
3. 刷卡支付是一个异步操作，提交刷卡支付成功，不代表支付成功，只代表 SDK 已经受理这笔交易，调用方需要调用查单接口来确认支付结果。
4. 刷卡支付提交后，返回参数里会有一个 json 结构的支付平台，需要调用方解析出来，查单的时候需用这里解析出来的支付平台。
5. SDK 提供的接口，请求参数和返回参数均是 json 结构。
6. 使用 SDK 的 get_errmsg() 接口获取具体的错误描述信息。

#### 退款接入流程
![](https://main.qcloudimg.com/raw/183cd1b43b7910b49d9ec5cc5934c5f4.png)
- 申请退款成功，并不代表退款成功。
退款是一个异步过程，申请退款成功后，只是代表第三方支付平台受理这笔退款，是否到账需要看这笔钱退到哪里。
 - 如果是退款至微信零钱账户或支付宝账户，会很快到账。
 - 如果是退款至顾客的银行卡，到账时间与银行处理进度相关，可能要花几个小时。
 因此申请退款成功后，需告知顾客，申请退款已经成功，请关注后续到账情况。顾客可以关注微信或支付宝的消息，查看已经发起退款或退款到账的消息。
- 如果想在设备上看这笔退款是否到账，可以调用退款查询接口，通过退款单的状态来查看是否退款成功。

### 日志上报
#### 接口说明
机具直接对接云支付的情况下，为方便商户定位问题，云支付提供日志上报接口，将日志数据上报到云支付的后端，可以帮助商户分析问题，例如机具业务流程各个环节消耗了多少时延，业务流程各个环节的数据情况等。
接口名：https://pay.qcloud.com/cpay/upload_client_monitor_info
>?
- 云支付日志上报是接口维度的，例如刷卡支付、查询订单、退款。每个接口，调用方可以统计调用接口的时延传到云支付。
- 业务流程上的日志，可以上传多条，每天日志的记录时间点、精确到毫秒，需要调用方自己来完成。
 
#### 流程说明
 ![](https://main.qcloudimg.com/raw/ff1f644df9d340dc255cddb0081211a0.png)
>?总时延 = 记录结束时间 - 记录起始时间

### 设备维度订单统计
商户需要按设备维度统计订单相关的信息时：
- 统计某一个设备的订单信息，需要接入方知会商家在手机端管理系统，添加门店的设备 ID 和设备名称。
- 统计某一个款设备型号的订单，需要在支付时，OrderClient 结构里填写 sub_terminal_type 字段。
- 统计某一个平台的订单，例如 Windows 平台、Andriod 平台，需要在支付时，OrderClient 结构里填写 terminal_type 字段。

## 常见问题
### 请求格式
以下是刷卡支付的请求内容， 为方便用户查看需注意点，以下一整个字符串换行显示。
 ![](https://main.qcloudimg.com/raw/f0f5fd8ef9c3c3ed6de5690bbbc40374.png)

**格式注意一**
整个数据格式是一个 json，其中 request_content 的内容也是一个 json，因此这里有两层，所以第二层有\出现。如下图，括号里的内容本身也是一个 json 结构，toString 后赋给 request_content。
![](https://main.qcloudimg.com/raw/a388572ba9259372c0202be1fa78ea3d.png)

**格式注意二**
request_content 的内容是一个字符串，如下图，所以第2行和第7号，分别有一个双引号。
![](https://main.qcloudimg.com/raw/6542cd91443b0303e984e0630c3be4f9.png)

**计算认证码**
参与计算认证码的数据内容如下图，双引号内的数据参与计算认证码，request_content 这个关键字不参与计算认证码。
 ![](https://main.qcloudimg.com/raw/44032f9492224e12f359b35315819526.png)

**请求包完整示例**

```
Json::Value pay_mch_key;      // 构造 pay_mch_key
pay_mch_key["pay_platform"]   = 1;
pay_mch_key["out_mch_id"]     = "sz013NzuonO6CMJd0rCB";
pay_mch_key["out_sub_mch_id"] = "sz01ELTR281OFpmdAp6J";
pay_mch_key["out_shop_id"]    = "sz01qyoPJmd3j1hWmul4";

Json::Value pay_content;      // 构造 pay_content
pay_content["out_trade_no"]   = "sz0100lmnx20171228151031";
pay_content["author_code"]    = "134680423163089456";
pay_content["total_fee"]      = 1;
pay_content["fee_type"]       = "CNY";
pay_content["attach"]         = "attach";

Json::Value order_client;        // 构造 order_client
order_client["machine_no"]       = "32-62-A8-14-B3-C0";
order_client["sdk_version"]      = "1.0";
order_client["device_id"]        = 1;
order_client["spbill_create_ip"] = "10.15.244.75";
order_client["staff_id"]         = "1003";
order_client["terminal_type"]    = 2;  // 平台 Windows Linux Android pos
order_client["sub_terminal_type"]    = 1111; //设备型号，如商家的 pos 的 AXX01 型号，这个字段接入方自定义，保证自己设备型号的唯一性，可用于统计某一款设备的订单信息。

Json::Value request_content;     // 构造 request_content
request_content["pay_mch_key"]   = pay_mch_key;
request_content["pay_content"]   = pay_content;
request_content["order_client"]  = order_client;
request_content["nonce_str"]     = "416492026bc84091bcaf7e74ea90ceba";

Json::FastWriter w;
std::string request_content_str = w.write(request_content);

Json::Value authen;
authen["authen_code"] = hmac_sha256(authen_key, request_content_str); //计算认证码
authen["authen_type"] = 1; //hmac_sha256 为1

Json::Value authen_info;
authen_info["a"] = authen;  //认证码，签名是 s

Json::Value request;       //构造最终发给服务器的请求
request["request_content"] = request_content_str;
request["authen_info"]     = authen_info;

std::string request_str = w.write(request);

return request_str;
```

        
### 订单号

**不同设备的唯一性**
订单号由云支付分配的订单唯一前缀+商户自定义两部分组成。其中商户自定义部分需要保证不同设备的唯一性，例如一个商户的订单号自定义部分为年+月+日+时+分+秒，会在多个机器支付时出现订单号重复，导致支付失败。

**订单号不能回滚**
例如商户自定义部分订单号为：机号+年月日+序列号，序列号由1、2、3、.. 往上增。如果某个时间点机器故障或软件故障，序列号不能又从1、2、3往上增，否则会出现订单号重复导致支付失败。
