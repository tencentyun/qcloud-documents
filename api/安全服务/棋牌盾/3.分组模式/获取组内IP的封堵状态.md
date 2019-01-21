## 接口描述
用于通过分组 ID 获取分组内所有棋牌盾 IP 的封堵状态的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldGetIPStatus`

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数说明](https://cloud.tencent.com/document/api/213/6976) 页面。其中，此接口的 Action 字段为 `ShieldGetIPStatus`。

| 参数      | 必选 | 类型    | 描述                                       |
| ------- | ---- | ------ | ---------------------------------------- |
| grpId  | 是   | String  | 棋牌盾分组的资源 ID</br>格式：grp-XXXXXXX |

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
| --------- | ----------- | ------- | ------------------ |
| list | [obj,…] | Array  | 转发规则数组，数组元素如下：<pre>{</br>"region": "gz", </br>"ip": "10.1.1.1",</br>"status":"0/1",</br>"unblockTime":"2016-03-02 01:23:45",</br>"name":"www",</br>}</pre> |
| region | gz/sh/bj | String  | 棋牌盾 IP 的地域，目前有一个地区：</br>sh：上海  |
| ip | 10.2.3.4 | String  | 棋牌盾 IP 的 IP 地址 |
| status | 0/1 | Integer | 棋牌盾 IP 的封堵状态</br>0：表示未封堵</br>1：表示封堵中 |
| unblockTime | 2016-03-02</br>01:23:45 | Time | 棋牌盾 IP 的预计解封时间</br>如果状态为封堵中，该字段不为空，否则该字段为空  |
| name | 王者荣誉 | String | 棋牌盾 IP 的名称，由用户自定义 |
