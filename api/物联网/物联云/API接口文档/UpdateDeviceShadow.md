### 1. 接口描述
本接口 (UpdateDeviceShadow) 用于更新虚拟设备信息。

接口请求域名：`iothub.api.qcloud.com`

### 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/6976) 页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| productName | 是 | String | 产品名称。命名规则：[a-zA-Z0-9:_-]{1,128}。|
| deviceName | 是 | String | 设备名称。命名规则：[a-zA-Z0-9:_-]{1,128}。|
| state | 否 | String | 虚拟设备的状态，json格式，里面由reported或者desired结构组成。|
| version | 否 | Long | 当前版本号，如果带了version字段，需要和后台的version保持一致才能更新成功。|

### 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见错误码页面的【公共错误码】。|
| codeDesc | String | 返回码描述。|
| message | String | 模块错误信息描述，格式为 "（模块错误码）模块错误信息" 详见本页面的[模块错误信息](#module_error_info)。|
| state | Object | 虚拟设备当前状态。|
| metadata | Object | 虚拟设备属性的元信息，包括创建时间或者最后修改时间。|
| timestamp | DateTime | 服务器返回时间。|
| version | Long | 当前虚拟设备的版本。|

### 4. 示例
 
输入
<pre>
  var oState = {"state": {"reported": {"red": "red","blue": "blue"}}};
  var sState = encodeURIComponent(JSON.stringify(oProperties));
  https://iothub.api.qcloud.com/v2/index.php?Action=UpdateDeviceShadow
  &deviceName=sdfsdfsdf
  &productName=dante0831
  &state=${sProperties}
  &<<a href="https://cloud.tencent.com/document/api/213/6976">公共请求参数</a>>
</pre>

输出
```
{
    "state": {
        "reported": {
            "red": "red",
            "blue": "blue"
        }
    },
    "metadata": {
        "reported": {
            "red": {
                "timestamp": 1509092895971
            },
            "blue": {
                "timestamp": 1509443636316
            }
        }
    },
    "timestamp": 1509443636326,
    "version": 5,
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```
<span id = "module_error_info"></span>
### 5. 模块错误信息

|模块错误码|描述|
|---------|----|
|6|后台内部错误，请联系api负责人。|
|5000|请求中缺少关键信息，如endpoint或action。|
|5002|State json对象的层数超过了限制，最大为6层。|
|5003|State json对象中包含非法节点。|
|5004|State json对象格式非法。|
|5005|version不匹配，需要与后台版本一致。|
|5006|State json对象超过大小限制，最大为8k。|