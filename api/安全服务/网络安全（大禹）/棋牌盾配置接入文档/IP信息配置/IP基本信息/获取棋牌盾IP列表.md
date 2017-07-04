### 1. 接口描述
获取该用户名下所有棋牌盾IP的列表，每条记录中包含IP的一些信息。
协议：HTTPS 
接口名：ShieldGetServicePacks

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldGetServicePacks。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| filtering. name | <font color=red> 可选 </font color=red> | String | 以棋牌盾IP的名称进行关键字查询，支持模糊搜索 |
| filtering.ip|<font color=red> 可选 </font color=red>| String  | 以IP进行关键字查询，支持模糊搜索 |
| paging.index|<font color=red> 必选 </font color=red>| Integer |页面索引，0表示第一页|
| paging.count|<font color=red> 必选 </font color=red>| Integer | 每页返回详情数|
| region|<font color=red> 必选 </font color=red>| String  | 棋牌盾的地域，目前有一个地区：<br>sh:上海|



### 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 共有多少个棋牌盾IP |
|servicePacks |<font color=red> [obj,…] </font color=red>| Array | 攻击详情数组，数组元素如下：<br>   {       <br>"id": "bgpip-0000001", <br>"name": "服务包1",<br>"region": "gz/sh/bj",<br>"boundIP": "1.2.3.4",<br>"bandwidth": 10000, <br>"status":"idle/attacking/blocking/creating",<br>"expire": "2016-03-02 01:23:45",<br>"transTarget":"nqcloud ",<br>"transRules": "12"，<br>"grpName":"分组1",<br>"ipAmount":"20",<br>"packId":" pack-0000001",<br>} |
|id|<font color=red>bgpip-000001</font color=red>| String |棋牌盾IP的资源ID，格式是bgpip-XXXXXXX|
|name|<font color=red>王者荣誉 </font color=red>| String | 棋牌盾IP的名称，由用户自定义 |
|region|<font color=red>"gz/sh/bj" </font color=red>| String | 棋牌盾IP的地域，目前有一个地区：<br>sh:上海 |
|boundIP|<font color=red>1.2.3.4</font color=red>| String |棋牌盾IP的IP地址|
|bandwidth|<font color=red>5000Mbps </font color=red>| Integer | 棋牌盾IP的防护带宽，单位是Mbps |
|status|<font color=red>idle<br>attacking<br>blocking<br>creating </font color=red>| String | 棋牌盾IP的状态：<br>idle:正常工作中<br>attacking:正在被攻击<br>blocking:被封堵<br>creating:正常创建中 |
|expire|<font color=red>2016-03-02<br>01:23:45 </font color=red>| Time | 棋牌盾IP的到期时间，格式是YYYY-MM-DD XX:XX:XX，如2016-11-10 11:00:00|
|transTarget|<font color=red>nqcloud </font color=red>| String | 棋牌盾IP的转发目标（源站位置）<br>qcloud:腾讯云内<br>nqcloud:腾讯云外<br>目前固定 nqcloud|
|transRules|<font color=red>12</font color=red>| Integer | 该棋牌盾IP配置的转发规则数 |
|grpName|<font color=red>分组1 </font color=red>|String|棋牌盾IP所属分组的名称，如果没有分组则这个字段是空字符串 |
|ipAmount|<font color=red>1 </font color=red>| Integer | 可忽略 |
|packId|<font color=red>pack-0000001 </font color=red>| String | 可忽略 |