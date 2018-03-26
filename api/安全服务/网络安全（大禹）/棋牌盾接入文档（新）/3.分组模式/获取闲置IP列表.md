## 接口描述
用于获取棋牌盾闲置 IP （不属于任何分组）列表的接口。
协议：`HTTPS`
域名：`shield.api.qcloud.com`
接口名：`ShieldGroupGetFreeIPs`

## 请求参数
无。

## 响应参数

| 参数 | 示例 | 类型 | 描述 |
| --------- | ----------- | ------- | ------------------ |
| ipList  | [obj,…] | Array | 限制IP列表，数组元素如下：<pre>{</br>"vipId": "bgpip-0000001", </br>"ip": "1.1.1.1",</br>"status":"idle/attacking/blocking/creating",</br>"name": "www",</br>}</pre> |
| vipId  | bgpip-000001  | String | 棋牌盾 IP 的资源 ID</br>格式：bgpip-XXXXXXX |
| ip | 1.2.3.4  | String | 棋牌盾 IP 的 IP 地址 |
| status | idle</br>attacking</br>blocking</br>creating | String | 棋牌盾 IP 的状态</br>idle：正常工作中</br>attacking：正在被攻击</br>blocking：被封堵</br>creating：正常创建中 |
| name   | 王者荣誉 | String | 棋牌盾 IP 的名称，由用户自定义 |