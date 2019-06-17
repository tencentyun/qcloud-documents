>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
QueryBmTgwClusterMode 接口用于查询当前TGW集群所处的模式。

接口请求域名：bmvpc.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=QueryBmTgwClusterMode
    &<公共请求参数>
    &unVpcId=<vpc网络ID>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="https://cloud.tencent.com/document/api/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为QueryBmTgwClusterMode。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| unVpcId | 私有网络ID值，例如：vpc-kd7d06of| String | 是 |


## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"data": "shared"
}
```
### 响应参数

| 参数名称 | 描述 |  类型 |
|---------|---------|---------|
| code | 错误码。0: 成功, 其他值: 失败| Int |
| message | 错误信息| String |
| data    | Object | 返回异步操作的ID信息，具体结构描述如data结构所示。             |

data结构

| 参数名称   | 类型   | 描述                        |
| ------ | ---- | ------------------------- |
| data | String  | 返回当前集群的模式，取值为shared，exclusive；其中shared为共享模式，exclusive为独占模式 |

## 错误码
| 错误码   | 英文提示                                    | 错误描述             |
| ----- | --------------------------------------- | ---------------- |
| 9001  | InternalError.DbError                   | 操作数据库错误          |
| 9005  | InternalError.RbmqError                 | 操作系统队列错误         |
| 10001 | InvalidParameter                        | 参数错误             |


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=QueryBmTgwClusterMode
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&unVpcId=vpc-kd7d06of
	&Signature=xhpWkOBXHyEdddxK2KIH%2F14bMrc%3D
```

### 输出
```
{
	"code": 0,
	"message": "",
	"data": "exclusive"
}
```