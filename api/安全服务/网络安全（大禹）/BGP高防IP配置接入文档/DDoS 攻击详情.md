## 1.接口描述
获取BGP高防IP被CC攻击流量详情
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.Protection.CC.GetDetails 

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP. Protection.DDoS.GetDetails。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是YYYY-MM-DD，如2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是YYYY-MM-DD，如2016-11-11 |
| filtering.overload|<font color=red> 可选 </font color=red>| String | 取值范围：yes/no，yes表示只看超峰值的，no表示只看没有超峰值的 |
| sorting.field|<font color=red> 可选 </font color=red>| String | 取值范围：peak，表示以攻击峰值做排序 |
| sorting.order|<font color=red> 可选 </font color=red>| String | 取值范围：asc / desc，asc表示升序排列，desc表示降序排列 |
| paging.index|<font color=red> 必选 </font color=red>| Integer | 页面索引，0表示第一页 |
| paging.count|<font color=red> 必选 </font color=red>| Integer | 每页返回详情数 |

## 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 共有多少条攻击详情 |
|records |<font color=red> [obj,…] </font color=red>| Array | 攻击详情数组，数组元素如下：<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"startTime" : "2013-03-01 01:23:45",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "endTime" : "2013-03-01 01:23:45",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "peak" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :   1234<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "overload" : "yes/no"} |
|startTime|2013-03-01 01:23:45| Time | 攻击开始时间|
|endTime|2013-03-01 01:23:50| Time | 攻击结束时间|
|peak|<font color=red>80Mbps </font color=red>| Integer | 攻击峰值流量 |
|overload|<font color=red> yes/no </font color=red>| String | 是否超过防护峰值 |