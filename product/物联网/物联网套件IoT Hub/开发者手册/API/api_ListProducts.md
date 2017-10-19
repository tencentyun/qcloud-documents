## 物联云API: ListProducts

### 1 接口描述
本接口 (ListProducts) 用于列出产品列表。

接口请求域名：`iothub.api.cloud.tencent.com`

### 2 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/doc/api/229/1230)页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| maxResults | 否 | Number | 分页，当前页面中显示的最大数量。值范围 1-250，如果不填默认为 250。|
| nextToken | 否 | String | 用于获取剩下的结果，第一次请求无需设置，后续请求使用上一次请求返回结果中的 nextToken。|

### 3 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见错误码页面的[公共错误码]。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码]。|
| nextToken | String | 用于获取剩下的结果，超过 maxResults 结果会返回 nextToken。|
| products | Array | 产品对象的数组。|

产品对象的结构如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| productMetadata | Object | 包含产品的其他信息，包括产品创建日期时间、产品是否被禁用、禁用产品的时间。|
| productProperties | Object | 包含有关产品的信息，包括描述和可搜索设备属性名称的列表。|
| productName | String | 产品名称。|
| productDescription | String | 产品描述。|
| defaultPolicyName | String | 产品默认权限。|

productProperties部分的结构如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| searchableAttributes | String | 产品可搜索的属性名称。|
| productDescription | String | 产品描述。|

productMetadata部分的结构如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| creationDate | DateTime | 产品创建的时间。|
| deprecated | Boolean | 产品是否已禁用，true 表示产品已经被禁用，默认是 false。|
| deprecationDate | DateTime | 产品禁用的日期时间。|

### 4 示例
 
输入
<pre>
  https://iothub.api.cloud.tencent.com/v2/index.php?Action=ListProducts
  &<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "products": [
        {
            "productMetadata": {
                "creationDate": 1488362092000,
                "deprecated": true,
                "deprecationDate": 1488362099000
            },
            "productName": "1",
            "productProperties": {
                "productDescription": "sdf"
            },
            "defaultPolicyName": "OrImgO4F6e5hFVEmXH7MK0XH2GrT15Tr"
        },
        {
            "productMetadata": {
                "creationDate": 1488363213000
            },
            "productName": "2",
            "defaultPolicyName": "OrImgO4F6e5hFVEmXH7MK0XH2GrT15Tr"
        },
        {
            "productMetadata": {
                "creationDate": 1488444357000
            },
            "productName": "123",
            "defaultPolicyName": "OrImgO4F6e5hFVEmXH7MK0XH2GrT15Tr"
        },
        {
            "productMetadata": {
                "creationDate": 1488506139000
            },
            "productName": "hongxj",
            "defaultPolicyName": "OrImgO4F6e5hFVEmXH7MK0XH2GrT15Tr"
        },
        {
            "productMetadata": {
                "creationDate": 1488510855000,
                "deprecated": true,
                "deprecationDate": 1488512432000
            },
            "productName": "fruit",
            "productProperties": {
                "productDescription": "test",
                "searchableAttributes": [
                    "color",
                    "weight"
                ]
            }
        }
    ],
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```