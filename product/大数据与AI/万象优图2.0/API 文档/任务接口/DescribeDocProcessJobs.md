## 功能描述

DescribeDocProcessJobs 用于拉取符合条件的文档转码任务。

## 请求

#### 请求示例

```shell
GET /doc_jobs?queueId=<queueId>&tag=DocProcess HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型    | 是否必选 |
| :----------------- | :----- | :----------------------------------------------------------- | :------ | :------- |
| queueId            | 无     | 拉取该队列 ID 下的任务。                                     | String  | 是       |
| tag                | 无     | 任务的 Tag：DocProcess。                                     | String  | 是       |
| orderByTime        | 无     | Desc 或者 Asc。默认为 Desc。                                 | String  | 否       |
| nextToken          | 无     | 请求的上下文，用于翻页。上次返回的值。                       | String  | 否       |
| size               | 无     | 拉取的最大任务数。默认为10。最大为100。                      | Integer | 否       |
| states             | 无     | 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All。 | String  | 否       |
| startCreationTime  | 无     | 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |
| endCreationTime    | 无     | 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <JobsDetail></JobsDetail>
  <NextToken></NextToken>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息，同 [CreateDocProcessJobs](https://cloud.tencent.com/document/product/460/46942#.E5.93.8D.E5.BA.94) 接口中的 Response.JobsDetail 节点 | Container |
| NextToken          | Response | 翻页的上下文 Token                                           | String    |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /doc_jobs/queueId=QueueId&tag=DocProcess HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
```

#### 响应

```shell
<Response>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-07-20T10:43:17+0800</CreationTime>
                <EndTime>-</EndTime>
                <Input>
                        <Object>1.docx</Object>
                </Input>
                <JobId>JobId</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <EndPage>1</EndPage>
                                <ImageParams>ImageParams</ImageParams>
                                <SrcType/>
                                <StartPage>1</StartPage>
                                <TgtType>png</TgtType>
                        </DocProcess>
                        <Output>
                                <Bucket>BucketId</Bucket>
                                <Object>file/test-${Page}.jpg</Object>
                                <Region>Region</Region>
                        </Output>
                </Operation>
                <QueueId>QueueId</QueueId>
                <State>Submitted</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
        <JobsDetail>
                <Code>Success</Code>
                <CreationTime>2020-07-20T10:43:17+0800</CreationTime>
                <EndTime>-</EndTime>
                <Input>
                        <Object>test.docx</Object>
                </Input>
                <JobId>JobId</JobId>
                <Message/>
                <Operation>
                        <DocProcess>
                                <EndPage>1</EndPage>
                                <ImageParams>ImageParams</ImageParams>
                                <SrcType/>
                                <StartPage>1</StartPage>
                                <TgtType>png</TgtType>
                        </DocProcess>
                        <Output>
                                <Bucket>BucketId</Bucket>
                                <Object>file/test-${Page}.jpg</Object>
                                <Region>Region</Region>
                        </Output>
                </Operation>
                <QueueId>QueueId</QueueId>
                <State>Submitted</State>
                <Tag>DocProcess</Tag>
        </JobsDetail>
        <NextToken>19193</NextToken>
</Response>
```
