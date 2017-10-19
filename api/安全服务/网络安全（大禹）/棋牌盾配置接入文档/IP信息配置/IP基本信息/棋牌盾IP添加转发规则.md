### 1. 接口描述
为某个棋牌盾IP的添加转发规则
协议：HTTPS 
接口名：ShieldIPAddTransRules

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://cloud.tencent.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldIPAddTransRules。每个棋牌盾IP最多添加200条规则。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String |棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
| protocol | <font color=red> 必选 </font color=red> | String |转发协议，目前固定为TCP |
| virtualPort | <font color=red> 必选 </font color=red> | Integer | 转发端口 |
| sourcePort | <font color=red> 必选 </font color=red> | Integer |源站端口 |
| ipList | <font color=red> 必选 </font color=red> | String |源站IP列表，每个IP以“;”分隔，源站IP最多为20个 |


### 3.输出参数

| 参数名称 | 例子| 类型 | 描述 |
|---------|---------|---------|---------|
|ruleId| <font color=red> rule-000001</font color=red> |String | 规则ID，格式是rule-XXXXXXX|