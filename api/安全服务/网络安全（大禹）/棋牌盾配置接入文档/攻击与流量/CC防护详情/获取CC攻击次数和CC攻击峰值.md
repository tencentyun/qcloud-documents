### 1. 接口描述
获取棋牌盾IP的CC攻击次数和CC攻击峰值
协议：HTTPS 
接口名：ShieldCCGetCounter

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://cloud.tencent.com/document/product/295/7279)页面其中，此接口的Action字段为ShieldCCGetCounter。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String |棋牌盾分组的资源ID，格式是grp-XXXXXXX |
| beginDate | <font color=red> 必选 </font color=red> | String |统计的开始时间，格式是YYYY-MM-DD，如2016-11-10|
| endDate | <font color=red> 必选 </font color=red> | String |统计的结束时间，格式是YYYY-MM-DD，如2016-11-11 |

### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|attacks| <font color=red> 1035/次</font color=red> |Integer |该棋牌盾IP在统计时间内的CC攻击次数|
|attackPeak |<font color=red>35000/qps</font color=red>| Integer | 该棋牌盾IP在统计时间内CC攻击峰值qps |
