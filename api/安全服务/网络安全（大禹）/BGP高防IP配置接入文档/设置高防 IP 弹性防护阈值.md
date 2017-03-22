## 1.接口描述
设置BGP高防IP的弹性防护峰值，当阈值是0表示关闭高防IP的弹性防护功能
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.SetElasticProtectionLimit

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.ServicePack.SetElasticProtectionLimit。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |
| limit |<font color=red> 必选 </font color=red>| Integer | 弹性防护峰值，传0表示关闭弹性防护,单位是Mb |
