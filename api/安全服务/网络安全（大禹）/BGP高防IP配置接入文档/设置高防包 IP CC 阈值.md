## 1.接口描述
设置BGP高防IP的CC防护阈值，当阈值是0表示关闭高防IP的CC防护
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：NS.BGPIP.ServicePack.SetCCThreshold

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.ServicePack.SetCCThreshold。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String | BGP高防IP的资源ID |
| threshold |<font color=red> 必选 </font color=red>| String | CC防护阈值，传0表示关闭CC防护，注意CC防护阈值只能小于当前防护套餐的CC防护峰值，对应关系如下：![](https://mc.qcloudimg.com/static/img/48aebbd9e0e609608399b189c40682dd/image.png)|