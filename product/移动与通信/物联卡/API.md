## 约定
<table>
<tr>
	<td>请求行</td>
	<td>https://yun.tim.qq.com/版本号/iotcard/命令字?sdkappid=xxxxx&random=xxxx</td>
</tr>
<tr>
	<td>协议</td>
	<td>HTTPS</td>
<tr>
	<td>方法</td>
	<td>POST</td>
</tr>
</table>

请求数据和应答数据均采用 json 格式，sdkappid 由腾讯物联卡平台分配，random 为随整数，不要添加零前缀。内测阶段 sdkappid 和 appkey 请向腾讯云物联卡技术支持(QQ：3513545165)申请。

## 查询账户信息
### 说明
<table>
<tr><td>命令字</td><td>getappinfo</td></tr>
<tr><td>版本号</td><td>v1</td></tr>
</table>

### 请求格式
	{
	    "token": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
	    "time": "1505812393",           // unix 时间戳
	    "echo": ""
	}

token 计算方式  
token = sha256("action=getappinfo&appkey=xxxxxxx&sdkappid=xxxxxxxx&time=xxxxxxxx")

### 应答格式
	{
	    "code": 0,
	    "message": "OK",
	    "echo": "",
	    "data": {
	        "name": "售货机",
	        "description": "星星街边售货机物联卡",
	        "yd_card_cnt": 10,
	        "dx_card_cnt": 10,
	        "lt_card_cnt": 10
	    }
	}

## 查询卡片列表
### 说明
<table>
<tr><td>命令字</td><td>getcardlist</td></tr>
<tr><td>版本号</td><td>v1</td></tr>
</table>

### 请求格式
	{
	    "teleoperator": 1,      // 0 全部运营商 1 移动 2 电信 3 联通
	    "limit": 20,            // 单词返回的数量限制，最大为 20
	    "offset": 0,            // 分页偏移
	    "token": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
	    "time": "1505812393",   // unix 时间戳
	    "echo": ""
	}
token 计算方式
token = sha256("action=getcardlist&appkey=xxxxxxx&random=xxxxxx&time=xxxxxxxx")

### 应答格式
	{
	    "code": 0,
	    "message": "OK",
	    "echo": "",
	    "data": {
	        "card_brief_infos": [
	            {
	                 "iccid": "898602B7091701054333",   // iccid
	                 "msisdn": "1064878384333",         // 电话号码
	                 "teleoperator": 1,                 // 运营商 1 移动 2 电信 3 联通
	                 "type": 1,                         // 类型 1 单卡 2 流量池
	                 "card_status": 1,                  // 卡片状态 1 未激活 2 已激活 3 已停用
	                 "network_status": 1,               // 网络状态 1 关闭 2 开启
	                 "data_used_in_period": 14.970,     // 周期内已使用的流量，单位MB
	                 "data_total_in_period": 30.000     // 周期内可用的流量，单位MB
	            },
	            {
	                 "iccid": "898607B0101730318875",
	                 "msisdn": "1064706584079",
	                 "teleoperator": 1,
	                 "type": 1,
	                 "card_status": 1,
	                 "network_status": 0,
	                 "data_used_in_period": 14.170,
	                 "data_total_in_period": 30.000
	            },
	            {
	                 "iccid": "898607B0101730321069",
	                 "msisdn": "1064706586274",
	                 "teleoperator": 1,
	                 "type": 1,
	                 "card_status": 1,
	                 "network_status": 0,
	                 "data_used_in_period": 12.170,
	                 "data_total_in_period": 30.000
	            }
	        ]
	    }
	}

## 查询卡片信息
### 说明
<table>
<tr><td>命令字</td><td>getcardinfo</td></tr>
<tr><td>版本号</td><td>v1</td></tr>
</table>

### 请求格式
	{
	    "iccid": "898602B7091701054333",
	    "token": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
	    "time": "1505812393",           // unix 时间戳
	    "echo": ""
	}

token 计算方式
token = sha256("action=getcardinfo&appkey=xxxxxxx&sdkappid=xxxxxxxx&time=xxxxxxxx")

### 应答格式
	{
	    "code": 0,
	    "message": "OK",
	    "echo": "",
	    "data": {
	        "iccid": "898602B7091701054333",   // iccid
	        "msisdn": "1064878384333",         // 电话号码
	        "teleoperator": 1,                 // 运营商 1 移动 2 电信 3 联通
	        "type": 1,                         // 类型 1 单卡 2 流量池
	        "card_status": 1,                  // 卡片状态 1 未激活 2 已激活 3 已停用
	        "network_status": 1,               // 网络状态 1 关闭 2 开启
	        "data_used_in_period": 14.970,     // 周期内已使用的流量，单位MB
	        "data_total_in_period": 30.000     // 周期内可用的流量，单位MB
	        "product_id": "xxxxxxxxxxxxxxxxx", // 套餐 id
	        "pool_id": "yyyyyyyyyyyyyyyy",     // 流量池 id
	        "product_expired_time": 1506494258 // 套餐过期时间
	    }
	}

## 发送短信
### 说明
<table>
<tr><td>命令字</td><td>sendsms</td></tr>
<tr><td>版本号</td><td>v1</td></tr>
<tr><td>说明</td><td>给物联卡下发短信，内容长度不超过70字。</td></tr>
</table>
### 请求格式
	{
	    "iccid": "898602b8011730558259",	// 物联卡ID
	    "msg": "发送的短信内容",				// 短信内容
	    "token": "4445829b4301d3f2a120c038605f376a3fb48b2e7902275b85044447008f6bd2",	//发送短信凭证，生成方式见下注
	    "time": 1506074049,					// unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败
	    "echo": "" 							// 用户自定义内容，腾讯server回包中会原样返回，不需要就填空。
	}
token 计算方式
	string iccid = "898602b8011730558259";	// tel的mobile字段的内容
	string appkey = "cefd16fb530a61b6d69f95a038e420d5"; 	// sdkappid对应的appkey，需要业务方高度保密
	string random = "1234";									// url中的random字段的值
	string time = "1506074049";								// unix时间戳
	string token = sha256("action=sendsms&appkey=$appkey&iccid=$iccid&random=$random&time=$time");
### 应答格式
	{
	    "code": 0,  		// 0 表示成功，非 0 表示失败
	    "message": "OK", 	// code 非 0 时的具体错误信息
	    "sid": "xxxxxxx", 	// 标识本次发送 id，标识一次短信下发记录
	    "echo": "" 			// 用户自定义内容，腾讯 server 回包中会原样返回
	}
## 短信回执
### 说明
<table>
<tr><td>说明</td><td>给用户后台服务推送短信状态回执，需要由用户提供接收回执的地址</td></tr>
</table>
### 请求格式
	{
	    "type": "report",
	    "iccid": "898602b8011730558259",
	    "user_receive_time": "2017-09-17 08:03:04", 
	    "report_status": "SUCCESS",
	    "sid": xxxxx
	}
### 应答格式
	{
	    "code": 0,  	// 0 表示成功，非0表示失败
	    "message": "OK"	// code 非 0 时的具体错误信息
	}
## 短信回复
### 说明
<table>
<tr><td>说明</td><td>一般用于物联卡设备收到短信之后进行回复，需要由用户提供接收回复的地址</td></tr>
</table>
### 请求格式
	{
	    "type": "reply",
	    "iccid": "898602b8011730558259",
	    "user_reply_time": "2017-09-17 08:03:04", 
	    "msg ": "回复的内容"
	}
### 应答格式
	{
	    "code": 0,  	// 0 表示成功，非0表示失败
	    "message": "OK"	// code 非 0 时的具体错误信息
	}
