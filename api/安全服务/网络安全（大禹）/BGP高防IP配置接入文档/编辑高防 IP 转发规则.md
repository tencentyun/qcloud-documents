## 1.接口描述
修改转发规则 
<br>协议：HTTPS
<br>域名：csec.api.qcloud.com
<br>接口名：NS.BGPIP.ServicePack.EditTransRules

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.ServicePack.EditTransRules。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| ruleId | <font color=red> 必选 </font color=red> | String | 该转发规则的ID |
| vip | <font color=red> 必选 </font color=red> | String | 高防IP的IP地址 |
| protocol | <font color=red> 必选 </font color=red> | String | 转发规则所用协议，目前只支持TCP |
| virtualPort | <font color=red> 必选 </font color=red> | Integer | 转发端口 |
| sourcePort | <font color=red> 必选 </font color=red> | Integer | 源站端口 |
| ipList | <font color=red> 必选 </font color=red> | String | 要转发到机器的IP列表，一条规则不超过20个IP |