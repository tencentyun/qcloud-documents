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
获取某 BGP 高防 IP 的详细信息 
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.GetInfo

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的 Action 字段为 NS.BGPIP.ServicePack.GetInfo。

| 参数名称 | 是否必须 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| bgpId| <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |

### 3.输出参数
| 参数名称 | 例子 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| id |bgpip-000001| String | 高防 IP 的资源 ID |
| lbid|<font color=red> lb-xxxxxxxx </font color=red>| String | 负载均衡 IP 的资源 ID，只有高防 IP 是云内 IP 时才有该字段 |
|name|<font color=red> 80Gbps</font color=red>| String | 高防 IP 的名称，由用户自定义 |
|region|<font color=red> "gz/sh/bj"</font color=red>| String | 高防 IP 的地域，目前有三个地区：<br>gz: 广州<br>sh: 上海<br>bj: 北京 |
|status|<font color=red>idle<br>attacking<br>blocking<br>creating<br>isolate</font color=red>| String | 高防 IP 的状态：<br>idle：正常工作中<br>attacking：正在被攻击<br>blocking：被封堵<br>creating：正常创建中<br>isolate：到期后被隔离|
|expire|<font color=red> 2016-03-02<br>01:23:45</font color=red>| Time | 高防 IP 的到期时间|
|boundIP|<font color=red> 1.2.3.4</font color=red>| String | 高防 IP 的 IP 地址 |
|bandwidth|<font color=red> 10000Mbps</font color=red>| Integer | 高防 IP 的防护带宽 |
|ccPeak|<font color=red> 10000Mbps</font color=red>| Integer | CC 防护最大值 |
|ccThreshold|<font color=red> 100 Mbps</font color=red>| Integer | 当前 CC 防护峰值 |
|elasticLimit|<font color=red> 10000Mbps</font color=red>| Integer | 弹性防护的阈值，超过该阈值后 IP 将被封堵 |
|transTarget|<font color=red> qcloud<br>nqcloud</font color=red>| String | 高防 IP 的转发目标<br>qcloud：腾讯云内<br>nqcloud：腾讯云外 |
|vpcId|<font color=red> 1234 </font color=red>| Integer | vpc 网络 ID |
