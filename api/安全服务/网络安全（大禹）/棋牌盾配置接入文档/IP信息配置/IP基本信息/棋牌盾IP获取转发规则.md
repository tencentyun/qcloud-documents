### 1. 接口描述
获取某个棋牌盾IP的转发规则
协议：HTTPS 
接口名：ShieldIPGetTransRules

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldIPGetTransRules。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String  | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
| paging.index | <font color=red> 必选 </font color=red> | Integer |页面索引，0表示第一页 |
| paging.count| <font color=red> 必选 </font color=red> | Integer |每页返回详情数 |

### 3.输出参数
| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|total| <font color=red> 123 </font color=red> |Integer | 该棋牌盾IP共有多少条规则 |
|transRules |<font color=red> [obj,…] </font color=red>| Array | 攻击详情数组，数组元素如下：<br>   {       <br>"id": "rule-0000001", <br>"ipList": "1.1.1.1",<br>"protocol": "gz/sh/bj",<br>"virtualPort": "1.2.3.4",<br>"sourcePort": 10000 <br>} |
|id|<font color=red>rule-0000001</font color=red>| String |规则ID，格式是rule-XXXXXXX|
|ipList |<font color=red>1.1.1.1;2.2.2.2</font color=red>| String | 源站IP列表，每个IP以“;”分隔，源站IP最多为20个|
|protocol|<font color=red>TCP</font color=red>| String |转发协议，目前固定为TCP|
|virtualPort|<font color=red>80</font color=red>| Integer | 转发端口 |
|sourcePort|<font color=red>80</font color=red>| Integer| 源站端口 |