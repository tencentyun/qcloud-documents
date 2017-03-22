## 1.接口描述
获取BGP高防IP被DDoS攻击次数、攻击峰值和弹性防护开启的次数。
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.Protection.DDoS.GetCounter  

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.Protection.DDoS.GetCounter。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |
| beginDate|<font color=red> 必选 </font color=red>| String | 统计的开始时间，格式是YYYY-MM-DD，如2016-11-10 |
| endDate|<font color=red> 必选 </font color=red>| String | 统计的结束时间，格式是YYYY-MM-DD，如2016-11-11 |

## 3.输出参数
| 参数名称 | 例子/单位| 类型 | 描述 |
|---------|---------|---------|---------|
|attacks| <font color=red> 1035/次 </font color=red> |Integer | DDoS攻击次数 |
| attackPeak |<font color=red> 35000/Mbps </font color=red>| Integer | DDoS攻击峰值 |
| overload|<font color=red> 6/次 </font color=red>| Integer | 弹性防护开启次数 |
|bandwitdh|<font color=red> 80000/Mbps</font color=red>| Integer | 该BGP高防IP的防护带宽 |
