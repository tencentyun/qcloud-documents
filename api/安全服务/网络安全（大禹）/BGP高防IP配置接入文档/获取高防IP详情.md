## 1.接口描述
获取某BGP高防IP的详细信息 
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.GetInfo

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.ServicePack.GetInfo。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId| <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |

## 3.输出参数
| 参数名称 | 例子/单位| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 共有多少条攻击详情 |
| id |bgpip-000001| String | 高防IP的资源ID |
| lbid|<font color=red> lb-xxxxxxxx </font color=red>| String | 负载均衡IP的资源ID，只有高防IP是云内IP时才有该字段 |
|name|<font color=red> 80Gbps</font color=red>| String | 高防IP的名称，由用户自定义 |
|region|<font color=red> "gz/sh/bj"</font color=red>| String | 高防IP的地域，目前有三个地区：<br>gz:广州<br>sh:上海<br>bj:北京 |
|boundIP|<font color=red> 1.2.3.4</font color=red>| String | 高防IP的IP地址 |
|bandwidth|<font color=red> 10000Mbps</font color=red>| Integer | 高防IP的防护带宽 |
|ccPeak|<font color=red> 10000Mbps</font color=red>| Integer | CC防护最大值 |
|ccThreshold|<font color=red> 100 Mbps</font color=red>| Integer | 当前CC防护峰值 |
|elasticLimit|<font color=red> 10000Mbps</font color=red>| Integer | 弹性防护的阈值，超过该阈值后IP将被封堵 |