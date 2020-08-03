## 功能描述

DescribeJob 用于获取您配置的批量处理任务的参数和任务执行状态。有关批量处理任务的详细信息，可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

## 请求

#### 请求示例

```shell
GET /jobs/<JobId> HTTP/1.1
Host: <UIN>.cos-control.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Authorization: Auth String
x-cos-appid: <APPID>
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 DescribeJob 所需的参数。该参数格式如下：

| 参数        | 描述                     | 是否必选 |
| ----------- | ------------------------ | ---- |
| JobId       | 任务 ID。                | 是   |
| x-cos-appid | 用户的 APPID，长度为1 - 64字节。 | 是   |

#### 请求头
此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

```shell
<DescribeJobResult>
    <Job>
        <ConfirmationRequired>boolean</ConfirmationRequired>
        <CreationTime>timestamp</CreationTime>
        <Description>string</Description>
        <FailureReasons>
            <JobFailure>
                <FailureCode>string</FailureCode>
                <FailureReason>string</FailureReason>
            </JobFailure>
        </FailureReasons>
        <JobId>string</JobId>
        <Manifest>
            <Location>
                <ETag>string</ETag>
                <ObjectArn>string</ObjectArn>
            </Location>
            <Spec>
                <Format>string</Format>
            </Spec>
        </Manifest>
        <Operation>
            <COSPutObjectCopy>
                <CannedAccessControlList>string</CannedAccessControlList>
                <MetadataDirective>string</MetadataDirective>
                <NewObjectMetadata>
                    <SSEAlgorithm>string</SSEAlgorithm>
                    <UserMetadata>
                        <member>
                            <Key>string</Key>
                            <Value>string</Value>
                        </member>
                        <member>
                            <Key>string</Key>
                            <Value>string</Value>
                        </member>
                    </UserMetadata>
                </NewObjectMetadata>
                <StorageClass>string</StorageClass>
                <TargetResource>string</TargetResource>
            </COSPutObjectCopy>
        </Operation>
        <Priority>integer</Priority>
        <ProgressSummary>
            <NumberOfTasksFailed>integer</NumberOfTasksFailed>
            <NumberOfTasksSucceeded>integer</NumberOfTasksSucceeded>
            <TotalNumberOfTasks>integer</TotalNumberOfTasks>
        </ProgressSummary>
        <Report>
            <Bucket>string</Bucket>
            <Enabled>boolean</Enabled>
            <Format>string</Format>
            <Prefix>string</Prefix>
            <ReportScope>string</ReportScope>
        </Report>
        <RoleArn>string</RoleArn>
        <Status>string</Status>
        <StatusUpdateReason>string</StatusUpdateReason>
        <SuspendedCause>string</SuspendedCause>
        <SuspendedDate>timestamp</SuspendedDate>
        <TerminationDate>timestamp</TerminationDate>
    </Job>
</DescribeJobResult>
```

具体内容描述如下：

**DescribeJobResult**

包含待描述批量处理任务的参数和状态信息。

| 节点名 | 父节点            | 描述                                       | 类型       |
| ------ | ----------------- | ------------------------------------------ | ---------- |
| Job    | DescribeJobResult | 您指定查询的批量处理任务的参数和状态信息。 | Job Object |

**Job**

| 节点名             | 父节点 | 描述                                                         | 类型                   |
| ------------------ | ------ | ------------------------------------------------------------ | ---------------------- |
| ClientRequestToken | Job    | 每个请求唯一的 token，用于避免前端重复发起同一批处理任务。<br>长度为1 - 64字节，建议使用 UUID。 | String                 |
| CreationTime       | Job    | 任务创建时间。                                               | Timestamp              |
| Description        | Job    | 任务描述。若您在创建任务时配置了此信息，则会返回该项内容。<br>长度范围为1 - 256字节。 | String                 |
| FailureReasons     | Job    | 如果任务失败，描述失败的原因。                               | FailureReasons Object  |
| JobId              | Job    | 创建任务成功后，生成的任务 ID。长度1 - 64字节。                 | String                 |
| Manifest           | Job    | 待处理的对象清单。您需要将需要处理的对象记录在此对象清单内。 | Manifest Object        |
| Operation          | Job    | 您需要对清单内的对象批量执行的操作。                         | Operation Object       |
| Priority           | Job    | 任务优先级。越高的数值代表此项任务的优先级越高。<br>优先级数值范围为0 - 2147483647。 | Integer                |
| ProgressSummary    | Job    | 任务执行状况概述。描述您此项任务中所执行的操作总数，成功的操作数量以及失败的操作数量。 | ProgressSummary Object |
| Report             | Job    | 指定清单报告的相关配置。                                     | Report Object          |
| RoleArn            | Job    | 您为该任务分配的角色的标识符。长度1 - 1024字节。               | String                 |
| Status             | Job    | 任务当前状态。合法参数值包括 Active、Cancelled、Cancelling、Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、Suspended | String                 |
| StatusUpdateReason | Job    | 状态更新原因。长度为0 - 256字节。                              | String                 |
| SuspendedCause     | Job    | 任务中断的原因。任务仅在您使用控制台创建任务时会进入中断状态，等待您的确认后再进入执行状态。长度为0 - 1024字节。 | String                 |
| SuspendedDate      | Job    | 任务中断的时间。当任务进入中断状态时，会记录任务中断的时间。 | Timestamp              |
| TerminationDate    | Job    | 任务终止的时间。                                             | Timestamp              |

**FailureReasons**

| 节点名     | 父节点         | 描述                 | 类型              |
| ---------- | -------------- | -------------------- | ----------------- |
| JobFailure | FailureReasons | 任务失败代码和原因。 | JobFailure Object |

**FailureCode**

| 节点名        | 父节点     | 描述                          | 类型   |
| ------------- | ---------- | ----------------------------- | ------ |
| FailureCode   | JobFailure | 任务失败代码。长度0 - 64字节。  | String |
| FailureReason | JobFailure | 任务失败原因。长度0 - 256字节。 | String |

其他元素请参见 [批量处理功能公共元素](https://cloud.tencent.com/document/product/436/38607)。

#### 错误码

该请求可能会发生的一些常见的特殊错误如下，其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。

| 错误码  | 描述                             | 状态码 | API         |
| --------- | -------------------------------- | ------ | ----------- |
| NoSuchJob | 指定任务不存在 | 404    | DescribeJob |

## 实际案例

#### 请求
```shell
GET /jobs/53dc6228-c50b-46f7-8ad7-65e7159f1aae HTTP/1.1
Host: 100000000001.cos-control.ap-chengdu.myqcloud.com
Date: Thu, 19 Dec 2019 18:01:11 GMT
x-cos-appid: 1250000000
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1576778471;1576785671&q-key-time=1576778471;1576785671&q-header-list=date;host;x-cos-appid&q-url-param-list=&q-signature=b1dfedd04199a1875904d0aed79cdb839c8d****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1555
Connection: close
Date: Thu, 19 Dec 2019 18:01:11 GMT
Server: tencent-cos
x-cos-request-id: NWRmYmJhZTdfNGQ5ZTU4NjRfMzQwYl9mZGY2****

<DescribeJobResult>
	<Job>
		<ConfirmationRequired>false</ConfirmationRequired>
		<CreationTime>2019-12-19T18:00:30Z</CreationTime>
		<Description>example-job</Description>
		<FailureReasons>
			<JobFailure>
				<FailureCode/>
				<FailureReason/>
			</JobFailure>
		</FailureReasons>
		<JobId>53dc6228-c50b-46f7-8ad7-65e7159f1aae</JobId>
		<Manifest>
			<Location>
				<ETag>&quot;15150651828fa9cdcb8356b6d1c7638b&quot;</ETag>
				<ObjectArn>qcs::cos:ap-chengdu::sourcebucket-1250000000/manifests/batch-copy-manifest.csv</ObjectArn>
			</Location>
			<Spec>
				<Fields>
					<member>Bucket</member>
					<member>Key</member>
				</Fields>
				<Format>COSBatchOperations_CSV_V1</Format>
			</Spec>
		</Manifest>
		<Operation>
			<COSPutObjectCopy>
				<TargetResource>qcs::cos:ap-chengdu::destinationbucket-1250000000</TargetResource>
			</COSPutObjectCopy>
		</Operation>
		<Priority>10</Priority>
		<ProgressSummary>
			<NumberOfTasksFailed>0</NumberOfTasksFailed>
			<NumberOfTasksSucceeded>10</NumberOfTasksSucceeded>
			<TotalNumberOfTasks>10</TotalNumberOfTasks>
		</ProgressSummary>
		<Report>
			<Bucket>qcs::cos:ap-chengdu::sourcebucket-1250000000</Bucket>
			<Enabled>true</Enabled>
			<Format>Report_CSV_V1</Format>
			<Prefix>job-result</Prefix>
			<ReportScope>AllTasks</ReportScope>
		</Report>
		<RoleArn>qcs::cam::uin/100000000001:roleName/COS_Batch_QcsRole</RoleArn>
		<Status>Complete</Status>
		<StatusUpdateReason>Job complete</StatusUpdateReason>
		<TerminationDate>2019-12-19T18:00:42Z</TerminationDate>
	</Job>
</DescribeJobResult>
```

