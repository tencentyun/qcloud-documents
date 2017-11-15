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
向某 BGP 高防 IP 下配置转发规则 
<br>协议：HTTPS
<br>域名：csec.api.qcloud.com
<br>接口名：NS.BGPIP.ServicePack.AddTransRules

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的 Action 字段为 NS.BGPIP.ServicePack.AddTransRules。

| 参数名称 | 是否必须 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| bgpId | <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |
| vip | <font color=red> 必选 </font color=red> | String | 高防 IP 的 IP 地址 |
| protocol | <font color=red> 必选 </font color=red> | String | 转发规则所用协议，目前只支持 TCP |
| virtualPort | <font color=red> 必选 </font color=red> | Integer | 转发端口 |
| sourcePort | <font color=red> 必选 </font color=red> | Integer | 源站端口 |
| ipList | <font color=red> 必选 </font color=red> | String | 要转发到机器的 IP 列表，一条规则不超过 20 个 IP |

### 3.输出参数
| 参数名称 | 是否必须 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| ruleId | <font color=red> 必选 </font color=red> | String | 该转发规则的 ID |
