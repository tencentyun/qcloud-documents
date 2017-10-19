## 物联云API: CreateProduct

### 1 接口描述

本接口 (CreateProduct) 用于创建一个新的物联云产品。

接口请求域名：`iothub.api.cloud.tencent.com`

> **注意:**
> 同一开发商账户下产品名称需保持唯一。

### 2 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.cloud.tencent.com/doc/api/229/6976)页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| productName | 是 | String | 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,128}。|
| productDescription | 否 | String | 产品描述。|


### 3 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见错误码页面的[公共错误码]。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码]。|
| productName | String | 产品的名称。|
| productQcs | String | 设备的腾讯云资源唯一标识。|


### 4 示例
 
输入
<pre>
  https://iothub.api.qcloud.com/v2/index.php?Action=CreateProduct
  &productName=fruit
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
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





