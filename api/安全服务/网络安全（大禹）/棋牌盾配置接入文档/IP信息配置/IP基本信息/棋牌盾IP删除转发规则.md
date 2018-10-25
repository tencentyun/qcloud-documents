### 1. 接口描述
删除某个棋牌盾IP的转发规则
协议：HTTPS 
接口名：ShieldIPDeleteTransRules

### 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详见[公共参数说明](https://cloud.tencent.com/document/product/295/7279)页面。其中，此接口的Action字段为ShieldIPDeleteTransRules。

| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
| ruleId | <font color=red> 必选 </font color=red> | String |规则ID，格式是rule-XXXXXXX |
