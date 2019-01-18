## 接口描述
用于获取棋牌盾IP的CC攻击统计的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldCCGetStatistics`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldCCGetStatistics`。

| 参数 | 是否必选 | 类型 | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| id | 是 | String  | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX  |
| beginDate | 是 | String | 统计的开始时间</br>格式：YYYY - MM - DD，如 2016-11-10        |
| endDate | 是 | String | 统计的结束时间</br>格式：YYYY - MM - DD，如 2016-11-11 |
| stride | 是 | Integer | 获取 CC 攻击的统计粒度，单位：分钟</br>对应关系如下：</br>时间长度 = 1 天，stride = 5</br>时间长度 = 7 天，stride = 60</br>时间长度 = 30 天，stride = 1440 |

## 响应参数

| 参数 | 示例/单位  | 类型   | 描述 |
| ----- | ---- | ------ | ---------------------------------------- |
| total | 123 | Integer | 共有多少条 CC 攻击记录 |
| records | [obj,…] | Array | 攻击详情数组，数组元素如下：<pre>{</br>"count": "grp-0000001",</br>"endTime": "分组1",</br>"startTime": "40"</br>}</pre> |
| count | 3 | Integer | 该 CC 攻击的总数 |
| startTime | 2013-03-01 01:23:45 | Time | CC 攻击的开始时间</br>格式：YYYY - MM - DD XX:XX:XX</br>如 2016-11-10 11:00:00 |
| endTime | 2013-03-01 01:23:50 | Time | CC攻击的结束时间</br>格式：YYYY  - MM - DD XX:XX:XX</br>如 2016-11-10 11:00:00 |