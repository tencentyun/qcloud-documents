
本文主要介绍了信鸽版本到移动推送 TPNS 版本的接口迁移说明，包括 V3 和 V2 的推送接口、账号接口和标签接口的差异。

## 请求域名地址变动说明

**请求参数变动说明**

| 协议字段 | 字段含义说明 | 变动说明 |
| ----------------- | ------------ | ------------------------------------------------------------ |
| openapi.xg.qq.com | 域名 | 请根据选择的服务接入点选择对应的域名地址：<br>1. 广州服务接入点：api.tpns.tencent.com<br>2. 中国香港服务接入点：api.tpns.hk.tencent.com<br>3. 新加坡服务接入点：api.tpns.sgp.tencent.com<br>4. 上海服务接入点：api.tpns.sh.tencent.com |

## V3 接口协议变动说明

[移动推送 TPNS 版本 V3 接口协议格式](https://cloud.tencent.com/document/product/548/39061) 对比 [信鸽版本V3接口协议格式](https://xg.qq.com/docs/server_api/v3/rest_api_summary.html)基本相同。
协议中部分字段格式以及命名有变化，具体差异如下：

### 鉴权方式

信鸽版本使用 `AppId + SecretKey` 进行 `Basic Auth` 鉴权。([信鸽版本鉴权说明](https://xg.qq.com/docs/server_api/v3/rest_api_summary.html#%E9%89%B4%E6%9D%83%E6%96%B9%E5%BC%8F))

移动推送 TPNS 版本使用 `AccessId + SecretKey` 进行 `Basic Auth` 鉴权。([移动推送 TPNS 版本鉴权说明](https://cloud.tencent.com/document/product/548/39062))

>?**移动推送 TPNS 版本没有对应 AppId 字段， 需要使用对应的应用 id `AccessId` 和密钥 `SecretKey ` 进行鉴权**。


### 推送接口


[移动推送 TPNS 版本推送接口协议](https://cloud.tencent.com/document/product/548/39064) 格式和 [信鸽版本](https://xg.qq.com/docs/server_api/v3/push_api_v3.html) 基本相同, 主要区别如下:

**请求参数变动说明**

| 协议字段 | 字段含义说明 | 信鸽版 | 移动推送 TPNS 版 |
| --------------- | -------------------------------------------------- | ------------------------------------------------------------ | -------------------------------- |
| custom\_content | Android 推送自定义参数 | 字段格式： json | 字段格式：需要序列化为 json string |
| custom\_content | iOS 推送自定义参数 | 字段格式： json | 字段格式：需要序列化为 json string |
| push\_id | 账号列表推送和设备列表推送时，需要填写的推送任务ID | 账号列表推送和设备列表推送时，<br/>第一次推送该值填0，系统会创建<br/>对应的推送任务，并且返回对应的<br/>pushid：123，后续推送push\_id填<br/>123(同一个文案）表示使用与123 id 对应的文案进行推送 | 不再支持该字段对应功能 |


### 账号绑定接口

[移动推送 TPNS 版本账号绑定协议格式](https://cloud.tencent.com/document/product/548/39070) 和 [信鸽版本](https://xg.qq.com/docs/server_api/v3/account-api.html) 完全相同，无需特别改动。


### 账号查询接口

[移动推送 TPNS 版本账号查询协议格式](https://cloud.tencent.com/document/product/548/39071) 和 [信鸽版本](https://xg.qq.com/docs/server_api/v3/account-api.html#账号-设备绑定查询（批量操作）) 基本相同，主要区别如下：

**响应参数变动说明**

| 协议字段 | 字段含义说明 | 变动说明 |
| --------- | ------------ | ------------------- |
| ret\_code | 操作返回码 | 字段名变更为 retCode |
| err\_msg | 操作响应消息 | 字段名变更为 errMsg |

### 标签绑定接口

[移动推送 TPNS 版本标签绑定协议格式](https://cloud.tencent.com/document/product/548/39067) 和 [信鸽版本](https://xg.qq.com/docs/server_api/v3/tag_api_v3.html) 基本相同，主要区别如下:

**请求参数变动说明**

| 协议字段 | 字段含义说明 | 信鸽版 | 移动推送 TPNS 版 |
| ---------------- | --------------------------------- | ---------------------------------------- | ------------------------------------------ |
| tag\_token\_list | 当进行标签和设备批量绑定/解绑时，提供需要绑定/解绑<br/>的标签设备列表，operator\_type =9,10时必填 | 字段格式：[[&quot;tag1&quot;,&quot;token1&quot;]，[&quot;tag2&quot;,&quot;token2&quot;]]，每个对里面标签在前，token在后， 列表中每个元素为 jsonArray | 字段格式：[{&quot;tag&quot;:&quot;tag123&quot;, &quot;token&quot;:&quot;token123&quot;}]，列表中每个原始为 jsonObject |

### 返回码

移动推送 TPNS 版本错误码是一套全新的返回码，和信鸽版本不同。
信鸽版本返回码定义参考：[信鸽版本返回码](https://xg.qq.com/docs/server_api/v3/push_api_v3.html#错误码)
移动推送 TPNS 版本返回码定义参考：[移动推送 TPNS 版本返回码](https://cloud.tencent.com/document/product/548/39080)

## V2 接口协议变动说明

**移动推送 TPNS 版本不再支持V2 协议接口**

V2 版本对应的V3 版本接口参考如下：

| V2接口 | V2接口url | V3 接口 | V3 接口url | 接口定义说明 |
| ---------------- | -------------------------------- | ---------------------------- | -------------- | ------------------------------------------------------------ |
| 全量推送 | /v2/push/all\_device | 推送接口 | /v3/push/app |参考 [推送接口文档](https://cloud.tencent.com/document/product/548/39064) |
| 标签推送 | /v2/push/tags\_device | 推送接口 | /v3/push/app |参考 [推送接口文档](https://cloud.tencent.com/document/product/548/39064) |
| 账号群推 | /v2/push/account\_list | 推送接口 | /v3/push/app |参考 [推送接口文档](https://cloud.tencent.com/document/product/548/39064) |
| 设备单推 | /v2/push/single\_device | 推送接口 | /v3/push/app |参考 [推送接口文档](https://cloud.tencent.com/document/product/548/39064) |
| 账号单推 | /v2/push/single\_account | 推送接口 | /v3/push/app | 参考 [推送接口文档](https://cloud.tencent.com/document/product/548/39064) |
| 超大批量账号推送 | /v2/push/account\_list\_multiple | 不支持，可使用号码包推送替代 |- | -|
| 超大批量设备推送 | v2/push/device\_list\_multiple | 不支持，可使用号码包推送替代 |- |- |
| 批量新增标签 | /v2/tags/batch\_set | 标签绑定接口 | /v3/device/tag | 参考 [标签接口文档](https://cloud.tencent.com/document/product/548/39067) |
| 批量删除标签 | /v2/tags/batch\_del | 标签绑定接口 | /v3/device/tag |参考 [标签接口文档](https://cloud.tencent.com/document/product/548/39067) |
