## 功能描述
用于查询指定的任务。

## 请求

#### 请求示例

```plaintext
GET /project/<ProjectId>/jobs?ids=<JobId>&tag=Concat HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数
此接口无请求参数。


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
| JobsDetail | Response | 任务的详细信息，同 CreateJob 接口的 Response.JobsDetail 节点 |  Container |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。


## 实际案例

#### 请求

```plaintext
GET /project/p893bcda225bf4945a378da6662e81a89/jobs?ids=jabcsdssfeipplsdfwe&tag=Concat HTTP/1.1
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
    <Message>Success</Message>
    <JobId>jabcsdssfeipplsdfwe</JobId>
    <State>Submitted</State>
    <CreationTime>2020-07-07T12:12:12+0800</CreationTime>
    <EndTime></EndTime>
    <ProjectId>p893bcda225bf4945a378da6662e81a89</ProjectId>
    <Tag>Concat</Tag>
    <Operation>
        <Concat>
            <Fragments>
                <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
            </Fragments>
            <Fragments>
                <Url>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
            </Fragments>
            <Audio>
                <Codec>mp3</Codec>
                <Samplerate></Samplerate>
                <Bitrate></Bitrate>
                <Channels></Channels>
            </Audio>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Container>
                <Format>mp4</Format>
            </Container>
        </Concat>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>aabc-1250000000</Bucket>
            <Object>concat.mp4</Object>
        </Output>
    </Operation>
  </JobsDetail>
</Response>
```


