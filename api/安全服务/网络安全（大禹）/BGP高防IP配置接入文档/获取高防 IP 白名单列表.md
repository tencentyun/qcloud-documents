## 1.接口描述
获取某BGP高防IP下白名单列表 
<br>协议：HTTPS
<br>域名：csec.api.qcloud.com
<br>接口名：NS.BGPIP.Whitelist.Get

## 2.输出参数
| 参数名称 | 例子 | 类型 | 描述 |
|---------|---------|---------|---------|
| whitelist | <font color=red> [“域名列表”,…] </font color=red> | Array | 返回用户配置过的白名单列表：<br>"whitelist": [<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"http ://www.website1.com/",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"http ://www.website2.com/"<br>] |