## 接口描述
用于获取棋牌盾 IP 的 CC 攻击次数和 CC 攻击峰值的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldCCGetCounter`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldCCGetCounter`。

| 参数 | 是否必选 | 类型 | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| id | 是 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX       |
| beginDate | 是  | String | 统计的开始时间</br>格式：YYYY-MM-DD，如2016-11-10 |
| endDate | 是 | String | 统计的结束时间</br>格式：YYYY-MM-DD，如2016-11-11 |

## 响应参数

| 参数 | 示例/单位  | 类型   | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| attacks  | 1035/次    | Integer | 该棋牌盾 IP 在统计时间内的 CC 攻击次数   |
| attackPeak | 35000次/秒 | Integer | 该棋牌盾 IP 在统计时间内 CC 攻击峰值 |
