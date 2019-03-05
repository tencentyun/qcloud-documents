## 1. 接口描述
本接口(OpenCdbGtid)用于开通云数据库实例的GTID。
接口请求域名：<font style='color:red'>cdb.api.qcloud.com </font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/document/product/236/6921' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为OpenCdbGtid。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cdbInstanceId | 是 | String | 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](/doc/api/253/1266) 接口获取，其值为输出参数中字段 uInstanceId 的值。 |


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 英文错误描述 |
| data | Array | 返回任务数据 |
其中， data 参数的构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| jobId | String | 任务ID |


## 4. 错误码表
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 9003 | InvalidParameter | 参数错误 |

## 5. 示例
输入
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=OpenCdbExtranetAccess
&<<a href="/document/product/236/6921">公共请求参数</a>>
&cdbInstanceId=cdb-8qrg9t04
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "jobId": 223
    }
}
```

