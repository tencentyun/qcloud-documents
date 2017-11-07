### 1. 接口描述
本接口 (ListDevices) 用于查询物联云设备的设备列表。

接口请求域名：`iothub.api.qcloud.com`

### 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/6976) 页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| pageSize | 是 | Int | 分页展示的大小。数值范围 10-250。|
| pageNum | 是 | Int | 分页的页数，当前页面会返回第pageNum页的pageSize个结果。|
| productName | 是 | String | 需要查看设备列表的产品名称。|

### 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见[公共错误码](https://cloud.tencent.com/document/product/634/12279)页面。|
| message | String | 模块错误信息描述，格式为 "(模块错误码)模块错误信息" 详见本页面的[模块错误信息](#module_error_info)。|
| codeDesc | String | 模块错误码的英文描述。|
| totalCnt | Int | 设备总数。 |
| devices | Array of Device | 设备对象的数组。|

Device 的结构如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| deviceId | String | 设备的腾讯云资源唯一标识。|
| deviceName | String | 设备的名称。|
| productName | String | 产品的名称。|

### 4. 示例
 
输入
<pre>
  GET https://iothub.api.qcloud.com/v2/index.php?Action=ListDevices
  &productName=fruit&pageSize=10&pageNum=1
  &<<a href="https://cloud.tencent.com/document/api/213/6976">公共请求参数</a>>
</pre>

输出
```
{
    "totalCnt": 2, 
    "devices": [
        {
            "deviceName": "device22", 
            "deviceId": "144115205259838230", 
            "productName": "fruit"
        }, 
        {
            "deviceName": "device21", 
            "deviceId": "144115205260828172", 
            "productName": "fruit"
        }
    ],
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
|2004|获取设备列表的分页参数非法。|



