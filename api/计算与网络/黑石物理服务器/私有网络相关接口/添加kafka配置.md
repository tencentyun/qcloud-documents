>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
AddBmAppKafkaConf 接口用于添加ckafka配置信息，包括实例ID，以及topic名称，以便接收NAT日志。

接口请求域名：bmvpc.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=AddBmAppKafkaConf
	&<公共请求参数>
	&kafkaId=<实例ID>
	&topicName=<队列名称>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="https://cloud.tencent.com/document/api/386/6718" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为AddBmAppKafkaConf。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| kafkaId | ckafka实例ID，例如：ckafka-kd7d06of| String | 是 |
| topicName | 队列名称，例如：receive-test| String | 是 |


## 响应
### 响应示例
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": <异步任务ID>
	}
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
| taskId | Int  | 以taskId为key，对应的值为异步操作的ID。创建结果可调用<a href="https://cloud.tencent.com/document/product/386/9356" title="查询异步任务操作状态">查询异步任务操作状态</a>查询 |

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
	Action=AddBmAppKafkaConf
	&SecretId=AKID1ub7R1JoyBF7nHqjk7IH8nGWaR6Yezwd
	&Nonce=4557
	&Timestamp=1507692902
	&Region=gz
	&kafkaId=ckafka-kd7d06of
	&topicName=receive-test
	&Signature=xhpWkOBXHyEdddxK2KIH%2F14bMrc%3D
```

### 输出
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 1641
	}
}
```
