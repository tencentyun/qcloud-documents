### 1. 接口描述
获取棋牌盾IP的DDoS攻击详情 
协议：HTTPS 
接口名：ShieldDDoSGetDetails

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldDDoSGetDetails。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id|<font color=red> 必选 </font color=red>| String  | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX|
| beginDate | <font color=red> 必选 </font color=red> | String | 统计的开始时间，格式是YYYY-MM-DD，如2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String |统计的结束时间，格式是YYYY-MM-DD，如2016-11-11|
| paging.index|<font color=red> 必选 </font color=red>| Integer |页面索引，0表示第一页|
| paging.count|<font color=red> 必选 </font color=red>| Integer |每页返回详情数|


### 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123</font color=red> |Integer | 共有多少条DDoS攻击记录 |
|records |<font color=red> [obj,…]</font color=red>| Array | DDoS攻击详情数组，数组元素如下：<br>{<br>"peak": "300000", <br>"endTime": "2013-03-01 01:23:45",<br>"startTime": "2013-03-01 01:23:50",<br>"overload": "yes/no"<br>}|
|peak| <font color=red> 35000/Mbps</font color=red> |Integer | 该条记录记录的DDoS攻击峰值 |
|startTime| <font color=red> 2013-03-01 01:23:45</font color=red> |Time | DDoS攻击的开始时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00 |
|endTime| <font color=red> 2013-03-01 01:23:50</font color=red> |Time | DDoS攻击的结束时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00 |
|overload| <font color=red> yes/no</font color=red> |String | 该次攻击是否超过防护峰值 |