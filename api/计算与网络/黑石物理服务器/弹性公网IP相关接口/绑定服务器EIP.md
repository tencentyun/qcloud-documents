>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBmBindRs 接口用于绑定黑石弹性公网IP到黑石物理服务器上。弹性公网 EIP 是支持公网双向互通的产品，客户租用黑石物理服务器后，可以通过绑定 EIP 的方式实现单个设备的公网内外互访。弹性 EIP 和黑石物理服务器的绑定关系是1:1。

接口访问域名: bmeip.api.qcloud.com


## 请求

### 请求示例

```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmBindRs
	&<公共请求参数>
	&eipId=<EIP实例ID>
	&instanceId=<服务器实例ID>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数页面](/document/product/386/6718)。其中，此接口的 Action 字段为 EipBmBindRs。
 
|参数名称|必选|类型|描述|
|-------|-------|-------|-------|
| eipId | 是 | String | EIP 实例 ID，格式形如：eip-testid |
| instanceId | 是 | String | 服务器实例 ID，可通过 [DescribeDevice](/document/product/386/6728) 接口返回字段中的instanceId 获取|

>? 已绑定到 NAT 网关的物理机，目前暂不支持同时绑定 EIP。
>

## 响应
### 响应示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": "<EIP异步任务ID>"
    }
}
```

### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容（此接口中为异步任务 ID）

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考 [错误码](/document/product/386/6725) |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务信息 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务 ID，可以通过 [EipBmQueryTask](/document/product/386/6670) 查询任务状态|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30009|EipNotExist|操作的 EIP 记录不存在|
|30010|EipStateCannotOp|EIP 当前状态不允许绑定|
|30012|EipInArrears|操作的 EIP 已欠费|
|30017|EipHasBindRs|EIP 已经绑定 RS|
|30021|VpcIdNotMatch|EIP 和 RS 的 VPC 不一致|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmBindRs
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=17056
	&Timestamp=1507730005
	&Region=bj
	&eipId=eip-kpge33wo
	&instanceId=cpm-tqge3eeo
	&Signature=FSZxYV2dUIjTZ3rNRppPJPPJ23E%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 100000
    }
}
```

