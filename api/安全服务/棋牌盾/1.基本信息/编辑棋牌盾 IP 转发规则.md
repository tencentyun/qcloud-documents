## 接口描述
用户编辑某个棋牌盾 IP 的转发规则的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldIPEditTransRules`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldIPEditTransRules`。

| 参数 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| ruleId | 是 | String | 规则 ID</br>格式：rule-XXXXXXX |
| protocol | 是 | String | 转发协议</br>目前固定为 TCP |
| virtualPort | 是  | Integer | 转发端口                         |
| sourcePort  | 是  | Integer | 源站端口                         |
| ipList      | 是  | String  | 源站 IP 列表</br>每个 IP 以**“;”**分隔</br>源站 IP 最多为20个 |

## 响应参数
无。
