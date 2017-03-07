## 1.接口描述
获取某BGP高防IP配置过的转发规则列表 
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.GetTransRules

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.ServicePack.GetTransRules。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |
| paging.index|<font color=red> 必选 </font color=red>| Integer | 页面索引，0表示第一页 |
| paging.count|<font color=red> 必选 </font color=red>| Integer | 每页返回详情数|


## 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 该高防IP共配置过多少条转发规则 |
|transRules |<font color=red> [obj,…] </font color=red>| Array | 攻击详情数组，数组元素如下：<br>{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": "rule-00000001",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"protocol": "TCP" <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"virtualPort": "80",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"sourcePort": "80",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ipList": "1.2.3.4；1.1.1.1"<br>} |
|id|rule-00000001| String | 该转发规则的ID|
|protocol|<font color=red>TCP </font color=red>| String | 转发规则所用协议，目前只支持TCP |
|virtualPort|<font color=red>80 </font color=red>| Integer | 转发端口 |
|sourcePort|<font color=red>80 </font color=red>| Integer | 源站端口 |
|ipList|<font color=red>"1.2.3.4；1.1.1.1" </font color=red>| String | 要转发到机器的IP列表，一条规则不超过20个IP |

