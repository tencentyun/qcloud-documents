## 功能描述

本接口用于消费读取日志。根据游标（cursor）、数量（count）获取对应主题分区上的日志数据。

## 请求

#### 请求示例

```shell
GET /pulllogs?topic_id=xxxxxxxx-xxxx-xxxx-xxxx&partition_id=1&cursor=xxxxxxxxx&count=10 HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 参数名       | 类型   | 位置  | 是否必须 | 描述                                           |
| ------------ | ------ | ----- | -------- | ---------------------------------------------- |
| topic_id     | string | query | 是       | 日志主题 ID                                    |
| partition_id | int    | query | 是       | 消费的主题分区编号                             |
| cursor       | string | query | 是       | 游标值，base64 编码，表示从当前位置开始读取数据 |
| count        | int    | query | 是       | 单次消费的 LogGroup 个数，最多1000个（一个 LogGroup 会包含多条日志，LogGroup 定义参考 [上传结构化日志](https://cloud.tencent.com/document/product/614/16873) 文档）           |



## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/x-protobuf
Content-Length: 23
x-cls-cursor: xxxxxx
x-cls-count: 10

<LogGroupList 的pb格式打包内容>
```

#### 响应头

| Header名     | 含义                                                         |
| ------------ | ------------------------------------------------------------ |
| x-cls-cursor | 游标值，base64 编码，表示下次从当前位置开始读取数据，供继续消费使用                  |
| x-cls-count  | 当前请求返回的 LogGroup 个数（一个 LogGroup 会包含多条日志，LogGroup 定义参考 [上传结构化日志](https://cloud.tencent.com/document/product/614/16873) 文档） |

#### 响应参数

返回 LogGroupList 对象的打包内容，pb 文件描述详见 [上传结构化日志](https://cloud.tencent.com/document/product/614/16873) 接口。

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

