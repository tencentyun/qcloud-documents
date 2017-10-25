## 约定

|请求行|https://yun.tim.qq.com/版本号/iotcard/命令字?sdkappid=xxxxx&random=xxxx|
|协议|HTTPS|
|方法|POST|

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

请求数据和应答数据均采用 json 格式，sdkappid 由腾讯物联卡平台分配，random 为随机整数，不要添加零前缀。内测阶段 sdkappid 和 appkey 请向腾讯云物联卡技术支持(QQ：3513545165)申请。
## 查询账户信息
### 请求行

|命令字|版本号|
|--------|--------|
|getappinfo|v1|

### 请求格式

```
{
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
    "time": "1505812393"            // unix 时间戳
}
```

sig 计算方式  
sig = sha256("appkey=xxxxxxx&sdkappid=xxxxxxxx&time=xxxxxxxx")
### 应答格式

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "name": "售货机",
        "description": "星星街边售货机物联卡",
        "yd_card_cnt": 10,
        "dx_card_cnt": 10,
        "lt_card_cnt": 10
    }
}
```

## 查询卡片列表
### 请求行

|命令字|版本号|
|--------|--------|
|getcardlist|v1|

### 请求格式

```
{
    "teleoperator": 1,      // 0 全部运营商 1 移动 2 电信 3 联通
    "limit": 20,            // 单词返回的数量限制，最大为 20
    "offset": 0,            // 分页偏移
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
    "time": "1505812393"    // unix 时间戳
}
```

sig 计算方式  
sig = sha256("appkey=xxxxxxx&sdkappid=xxxxxxxx&time=xxxxxxxx")

### 应答格式

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "card_brief_infos": [
            {
                 "iccid": "898602B7091701054333",   // iccid
                 "msisdn": "1064878384333",         // 电话号码
                 "teleoperator": 1,                 // 运营商 1 移动 2 电信 3 联通
                 "type": 1,                         // 类型 1 单卡 2 流量池
                 "card_status": 1,                  // 卡片状态 1 未激活 2 已激活 3 已停用
                 "network_status": 1,               // 网络状态 1 关闭 2 开启
                 "data_used_in_period": 14.970,     // 周期内已使用的流量，单位 MB
                 "data_total_in_period": 30.000     // 周期内可用的流量，单位 MB
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
```

## 查询卡片信息
### 请求行

|命令字|版本号|
|--------|--------|
|getcardinfo|v1|

### 请求格式

```
{
    "iccid": "898602B7091701054333",
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
    "time": "1505812393"            // unix 时间戳
}
```

sig 计算方式  
sig = sha256("appkey=xxxxxxx&sdkappid=xxxxxxxx&time=xxxxxxxx")
### 应答格式

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "iccid": "898602B7091701054333",   // iccid
        "msisdn": "1064878384333",         // 电话号码
        "teleoperator": 1,                 // 运营商 1 移动 2 电信 3 联通
        "type": 1,                         // 类型 1 单卡 2 流量池
        "card_status": 1,                  // 卡片状态 1 未激活 2 已激活 3 已停用
        "network_status": 1,               // 网络状态 1 关闭 2 开启
        "data_used_in_period": 14.970,     // 周期内已使用的流量，单位 MB
        "data_total_in_period": 30.000     // 周期内可用的流量，单位 MB
        "product_id": "xxxxxxxxxxxxxxxxx", // 套餐 id
        "pool_id": "yyyyyyyyyyyyyyyy",     // 流量池 id
        "product_expired_time": 1506494258 // 套餐过期时间
    }
}
```

