## 功能描述

提交一个图片处理任务。

## 请求

#### 请求示例

```shell
POST /pic_jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
    <Tag>PicProcess</Tag>
    <Input>
        <Object>input/deer.jpg</Object>
    <Operation>
        <TemplateId>t10461fe2bd5a649db9022452ec71e0381</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/out.jpg</Object>
        </Output>
        <UserData>This is my data.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2911917386e148639319e13c285cc774</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

<span id="Request"></span>
Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 创建任务的 Tag：PicProcess                                 | String    | 是   |
| Input              | Request | 待操作的媒体信息                                         | Container | 是   |
| Operation          | Request | 操作规则                        | Container | 是       |
| QueueId            | Request | 任务所在的队列 ID               | String    | 是       |
| CallBackFormat     | Request | 任务回调格式，JSON 或 XML，默认 XML，优先级高于队列的回调格式                    | String | 否 |
| CallBackType       | Request | 任务回调类型，Url 或 TDMQ，默认 Url，优先级高于队列的回调类型                    | String | 否 |
| CallBack           | Request | 任务回调地址，优先级高于队列的回调地址。设置为 no 时，表示队列的回调地址不产生回调 | String | 否 |
| CallBackMqConfig   | Request | 任务回调 TDMQ 配置，当 CallBackType 为 TDMQ 时必填。详情见 [CallBackMqConfig](https://cloud.tencent.com/document/product/460/78927#CallBackMqConfig)                | Container | 否 |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述            | 类型   | 是否必选 |
| ------------------ | ------------- | --------------- | ------ | ---- |
| Object             | Request.Input | 媒体文件名 | String | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| PicProcess                   | Request.Operation | 指定该任务的参数，同创建图片处理模板 <a href="https://cloud.tencent.com/document/product/460/77182#PicProcess" target="_blank">CreateMediaTemplate</a> 接口中的 Request.PicProcess | Container | 否   |
| TemplateId                   | Request.Operation | 指定的模板 ID                                        | String    | 否   |
| Output                       | Request.Operation | 结果输出地址                                          | Container | 是   |
| UserData                     | Request.Operation | 透传用户信息, 可打印的 ASCII 码, 长度不超过1024                 | String | 否 |
| JobLevel                     | Request.Operation | 任务优先级，级别限制：0 、1 、2。级别越大任务优先级越高，默认为0 | String | 否   |

>!优先使用 TemplateId，无 TemplateId 时使用对应任务类型的参数。

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Request.Operation.Output | 存储桶的地域                                                | String | 是   |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                              | String | 是   |
| Object             | Request.Operation.Output | 结果文件的名字                                               | String | 是   |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>c93984788066911ed89ed352d4d9d2084</JobId>
        <State>Submitted</State>
        <CreationTime>2022-07-18T15:16:43+0800</CreationTime>
        <EndTime>-</EndTime>
        <StartTime>-</StartTime>
        <QueueId>p2911917386e148639319e13c285cc774</QueueId>
        <Tag>PicProcess</Tag>
        <Input>
            <BucketId>test-1234567890</BucketId>
            <Object>input/deer.jpg</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Output>
                <Bucket>test-1234567890</Bucket>
                <Object>output/out.jpg</Object>
                <Region>ap-chongqing</Region>
            </Output>
            <TemplateId>t10461fe2bd5a649db9022452ec71e0381</TemplateId>
            <TemplateName>test</TemplateName>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息 | Container |

<span id="jobsDetail"></span>
Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                        | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                      | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                              | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：PicProcess                           | String    |
| State              | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String   |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| StartTime          | Response.JobsDetail | 任务的开始时间                                               | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                            | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点                   | 描述             | 类型   |
| ------------------ | ------------------------ | ---------------- | ------ |
| Region             | Response.JobsDetail.Input | 存储桶的地域     | String |
| Bucket             | Response.JobsDetail.Input | 存储结果的存储桶 | String |
| Object             | Response.JobsDetail.Input | 输出结果的文件名 | String |

Container 节点 Operation 的内容：

| 节点名称（关键字）  | 父节点                        | 描述                                                         | 类型      |
| :------------------ | :---------------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId          | Response.JobsDetail.Operation | 任务的模板 ID                                                | String    |
| TemplateName        | Response.JobsDetail.Operation | 任务的模板名称, 当 TemplateId 存在时返回 | String    |
| PicProcess          | Response.JobsDetail.Operation | 同请求中的 Request.Operation.PicProcess                       | Container |
| Output              | Response.JobsDetail.Operation | 同请求中的 Request.Operation.Output                           | Container |
| PicProcessResult    | Response.JobsDetail.Operation | 图片处理后输出图片的信息，没有时不返回                           | Container |
| UserData            | Response.JobsDetail.Operation | 透传用户信息                                                   | String |

Container 节点 PicProcessResult 的内容：
同 [图片持久化处理](https://cloud.tencent.com/document/product/460/18147) 接口中的 UploadResult 节点。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求1：使用图片处理模板 ID

```shell
POST /pic_jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:test-1234567890.ci.ap-chongqing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <Tag>PicProcess</Tag>
    <Input>
        <Object>input/deer.jpg</Object>
    <Operation>
        <TemplateId>t10461fe2bd5a649db9022452ec71e0381</TemplateId>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/out.jpg</Object>
        </Output>
        <UserData>This is my data.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2911917386e148639319e13c285cc774</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Mon, 18 Jul 2022 19:37:29 GMT
Server: tencent-ci
x-ci-request-id: NjMxMDJhYTNfMThhYTk0MGFfYmU1OV8zZjc=

<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>c93984788066911ed89ed352d4d9d2084</JobId>
        <State>Submitted</State>
        <CreationTime>2022-07-18T15:16:43+0800</CreationTime>
        <EndTime>-</EndTime>
        <StartTime>-</StartTime>
        <QueueId>p2911917386e148639319e13c285cc774</QueueId>
        <Tag>PicProcess</Tag>
        <Input>
            <BucketId>test-1234567890</BucketId>
            <Object>input/deer.jpg</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Output>
                <Bucket>test-1234567890</Bucket>
                <Object>output/out.jpg</Object>
                <Region>ap-chongqing</Region>
            </Output>
            <TemplateId>t10461fe2bd5a649db9022452ec71e0381</TemplateId>
            <TemplateName>test</TemplateName>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```

#### 请求2：使用图片处理处理参数

```shell
POST /pic_jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:test-1234567890.ci.ap-chongqing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <Tag>PicProcess</Tag>
    <Input>
        <Object>input/deer.jpg</Object>
    <Operation>
         <PicProcess>
            <IsPicInfo>true</IsPicInfo>
            <ProcessRule>imageMogr2/rotate/90</ProcessRule>
        </PicProcess>
        <Output>
            <Region>ap-chongqing</Region>
            <Bucket>test-123456789</Bucket>
            <Object>output/out.jpg</Object>
        </Output>
        <UserData>This is my data.</UserData>
        <JobLevel>0</JobLevel>
    </Operation>
    <QueueId>p2911917386e148639319e13c285cc774</QueueId>
    <CallBack>http://callback.demo.com</CallBack>
    <CallBackFormat>JSON<CallBackFormat>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Mon, 18 Jul 2022 19:37:29 GMT
Server: tencent-ci
x-ci-request-id: NjMxMDJhYTNfMThhYTk0MGFfYmU1OV8zZjc=

<Response>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>c93984788066911ed89ed352d4d9d2084</JobId>
        <State>Submitted</State>
        <CreationTime>2022-07-18T15:16:43+0800</CreationTime>
        <EndTime>-</EndTime>
        <StartTime>-</StartTime>
        <QueueId>p2911917386e148639319e13c285cc774</QueueId>
        <Tag>PicProcess</Tag>
        <Input>
            <BucketId>test-1234567890</BucketId>
            <Object>input/deer.jpg</Object>
            <Region>ap-chongqing</Region>
        </Input>
        <Operation>
            <Output>
                <Bucket>test-1234567890</Bucket>
                <Object>output/out.jpg</Object>
                <Region>ap-chongqing</Region>
            </Output>
            <PicProcess>
                <IsPicInfo>true</IsPicInfo>
                <ProcessRule>imageMogr2/rotate/90</ProcessRule>
            </PicProcess>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
</Response>
```
