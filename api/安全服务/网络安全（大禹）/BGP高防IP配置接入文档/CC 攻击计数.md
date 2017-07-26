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
#### 接口描述
获取 BGP 高防 IP 被 CC 攻击次数、攻击峰值。
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.Protection.CC.GetCounter

#### 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的 Action 字段为 NS.BGPIP.Protection.CC.GetCounter。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是 YYYY-MM-DD，如 2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是 YYYY-MM-DD，如 2016-11-11 |

#### 输出参数
| 参数名称 | 例子/单位| 类型 | 描述 |
|---------|---------|---------|---------|
|attacks| <font color=red> 1035 / 次 </font color=red> |Integer | CC 攻击次数 |
| attackPeak |<font color=red> 35000 / QPS </font color=red>| Integer | CC 攻击峰值 QPS |

