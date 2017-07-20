### 1. 接口描述
设置某个棋牌盾IP的CC防护状态
协议：HTTPS 
接口名：ShieldSetCCThreshold

### 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://www.qcloud.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldSetCCThreshold。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | <font color=red> 必选 </font color=red> | String  | 棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
| threshold | <font color=red> 必选 </font color=red> | Integer |CC防护阈值，单位是qps，传0表示关闭CC防护，大于0表示开启CC防护 |