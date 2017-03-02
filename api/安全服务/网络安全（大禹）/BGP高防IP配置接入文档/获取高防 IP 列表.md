## 1.接口描述
获取该用户名下所有BGP高防IP的列表，每条记录中包含高防IP的一些信息。
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.GetServicePacks 

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.GetServicePacks。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是YYYY-MM-DD，如2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是YYYY-MM-DD，如2016-11-11 |
| filtering. name|<font color=red> 可选 </font color=red>| String | 以高防IP的名称进行关键字查询，支持模糊搜索 |
| filtering.ip|<font color=red> 可选 </font color=red>| String | 以高防IP进行关键字查询，支持模糊搜索 |
| sorting.field|<font color=red> 可选 </font color=red>| String | 取值范围： bandwidth/ overloadCount，bandwidth表示以带宽进行排序， overloadCount表示以超峰次数进行排序 |
| sorting.order|<font color=red> 可选 </font color=red>| String | 取值范围：asc / desc，asc表示升序排列，desc表示降序排列|
| paging.index|<font color=red> 必选 </font color=red>| Integer | 页面索引，0表示第一页|
| paging.count|<font color=red> 必选 </font color=red>| Integer | 每页返回详情数|

## 3.输出参数
| 参数名称 | 例子/单位| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 共有多少个高防IP |
| records|<font color=red> [obj,…]</font color=red>| Array | 攻击详情数组，数组元素如下：<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": "bgp-00000001",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"lbid": "lb-xxxxxxxx" <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "服务包1",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"region": "gz/sh/bj",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"boundIP": "1.2.3.4",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"bandwidth": 10000, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"elasticLimit" : 100000, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"overloadCount" : 100, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"status":"idle/attacking/blocking/creating",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"expire": "2016-03-02 01:23:45",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"locked": "yes/no"<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transTarget":"qcloud/nqcloud/blackstone/finance",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transRules": "12"<br>}|
|id|bgpip-000001| String | 高防IP的资源ID |
| lbid|<font color=red>lb-xxxxxxxx</font color=red>| String | 负载均衡IP的资源ID，只有高防IP是云内IP时才有该字段|
| name|<font color=red>80Gbps</font color=red>| String | 高防IP的名称，由用户自定义|
| region|<font color=red>"gz/sh/bj"</font color=red>| String | 高防IP的地域，目前有三个地区：<br>gz:广州<br>sh:上海<br>bj:北京|
| boundIP|<font color=red>1.2.3.4</font color=red>| String | 高防IP的IP地址|
| bandwidth|<font color=red>10000Mbps</font color=red>| Integer | 高防IP的防护带宽|
| elasticLimit|<font color=red>10000Mbps</font color=red>| Integer | 弹性防护的阈值，超过该阈值后IP将被封堵|
| overloadCount|<font color=red>100</font color=red>| Integer |该高防IP被攻击超峰次数|
| status|<font color=red>idle<br>attacking<br>blocking<br>creating<br>isolate</font color=red>| String |高防IP的状态：<br>idle:正常工作中<br>attacking:正在被攻击<br>blocking:被封堵<br>creating:正常创建中<br>isolate:到期后被隔离|
| expire|<font color=red>2016-03-02 01:23:45</font color=red>| Time | 高防IP的到期时间|
| locked|<font color=red>yes/no</font color=red>|String | 是否被锁|
| transTarget|<font color=red>qcloud<br>nqcloud</font color=red>|String | 高防IP的转发目标<br>qcloud:腾讯云内<br>nqcloud:腾讯云外|
| transRules|<font color=red>12</font color=red>|Integer| 该高防IP配置的转发规则数|

