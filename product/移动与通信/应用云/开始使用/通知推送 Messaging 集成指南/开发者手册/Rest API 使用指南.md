# 1. Rest API 使用指南

## 1.1. 协议描述

请求URL结构为：``` http://接口域名/v2/class/method?params```

|字段名| |用途|备注|
|-----|-----|-----|
|接口域名|接口域名|统一使用openapi.xg.qq.com|
|v2|表示当前api的版本号|无|
|class|提供的接口类别|无|
|method|每个接口大类提供的具体操作接口|如查询、设置、删除等|
|params|以GET方式调用接口时传递的参数|	包括通用参数和api相关特定参数。所有的参数都必须为utf8编码，params字符串应进行url encode
注：以POST方式调用接口时，参数应以POST参数形式传递，内容要求同params字段。HTTP HEADER中“Content-type”字段要设置为“application/x-www-form-urlencoded”

### 1.1.1. 通用参数
各接口url结构的params字段有共同参数

|参数名|	类型|	是否必要|	参数描述|
|------|---|--------|--------|
|access_id|	uint|	是|	应用的唯一标识符，在提交应用时管理系统返回。可在xg.qq.com管理台查看|
|cal_type|	int|	否|	0-使用离线计算，1-使用实时统计，默认情况下为0|
|timestamp|	uint|	是|	本请求的unix时间戳，用于确认请求的有效期。默认情况下，请求时间戳与服务器时间（北京时间）偏差大于600秒则会被拒绝|
|valid_time|	uint|	否|	配合timestamp确定请求的有效期，单位为秒，最大值为600。若不设置此参数或参数值非法，则按默认值600秒计算有效期|
|sign|	string|	是|	内容签名|
备注：内容签名生成规则：

A）提取请求方法method（GET或POST）；

B）提取请求url信息，包括Host字段的IP或域名和URI的path部分，注意不包括Host的端口和Path的querystring。请在请求中带上Host字段，否则将视为无效请求。比如openapi.xg.qq.com/v2/push/single_device或者10.198.18.239/v2/push/single_device;

C）将请求参数（不包括sign参数）格式化成K=V方式，注意：计算sign时所有参数不应进行urlencode；

D）将格式化后的参数以K的字典序升序排列，拼接在一起，注意字典序中大写字母在前；

E）拼接请求方法、url、排序后格式化的字符串以及应用的secret_key；

F）将E形成字符串计算MD5值，形成一个32位的十六进制（字母小写）字符串，即为本次请求sign（签名）的值； Sign=MD5($http_method$url$k1=$v1$k2=$v2$secret_key); 该签名值基本可以保证请求是合法者发送且参数没有被修改，但无法保证不被偷窥。

例如： POST请求到接口 http://openapi.xg.qq.com/v2/push/single_device ，有四个参数，access_id=123，timestamp=1386691200，Param1=Value1，Param2=Value2，secret_key为abcde。

则上述E步骤拼接出的字符串为

POSTopenapi.xg.qq.com/v2/push/single_deviceaccess_id=123Param1=Value1Param2=Value2timestamp=1386691200abcde，注意字典序中大写在前。

计算出该字符串的MD5为6b90c7f4a137c7d0b756d48f748c93b2，以此作为sign参数的值

### 1.1.2. 通用返回结果
~~~
{
"ret_code":0,
"erroeMsg":"ok"
"result":{"status":0}
}
~~~
(1)字段定义如下

|参数名|	类型|	是否必要|	参数描述|
|------|---|-------|------|
|ret_code |int |是 |返回码|
|err_msg |string |否 |请求出错时的错误信息|
|result |json |否 |请求正确时，若有额外数据要返回，则结果封装在该字段的json中。若无额外数据，则可能无此字段特别注意： 1）参数和值都是大小写敏感，如没有特别注明，都是小写 2）所有的K和V须urlencode，避免里面有“&”或“=”之类字符影响解析|
1.1.3. 通用返回码

描述如下

值 |含义 |可采取措施
----|----|
0 |调用成功 |
-1 |参数错误 |检查参数配置
-2 |请求时间戳不在有效期内 |检查设备当前时间
-3 |sign校验无效 |检查Access ID和Secret Key（注意不是Access Key）
2 |参数错误 |检查参数配置
14 |收到非法token，例如iOS终端没能拿到正确的token |Android Token长度为40位iOS Token长度为64位
15 |信鸽逻辑服务器繁忙 |稍后重试
19 |操作时序错误。例如进行tag操作前未获取到deviceToken |没有获取到deviceToken的原因：1.没有注册信鸽或者苹果推送2.provisioning profile制作不正确
20 |鉴权错误，可能是由于Access ID和Access Key不匹配 |检查Access ID和Access Key
40 |推送的token没有在信鸽中注册 |检查token是否注册
48 |推送的账号没有绑定token |检查account和token是否有绑定关系见推送指南：绑定/设置账号见热门问题解答：账号和设备未绑定的解答
63 |标签系统忙 |检查标签是否设置成功见推送指南：设置标签
71 |APNS服务器繁忙 |苹果服务器繁忙，稍后重试
73 |消息字符数超限 |iOS目前是1000字节左右，苹果的额外推送设置如角标，也会占用字节数
76 |请求过于频繁，请稍后再试 |全量广播限频为每3秒一次
78 |循环任务参数错误 |
100 |APNS证书错误。请重新提交正确的证书 |证书格式是pem的，另外，注意区分生产证书、开发证书的区别
其他 |其他错误

### 1.1.4. 推送Android平台

message参数值应为如下所述的json字符串，其总长度不能超过4096字节。

(1)推送通知定义示例（默认展示在手机或设备通知栏）
~~~
{"content":"this is content","title":"this is title", "vibrate":1}
~~~
(2)完整定义
~~~
{
"title ":"xxx", // 标题，必填
"content ":"xxxxxxxxx", // 内容，必填
"accept_time": //表示消息将在哪些时间段允许推送给用户，选填
[
{
“start”:{“hour”:”13”,“min”:”00”},
”end”: {“hour”:”14”,“min”:”00”}
},
{
“start”:{“hour”:”00”,”min”:”00”},
”end”: {“hour”:”09”,“min”:”00”}
}
],
"n_id":0, //通知id，选填。若大于0，则会覆盖先前弹出的相同id通知；若为0，展示本条通知且不影响其他通知；若为-1，将清除先前弹出的所有通知，仅展示本条通知。默认为0
"builder_id":0, // 本地通知样式，必填
"ring":1， // 是否响铃，0否，1是，下同。选填，默认1
"ring_raw":"ring", // 指定应用内的声音（ring.mp3），选填
"vibrate":1, // 是否振动，选填，默认1
"lights":1// 是否呼吸灯，0否，1是，选填，默认1
"clearable":1, // 通知栏是否可清除，选填，默认1
"icon_type":0 //默认0，通知栏图标是应用内图标还是上传图标,0是应用内图标，1是上传图标,选填
"icon_res":"xg",// 应用内图标文件名（xg.png）或者下载图标的url地址，选填
"style_id":1 //Web端设置是否覆盖编号的通知样式，默认1，0否，1是,选填
"small_icon":"xg"指定状态栏的小图片(xg.png),选填
"action":{ // 动作，选填。默认为打开app
"action_type ": 1, // 动作类型，1打开activity或app本身，2打开浏览器，3打开Intent
"activity ": "xxx"
"aty_attr ": // activity属性，只针对action_type=1的情况
{
"if":0, // 创建通知时，intent的属性，如：intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
"pf":0, // PendingIntent的属性，如：PendingIntent.FLAG_UPDATE_CURRENT
}
"browser": {"url": "xxxx ","confirm": 1}, // url：打开的url，confirm是否需要用户确认
“intent”: “xxx”
},
"custom_content":{ // 用户自定义的key-value，选填
"key1": "value1",
"key2": "value2"
}
}
~~~
(3)透传消息定义示例（可以由app识别的任意透传消息命令，比推送通知更灵活）
~~~
{"content":"this is content","title":"this is title"}
~~~
(4)完整定义

~~~
{
"title":"xxx", // 标题，选填
"content ":"xxxxxxxxx", // 内容，选填
"accept_time": //表示消息将在哪些时间段允许推送给用户，选填
[
{
“start”:{“hour”:”13”,“min”:”00”},
”end”: {“hour”:”14”,“min”:”00”}
},
{
“start”:{“hour”:”00”,”min”:”00”},
”end”: {“hour”:”09”,“min”:”00”}
}
],
"custom_content":{ // 用户自定义的key-value，选填
"key1": "value1",
"key2": "value2"
}
}
~~~
### 1.1.5. 推送iOS平台

message参数应为APNS规定的payload（也是一个json字符串），详细定义参考APNS官方手册。

信鸽在其基础上仅增添了两保留字段 xg 和 accept_time。payload不能超过800字节。需要注意的是accept_time字段不会传递给APNS，因此不占用payload容量。

(1)普通通知示例
~~~
{
"aps" : { // apns规定的key-value
"alert" : { //设置消息通知栏的字段
"title": "this is a title", //通知标题
"body" : "Bob wants to play poker", //通知内容
},
"badge" : 5,
“category” : “INVITE_CATEGORY”,
},
"accept_time":[ //允许推送给用户的时段，选填。accept_time不会占用payload容量
{
"start":{"hour":"13","min":"00"},
"end": {"hour":"14","min":"00"}
},
{
"start":{"hour":"00","min":"00"},
"end": {"hour":"09","min":"00"}
}
] // 仅0~9点和13~14点这两个时段可推送
"custom1" : "bar", // 合法的自定义key-value，会传递给app
"custom2" : [ "bang", "whiz" ], // 合法的自定义key-value，会传递给app
"xg" : "oops" // 错误！xg为信鸽系统保留key，其value会被信鸽系统覆盖，应避免使用
}
~~~
(2)静默通知示例
~~~
{
"aps" : { // apns规定的key-value
"badge" : 5,
"category" : “INVITE_CATEGORY”,
"content-available": 1, //静默通知的标识
},
"custom1" : "bar", // 合法的自定义key-value，会传递给app
"custom2" : [ "bang", "whiz" ], // 合法的自定义key-value，会传递给app
"xg" : "oops" // 错误！xg为信鸽系统保留key，其value会被信鸽系统覆盖，应避免使用
}
~~~
## 1.2. 推送接口

### 1.2.1. 单个设备

url路径
~~~
http://接口域名/v2/push/single_device?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数说明

参数名 |类型 |必需 |默认值 |描述
-----|-----|----|-----|---
device_token |string |是 |无 |针对某一设备推送，token是设备的唯一识别 ID
message_type |uint |是 |无 |消息类型：1：通知 2：透传消息。iOS平台请填0
message |string |是 |无 |参见1.1.4、1.1.5两节
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则使用默认值（3天）
send_time |string |否 |立即 |指定推送时间，格式为year-mon-day hour:min:sec 若小于服务器当前时间，则会立即推送
multi_pkg |uint |否 |0 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息。本字段对iOS平台无效
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
响应结果：在通用返回结果参数中，result字段的json为空。

返回：本接口不返回push id

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/single_deviceaccess_id=2100250470device_token=76501cd0277cdcef4d8499784a819d4772e0fddemessage={"title":"测试消息","content":"来自restapi的单推接口测试消息"}message_type=1timestamp=1502356505f1fa8b11f540794bf13e10d499ac5c36
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/single_device?access_id=2100250470&timestamp=1502356505&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&message_type=1&message={"title":"测试消息","content":"来自restapi的单推接口测试消息"}&sign=b7f5761d37fb352536e53db0c50ffcc6
~~~
### 1.2.2. 批量设备

- 首先，需要创建批量消息
url路径
~~~
http://接口域名/v2/push/create_multipush?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|---|---|-----|----
message_type |uint |是 |无 |消息类型：1：通知 2：透传消息
message |string |是 |无 |参见1.1.4、1.1.5两节
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则不存储；iOS无需设置此参数
multi_pkg |uint |否 |无 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
响应结果：在通用返回结果参数中，result字段的json如下
~~~
{
“push_id”:string (表示给app下发的任务id)
}
~~~
- 其次，按照已创建的批量推送消息推送给多个设备
url路径
~~~
http://接口域名/v2/push/device_list_multiple?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
----|----|----|----|---
device_list |string |是 |无 |Json数组格式，每个元素是一个token，string类型，单次发送token不超过1000个。例：[“token1”,”token2”,”token3”]
push_id |uint |是 |无 |创建批量推送消息 接口的返回值中的 push_id
响应结果：在通用返回结果参数中，result字段的json为空

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

获取push_id：

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/create_multipushaccess_id=2100264266message={"title":"测试消息","content":"来自restapi的批量接口测试消息","custom_content":{"key1":"value1","key2":"value2"}}message_type=2timestamp=1502694940d8fc29c627259a06452794e31dab5bb8
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/create_multipush?access_id=2100264266&message={"title":"测试消息","content":"来自restapi的批量接口测试消息","custom_content":{"key1":"value1","key2":"value2"}}&message_type=2&timestamp=1502694940&sign=e5ca158c01712fb185399e67b6a57d1f
~~~
进行推送：

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/device_list_multipleaccess_id=2100264266device_list=["78e8540853619eb14fb49fdd53274c0c82ca2025"]push_id=2854657652timestamp=1502694940d8fc29c627259a06452794e31dab5bb8
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/device_list_multiple?access_id=2100264266&device_list=["78e8540853619eb14fb49fdd53274c0c82ca2025"]&push_id=2854657652&timestamp=1502694940&sign=e4779a9173a1c51541800e76b8a25322
~~~
### 1.2.3. 全量设备

后台对本接口的调用频率有限制，两次调用之间的时间间隔不能小于3秒。

url路径
~~~
http://接口域名/v2/push/all_device?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
------|-----|----|----|----
message_type |uint |是 |无 |消息类型：1：通知 2：透传消息。iOS平台请填0
message |string |是 | |参见1.1.4、1.1.5两节
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则使用默认值（3天）
send_time |string |否 |立即 |指定推送时间,格式为year-mon-day hour:min:sec 若小于服务器当前时间，则会立即推送
multi_pkg |uint |否 |0 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息。本字段对iOS平台无效
environment |uint |仅iOS必需 | |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
loop_times |uint |否 | |循环任务执行的次数，取值[1, 15]
loop_interval |uint |否|	|循环任务的执行间隔，以天为单位，取值[1, 14]。loop_times和loop_interval一起表示任务的生命周期，不可超过14天

响应结果：在通用返回结果参数中，result字段的json示例如下
~~~
{
“push_id”:string (表示给app下发的任务id，如果是循环任务，返回的是循环父任务id)
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/all_deviceaccess_id=2100240957message={"title":"测试消息","content":"来自restapi的全量接口测试消息"}message_type=1timestamp=1502360486f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/all_device?access_id=2100240957&message={"title":"测试消息","content":"来自restapi的全量接口测试消息"}&message_type=1&timestamp=1502360486&sign=4813a111880885223b72229495508813
~~~
### 1.2.4. 标签

可以针对设置过标签的设备进行推送。如：女、大学生、低消费等任意类型标签。

标签推送url路径
~~~
http://接口域名/v2/push/tags_device?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|---
message |string |是 |无 |参见1.1.4、1.1.5两节
message_type |uint |是 |1 |消息类型：1：通知 2：透传消息。iOS平台请填0
tags_list |json |是 |无 |[“tag1”,”tag2”,”tag3”]
tags_op |string |是 |无 |取值为AND或OR
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则使用默认值（3天）
send_time |string |否 |立即 |指定推送时间，格式为year-mon-day hour:min:sec 若小于服务器当前时间，则会立即推送
multi_pkg |uint |否 |0 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息。本字段对iOS平台无效
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
loop_times |uint |否 |无 |循环任务执行的次数，取值[1, 15]
loop_interval |uint |否 |无|循环任务的执行间隔，以天为单位，取值[1, 14]。loop_times和loop_interval一起表示任务的生命周期，不可超过14天
响应结果：在通用返回结果参数中，result字段的json示例如下
~~~
{
“push_id”:string (表示给app下发的任务id，如果是循环任务，返回的是循环父任务id)
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/tags_deviceaccess_id=2100240957message={"title":"测试消息","content":"来自restapi的标签接口测试消息"}message_type=1tags_list=["qwertyuiop"]tags_op=ORtimestamp=1502360486f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/tags_device?access_id=2100240957&message={"title":"测试消息","content":"来自restapi的标签接口测试消息"}&message_type=1&timestamp=1502360486&tags_list=["qwertyuiop"]&tags_op=OR&sign=95dbc4d1107a99d6824fda19e7ff09c9
~~~
### 1.2.5. 单个帐号

设备的账户或别名由终端SDK在调用推送注册接口时设置，详情参考终端SDK文档。

url路径
~~~
http://接口域名/v2/push/single_account?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|-----|-----|----
account |string |是 |无 |针对某一账号推送，帐号可以是qq号，邮箱号，openid，手机号等各种类型
message_type |uint |是 |1 |消息类型：1：通知 2：透传消息
message |string |是 |无 |参见1.1.4、1.1.5两节
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则使用默认值（3天）
send_time |string |否 |立即 |指定推送时间，格式为year-mon-day hour:min:sec 若小于服务器当前时间，则会立即推送
multi_pkg |uint |否 |0 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
响应结果：在通用返回结果参数中，result字段的json为空。本接口不返回push id

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/single_accountaccess_id=2100240957account=easonshipushtestaccountmessage={"title":"测试消息","content":"来自restapi的单个账号接口测试消息"}message_type=1timestamp=1502361241f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/single_account?access_id=2100240957&account=easonshipushtestaccount&message={"title":"测试消息","content":"来自restapi的单个账号接口测试消息"}&message_type=1&timestamp=1502361241&sign=0d7bee840e87801e8a90b831ee87eefb
~~~
### 1.2.6. 批量帐号

设备的账户或别名由终端SDK在调用推送注册接口时设置，详情参考终端SDK文档。

url路径
~~~
http://接口域名/v2/push/account_list?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
----|----|----|----|---
account_list |string |是 |无 |Json数组格式，每个元素是一个account，string类型，单次发送account不超过100个。例：[“account1”,”account2”,”account3”]
message_type |uint |是 |无 |消息类型：1：通知 2：透传消息
message |string |是 |无 |参见1.1.4、1.1.5两节
expire_time |uint |否 |3天 |消息离线存储时间（单位为秒），最长存储时间3天。若设置为0，则使用默认值（3天）
multi_pkg |uint |否 |0 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
响应结果：在通用返回结果参数中，result字段的json为每个account发送返回码。本接口不返回push id

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/account_listaccess_id=2100240957account_list=["easonshipushtestaccount"]message={"title":"测试消息","content":"来自restapi的批量账号接口测试消息"}message_type=1timestamp=1502361241f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/account_list?access_id=2100240957&account_list=["easonshipushtestaccount"]&message={"title":"测试消息","content":"来自restapi的批量账号接口测试消息"}&message_type=1&timestamp=1502361241&sign=cff802738763385db89aaadb49dbe345
~~~
注：

如果推送目标帐号数量很大（比如≥10000），推荐使用account_list_multiple接口，用户请自行比较异同

首先，（如同推送批量设备）需要创建批量消息：

url路径
~~~
http://接口域名/v2/push/create_multipush?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|-----|-----|----
message_type |uint |是 |无 |消息类型：1：通知 2：透传消息
message |string |是 |无 |参见1.1.4、1.1.5两节
expire_time |uint |否 |无 |消息离线存储多久，单位为秒，最长存储时间3天。在超时时间内，可以发起此消息的批量推送
multi_pkg |uint |否 |无 |0表示按注册时提供的包名分发消息；1表示按access id分发消息，所有以该access id成功注册推送的app均可收到消息
environment |uint |仅iOS必需 |无 |向iOS设备推送时必填，1表示推送生产环境；2表示推送开发环境。推送Android平台不填或填0
其次，选择推送批量帐号：

url路径
~~~
http://接口域名/v2/push/account_list_multiple?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
account_list |string |是 |无 |Json数组格式，每个元素是一个account，string类型，单次发送account不超过1000个。例：[“account1”,”account2”,”account3”]
push_id |uint |是 |无 |创建批量推送消息 接口的返回值中的 push_id
响应结果：在通用返回结果参数中，result字段的json为空

示例：请参考批量设备示例

## 1.3. 标签设置/删除接口

(1)批量设置标签
url路径
~~~
http://接口域名/v2/tags/batch_set
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
tag_token_list |string |是 |无 |json字符串，包含若干标签-token对，后台将把每一对里面的token打上对应的标签。每次调用最多允许设置20对，每个对里面标签在前，token在后。注意标签最长50字节，不可包含空格；真实token长度至少40字节。示例（其中token值仅为示意）： [[”tag1”,”token1”],[”tag2”,”token2”]]
响应结果：在通用返回结果参数中，result字段的json为空

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/tags/batch_setaccess_id=2100240957tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]timestamp=1502361905f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/tags/batch_set?access_id=2100240957&tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]&timestamp=1502361905&sign=3c0ea17401f02fed8397eef9230fb607
~~~
(2)批量删除标签
url路径
~~~
http://接口域名/v2/tags/batch_del
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
tag_token_list |string |是 |无 |json字符串，包含若干标签-token对，后台将为每一对里面的token删除对应的标签。每次调用最多允许设置20对，每个对里面标签在前，token在后。注意标签最长50字节，不可包含空格；真实token长度至少40字节。示例如下（其中token值仅为示意）： [[”tag1”,”token1”],[”tag2”,”token2”]]
响应结果：在通用返回结果参数中，result字段的json为空

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/tags/batch_delaccess_id=2100240957tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]timestamp=1502361905f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/tags/batch_del?access_id=2100240957&tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]&timestamp=1502361905&sign=301fd2e83a7f65223e1d9e38fb0b5864
~~~
## 1.4. 账号映射删除接口

### 1.4.1. 单清

(1)删除应用中某个account映射的某个token

url路径
~~~
http://接口域名/v2/application/del_app_account_tokens?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
----|----|----|----|---
account |string |是 |无 |账号，可以是邮箱号、手机号、QQ号等任意形式的业务帐号
device_token |string |是 |无 |token，设备的唯一识别ID
响应结果：在通用返回结果参数中，result字段的json如下
~~~
{
“tokens”:[“token1”,”token2”]
}
~~~
即显示删除device_token后该account映射的剩余token

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/application/del_app_account_tokensaccess_id=2100240957account=easonshipushtestaccountdevice_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502361905f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/application/del_app_account_tokens?access_id=2100240957&account=easonshipushtestaccount&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502361905&sign=c8c86feab7a1d8b1a3064c733a76079a
~~~
### 1.4.2. 全清

(1)删除应用中某account映射的所有token

url路径
~~~
http://接口域名/v2/application/del_app_account_all_tokens?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
----|----|----|----|---
account |string |是 |无 |账号
响应结果：在通用返回结果参数中，result字段的json为空

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/application/del_app_account_all_tokensaccess_id=2100240957account=easonshipushtestaccounttimestamp=1502701471f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/application/del_app_account_all_tokens?access_id=2100240957&account=easonshipushtestaccount&timestamp=1502701471&sign=88fbcc8b5c29a3f5ae1dab99b7479439
~~~
## 1.5. 查询接口

### 1.5.1. 查询消息/设备/帐号

(1)查询群发消息发送状态

url路径
~~~
http://接口域名/v2/push/get_msg_status?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
----|----|----|----|---
push_id |json |是 | |[{“push_id”: string}, {“push_id”:“xxxx”}, ]

响应结果：在通用返回结果参数中，result字段的json形式为：
~~~
{
“list”: [
{
“push_id”: “27ABC5486977”
“status”: 0（未处理）/1（推送中）/2（推送完成）/3（推送失败）
“start_time”:”year-mon-day hour:min:sec“
“finished”:xxxx （已发送）
“total”:xxxxx （共需要发送）
},
]
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/get_msg_statusaccess_id=2100240957push_id=2841253998timestamp=1502698593f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/get_msg_status?access_id=2100240957&push_id=2841253998&timestamp=1502698593&sign=39b62ab54f08e7844ed1d86e00cec76a
~~~
(2)查询应用覆盖的设备数（token总数）

url路径
~~~
http://接口域名/v2/application/get_app_device_num?params
~~~
请求参数：本接口仅包括公共参数

响应结果：在通用返回结果参数中，result字段的json形式为：

{
“device_num”: 34567(设备数)
}
若请求应用列表中某个应用信息非法，则不会在result中返回结果

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/application/get_app_device_numaccess_id=2100240957timestamp=1502701471f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/application/get_app_device_num?access_id=2100240957&timestamp=1502701471&sign=e4385f856ddaa932170c181927965cb1
~~~
(3)查询应用的某个token的信息（查看是否有效）

url路径
~~~
http://接口域名/v2/application/get_app_token_info?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
device_token |string |是 |无 |无
响应结果：在通用返回结果参数中，result字段的json如下：
~~~
{
"isReg":1,（1为token已注册，0为未注册）
"connTimestamp":1426493097, （最新活跃时间戳）
"msgsNum":2（该应用的离线消息数）
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/application/get_app_token_infoaccess_id=2100240957device_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502698593f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/application/get_app_token_info?access_id=2100240957&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502698593&sign=c4f650c6c468adba2e2b82a15ca68c3e
~~~
(4)查询应用某帐号映射的token（查看帐号-token对应关系）

url路径
~~~
http://接口域名/v2/application/get_app_account_tokens?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
account |string |是 |无 |帐号
响应结果：在通用返回结果参数中，result字段的json如下
~~~
{
“tokens”:[“token1”,”token2”]
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/application/get_app_account_tokensaccess_id=2100240957account=easonshipushtestaccounttimestamp=1502699212f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/application/get_app_account_tokens?access_id=2100240957&account=easonshipushtestaccount&timestamp=1502699212&sign=015ef9e7fde208f2d12674f731e13e8c
~~~
1.5.2. 查询标签

(1)查询应用设置的标签

url路径
~~~
http://接口域名/v2/tags/query_app_tags?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
start |uint |否 |0 |开始值
limit |uint |否 |100 |限制数量
响应结果：在通用返回结果参数中，result字段的json格式如下
~~~

{
“total”: 2, //应用的tag总数，注意不是本次查询返回的tag数
“tags”:[“tag1”,”tag2”]
}
~~~

示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/tags/query_app_tagsaccess_id=2100240957timestamp=1502699212f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/tags/query_app_tags?access_id=2100240957&timestamp=1502699212&sign=5dbf914884378af6b62cba919e012b34
~~~
(2)查询应用的某个设备上设置的标签

url路径
~~~
http://接口域名/v2/tags/query_token_tags?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
device_token |string |是 |无 |无
响应结果：在通用返回结果参数中，result字段的json格式如下
~~~
{
“tags”:[“tag1”,”tag2”]
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/tags/query_token_tagsaccess_id=2100240957device_token=76501cd0277cdcef4d8499784a819d4772e0fddetimestamp=1502699212f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/tags/query_token_tags?access_id=2100240957&device_token=76501cd0277cdcef4d8499784a819d4772e0fdde&timestamp=1502699212&sign=4cbd1b7a5553ed263f47a4a0b96402e9
~~~
(3)查询应用某个标签下关联的设备数

url路径
~~~
http://接口域名/v2/tags/ query_tag_token_num?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
tag |string |是 |无 |无
响应结果：在通用返回结果参数中，result字段的json格式如下
~~~
{
“device_num”:589874
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/tags/query_tag_token_numaccess_id=2100240957tag=easonmipushtesttimestamp=1502699920f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/tags/query_tag_token_num?access_id=2100240957&tag=easonmipushtest&timestamp=1502699920&sign=0ea7f16df1b59d69c9b81b385f938822
~~~
### 1.5.3. 查询SDK版本号

接口定义：查询app内信鸽的SDK版本。该接口为终端接口。

Android：

com.tencent.android.tpush.common.Constants.PUSH_SDK_VERSION

iOS：

XGSetting.h里面的XG_SDK_VERSION宏

## 1.6. 任务删除/取消接口

(1)删除群发推送任务的离线消息

后悔药，针对有任务ID（push ID），并且已发送任务可以删除离线消息

注意：该功能仅支持在管理台使用，点击“停止”按钮即可

(2)取消尚未触发的定时群发任务

后悔药，针对尚未发送的任务，需要任务ID

url路径
~~~
http://接口域名/v2/push/cancel_timing_task?params
~~~
请求参数：除了通用参数外，还包括如下参数

参数名 |类型 |必需 |默认值 |描述
-----|----|----|----|----
push_id |string |是 |无 |要取消的任务ID
响应结果：在通用返回结果参数中，result字段的json格式如下
~~~
{
“status”: 0, //0为成功，其余为失败
}
~~~
示例：MD5加密前url用作生成sign，RestApi Url为最终请求的url（以下为android推送示例，需替换通用参数后使用）

MD5加密前：
~~~
GETopenapi.xg.qq.com/v2/push/cancel_timing_taskaccess_id=2100240957push_id=2853333945timestamp=1502700856f255184d160bad51b88c31627bbd9530
~~~
RestApi Url:
~~~
http://openapi.xg.qq.com/v2/push/cancel_timing_task?access_id=2100240957&push_id=2853333945&timestamp=1502700856&sign=1fb3b7846f79d0027542acd05effb4a3
~~~
