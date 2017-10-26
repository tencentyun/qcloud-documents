### 1. 接口描述
获取某个棋牌盾IP的详细信息
协议：HTTPS 
接口名：ShieldIPGetInfo

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://cloud.tencent.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldIPGetInfo。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String |棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |

### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|bgpId| <font color=red> bgpip-000001</font color=red> |String | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
|name |<font color=red>王者荣誉</font color=red>| String | 棋牌盾IP的名称，由用户自定义 |
|region |<font color=red>"gz/sh/bj"</font color=red>| String | 棋牌盾IP的地域，目前有一个地区：<br>sh:上海|
|boundIP|<font color=red>1.2.3.4</font color=red>| String | 棋牌盾IP的IP地址 |
|bandwidth|<font color=red>5000Mbps</font color=red>| Integer |棋牌盾IP的防护带宽，单位是Mbps|
|status|<font color=red>idle<br>attacking<br>blocking<br>creating </font color=red>| String | 棋牌盾IP的状态：<br>idle:正常工作中<br>attacking:正在被攻击<br>blocking:被封堵<br>creating:正常创建中 |
|expire|<font color=red>2016-03-02<br>01:23:45 </font color=red>| Time | 棋牌盾IP的到期时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00|
|transTarget|<font color=red>nqcloud </font color=red>| String | 棋牌盾IP的转发目标（源站位置）<br>qcloud:腾讯云内<br>nqcloud:腾讯云外<br>目前固定 nqcloud|
|ccPeak|<font color=red>1200</font color=red>| Integer | CC防护峰值，单位是qps |
|grpName|<font color=red>分组1 </font color=red>|String|棋牌盾IP所属分组的名称，如果没有分组则这个字段是空字符串 |
|ipAmount|<font color=red>1 </font color=red>| Integer | 可忽略 |
|packId|<font color=red>pack-0000001 </font color=red>| String | 可忽略 |