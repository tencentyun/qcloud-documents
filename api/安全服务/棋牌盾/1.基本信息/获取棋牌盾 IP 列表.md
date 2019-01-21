## 接口描述
用于获取该用户名下所有棋牌盾 IP 的列表的接口，每条记录中包含 IP 的一些相关信息。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldGetServicePacks`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldGetServicePacks`。

| 参数 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| filtering. name | 否 | String | 以棋牌盾 IP 的名称进行关键字查询，支持模糊搜索 |
| filtering.ip | 否 | String | 以 IP 进行关键字查询，支持模糊搜索 |
| paging.index | 是 | Integer | 页面索引</br>0表示第1页 |
| paging.count | 是 | Integer | 每页返回的详情数 |
| region | 是 | String | 棋牌盾的地域</br>目前只有一个地区：</br>sh：上海 |

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
|---------|---------|---------|---------|
| total | 123 | Integer | 共有多少个棋牌盾 IP|
| servicePacks | [obj,…] | Array | 攻击详情数组，数组元素如下：<pre>{</br>"id": "bgpip-0000001", </br>"name": "服务包1",</br>"region": "gz/sh/bj",</br>"boundIP": "10.2.3.4",</br>"bandwidth": 10000,</br>"status":"idle/attacking/blocking/creating",</br>"expire":"2016-03-02 01:23:45",</br>"transTarget":"nqcloud ",</br>"transRules": "12"，</br>"grpName":"分组1",</br>"ipAmount":"20",</br>"packId":" pack-0000001",</br>}</pre> |
| id | bgpip-000001 | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX |
| name | 王者荣誉 | String | 棋牌盾 IP 的名称，由用户自定义 |
| region | gz/sh/bj | String | 棋牌盾 IP 的地域</br>目前只有一个地区：</br>sh：上海 |
| boundIP | 10.2.3.4 | String | 棋牌盾 IP 的 IP 地址 |
| bandwidth | 5000 Mbps | Integer | 棋牌盾 IP 的防护带宽</br>单位： Mbps |
| status | idle</br>attacking</br>blocking</br>creating | String | 棋牌盾 IP 的状态：</br>idle：正常工作中</br>attacking：正在被攻击</br>blocking：被封堵</br>creating：正常创建中 |
| expire | 2016-03-02</br>01:23:45 | Time | 棋牌盾 IP 的到期时间</br>格式：YYYY-MM-DD XX:XX:XX</br>如2016-11-10 11:00:00 |
| transTarget | nqcloud | String | 棋牌盾 IP 的转发目标（源站位置）</br>qcloud：腾讯云内</br>nqcloud：腾讯云外</br>目前固定为 nqcloud |
| transRules | 12 | Integer | 该棋牌盾 IP 配置的转发规则数 |
| grpName | 分组 1 | String | 棋牌盾 IP 所属分组的名称</br>如果没有分组则这个字段是空字符串 |
| ipAmount | 1 | Integer | 可忽略 |
| packId | pack-0000001 | String | 可忽略 |
