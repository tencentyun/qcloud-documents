## 接口描述
用于获取某个棋牌盾 IP 的转发规则的接口。
协议：HTTPS 
域名：`shield.api.qcloud.com`
接口名：`ShieldIPGetTransRules`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldIPGetTransRules`。

| 参数 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId        | 是  | String  | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX |
| paging.index | 是   | Integer | 页面索引</br>0 示第 1 页          |
| paging.count | 是 | Integer | 每页返回详情数      |

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
| ------- | --------- | ------- | ---------- |
| total       | 123 | Integer | 该棋牌盾 IP 共有多少条规则 |
| transRules  | [obj,…] | Array | 转发规则数组，数组元素如下：<pre>{</br>"id": "rule-0000001",</br> "ipList": "1.1.1.1",</br>"protocol": "gz/sh/bj",</br>"virtualPort": "1.2.3.4",</br>"sourcePort": 10000</br>} </pre> |
| id  | rule-0000001    | String  | 规则 ID</br>格式：rule-XXXXXXX  |
| ipList      | 1.1.1.1;2.2.2.2 | String  | 源站 IP 列表</br>每个 IP 以 **";"** 分隔</br>源站 IP 最多为 20 个  |
| protocol    | TCP             | String  | 转发协议</br>目前固定为 TCP |
| virtualPort | 80              | Integer | 转发端口  |
| sourcePort  | 80              | Integer | 源站端口  |
