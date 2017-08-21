## 1. 接口描述
该接口用于修改弹性公网IP的计费模式，目前有两种计费模式，用户可以根据自己的业务场景，使用该接口进行修改。修改后，变更计费模式的请求将在下个计费周期（每个自然小时为一计费周期）生效。
 
域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: EipBmModifyCharge
 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipIds.n|否|Array|EIP实例ID列表，可以通过[DescribeEipBm](/doc/api/456/6671)接口查询，数组下标从0开始|
| payMode|是|String|EIP计费方式：flow-流量计费；bandwidth-带宽计费|
| bandwidth|否|Int|带宽上限（该字段只在带宽计费模式下生效），单位MB，默认值为1，最小为0


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务id，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[EipBmQueryTask](/doc/api/456/6670)查询任务状态|

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30016|ISPInvalid|ISP非法|

## 5. 示例
 
输入
<pre>

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=EipBmModifyCharge
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>&eipIds.0=eip-test&payMode=bandwidth&bandwidth=40
</pre>

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383050
    }
}
```

