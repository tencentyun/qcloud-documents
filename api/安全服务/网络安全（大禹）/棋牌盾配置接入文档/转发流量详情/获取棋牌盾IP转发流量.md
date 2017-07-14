### 1. 接口描述
获取棋牌盾IP的转发流量
协议：HTTPS 
接口名：ShieldGetTransFlow

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldGetTransFlow。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id|<font color=red> 必选 </font color=red>| String  | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX|
| beginDate | <font color=red> 必选 </font color=red> | String | 统计的开始时间，格式是YYYY-MM-DD，如2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String |统计的结束时间，格式是YYYY-MM-DD，如2016-11-11|
|stride|<font color=red> 必选 </font color=red>| Integer |获取DDoS攻击的统计粒度，单位是分钟，对应关系如下：<br>时间长度=1天，stride=5<br>时间长度=7天，stride=60<br>时间长度=30天，stride=1440|



### 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|points| <font color=red> [10,20,15,…]</font color=red> |Array | 防护（清洗）后的正常流量，每个点代表stride时间内的流量峰值，单位是mbps |
