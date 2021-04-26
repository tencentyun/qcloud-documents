## 接口描述
用于获取棋牌盾分组 IP 列表信息的接口，该接口可以拉取分组内的 IP 列表和闲置 IP 列表。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldGroupGetIPInfo`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldGroupGetIPInfo`。

| 参数      | 必选 | 类型    | 描述                                       |
| ------- | ---- | ------ | ---------------------------------------- |
| id  | 是   | String  | 要添加规则的棋牌盾分组的资源 ID</br>格式：grp-XXXXXXX |

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
| --------- | ----------- | ------- | ------------------ |
| validIpList | [obj,…] | Array  | 未进入分组的 IP 列表，数组元素如下：<pre>{</br>"vipId": "bgpip-0000001",</br>"ip": "10.1.1.1",</br>"status":"idle/attacking/blocking/creating",</br>"name": "www",</br>}</pre> |
| groupIpList | [obj,…] | Array  | 已进入分组的 IP 列表，数组元素如下：<pre>{</br>"vipId": "bgpip-0000001",</br>"ip": "10.1.1.1",</br>"status":"idle/attacking/blocking/creating",</br>"name": "www",</br>}</pre> |
| vipId  | bgpip-000001  | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX |
| ip  | 10.2.3.4  | String | 棋牌盾 IP 的 IP 地址  |
| status | idle</br>attacking</br>blocking</br>creating | String | 棋牌盾 IP 的状态</br>idle：正常工作中</br>attacking：正在被攻击</br>blocking：被封堵</br>creating：正常创建中 |
| name  | 王者荣誉  | String | 棋牌盾 IP 的名称，由用户自定义 |
