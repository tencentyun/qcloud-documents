## 接口描述
用于设置某个棋牌盾 IP 的 CC 防护状态的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldSetCCThreshold`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldSetCCThreshold`。

| 参数   | 必选 | 类型     | 描述                   |
| ------ | ---- | ------ | -------------------- |
| bgpId     | 是   | String  | 棋牌盾 IP 的资源ID</br>格式：bgpip-XXXXXXX          |
| threshold | 是   | Integer | CC 防护阈值，单位：QPS</br>等于0表示关闭 CC 防护</br>大于0表示开启 CC 防护 |

## 响应参数
无。
