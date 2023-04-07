## 功能描述

拉取符合条件的任务。


## 请求

#### 请求示例

```shell
GET /pic_jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>?
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体
该请求无请求体。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型    | 是否必选 |
| :----------------- | :----- | :----------------------------------------------------------- | :------ | :------- |
| queueId            | 无     | 拉取该队列 ID 下的任务                                       | String  | 是       |
| tag                | 无     | 任务的 Tag                                                  | String  | 是       |
| workflowId         | 无     | 触发该任务的工作流ID                                          | String  | 否       |
| inventoryTriggerJobId | 无     | 触发该任务的存量触发任务ID                                                  | String  | 否       |
| inputObject | 无     | 该任务的输入文件名，暂仅支持精确匹配                                                  | String  | 否       |
| orderByTime        | 无     | Desc 或者 Asc。默认为 Desc                                   | String  | 否       |
| nextToken          | 无     | 请求的上下文，用于翻页。上次返回的值                         | String  | 否       |
| size               | 无     | 拉取的最大任务数。默认为10。最大为100                        | Integer | 否       |
| states             | 无     | 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All | String  | 否       |
| startCreationTime  | 无     | 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`，示例：2001-01-01T00:00:00+0800 | String  | 否 |
| endCreationTime    | 无     | 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`，示例：2001-01-01T23:59:59+0800 | String  | 否 |


tag 支持以下几种类型:

| 任务类型 | tag |
| :----------------- | :----- |
| 图片处理          | PicProcess |
| 图片处理          | PosterProduction |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
    <JobsDetail>
        ...
    </JobsDetail>
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
| JobsDetail         | Response | 任务的详细信息                                               | Container数组 |
| NextToken          | Response | 翻页的上下文 Token                                            | String    |

对于不同的任务类型，JobsDetail 的内容不同，请参照以下链接：
- <a href="https://cloud.tencent.com/document/product/460/77012#jobsDetail" target="_blank">图片处理</a>

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
GET /pic_jobs?queueId=p2911917386e148639319e13c285cc774&tag=PicProcess HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:test-1234567890.ci.ap-chongqing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
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
        <Tag>PosterProduction</Tag>
        <Operation>
            <PosterProduction>
                <TemplateId>6324349b569067d4d11a2c2c</TemplateId>
                <Info>
                    <Background>https://static.taishan.qq.com/xrdnest/pstemplate/assets/e96c14ea085cda431481e774954fa3a5.png?imageMogr2/format/webp</Background>
                    <EXPIRY>EXPIRY</EXPIRY>
                    <MM>MM</MM>
                    <YY>YY</YY>
                    <base>https://static.taishan.qq.com/xrdnest/pstemplate/assets/ba206498074a034722a936ec12eef1f6.png?imageMogr2/format/webp</base>
                </Info>
            </PosterProduction>
            <Output>
                <Bucket>test-1234567890</Bucket>
                <Object>output/out.png</Object>
                <Region>ap-chongqing</Region>
            </Output>
            <TemplateId>t10461fe2bd5a649db9022452ec71e0381</TemplateId>
            <TemplateName>test</TemplateName>
            <UserData>This is my data.</UserData>
            <JobLevel>0</JobLevel>
        </Operation>
    </JobsDetail>
    <JobsDetail>
        <Code>Success</Code>
        <Message/>
        <JobId>c93984788066911ed89ed352d4d9d2084</JobId>
        <State>Submitted</State>
        <CreationTime>2022-07-18T15:16:43+0800</CreationTime>
        <EndTime>-</EndTime>
        <StartTime>-</StartTime>
        <QueueId>p2911917386e148639319e13c285cc774</QueueId>
        <Tag>PosterProduction</Tag>
        <Operation>
            <PosterProduction>
                <TemplateId>6324349b569067d4d11a2c2c</TemplateId>
                <Info>
                    <Background>https://static.taishan.qq.com/xrdnest/pstemplate/assets/e96c14ea085cda431481e774954fa3a5.png?imageMogr2/format/webp</Background>
                    <EXPIRY>EXPIRY</EXPIRY>
                    <MM>MM</MM>
                    <YY>YY</YY>
                    <base>https://static.taishan.qq.com/xrdnest/pstemplate/assets/ba206498074a034722a936ec12eef1f6.png?imageMogr2/format/webp</base>
                </Info>
            </PosterProduction>
            <Output>
                <Bucket>test-1234567890</Bucket>
                <Object>output/out.png</Object>
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

