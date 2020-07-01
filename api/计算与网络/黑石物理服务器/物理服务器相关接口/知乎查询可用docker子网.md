>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述

ZhDockerSubnetAvailable接口给知乎专用的用来查询空闲可用的docker子网。

接口访问域名：bm.api.qcloud.com

## 请求

### 请求示例
```
https://bm.api.qcloud.com/v2/index.php?
	Action=ZhDockerSubnetAvailable
	&<公共请求参数>
	&unVpcId=<私有网络的ID>
```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，其它参数参见[公共请求参数](/doc/api/456/6718)页面。其中，此接口的Action字段为DescribeDevice。

| 参数名称              | 必选   | 类型            | 描述                                       |
| ----------------- | ---- | ------------- | ---------------------------------------- |
| unVpcId           | 否    | String        | 私有网络ID。通过接口[查询私有网络列表(DescribeBmVpcEx)](/doc/api/456/6646)获取私有网络信息, 取unVpcId字段，如vpc-8e0ypm3z                                  |


## 响应

### 响应示例
```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
		"vpcId": <私有网络的整型ID>,
		"unVpcId":<私有网络的唯一ID>,
		"subnetId":<私有网络的子网整型ID>,
		"unSubnetId":<私有网络的子网唯一ID>
	}
  ]
}
```

### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括服务器等信息。

| 参数名称    | 类型     | 描述                                       |
| ------- | ------ | ---------------------------------------- |
| code    | Int    | 错误码，0：成功， 其他值：失败，具体含义参见[错误码](/doc/api/456/6725)。 |
| message | String | 错误信息。                                    |
| data    | Array(Object) | 子网列表。                    |


data中对象结构

| 参数名称       | 类型            | 描述                                    |
| ---------- | ------------- | ------------------------------------- |
| vpcId   | Int           | 私有网络的整型ID                                 |
| unVpcId | Array(Object) | 私有网络的唯一ID |
| subnetId   | Int           | 私有网络的子网整型ID                                  |
| unSubnetId | Array(Object) | 私有网络的子网唯一ID |


## 错误码

| 错误码   | 英文提示                  | 错误描述    |
| ----- | --------------------- | ------- |
| 9003  | InternalError.DbError | 操作数据库错误 |
| 10001 | InvalidParameter      | 参数错误    |
| 10004 | OperationDenied      | 无权限    |


## 实际案例

### 输入

```
https://bm.api.qcloud.com/v2/index.php?
	Action=ZhDockerSubnetAvailable
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
	&unVpcId=un-1111
```

### 输出

```
{
  "code": 0,
  "message": "OK",
  "data":  [
    {
		"vpcId":"1111",
		"unVpcId":"un-1111",
		"subnetId":"1111",
		"unSubnetId":"un-1111"
	}
  ]
}
```