## 功能描述
用于查询指定的任务。

## 请求

#### 请求示例

```plaintext
GET /project/<ProjectId>/jobs?ids=<JobId>&tag=AI HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。



#### 请求体
该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <JobsDetail>
    </JobsDetail>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息列表 |  Container |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                   | 类型      |
| :----------------- | :------------------ | :------------------------------------- | :-------- |
| Code | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义 |  String |
| JobId              | Response.JobsDetail | 任务的 ID                               | String    |
| Tag | Response.JobsDetail | 任务的 Tag：AI | String |
| State              | Response.JobsDetail | 任务的状态，为 Success、Failed 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                         | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                         | String    |
| ProjectId          | Response.JobsDetail | 任务所属的项目 ID                       | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                   | Container |
| Operation          | Response.JobsDetail | 该任务的规则和结果                     | Container |

Container 节点 Input 的内容：

| 节点名称（关键字） | 父节点                    | 描述               | 类型      |
| ------------------ | ------------------------- | ------------------ | --------- |
| Url                | Response.JobsDetail.Input | 媒体文件的下载地址 | String    |
| Decrypt            | Response.JobsDetail.Input | 媒体文件的解密方式 | Container |

Container 类型 Decrypt 的具体数据描述如下：

| 节点名称（关键字） | 父节点                            | 描述                                            | 类型   |
| ------------------ | --------------------------------- | ----------------------------------------------- | ------ |
| Key                | Response.JobsDetail.Input.Decrypt | 解密的 Key，当 Method 为 XIAOYI 时，此值对应 pwd      | String |
| Salt               | Response.JobsDetail.Input.Decrypt | 额外的处理参数，当 Method 为 XIAOYI 时，此值对应 uid | String |
| Method             | Response.JobsDetail.Input.Decrypt | 解密方法。可选值为 XIAOYI                      | String |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                        | 描述             | 类型      |
| ------------------ | ----------------------------- | ---------------- | --------- |
| AI                 | Response.JobsDetail.Operation | 任务参数         | Container |
| AIResult           | Response.JobsDetail.Operation | 分析结果         | Container |
| Notify             | Response.JobsDetail.Operation | 任务结果通知地址 | Container |

Container 类型 AI 的具体数据描述如下：

| 节点名称（关键字） | 描述                                    | 类型      |
| ------------------ | ------------------------------------ | --------- |
| Mode               | 分析类型。可选值为 Highlights         | String    |
| Highlights         | 当Mode为Highlights时此值有效          | Container |

Container 类型 AI.Highlights 的具体数据描述如下：

| 节点名称（关键字） | 描述                           | 类型   |
| ------------------ | ------------------------------ | ------ |
| Type               | 分析类型。可选值为 Basketball  | String |

Container 类型 AIResult 的具体数据描述如下：

| 节点名称（关键字） | 描述                                    | 类型      |
| ------------------ | --------------------------------------- | --------- |
| Mode               | 分析类型。可选值为 Highlights         | String    |
| Highlights         | 当 Mode 为 Highlights 时此值有效          | Container |

Container 节点 AIResult.Highlights 的内容：

| 节点名称（关键字） | 描述                                         | 类型      |
| ------------------ | -------------------------------------------- | --------- |
| Urls              | 生成的精彩集锦视频地址，包含多个                   | String   |

Container 类型 Notify 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                           | 类型   | 是否必选 | 默认值 |
| ------------------ | ------------------------ | ------------------------------ | ------ | ---- | ------ |
| Url                | Request.Operation.Notify | 通知地址                       | String | 是   | 无     |
| ContentType        | Request.Operation.Notify | 内容格式。可选值为 XML、JSON  | String | 否   | XML    |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。


## 实际案例

#### 请求

```plaintext
GET /project/p893bcda225bf4945a378da6662e81a89/jobs?ids=jccddc41c27e711ebbff5874bc5b36868&tag=AI HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:iss.ap-beijing.myqcloud.com

```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
	<JobsDetail>
		<Code>Success</Code>
		<CreationTime>2021-11-24T11:57:01+0800</CreationTime>
		<EndTime>2021-11-24T11:57:35+0800</EndTime>
		<Input>
			<Url>https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/basketball.mp4</Url>
		</Input>
		<JobId>in943ba04d4cda11ec8707525400276c76</JobId>
		<Message/>
		<Operation>
			<AI>
				<Highlights>
					<Type>Basketball</Type>
				</Highlights>
				<Mode>Highlights</Mode>
			</AI>
			<AIResult>
				<Highlights>
					<Urls>https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/in943ba04d4cda11ec8707525400276c76-basketball.mp4-highlights-0.mp4</Urls>
					<Urls>https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/in943ba04d4cda11ec8707525400276c76-basketball.mp4-highlights-1.mp4</Urls>
					<Urls>https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/in943ba04d4cda11ec8707525400276c76-basketball.mp4-highlights-2.mp4</Urls>
				</Highlights>
				<Mode>Highlights</Mode>
			</AIResult>
			<Notify>
				<ContentType>JSON</ContentType>
				<Url>http://82.xx.xx.21:9081/receiveCallback/2021-11-24-iss-ai</Url>
			</Notify>
		</Operation>
		<ProjectId>pa3a3d92a1702403aa70d77bea30b73e4</ProjectId>
		<StartTime>2021-11-24T11:57:02+0800</StartTime>
		<State>Success</State>
		<Tag>AI</Tag>
	</JobsDetail>
</Response>
```


