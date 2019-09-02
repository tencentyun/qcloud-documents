## 1. 接口描述

本接口（RefreshCdnOverSeaUrl）用于将境外 CDN 节点上指定资源设置为过期。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

[调用Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 RefreshCdnOverSeaUrl。

| 参数名称   | 是否必选 | 类型     | 描述                     |
| ------ | ---- | ------ | ---------------------- |
| urls.n | 是    | String | 需要刷新的 URL，支持刷新一个或多个 URL |



>!
>+ 支持刷新一个或多个 URL，刷新多个URL时，参数传入方式可参考： ```urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg```
+ 注意 URL 必须以 'http://' 或 'https://' 开头，否则会报错。
+ 每日刷新数量不超过10000个，每次提交的 URL 数量不超过1000个




## 3. 输出参数

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关                           |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array  | 详细说明见下文                                  |

**data字段说明：**

| 参数名称  | 类型   | 描述           |
| ----- | ---- | ------------ |
| count | Int  | 此次刷新提交的 URL 数目 |




## 4. 示例

### 4.1 输入示例

```
urls.0: https://www.test.com/1.jpg
```



### 4.2 GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=RefreshCdnOverSeaUrl
&SecretId=XXXXXXXXXXXXXXXXXX
&Timestamp=1462521223
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&urls.0=https%3A%2F%2www.test.com%2F1.jpg
```



### 4.3 POST 请求

POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'RefreshCdnOverSeaUrl',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462864833,
  'Nonce' => 1149033341,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'urls.0' => 'https://www.test.com/1.jpg'
)
```



### 4.4 返回结果示例

#### 刷新提交成功 

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "count": 1
    }
}
```

#### 刷新提交失败

```json
{
    "code": 4000,
    "message": "(9110)没有这个域名的信息 cdn no such host",
    "codeDesc": "9110"
}
```
