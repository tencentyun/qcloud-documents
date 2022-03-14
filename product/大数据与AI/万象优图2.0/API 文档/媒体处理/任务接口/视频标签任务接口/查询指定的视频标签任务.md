## 功能描述

DescribeMediaJob 接口用于查询指定的任务。

## 请求

#### 请求示例

```plaintext
GET /jobs/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` plaintext
<Response>
      <JobsDetail>
      </JobsDetail>
      <NonExistJobIds></NonExistJobIds>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息，同 CreateMediaJobs 接口的 Response.JobsDetail 节点 |  Container |
| NonExistJobIds | Response | 查询的 ID 中不存在任务，所有任务都存在时不返回 |  String |

Container 节点 Operation 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| VideoTag | Response.JobsDetail.Operation | 同 CreateMediaJobs 接口中的 Request.Operation.VideoTag |  Container |
| VideoTagResult | Response.JobSDetail.Operation | 在 job 的类型为 VideoTag 且状态为 success 时，返回视频标签任务结果详情| Container |

Container 节点 VideoTagResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| StreamData | Response.JobsDetail.Operation.VideoTagResult | Stream 场景下视频标签任务的结果 |  Container |

Container 节点 StreamData 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Data | Response.JobsDetail.Operation.VideoTagResult.StreamData | Stream 场景视频标签任务的结果列表 |  Container |
| SubErrCode | Response.JobsDetail.Operation.VideoTagResult.StreamData | 算法状态码，成功为0，非0异常 |  Container |
| SubErrMsg | Response.JobsDetail.Operation.VideoTagResult.StreamData | 算法错误描述，成功为 ok，不成功返回对应错误 |  Container |


Container 节点 Data 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Tags | Response.JobsDetail.Operation.VideoTagResult.StreamData.Data | Stream 场景视频标签信息 |  Container |

Container 节点 Tags 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Tag | Response.JobsDetail.Operation.VideoTagResult.StreamData.Data.Tags | 视频标签名称或视频分类名称 |  String |
| TagCls | Response.JobsDetail.Operation.VideoTagResult.StreamData.Data.Tags | 视频标签分类名称，如果该 Tags 无 TagCls，则该 Tags 为视频分类 |  String |
| Confidence | Response.JobsDetail.Operation.VideoTagResult.StreamData.Data.Tags | 视频标签模型预测分数 |  Float |



#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
GET /jobs/jabcsdssfeipplsdfwe HTTP/1.1
Accept: */*
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
```

#### 响应

```plaintext
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
    <JobId>jabcxxxxfeipplsdfwe</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <StartTime></StartTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>VideoTag</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
      <VideoTag>
        <Scenario>Stream</Scenario>
      </VideoTag>
      <VideoTagResult>
        <StreamData>
          <Data>
            <Tags>
              <Confidence>0.939035</Confidence>
              <Tag>自然风景</Tag>
              <TagCls>生活</TagCls>
            </Tags>
            <Tags>
              <Confidence>0.884062</Confidence>
              <Tag>雪山</Tag>
              <TagCls>旅行风景</TagCls>
            </Tags>
            <Tags>
              <Confidence>0.345798</Confidence>
              <Tag>云彩</Tag>
              <TagCls>旅行风景</TagCls>
            </Tags>
            <Tags>
              <Confidence>0.997328</Confidence>
              <Tag>自然风景</Tag>
            </Tags>
            <Tags>
              <Confidence>0.997595</Confidence>
              <Tag>旅行风景</Tag>
            </Tags>
          </Data>
          <SubErrCode>0</SubErrCode>
          <SubErrMsg>ok</SubErrMsg>
        </StreamData>
      </VideoTagResult>
    </Operation>
  </JobsDetail>
</Response>
```


