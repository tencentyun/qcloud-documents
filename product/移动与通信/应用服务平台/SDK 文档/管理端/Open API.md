Cloudbase Open API 让开发者可以通过 HTTP 的方式，以管理员身份调用 CloudBase 的服务。

对于 CloudBase 尚未提供 SDK 的语言（如 Java、Go、C++ 等），开发者可以通过此种方式访问 Cloudbase。

## 了解请求结构

1. 服务地址

**https://tcb-api.tencentcloudapi.com**

1. 请求方法

支持的 HTTP 请求方法：**GET**, **POST**, **PUT**, **PATCH**, **DELETE**

3. 请求头构造

| 头部字段                  | 类型   | 必填 | 说明                                                                 |
| ------------------------- | ------ | ---- | -------------------------------------------------------------------- |
| X-CloudBase-Authorization | String | 是   | 结构为：`"<凭证版本> <CloudBase 签名>"`，CloudBase Open API 标准凭证 |
| X-CloudBase-SessionToken  | String | 是   | 腾讯云 CAM 临时密钥的 Session Token                                  |
| X-CloudBase-TimeStamp     | Number | 否   | Unix 时间戳，以秒为单位                                              |
| content-type              | String | 否   | POST 时请指定 application/json                                       |

## API 文档

- [介绍](https://docs.cloudbase.net/api-reference/openapi/introduction.html)

- [数据库](https://docs.cloudbase.net/api-reference/openapi/database.html)

- [云函数](https://docs.cloudbase.net/api-reference/openapi/function.html)

- [文件存储](https://docs.cloudbase.net/api-reference/openapi/storage.html)
