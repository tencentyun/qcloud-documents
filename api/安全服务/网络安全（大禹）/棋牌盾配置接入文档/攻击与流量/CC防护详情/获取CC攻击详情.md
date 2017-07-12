### 1. 接口描述
获取棋牌盾IP的CC攻击详情 
协议：HTTPS 
接口名：ShieldCCGetDetails

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldCCGetDetails。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String |棋牌盾分组的资源ID，格式是grp-XXXXXXX |
| beginDate | <font color=red> 必选 </font color=red> | String |统计的开始时间，格式是YYYY-MM-DD，如2016-11-10|
| endDate | <font color=red> 必选 </font color=red> | String |统计的结束时间，格式是YYYY-MM-DD，如2016-11-11 |
|paging.index | <font color=red> 必选 </font color=red> | Integer |页面索引，0表示第一页 |
| paging.count | <font color=red> 必选 </font color=red> | Integer |每页返回详情数 |

### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123</font color=red> |Integer |共有多少条CC攻击记录|
|records |<font color=red>[obj,…]</font color=red>|Array | CC攻击详情数组，数组元素如下：<br>{<br>"count": "3", <br>"endTime": "2013-03-01 01:23:45",<br>"startTime": "2013-03-01 01:23:50"<br>} |
|count| <font color=red> 3</font color=red> |Integer |该CC攻击一共受到多少次攻击|
|startTime| <font color=red>2013-03-01 01:23:45</font color=red> |Time |CC攻击的开始时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00|
|endTime| <font color=red>2013-03-01 01:23:45</font color=red> |Time |CC攻击的结束时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00|