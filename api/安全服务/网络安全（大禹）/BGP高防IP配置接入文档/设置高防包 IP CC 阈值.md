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
设置 BGP 高防 IP 的 CC 防护阈值，当阈值是 0 表示关闭高防 IP 的 CC 防护
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.SetCCThreshold

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的 Action 字段为 NS.BGPIP.ServicePack.SetCCThreshold。

| 参数名称 | 是否必须 | 类型 | 描述 |
|:---------:|:---------:|:---------:|:---------:|
| bgpId | <font color=red> 必选 </font color=red> | String | BGP 高防 IP 的资源 ID |
| threshold |<font color=red> 必选 </font color=red>| String | CC 防护阈值，传 0 表示关闭 CC 防护，注意 CC 防护阈值只能小于当前防护套餐的 CC 防护峰值，对应关系如下：![](https://mc.qcloudimg.com/static/img/48aebbd9e0e609608399b189c40682dd/image.png)|
