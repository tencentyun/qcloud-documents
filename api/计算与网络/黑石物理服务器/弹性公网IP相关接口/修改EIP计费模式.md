>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBmModifyCharge 接口用于修改弹性公网EIP的计费模式，目前有两种计费模式：流量计费和带宽计费。用户可以根据自己的业务场景，使用该接口进行修改。变更后的计费模式将在下个计费周期（每个自然小时为一计费周期）生效。
 
接口访问域名: bmeip.api.qcloud.com
 

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmModifyCharge
	&<公共请求参数>
	&bandwidth=<带宽计费模式下的带宽上限值>
	&eipIds.0=<EIP实例ID>
	&payMode=<EIP计费模式>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 EipBmModifyCharge。
 
|参数名称|必选|类型|描述|
|-------|----|---|----|
| eipIds.n|否|Array|EIP实例ID列表，可以通过[查询EIP列表](/document/product/386/6671)接口查询，数组下标从0开始|
| payMode|是|String|EIP计费模式：flow-流量计费；bandwidth-带宽计费|
| bandwidth|否|Int|带宽上限（该字段只在带宽计费模式下生效），单位MB，默认值为1，最小为0，最大为1000MB|


## 响应
### 响应示例
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
### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，主要包括修改计费模式的异步任务ID。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务id，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 修改计费模式的异步任务ID，可以通过[查询EIP任务状态](/document/product/386/6670)查询任务状态|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30016|ISPInvalid|ISP非法|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmModifyCharge
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=33075
	&Timestamp=1507793501
	&Region=bj
	&bandwidth=1
	&eipIds.0=eip-e791epal
	&payMode=bandwidth
	&Signature=CrKnTxztb5VMm9HdFXswEDrbGZo%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2388138
    }
}
```

