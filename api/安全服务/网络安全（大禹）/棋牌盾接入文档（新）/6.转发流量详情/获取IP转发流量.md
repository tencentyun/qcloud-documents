## 接口描述
用于获取棋牌盾IP的转发流量的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldGetTransFlow`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldGetTransFlow`。

| 参数 | 是否必选 | 类型 | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| id  | 是 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX   |
| beginDate | 是  | String | 统计的开始时间</br>格式：YYYY - MM - DD</br>如 2016-11-10 |
| endDate   | 是   | String | 统计的结束时间</br>格式：YYYY - MM - DD</br>如 2016-11-11 |
| stride | 是 | Integer | 获取转发流量的统计粒度，单位：分钟</br>对应关系如下：</br>时间长度 = 1 天，stride = 5</br>时间长度 = 7 天，stride = 60</br>时间长度 = 30 天，stride = 1440 |

## 响应参数

| 参数 | 示例/单位  | 类型   | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| points | [10,20,15,…]  | Array | 防护（清洗）后的正常流量，每个点代表 stride 时间内的总流量，单位：Mbps  |