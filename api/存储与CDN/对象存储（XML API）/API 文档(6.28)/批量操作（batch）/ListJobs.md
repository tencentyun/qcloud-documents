## 功能描述

ListJobs 用于列出您的批量处理任务。有关批量处理任务的详细介绍，可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

## 请求

**请求示例**

```shell
GET /jobs?jobStatuses=<JobStatuses>&maxResults=<MaxResults>&nextToken=<NextToken> HTTP/1.1
Host: <UIN>.cos-control.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Authorization: Auth String
x-cos-appid: <APPID>
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

**请求参数**

调用 ListJobs 所需要使用的参数。该参数格式如下：

| 参数        | 描述                                                         | 是否必选 |
| ----------- | ------------------------------------------------------------ | ---- |
| jobStatuses | 您所需查询的任务状态信息。如您未指定任务状态，则 COS 将返回所有执行过的任务状态，包括正在执行的任务。若您指定任务状态，则 COS 将返回指定状态的任务。可选的任务状态包括：Active、Cancelled、Cancelling、Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、Suspended。 | 否   |
| maxResults  | COS 返回的任务数量最大值。如您配置了此项参数，每次返回的任务数最多不会超过这个最大值。您可以配合 nextToken 参数进行分页返回。该参数范围为1 - 1000，默认为1000。 | 否   |
| nextToken   | 翻页符。每次 list 操作会返回本次任务列表的最后一个 JobId 作为 nextToken，在下一次 list 传入该值，即可接续上一次 list 的内容进行 list，用于分页。该参数的长度限制在1 - 64字节。 | 否   |
| x-cos-appid | 用户的 APPID，长度为1 - 64字节。                                     | 是   |

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**
该请求无请求体。

## 响应


**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

```shell
<ListJobsResult>
    <Jobs>
        <member>
            <CreationTime>timestamp</CreationTime>
            <Description>string</Description>
            <JobId>string</JobId>
            <Operation>string</Operation>
            <Priority>integer</Priority>
            <ProgressSummary>
                <NumberOfTasksFailed>integer</NumberOfTasksFailed>
                <NumberOfTasksSucceeded>integer</NumberOfTasksSucceeded>
                <TotalNumberOfTasks>integer</TotalNumberOfTasks>
            </ProgressSummary>
            <Status>string</Status>
            <TerminationDate>timestamp</TerminationDate>
        </member>
    </Jobs>
    <NextToken></NextToken>
</ListJobsResult>
```

具体内容描述如下：

**ListJobsResult**
包含 COS 返回的批量处理任务列表信息。

| 节点名    | 父节点         | 描述                                                         | 类型        |
| --------- | -------------- | ------------------------------------------------------------ | ----------- |
| Jobs      | ListJobsResult | 包含 COS 返回的多个批量处理任务信息。                          | Jobs Object |
| NextToken | ListJobsResult | 每次ListJobs操作会返回本次任务列表的最后一个 JobId 作为 nextToken，在下一次 ListJobs 传入该值，返回结果即可接续上一次 ListJobs 的内容，用于分页。该参数的长度限制在1 - 64字节。 | String      |

**Jobs**

| 节点名 | 父节点 | 描述                                | 类型          |
| ------ | ------ | ----------------------------------- | ------------- |
| member | Jobs   | 包含 COS 返回的某个批量处理任务信息。 | member Object |

**member**

| 节点名          | 父节点 | 描述                                                         | 类型                   |
| --------------- | ------ | ------------------------------------------------------------ | ---------------------- |
| CreationTime    | member | 任务创建时间。                                               | Timestamp              |
| Description     | member | 任务描述。长度限制为0 - 256字节。                              | String                 |
| JobId           | member | 任务 ID。长度限制为1 - 64字节。                                 | String                 |
| Operation       | member | 批量处理任务中对对象执行的操作。例如 COSPutObjectCopy         | String                 |
| Priority        | member | 任务优先级。值越大的任务将会被优先执行。<br>优先级大小限制为0 - 2147483647。 | Integer                |
| ProgressSummary | member | 任务执行状况概述。描述您此项任务中所执行的操作总数，成功的操作数量以及失败的操作数量。 | ProgressSummary Object |
| Status          | member | 任务执行状态。合法参数值包括 Active、Cancelled、Cancelling、Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、Suspended。 | String                 |
| TerminationDate | member | 批量处理任务的结束时间。                                     | Timestamp              |

其他元素请参见 [批量处理功能公共元素](https://cloud.tencent.com/document/product/436/38607)。

#### 错误码

该请求可能会发生的一些常见的特殊错误如下：

| 错误码        | 描述                             | 状态码 | API      |
| --------------- | -------------------------------- | ------ | -------- |
| InvalidArgument | Parameter jobStatuses is invalid | 400    | ListJobs |
| InvalidArgument | maxResults 参数必须为整数        | 400    | ListJobs |
| InvalidArgument | nextToken 参数无效               | 400    | ListJobs |

其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。

## 实际案例
#### 请求

```shell
GET /jobs?maxResults=2 HTTP/1.1
Host: 100000000001.cos-control.ap-chengdu.myqcloud.com
Date: Fri, 20 Dec 2019 03:31:41 GMT
x-cos-appid: 1250000000
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1576812701;1576819901&q-key-time=1576812701;1576819901&q-header-list=date;host;x-cos-appid&q-url-param-list=maxresults&q-signature=432bc3f2116d579e257742596c31528c0d72****
Connection: close
```


#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1166
Connection: close
Date: Fri, 20 Dec 2019 03:31:41 GMT
Server: tencent-cos
x-cos-request-id: NWRmYzQwOWRfNWFiMjU4NjRfNmU1M18xMTFh****

<ListJobsResult>
	<Jobs>
		<member>
			<CreationTime>2019-12-19T11:05:40Z</CreationTime>
			<Description>example-job</Description>
			<JobId>021140d8-67ca-4e89-8089-0de9a1e40943</JobId>
			<Operation>COSPutObjectCopy</Operation>
			<Priority>10</Priority>
			<ProgressSummary>
				<NumberOfTasksFailed>0</NumberOfTasksFailed>
				<NumberOfTasksSucceeded>10</NumberOfTasksSucceeded>
				<TotalNumberOfTasks>10</TotalNumberOfTasks>
			</ProgressSummary>
			<Status>Complete</Status>
			<TerminationDate>2019-12-19T11:05:56Z</TerminationDate>
		</member>
		<member>
			<CreationTime>2019-12-19T11:07:05Z</CreationTime>
			<Description>example-job</Description>
			<JobId>066d919e-49b9-429e-b844-e17ea7b16421</JobId>
			<Operation>COSPutObjectCopy</Operation>
			<Priority>10</Priority>
			<ProgressSummary>
				<NumberOfTasksFailed>0</NumberOfTasksFailed>
				<NumberOfTasksSucceeded>10</NumberOfTasksSucceeded>
				<TotalNumberOfTasks>10</TotalNumberOfTasks>
			</ProgressSummary>
			<Status>Complete</Status>
			<TerminationDate>2019-12-19T11:07:21Z</TerminationDate>
		</member>
	</Jobs>
	<NextToken>066d919e-49b9-429e-b844-e17ea7b16421</NextToken>
</ListJobsResult>
```

