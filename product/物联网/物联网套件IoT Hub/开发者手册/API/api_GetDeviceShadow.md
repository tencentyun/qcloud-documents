## 物联云API: GetDeviceShadow


### 1 接口描述
本接口 (GetDeviceShadow) 用于查询虚拟设备信息。

接口请求域名：`iothub.api.cloud.tencent.com`

### 2 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/doc/api/229/6976)页面。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| deviceName | 是 | String | 设备名称。命名规则：[a-zA-Z0-9:_-]{1,128}。|

### 3 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0 表示成功，其他值表示失败。详见错误码页面的[公共错误码]。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码]。|
| state | Object | 虚拟设备当前状态。|
| metadata | Object | 虚拟设备属性的元信息，包括创建时间或者最后修改时间。|
| timestamp | DateTime | 服务器返回时间。|
| version | Long | 当前虚拟设备的版本。|

### 4 示例
 
输入
<pre>
  https://iothub.api.qcloud.com/v2/index.php?Action=GetDeviceShadow
  &deviceName=apple
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "state": {
        "reported": {
            "color": "red"
        },
        "desired": {
            "size": "100"
        },
        "delta": {
            "size": "100"
        }
    },
    "metadata": {
        "reported": {
            "color": {
                "timestamp": 1488783778401
            }
        },
        "desired": {
            "size": {
                "timestamp": 1488783778401
            }
        }
    },
    "timestamp": 1488784436975,
    "version": 1,
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```





