

## 简介

云开发（Tencent CloudBase，TCB）是腾讯云提供的云原生一体化开发环境和工具平台，为开发者提供高可用、自动弹性扩缩的后端云服务，包含计算、存储、托管等 serverless 化能力，可用于云端一体化开发多种端应用（小程序，公众号，Web 应用，Flutter 客户端等），帮助开发者统一构建和管理后端服务和云资源，避免了应用开发过程中繁琐的服务器搭建及运维，开发者可以专注于业务逻辑的实现，开发门槛更低，效率更高。

>?云开发的云 API 是云开发提供的管理端能力 API，开发者可使用云 API 自定义管理云开发资源，个性化搭建自有的控制台，或者在云 API 上二次封装更多能力对外开放，以满足更丰富的需求场景。更多云 API 规范请参见 [腾讯云云 API](https://cloud.tencent.com/product/api)。



## 云 API 架构

云开发提供的一站式后端服务中，包含以下能力版块：
- 云函数，为云开发提供底层云函数管理及计算能力。
- 云数据库，为云开发提供底层数据库能力。
- 云存储，为云开发提供底层存储能力。

云开发对外提供服务，整体架构如下：
<img src="https://main.qcloudimg.com/raw/85228392c7e500ebeee75626f13ace04.jpg" width="80%">


如需了解整个产品概况，单击 [了解更多](https://cloud.tencent.com/document/product/876/18431)。

针对云开发的云 API 包含两大部分：
- 由云开发产品提供的云 API 能力。
- 由云函数、云数据库、云存储提供的 API 能力。

以上两大部分均通过云开发 API 服务统一对外提供服务。

>?
- 针对云开发提供的 API，可参见 [API 概览](https://cloud.tencent.com/document/product/876/34809)。
- 针对云函数、云数据库、云存储提供的 API 能力，可通过以下云开发提供的 **API Center** 能力调用。

## API Center 简介

### 主要功能
API Center 是云开发提供通过云开发 API 网管服务访问**云函数、云数据库、云存储**的 API 能力，主要有以下好处：
- API 请求入口统一化。
- 业务只需关注云开发即可。

调用情况如下图所示：
<img src="https://main.qcloudimg.com/raw/c4b4bd2bde4e0269b5615a507a15377c.jpg" width="80%">


云开发提供一个通用的云 API 接口 **CommonServiceAPI**，可查看 [文档说明](https://cloud.tencent.com/document/api/876/41230)，具体的使用方式如下：
- 云函数、云数据库、云存储**各自的 API 能力**。
- 通过**CommonServiceAPI**接口调用以上服务。

### 示例说明

以下使用云数据库的 DescribeRestoreTables 接口举例。

#### 正常的调用方式

接口名称：**DescribeRestoreTables**。
输入参数：除公共参数外（可参见 [公共请求参数](https://cloud.tencent.com/document/api/876/34812)），输入参数还包含：


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| InstanceId  | String |  数据库实例 ID|
| Time  | String | 回档时间|


请求示例：
``` json
{
    "Uin":"123456",
    "SubAccountUin":"12345678", 
    "Version":"2018-06-08",
    "Timestamp":"1575446253", 
    "Region":"ap-shanghai",
    "Action":"DescribeRestoreTables", // 调⽤用接⼝口
    "InstanceId": "tnt-123456789",    // 参数1
    "Time": "2019-12-01 00:00:00"    // 参数2
}
```

响应如下：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Tables  | List | 可回档表格  |

``` json
{
    "RequestId":"4a39f1ce-e11b-4954-881d-561504e1ab4e",
    "Tables":[] 
}
```


#### 通过 CommonServiceAPI 的调用方式

1. 将原调⽤⽅公共参数中的 Action，设置为 CommonServiceAPI 接⼝的 Service 参数。
2. 将原调⽤方 request 参数序列列化为 json 的字符串，设置为 CommonServiceAPI 接⼝的 JSONData 参数。

接⼝名称：**CommonServiceAPI**
参数：除公共参数外（可参见 [公共请求参数](https://cloud.tencent.com/document/api/876/34812)），输⼊入参数还有：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Service  | String |  转发云 API 的 Action 名 |
| JSONData  | String | 转发云 API 参数，Json 格式字符串|


请求示例：

```json
{
    "Uin" :"123456",
    "SubAccountUin":"12345678",
    "Version":"2018-06-08",
    "Timestamp":"1575446253",
    "Region":"ap-shanghai",
    "Action":"CommonServiceAPI",
    "Service":"DescribeRestoreTables", 
    "JSONData":"{
        \"InstanceId\": \"tnt-123456789\",
        \"Time\": \"2019-12-01 00:00:00\" 
    }"
}

```

响应如下：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| JSONResp  | String |  云 API 响应，Json 格式 |


```json
{
    "JSONResp": "{
        \"Response\":{
            \"RequestId\":\"4a39f1ce-e11b-4954-881d- 561504e1ab4e\",
            \"Tables\":[]
         }
     }",
     "RequestId": "427c6660-d389-4da4-aaa2-ca8c3626ba0e" 
}
```

