## 功能描述
Create AudioAuditing Jobs 接口用来提交一个音频审核任务。

## 请求
#### 请求示例

```shell
POST /audio/auditing HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体：

```plaintext
<Request>
			<Input>
				<Object></Object>
			</Input>
			<Conf>
				<DetectType>Porn,Politics</DetectType>
				<Callback></Callback>
			</Conf>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | -------- |
| Request            | 无     | 保存请求的容器 | Container | 是       |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述             | 类型      | 是否必选 |
| ------------------ | ------- | ---------------- | --------- | -------- |
| Input              | Request | 待操作的媒体信息 | Container | 是       |
| Conf               | Request | 操作规则         | Container | 是       |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述           | 类型   | 是否必选 |
| ------------------ | ------------- | -------------- | ------ | -------- |
| Object             | Request.Input | 音频对象 | String | 是       |

>?可识别普通话、英语。

Container 类型 Conf 的具体数据描述如下：

| 节点名称（关键字） | 父节点       | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| DetectType          | Request.Conf | 审核类型，涉黄 Porn、涉暴恐 Terrorism、政治敏感 Politics、广告 Ads，可以审核多种类型，以 `,` 分隔 | string | 是   |
| Callback            | Request.Conf | 回调地址，以`http://`或者`https://`开头的地址 | string | 否   |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
			<JobsDetail>
				<JobId></JobId>
				<State></State>
				<CreationTime></CreationTime>
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

Container 节点 JobsDetail 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Success、Failed、Auditing 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
POST /audio/auditing HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml



<Request>
			<Input>
				<Object>a.mp4</Object>
			</Input>
			<Conf>
				<DetectType>Porn,Politics</DetectType>
				<Callback>http://callback.com/</Callback>
			</Conf>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****



<Response>
			<JobsDetail>
				<JobId>vab1ca9fc8a3ed11ea834c525400863904</JobId>
				<State>Submitted</State>
				<CreationTime>2019-07-07T12:12:12+0800</CreationTime>
			</JobsDetail>
</Response>
```
