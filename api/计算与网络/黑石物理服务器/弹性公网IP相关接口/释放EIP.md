## 1. 接口描述
该接口用于释放弹性公网IP，以方便用户清理不使用的EIP资源。

域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: EipBmDelete



 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipIds.n|是|数组型|EIP实例ID列表，可以通过[DescribeEipBm](/doc/api/456/6671)接口查询，数组下标从0开始|

 > 绑定状态的EIP不可以释放，只可以释放未绑定状态的EIP。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务信息，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[EipBmQueryTask](/doc/api/456/6670)查询任务状态|

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InternalCgwErr|内部接口异常|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30009|EipNotExist|操作的EIP记录不存在|
|30010|EipStateCannotOp|EIP当前状态不允许释放|
|30013|EipRecordNotExist|EIP记录不存在|

## 5. 示例
 
输入
<pre>

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=EipBmDelete
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>&eipIds.0=eip-iiiii
</pre>

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383049
    }
}

```

