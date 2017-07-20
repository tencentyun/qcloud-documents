### 1. 接口描述
棋牌盾IP修改名称
协议：HTTPS 
接口名：ShieldIPRename

### 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldIPRename。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String  | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
| name | <font color=red> 必选 </font color=red> | name |棋牌盾IP的名称 |