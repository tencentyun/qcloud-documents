## 物联云API: ListDevices

### 1 接口描述
本接口 (ListDevices) 用于查询物联云设备的设备列表。

接口请求域名：`iothub.api.cloud.tencent.com`

### 2 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/document/api/213/6976)页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| maxResults | 否 | Number | 分页，当前页面中显示的最大数量。数值范围 1-250，默认为 250。|
| nextToken | 否 | String | 用于获取剩下的结果，超过 maxResults 结果会返回 nextToken。|
| productName | 否 | String | 产品名称。命名规则：[a-zA-Z0-9:_-]{1,128}。|

### 3 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见错误码页面的[公共错误码]。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码]。|
| nextToken | String | 用于获取剩下的结果，超过 maxResults 结果会返回 nextToken。|
| devices | Array of Device | 设备对象的数组。|

Device 的结构如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| attributes | Object| 设备的属性。|
| deviceName | String | 设备的名称。|
| productName | String | 产品的名称。|
| version | Long | 设备的当前版本号。|

### 4 示例
 
输入
<pre>
  https://iothub.api.cloud.tencent.com/v2/index.php?Action=ListDevices
  &productName=fruit
  &<<a href="https://cloud.tencent.com/document/api/213/6976">公共请求参数</a>>
</pre>

输出
```
{
    "devices": [
        {
            "attributes": {
                "color": "red",
                "weight": "200",
                "selfprop": "yeah"
            },
            "deviceName": "apple",
            "productName": "fruit",
            "version": 1,
            "principals": [
                "acf8af49a1d76060674585e4b45f4438c50ba21bb9024d82f704a1e45c3de847"
            ]
        },
        {
            "deviceName": "banana",
            "productName": "fruit",
            "version": 1,
            "principals": [
                "8d1f827c7bf6a139da231adf7c0a0cc57fa15ac08f85072940f425069e139f44"
            ]
        }
    ],
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```





