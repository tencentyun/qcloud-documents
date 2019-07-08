>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBmDelete 接口用于释放弹性公网EIP，以清理不再使用的EIP资源。需注意的是，弹性公网EIP必须已经处于未绑定或创建失败的的状态下，才可以进行释放操作。

接口访问域名: `bmeip.api.qcloud.com`


## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
Action=EipBmDelete
&<公共请求参数>
&eipIds.0=<EIP实例ID>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 EipBmDelete。
 
|参数名称|必选|类型|描述|
|-------|----|---|----|
| eipIds.n|是|数组型|EIP实例ID列表，可以通过[查询EIP列表](/document/product/386/6671)接口查询，数组下标从0开始|

 > 绑定状态的EIP不可以释放，只可以释放创建失败或未绑定状态的EIP。

## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": "<异步任务ID>"
    }
}
```
### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，主要包括释放EIP操作的异步任务ID。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务信息，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 释放EIP的异步任务ID，可以通过[查询EIP任务状态](/document/product/386/6670)查询任务状态|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9000|InternalCgwErr|内部接口异常|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30009|EipNotExist|操作的EIP记录不存在|
|30010|EipStateCannotOp|EIP当前状态不允许释放|
|30013|EipRecordNotExist|EIP记录不存在|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmDelete
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=49957
	&Timestamp=1507795216
	&Region=bj
	&eipIds.0=eip-e791epal
	&Signature=TS0574U%2FWHrXwIq217X6b%2FOxZyA%3D
```

### 输出
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

