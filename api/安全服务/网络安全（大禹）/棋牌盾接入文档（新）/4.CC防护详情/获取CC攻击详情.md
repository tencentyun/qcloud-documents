## 接口描述
用于获取棋牌盾 IP 的 CC 攻击详情的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldCCGetDetails`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldCCGetDetails`。

| 参数 | 是否必选 | 类型 | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| id  | 是 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX   |
| beginDate | 是    | String | 统计的开始时间</br>格式：YYYY - MM - DD</br>如2016-11-10 |
| endDate      | 是  | String  | 统计的结束时间</br>格式：YYYY - MM - DD</br>如 2016-11-11 |
| paging.index | 是   | Integer | 页面索引</br>0 表示第 1 页  |
| paging.count | 是   | Integer | 每页返回详情数  |

## 响应参数

| 参数 | 示例/单位  | 类型   | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| total | 123  | Integer | CC 攻击记录总数  |
| records  | [obj,…]  | Array | CC 攻击详情数组，数组元素如下：<pre>{</br>"count": "3",</br>"endTime": "2013-03-01 01:23:45",</br>"startTime": "2013-03-01 01:23:50"</br>}</pre> |
| count | 3 | Integer | 该 CC 攻击一共受到多少次攻击 |
| startTime | 2013-03-01 01:23:45 | Time | CC 攻击的开始时间</br>格式：YYYY - MM - DD XX:XX:XX</br>如 2016-11-10 11:00:00 |
| endTime | 2013-03-01 01:23:50 | Time | CC 攻击的结束时间</br>格式：YYYY  - MM - DD XX:XX:XX</br>如 2016-11-10 11:00:00 |