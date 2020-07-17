>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBmApply 接口用于创建黑石弹性公网IP。创建成功后，便可以绑定黑石服务器等相关资源。需注意的是：如果申请成功的EIP不进行绑定资源的操作，会收取相应的闲置费。
 
接口访问域名: bmeip.api.qcloud.com
 

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmApply
	&<公共请求参数>
	&goodsNum=<创建的EIP数量>
	&payMode=<计费模式>
	&unVpcId=<VPC的ID>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 EipBmApply。

|参数名称|必选|类型|描述|
|-------|----|---|----|
| goodsNum | 否 | Int | 创建的EIP数量，默认为1，最大20 |
| payMode | 否 | String | 创建的EIP计费模式，"flow"：流量计费；"bandwidth"：带宽计费（单位：MB）|
| bandwidth | 否 | Int | EIP为带宽计费时，此参数才有效。表示EIP最大带宽（单位：MB，当前最大为1000MB）|
| unVpcId | 是 | String | EIP归属的VPC的标识，格式形如：vpc-k7j1t2x1，可通过[查询私有网络列表](/document/product/386/6646)返回的字段unVpcId获得 |
| IpList | 否 | 数组 | 指定IP地址申请，数组元素个数如果大于goodsNum，将仅指定申请数组前面的goodsNum个IP，如果IP已被自己或者客户创建，则会申请失败 | 
| exclusive | 否 | Int | 是否使用独占集群，0：不使用，1：使用。默认为0 |

 > 平台对用户每地域能申请的EIP最大配额有所限制。上述配额可通过[查询EIP限额](/document/product/386/6668)接口获取。

## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipIds": [
            "eip-qcloudv5"
        ],
        "requestId": "<异步任务ID>"
    }
}
```
### 响应参数

响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括申请到的EIP实例ID列表以及异步任务ID。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回申请的eip实例对应的异步任务信息，具体结构描述如下 |

data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipIds | Array | 返回申请中的EIP实例ID列表|
| data.requestId | Int | 申请EIP的异步任务ID，可以通过[查询EIP任务状态](/document/product/386/6670)查询任务状态|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30001|ExceedTheLimit|申请总数超过限额|
|30003|ExceedDailyLimit|当日申请数超限额|
|30016|ISPInvalid|ISP非法|


## 实际案例

### 输入

```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmApply
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=13716
	&Timestamp=1507781567
	&Region=bj
	&goodsNum=1
	&payMode=flow
	&unVpcId=vpc-k7j1t2x1
	&Signature=TX6qOTgRhljuPI%2BqHdfo6O%2FunlE%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipIds": [
            "eip-e791epal"
        ],
        "requestId": 2388137
    }
}

```

