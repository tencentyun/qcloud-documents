>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述

QueryBmNatGatewayProductionStatus 接口用于查询操作黑石NAT网关任务的执行状态

接口请求域名：bmvpc.api.qcloud.com

## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php/?Action=QueryBmNatGatewayProductionStatus
    &<公共请求参数>
    &taskId=<NAT异步任务ID>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/document/product/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为QueryBmNatGatewayProductionStatus。

| 参数名称 | 描述 | 类型 | 必选  |
|---------|---------|---------|---------|
| taskId | 任务ID, 可使用该ID查询任务执行结果| String |是 | 

## 响应
### 响应示例
```
{
 "code": "0",
 "message": "",
 "data": {
  "status": "<任务执行状态>"
 }
}
```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code |错误码。0: 成功, 其他值: 失败| Int | 
| message | 错误信息| String |
| data.status | 0为执行成功，1为执行失败，2为正在执行中 | Int |

## 错误码
| 错误码   | 英文提示                  | 错误描述    |
| ----- | --------------------- | ------- |
| 9001  | InternalError.DbError | 操作数据库错误 |
| 10001 | InvalidParameter      | 参数错误    |

## 实际案例

### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?	
	Action=QueryBmNatGatewayProductionStatus
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=56046
	&Timestamp=1507703517
	&Region=gz
	&taskId=3000
	&Signature=QKEu1BoztPhLn%2B1MRThSbNogd1s%3D
```

### 输出

```
{
    "code": "0",
    "message": "",
    "data": {
        "status": 1
    }
}
```
