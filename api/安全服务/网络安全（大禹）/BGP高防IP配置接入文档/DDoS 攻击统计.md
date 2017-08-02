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
获取 BGP 高防 IP 被 DDoS 攻击流量统计图
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.Protection.DDoS.GetStatistics  

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。其中，此接口的 Action 字段为 NS.BGPIP.Protection.DDoS.GetStatistics。

| 参数名称 | 是否必须 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| id | <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是 YYYY-MM-DD，如 2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是 YYYY-MM-DD，如 2016-11-11 |
| stride|<font color=red> 必选 </font color=red>| Integer | 攻击流量的统计粒度，单位是分钟，对应关系如下：<br>时间长度 = 1 天，stride = 5<br>时间长度 = 7 天，stride = 60<br>时间长度 = 30 天，stride = 1440 |


### 3.输出参数
| 参数名称 | 例子 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
|before| <font color=red> [1000Mbps,…] </font color=red> |Array | 防护前流量峰值，即这段时间粒度内的流量最大值，例如粒度是五分钟，就表示 5 分钟之内的峰值 |
| after |<font color=red> [50Mbps,…] </font color=red>| Array | 清洗过的用户正常流量，即这段时间粒度内的流量最大值，例如粒度是五分钟，就表示 5 分钟之内的峰值 |
