<style rel="stylesheet">
table th:nth-of-type(1){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(2){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(3){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(4){
width:200px;
}</style>
<style rel="stylesheet">
table tr:hover {
background: #efefef; 
</style>
### 1.接口描述
获取 BGP 高防 IP 被 CC 攻击流量详情
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.Protection.CC.GetDetails 

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的 Action 字段为 NS.BGPIP. Protection.DDoS.GetDetails。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是 YYYY-MM-DD，如 2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是 YYYY-MM-DD，如 2016-11-11 |
| sorting.field|<font color=red> 可选 </font color=red>| String | 取值范围：count，表示以攻击峰值做排序 |
| sorting.order|<font color=red> 可选 </font color=red>| String | 取值范围：asc / desc，asc 表示升序排列，desc 表示降序排列 |
| paging.index|<font color=red> 必选 </font color=red>| Integer | 页面索引，0 表示第一页 |
| paging.count|<font color=red> 必选 </font color=red>| Integer | 每页返回详情数 |

### 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 共有多少条攻击详情 |
|records |<font color=red> [obj,…] </font color=red>| Array | 攻击详情数组，数组元素如下：<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"startTime" : "2013-03-01 01:23:45",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "endTime" : "2013-03-01 01:23:45",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "count" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 1234<br>} |
|startTime|2013-03-01 01:23:45| Time | 攻击开始时间|
|endTime|2013-03-01 01:23:50| Time | 攻击结束时间|
|count|<font color=red>80 次 </font color=red>| Integer | 攻击峰值 |
