
## 1. 微信云支付 SDK
SDK 支持C/C++/C#/JAVA。
SDK 说明请参见 [SDK](https://cloud.tencent.com/document/product/569/9806)。

## 2. 接入场景
本文为您介绍收银机 + 扫码枪场景的接入流程，在收银机上实现腾讯云支付功能，当用扫码枪扫码顾客微信支付或支付宝付款码，收银机调用云支付的 API 发起刷卡支付。
 
## 3. 接入简要流程说明
3.1 服务商/子商户入驻总流程
1、通过腾讯云官网PC端入驻
2、PC端录入子商户
3、具体操作见文档：配置服务商、配置子商户、配置门店。
 
注意，这里的out_mch_id，out_sub_mch_id，out_shop_id，decive_id，staff_id，子商户订单前缀、认证key、私钥在调用刷卡支付的时候需要用到。

3.1.1 获取云支付服务商账号
登录 云支付控制台 ，单击服务商账户管理（新），在服务商账号列表可查看到云支付服务商账号。
3.1.2 获取云支付子商户账号
登录 云支付控制台 ，单击子账户管理（新），在子商户账号列表可查看到云支付子商户账号。
3.1.3 获取订单号前缀
现在有两个订单前缀，推荐使用纯数字的8位订单前缀，好处是机具扫订单条码退款时很容易扫上。
 
 
3.1.4 获取全局门店ID
 
 
3.1.5 获取设备ID
 
 
3.1.6 获取店员ID
 
 
3.1.7 认证密钥和签名私钥
配置子商户到步骤五后，保存页面上的 认证密码 和 签名私钥 到本地电脑上。
 
3.2 SDK API接入流程
3.2.1 刷卡支付接入流程(顾客被扫)
1、SDK初始化时，common_conf的配置micro_pay_query_order_count和micro_pay_query_order_interval是刷卡支付后查询结果的次数和间隔，默认是25次，时间间隔是6s，即一共会持续查询150s看是否有支付结果。如果调用方觉得这个次数太多，间隔时间太长，可以自己再初始化时设置这两个参数的值。
2、提交刷卡支付时，out_trade_no为云支付分配的子商户订单前缀+商户自己定义的部分。子商户订单前缀可以登入腾讯云PC端进入子商户页面去获取。
3、刷卡支付时一个异步操作，提交刷卡支付成功，不代表支付成功，只代表SDK已经受理这笔交易，调用方需要调用查单接口去确认支付的结果。
4、刷卡支付提交后，返回的参数里会有一个支付平台，是json结构，需要调用方解析出来，然后查单的时候用这里解析出来的支付平台。
5、SDK提供的接口的请求参数和返回参数均是json结构。
6、获取具体的错误描述信息，使用SDK的get_errmsg()接口获取。
 


3.3.2 退款接入流程
 
注意：
1、申请退款成功，并不代表退款成功。
退款是一个异步过程，申请退款成功后，只是代表第三方支付平台受理这笔退款，是否到账需要看这笔钱退到哪里，如果是退款微信零钱账户或支付宝账户，会很快到账；如果是退款到顾客的银行卡，到账的时候是由银行确定的，可以要花几个小时。因此，申请退款成功后，可以告诉客户，申请退款已经成功，请关注后续是否到账。顾客可以关注微信或支付宝的消息，收到已经发起退款或退款到账的消息。
2、如果想在设备看这笔退款是否到账，可以调用退款查询接口，通过退款单的状态来看是否退款成功。


3.4 日志上报
3.4.1 接口说明
机具直接对接云支付的情况下， 为了定位问题，如机具的业务流程各个环节消耗了多少时延，业务流程各个环节的数据是怎么样的，云支付提供日志上报接口，将日志数据上报到云支付的后端，可以帮助商户分析问题。
	接口名：https://pay.qcloud.com/cpay/upload_client_monitor_info
	接口说明: 
1）	云支付日志上报是接口维度的，如刷卡支付、查询订单、退款。每个接口，调用方可以统计调用接口的时延传到云支付
2）	业务流程上的日志，可以上传多条，每天日志的需要记录时间点，精确到毫秒，这个需要调用方自己来完成。
 
3.4.2 流程规范
 
总时延为记录的结束时间减去记录的起始时间。
3.5 订单统计说明
商户有时需要按设备维度统计订单相关的信息，如下说明
1）	统计某一个设备的订单信息，需要接入方知会商家在手机端管理系统添加门店的设备ID和设备名称。
2）	统计某一个款设备型号的订单，需要在支付时OrderClient结构里填写sub_terminal_type字段
3）	统计某一个平台的订单，如windows平台，andriod平台，需要在支付时OrderClient结构里填写terminal_type字段
4 常见问题
4.1 请求格式
下面是刷卡支付的请求内容， 为了看有哪些需要注意的点，特意将一整个字符串换行显示。
 
4.1.1 格式注意一 
整个数据格式是一个json，其中request_content的内容也是一个json，因此这里有两层。所以第二层有\出现。如下图，括号里的内容本身也是一个json结构，toString后赋给request_content。
 
4.1.2 格式注意二
request_content 的内容是一个字符串，所以第2行和第7号，分别有一个双引号”，如下图
 

4.1.3 计算认证码
参与计算认证码的数据内容，如下图，双引号内的数据参与计算认证码，request_content这个关键字不参与计算认证码。
 
4.1.4 请求包的完整例子
        Json::Value pay_mch_key;      // 构造pay_mch_key
        pay_mch_key["pay_platform"]   = 1;
        pay_mch_key["out_mch_id"]     = "sz013NzuonO6CMJd0rCB";
        pay_mch_key["out_sub_mch_id"] = "sz01ELTR281OFpmdAp6J";
        pay_mch_key["out_shop_id"]    = "sz01qyoPJmd3j1hWmul4";

        Json::Value pay_content;      // 构造pay_content
        pay_content["out_trade_no"]   = "sz0100lmnx20171228151031";
        pay_content["author_code"]    = "134680423163089456";
        pay_content["total_fee"]      = 1;
        pay_content["fee_type"]       = "CNY";
        pay_content["attach"]         = "attach";

        Json::Value order_client;        // 构造order_client
        order_client["machine_no"]       = "32-62-A8-14-B3-C0";
        order_client["sdk_version"]      = "1.0";
        order_client["device_id"]        = 1;
        order_client["spbill_create_ip"] = "183.15.244.75";
        order_client["staff_id"]         = "1003";
        order_client["terminal_type"]    = 2;  // 平台windows linux android pos
order_client["sub_terminal_type"]    = 1111; //设备型号，如商家的pos的AXX01型号，这个字段接入方自定义，保证自己设备型号的唯一性，可用于统计某一款设备的订单信息。

        Json::Value request_content;     // 构造request_content
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
        authen_info["a"] = authen;  //认证码，签名是s

        Json::Value request;       //构造最终发给服务器的请求
        request["request_content"] = request_content_str;
        request["authen_info"]     = authen_info;

        std::string request_str = w.write(request);

        return request_str;
4.2 订单号
4.2.1 不同设备的唯一性
	订单号 为 云支付分配的订单唯一前缀 + 商户自定义两部分组成。其中商户子定义的部分需要保存不同设备的唯一性，比如一个商户的订单号自定义部分为年 + 月 + 日 + 时 + 分 + 秒， 这个是不行了，这个再多个机器上支付时会出现订单号重复的导致支付失败。
4.2.2 订单号不能回滚
假设商户自定义部分订单号如下：机号+年月日 + 序列号，序列号由1、2、3、.. 往上增。如果某个时间点机器故障或软件故障，序列号不能又从1、2、3 往上增，否则会出现订单号重复导致支付失败。	
