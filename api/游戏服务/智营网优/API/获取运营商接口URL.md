### 1 接口描述

本接口 (geturl) 用于获取手机用户的唯一标识值查询地址，该地址可以查询手机用户在运营商数据库的唯一标识值。

接口请求域名：`https://qos.api.cloud.tencent.com/qos`

* 请求方式：GET。

### 2 输入参数

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| Action | String | 是 | 接口方法名，固定值为“geturl”。 |
| ReqType | int | 是 | 0：客户端发起，1：服务器发起。 |
| GameId | String | 是 | 游戏 ID，可登录到腾讯云控制台查看，在创建服务时生成的。 |
| SecretId | String | 是 | 密钥 ID，可登录到腾讯云控制台查看，在创建服务时生成的。 |
| VersionId | String | 否 | 游戏版本号，可用于定位具体某一个用户网络状况，非必填项。 |
| PrivateIP | String | 是 | 用户手机内网 IP |
| PublicIP | String | 否/是 | 用户手机外网 IP（若 ReqType=1，必填）|
| DeviceCode | String | 否 | 用户手机设备码，可用于定位具体某一个用户网络状况，非必填项。|
| Timestamp | int | 是 | 时间戳 |
| Nonce | int | 是 | 随机整数，如 12345 |
| Signature | String | 是 | 签名信息，参见 [签名和鉴权文档](/document/product/594/10034) 页面。|


### 3 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| errno | int | 处理结果标识码，0 表求请求成功，其他表示失败|
| errmsg | String | 处理结果描述，"success" 为成功，其他为失败原因 |
| isQos | int | 1 为正处于加速状态，其他为未加速 |
| mobileUrl | String | 唯一标识查询地址，如用户无法查询则返回 "unknown" |

### 4 错误码
| 错误码 | 描述 |
|---------|---------|
| 1 | 获取唯一标识地址失败 |

### 5 示例

输入

<pre>
https://qos.api.qcloud.com/qos?Action=geturl
&ReqType=1
&GameId=8282828
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&VersionId=1.2
&PrivateIP=23.4.5.5
&PublicIP=124.4.5.6
&DeviceCode=xxx-yyy
&Timestamp=1496203804
&Nonce=345666
&Signature=ORFGm9wSTiI++b/NAIG63NRuEhA0x1AjXvrg72yls5Y=
</pre>

输出

<pre>
{
    "Response": {
        "errno"：0,           
        "errmsg"："success",   
        "isQos"：1,            
        "mobileUrl"："http://xxx.com"
    }
}
</pre>
