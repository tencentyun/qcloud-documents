## 接口描述
用于获取某个棋牌盾 IP 的详细信息的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldIPGetInfo`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldIPGetInfo`。

| 参数 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | 是 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX |

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
|---------|---------|---------|---------|
| bgpId | bgpip-000001 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX  |
| name | 王者荣耀 | String | 棋牌盾 IP 的名称，由用户自定义 |
| region | gz / sh / bj | String | 棋牌盾 IP 的地域</br>目前只有一个地区：</br>sh：上海 |
| boundIP | 10.2.3.4 | String | 棋牌盾 IP 的 IP 地址 |
| bandwidth | 5000 Mbps | Integer | 棋牌盾 IP 的防护带宽</br>单位： Mbps |
| status | idle</br>attacking</br>blocking</br>creating | String | 棋牌盾 IP 的状态：</br>idle：正常工作中</br>attacking：正在被攻击</br>blocking：被封堵</br>creating：正常创建中 |
| expire | 2016-03-02</br>01:23:45 | Time | 棋牌盾 IP 的到期时间</br>格式：YYYY-MM-DD XX:XX:XX</br>如2016-11-10 11:00:00 |
| transTarget | nqcloud | String | 棋牌盾 IP 的转发目标（源站位置）</br>qcloud：腾讯云内</br>nqcloud：腾讯云外</br>目前固定为 nqcloud |
| ccPeak | 1200 | Integer | CC 防护峰值,/br>单位：QPS |
| grpName | 分组 1 | String | 棋牌盾 IP 所属分组的名称</br>如果没有分组则这个字段是空字符串 |
| ipAmount | 1 | Integer | 可忽略 |
| packId | pack-0000001 | String | 可忽略 |
