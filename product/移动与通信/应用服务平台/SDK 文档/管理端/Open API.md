Cloudbase Open API 让开发者可以通过 HTTP 的方式，以管理员身份调用 CloudBase 的服务。

对于 CloudBase 尚未提供 SDK 的语言（如 Java、Go、C++ 等），开发者可以通过此种方式访问 Cloudbase。

## 了解请求结构

1. 服务地址
<dx-codeblock>
:::  URL
https://tcb-api.tencentcloudapi.com
:::
</dx-codeblock>
2. 请求方法
支持的 HTTP 请求方法：**GET**, **POST**, **PUT**, **PATCH**, **DELETE**
3. 请求头构造
<table>
    <thead>
    <tr>
        <th>头部字段</th>
        <th>类型</th>
        <th>必填</th>
        <th>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>X-CloudBase-Authorization</td>
        <td>String</td>
        <td>是</td>
        <td>结构为：<code>&quot;&lt;凭证版本&gt; &lt;CloudBase 签名&gt;&quot;</code>，CloudBase Open API 标准凭证</td>
    </tr>
    <tr>
        <td>X-CloudBase-SessionToken</td>
        <td>String</td>
        <td>是</td>
        <td>腾讯云 CAM 临时密钥的 Session Token</td>
    </tr>
    <tr>
        <td>X-CloudBase-TimeStamp</td>
        <td>Number</td>
        <td>否</td>
        <td>Unix 时间戳，以秒为单位</td>
    </tr>
    <tr>
        <td>content-type</td>
        <td>String</td>
        <td>否</td>
        <td>POST 时请指定 application/json</td>
    </tr>
    </tbody>
</table>

## API 文档

- [介绍](https://docs.cloudbase.net/api-reference/openapi/introduction)

- [数据库](https://docs.cloudbase.net/api-reference/openapi/database)

- [云函数](https://docs.cloudbase.net/api-reference/openapi/function)

- [文件存储](https://docs.cloudbase.net/api-reference/openapi/storage)
