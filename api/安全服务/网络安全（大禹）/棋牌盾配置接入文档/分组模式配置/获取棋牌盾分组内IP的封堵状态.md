### 1. 接口描述
通过分组ID获取分组内所有棋牌盾IP的封堵状态
协议：HTTPS 
接口名：ShieldGetIPStatus

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldGetIPStatus。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| grpId | <font color=red> 必选 </font color=red> | String |棋牌盾分组的资源ID，格式是grp-XXXXXXX |

### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|list| <font color=red> [obj,…]</font color=red> |Array |转发规则数组，数组元素如下：<br>{<br>"region": "gz", <br>"ip": "1.1.1.1",<br>"status":"0/1",<br>"unblockTime":"2016-03-02 01:23:45",<br>} |
|region |<font color=red>"gz/sh/bj"</font color=red>| String | 棋牌盾IP的地域，目前有一个地区：<br>sh:上海 |
|ip|<font color=red>1.2.3.4</font color=red>| String | 棋牌盾IP的IP地址 |
|status|<font color=red>0/1 </font color=red>| Integer | 棋牌盾IP的封堵状态：0表示未封堵，1表示封堵中 |
|unblockTime|<font color=red>2016-03-02 01:23:45 </font color=red>| Time | 棋牌盾IP的预计解封时间，如果状态为封堵中时该字段不为空，否则该字段是空字段 |