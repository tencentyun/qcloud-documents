## 1.接口描述
删除某BGP高防IP下添加白名单列表 
<br>协议：HTTPS
<br>域名：csec.api.qcloud.com
<br>接口名：NS.BGPIP.Whitelist. Remove

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上[公共请求参数](https://www.qcloud.com/document/product/295/7279)，见公共参数说明页面。
<br> 其中，此接口的Action字段为NS.BGPIP.Whitelist. Remove。

| 参数名称 | 例子 | 类型 | 描述 |
|---------|---------|---------|---------|
| whitelist | <font color=red>必选</font color=red> | Array | 白名单列表：<br>"whitelist": [<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"http://www.website1.com/",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"http://www.website2.com/"<br>] |