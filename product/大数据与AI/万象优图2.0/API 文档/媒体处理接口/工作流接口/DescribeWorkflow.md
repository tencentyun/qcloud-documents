## 功能描述

Describe Workflow 接口用于搜索工作流。

## 请求

#### 请求示例

```shell
GET /workflow HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml
```

> ?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

| 参数名称（关键字） | 描述                         | 类型   | 是否必选 |
| :----------------- | :--------------------------- | :----- | :------- |
| ids                | 工作流 ID，以`,`符号分割字符串 | string | 否       |
| name               | 工作流名称                   | string | 否       |
| pageNumber         | 第几页                       | string | 否       |
| pageSize           | 每页个数                     | string | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Snapshot_1581665960537,Animation_1581665960538,Animation_1581665960539</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Snapshot_1581665960537>End</Snapshot_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Animation_1581665960539>End</Animation_1581665960539>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Snapshot_1581665960537>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/snapshot-${number}.jpg</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Animation_1581665960539>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.webp</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 工作流总数                      | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| MediaWorkflowList  | Response | 工作流数组                      | Container |

Container节点 MediaWorkflowList 的内容：

| 节点名称（关键字） | 父节点                     | 描述       | 类型      | 是否必选 | 限制                                                 |
| ------------------ | -------------------------- | ---------- | --------- | -------- | ---------------------------------------------------- |
| Name               | Response.MediaWorkflowList | 工作流名称 | String    | 是       | 支持中文、英文、数字、—和_，长度限制128字符          |
| WorkflowId         | Response.MediaWorkflowList | 工作流 ID  | String    | 是       | 工作流唯一 ID                                        |
| State              | Response.MediaWorkflowList | 工作流状态 | String    | 是       | 1. Active <br/>2. Paused<br/>                        |
| CreateTime         | Response.MediaWorkflowList | 创建时间   | String    | 是       | 无                                                   |
| UpdateTime         | Response.MediaWorkflowList | 更新时间   | String    | 是       | 无                                                   |
| Topology           | Response.MediaWorkflowList | 拓扑信息   | Container | 是       | 同 POST Workflow 中的 Request.MediaWorkflow.Topology |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求1（工作流 ID）

```shell
GET /workflow?ids=demo,demo1 HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应1

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Snapshot_1581665960537,Animation_1581665960538,Animation_1581665960539</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Snapshot_1581665960537>End</Snapshot_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Animation_1581665960539>End</Animation_1581665960539>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Snapshot_1581665960537>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/snapshot-${number}.jpg</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Animation_1581665960539>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.webp</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
    <MediaWorkflowList>
        <Name>demo1</Name>
        <WorkflowId></WorkflowId>
        <State></State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Snapshot_1581665960537,Animation_1581665960538,Animation_1581665960539</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Snapshot_1581665960537>End</Snapshot_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Animation_1581665960539>End</Animation_1581665960539>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Snapshot_1581665960537>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/snapshot-${number}.jpg</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Animation_1581665960539>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.webp</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
</Response>
```

#### 请求2（工作流列表）

```shell
GET /workflow?pageNumber=1&pageSize=1 HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应2

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>11</PageSize>
    <MediaWorkflowList>
        <Name>demo</Name>
        <WorkflowId></WorkflowId>
        <State></State>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Snapshot_1581665960537,Animation_1581665960538,Animation_1581665960539</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Snapshot_1581665960537>End</Snapshot_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Animation_1581665960539>End</Animation_1581665960539>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <Snapshot_1581665960536>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/snapshot-${number}.${Ext}</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960536>
                <Snapshot_1581665960537>
                    <Type>Snapshot</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/snapshot-${number}.jpg</Object>
                        </Output>
                    </Operation>
                </Snapshot_1581665960537>
                <Animation_1581665960538>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>bcd/${RunId}/bcd.gif</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960538>
                <Animation_1581665960539>
                    <Type>Animation</Type>
                    <Operation>
                        <TemplateId></TemplateId>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/abc.webp</Object>
                        </Output>
                    </Operation>
                </Animation_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflowList>
</Response>
```
