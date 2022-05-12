## 功能描述
用于提交一个任务。

## 请求

#### 请求示例

```plaintext
POST /project/<ProjectId>/jobs HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
  <Tag>AI</Tag>
  <Input>
    <Url></Url>
    <Decrypt>
      <Key></Key>
      <Salt></Salt>
      <Method></Method>
    </Decrypt>
  </Input>
  <Operation>
    <AI>
        <Mode>MovingObjectDetect</Mode>
        <MovingObjectDetect>
            <Type>Pet</Type>
        </MovingObjectDetect>
    </AI>
    <Notify>
      <Url></Url>
      <ContentType></ContentType>
    </Notify>
  </Operation>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                  | 类型      | 是否必选 |
| ------------------ | ------- | ------------------------- | --------- | ---- |
| Tag                | Request | 创建任务的 Tag：AI。 | String    | 是   |
| Input              | Request | 待操作的媒体文件          | Container | 是   |
| Operation          | Request | 操作规则                  | Container | 是   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ------------- | ------------------ | --------- | ---- |
| Url                | Request.Input | 媒体文件的下载地址 | String    | 否   |
| Decrypt            | Request.Input | 媒体文件的解密方式 | Container | 否   |

Container 类型 Decrypt 的具体数据描述如下：

| 节点名称（关键字） | 父节点                | 描述                                            | 类型   | 是否必选 | 默认值 |
| ------------------ | --------------------- | ----------------------------------------------- | ------ | ---- | ------ |
| Key                | Request.Input.Decrypt | 解密的 Key，当 Method 为 XIAOYI 时，此值对应 pwd      | String | 是   | 无     |
| Salt               | Request.Input.Decrypt | 额外的处理参数，当 Method 为 XIAOYI 时，此值对应 uid | String | 否   | 无     |
| Method             | Request.Input.Decrypt | 解密方法，可选值为 XIAOYI                      | String | 否   | AES    |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| AI | Request.Operation | 指定任务参数 | Container | 是  |
| Notify   | Request.Operation | 任务结果通知地址 | Container | 否 |

Container 类型 AI 的具体数据描述如下：

| 节点名称（关键字） | 父节点                     | 描述                           | 类型   | 是否必选 |
| ------------------ | -------------------------- | ------------------------------ | ------ | ---- |
| Mode               | Request.Operation.AI | 分析类型，可选值为 MovingObjectDetect       | String | 是   |
| MovingObjectDetect | Request.Operation.AI | 移动物体检测参数                        | Container    | 是   |

Container 类型 MovingObjectDetect 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述             | 类型   | 是否必选 |
| ------------------ | ------------------------ | ---------------- | ------ | ---- |
| Type             | Request.Operation.AI.MovingObjectDetect |  检测物体类型。可选值为 Pet、Baby   | String | 是   |

Container 类型 Notify 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                           | 类型   | 是否必选 | 默认值 |
| ------------------ | ------------------------ | ------------------------------ | ------ | ---- | ------ |
| Url                | Request.Operation.Notify | 通知地址                       | String | 是   | 无     |
| ContentType        | Request.Operation.Notify | 内容格式。可选值为 XML、JSON  | String | 否   | XML    |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
  <JobsDetail>
    <Code></Code>
    <Message></Message>
    <JobId></JobId>
    <State></State>
    <CreationTime></CreationTime>
    <EndTime></EndTime>
    <ProjectId></ProjectId>
    <Tag>AI</Tag>
    <Input>
      <Url></Url>
      <Decrypt>
        <Key></Key>
        <Salt></Salt>
        <Method></Method>
      </Decrypt>
    </Input>
    <Operation>
        <AI>
            <Mode>MovingObjectDetect</Mode>
            <MovingObjectDetect>
                <Type>Pet</Type>
            </MovingObjectDetect>
        </AI>
        <Notify>
            <Url></Url>
            <ContentType></ContentType>
        </Notify>
    </Operation>
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
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| Tag | Response.JobsDetail | 任务的 Tag：AI | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| ProjectId | Response.JobsDetail | 任务所属的项目 ID |  String |
| Input | Response.JobsDetail | 该任务的输入资源地址 |  Container |
| Operation | Response.JobsDetail | 该任务的规则 |  Container |

Container 节点 Input 的内容：
同请求中的 Request.Input节点。

Container 节点 Operation 的内容：
同请求中的 Request.Operation节点。
#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求

```plaintext
POST /project/p893bcda225bf4945a378da6662e81a89/jobs HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1660
Content-Type: application/xml

<Request>
  <Tag>AI</Tag>
  <Input>
    <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/test.mp4</Url>
  </Input>
  <Operation>
    <AI>
        <Mode>MovingObjectDetect</Mode>
        <MovingObjectDetect>
            <Type>Pet</Type>
        </MovingObjectDetect>
    </AI>
    <Notify>
        <Url>http://www.test.com</Url>
        <ContentType>JSON</ContentType>
    </Notify>
  </Operation>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>je8f65004eb8511eaaed4f377124a303c</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <EndTime></EndTime>
    <ProjectId>p893bcda225bf4945a378da6662e81a89</ProjectId>
    <Tag>AI</Tag>
    <Input>
      <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/test.mp4</Url>
    </Input>
    <Operation>
        <AI>
            <Mode>MovingObjectDetect</Mode>
            <MovingObjectDetect>
                <Type>Pet</Type>
            </MovingObjectDetect>
        </AI>
        <Notify>
            <Url>http://www.test.com</Url>
            <ContentType>JSON</ContentType>
        </Notify>
    </Operation>
  </JobsDetail>
</Response>
```
