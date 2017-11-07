### 1. 接口描述

本接口 (CreateProduct) 用于创建一个新的物联云产品。

接口请求域名：`iothub.api.cloud.tencent.com`

> **注意:**
> 同一开发商账户下产品名称需保持唯一。

### 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/6976) 页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| productName | 是 | String | 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,128}。|
| productDescription | 否 | String | 产品描述。|


### 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见[公共错误码](https://cloud.tencent.com/document/product/634/12279)页面。|
| message | String | 模块错误信息描述，格式为 "(模块错误码)模块错误信息" 详见本页面的[模块错误信息](#module_error_info)。|
| productName | String | 产品的名称。|
| productQcs | String | 设备的腾讯云资源唯一标识。|


### 4. 示例
 
输入
<pre>
  https://iothub.api.cloud.tencent.com/v2/index.php?Action=CreateProduct
  &productName=fruit
  &<<a href="https://cloud.tencent.com/document/api/213/6976">公共请求参数</a>>
</pre>

输出
```
{
    "productQcs": "qcs::iothub::uin/${uin}:product/fruit",
    "productName": "fruit",
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```
<span id = "module_error_info"></span>
### 5. 模块错误信息

|模块错误码|描述|
|---------|----|
|6|后台内部错误，请重试。|
|1000|创建的产超过数量限制。|
|1001|创建的产品名已存在。|





