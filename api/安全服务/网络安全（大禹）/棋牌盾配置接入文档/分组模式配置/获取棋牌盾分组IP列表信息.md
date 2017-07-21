### 1. 接口描述
获取棋牌盾分组IP列表信息，该接口可以拉取分组内的IP列表和闲置IP列表
协议：HTTPS 
接口名：ShieldGroupGetIPInfo

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldGroupGetIPInfo。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | <font color=red> 必选 </font color=red> | String |要添加规则的棋牌盾分组的资源ID，格式是grp-XXXXXXX |

### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|validIpList| <font color=red> [obj,…]</font color=red> |Array |转发规则数组，数组元素如下：<br>{<br>"vipId": "bgpip-0000001", <br>"ip": "1.1.1.1",<br>"status":"idle/attacking/blocking/creating",<br>} |
|groupIpList |<font color=red>[obj,…]</font color=red>| Array | 转发规则数组，数组元素如下：<br>{<br>"vipId": "bgpip-0000001", <br>"ip": "1.1.1.1",<br>"status":"idle/attacking/blocking/creating",<br>} |
|vipId |<font color=red>bgpip-000001</font color=red>| String | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
|ip|<font color=red>1.2.3.4</font color=red>| String | 棋牌盾IP的IP地址 |
|status|<font color=red>idle<br>attacking<br>blocking<br>creating </font color=red>| String | 棋牌盾IP的状态：<br>idle:正常工作中<br>attacking:正在被攻击<br>blocking:被封堵<br>creating:正常创建中 |