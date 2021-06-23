## 功能描述
DescribeAudioAuditingJob 接口用来查询指定的音频审核任务。

## 请求

#### 请求示例

``` plaintext
GET /audio/auditing/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档）。
>


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。


####  请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
			<JobsDetail>
				<Code>Success</Code>
				<Message>Success</Message>
				<JobId>aab1ca9fc8a3ed11ea834c525400863904</JobId>
				<State>Success</State>
				<CreationTime>2019-07-07T12:12:12+0800</CreationTime>
				<Object>a.mp3</Object>
				<Result>1</Result>
				<PornInfo>
						<HitFlag>1</HitFlag>
						<Score>93</Score>
						<Label></Label>
				</PornInfo>
				<PoliticsInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</PoliticsInfo>
				<TerrorismInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</TerrorismInfo>
				<AdsInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</AdsInfo>
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
| JobsDetail | Response | 任务的详细信息 |  Container |

Container 节点 JobsDetail 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Code | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义 |  String |
| JobId | Response.JobsDetail | 任务的 ID |  String |
| State | Response.JobsDetail | 任务的状态，值为 Submitted、Success、Failed、Auditing 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| Object | Response.JobsDetail | 音频对象 |  String |
| Result | Response.JobsDetail | 供参考的识别结果，0表示确认正常，1表示确认敏感，2表示疑似敏感  |  String |
| PornInfo | Response.JobsDetail | 涉黄信息，审核信息 |  Container |
| TerrorismInfo | Response.JobsDetail | 涉暴恐信息，审核信息 |  Container |
| PoliticsInfo | Response.JobsDetail | 涉政信息，审核信息 |  Container |
| AdsInfo | Response.JobsDetail | 涉广告信息，审核信息 |  Container |

Container 节点 PornInfo，TerrorismInfo，PoliticsInfo，AdsInfo 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| HitFlag | Response.JobsDetail.*Info | 是否命中该审核分类，0表示确认正常，1表示确认敏感，2表示疑似敏感 |  String |
| Score | Response.JobsDetail.*Info | 审核分值 |  String |
| Label | Response.JobsDetail.*Info | 命中的标签 | String |



#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /audio/auditing/vab1ca9fc8a3ed11ea834c525400863904 HTTP/1.1
Accept: */*
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****



<Response>
			<JobsDetail>
				<Code>Success</Code>
				<Message>Success</Message>
				<JobId>aab1ca9fc8a3ed11ea834c525400863904</JobId>
				<State>Success</State>
				<CreationTime>2019-07-07T12:12:12+0800</CreationTime>
				<Object>a.mp3</Object>
				<Result>1</Result>
				<PornInfo>
						<HitFlag>1</HitFlag>
						<Score>93</Score>
						<Label></Label>
				</PornInfo>
				<PoliticsInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</PoliticsInfo>
				<TerrorismInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</TerrorismInfo>
				<AdsInfo>
						<HitFlag>0</HitFlag>
						<Score>0</Score>
						<Label></Label>
				</AdsInfo>
			</JobsDetail>
</Response>
```


