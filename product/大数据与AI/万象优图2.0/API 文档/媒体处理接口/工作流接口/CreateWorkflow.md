## 功能描述

Create Workflow 接口用于新增工作流。

## 请求

#### 请求示例

```plaintext
POST /workflow HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

> ?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```plaintext
<Request>
    <MediaWorkflow>
        <Name>demo</Name>
        <Topology>
            <Dependencies>
                <Start>Snapshot_1581665960536,Snapshot_1581665960537,Animation_1581665960538,Animation_1581665960539</Start>
                <Snapshot_1581665960536>End</Snapshot_1581665960536>
                <Snapshot_1581665960537>End</Snapshot_1581665960537>
                <Animation_1581665960538>End</Animation_1581665960538>
                <Animation_1581665960539>End</Animation_1581665960539>
                <SmartCover_1581665960539>End</SmartCover_1581665960539>
            </Dependencies>
            <Nodes>
                <Start>
                    <Type>Start</Type>
                    <Input>
                        <QueueId></QueueId>
                        <ObjectPrefix></ObjectPrefix>
                    </Input>
                </Start>
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                    </Operation>
                </SmartCover_1581665960539>
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
    </MediaWorkflow>
</Request>

```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | -------- |
| Request            | 无     | 保存请求的容器 | Container | 是       |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述       | 类型      | 是否必选 |
| ------------------ | ------- | ---------- | --------- | -------- |
| MediaWorkflow      | Request | 工作流节点 | Container | 是       |

Container 类型 MediaWorkflow 的具体数据描述如下：

| 节点名称（关键字） | 父节点                | 描述       | 类型      | 是否必选 | 限制                                        |
| ------------------ | --------------------- | ---------- | --------- | -------- | ------------------------------------------- |
| Name               | Request.MediaWorkflow | 工作流名称 | String    | 是       | 支持中文、英文、数字、—和_，长度限制128字符 |
| Topology           | Request.MediaWorkflow | 拓扑信息   | Container | 是       | 无                                          |
| State              | Request.MediaWorkflow | 工作流状态 | String    | 是       | <li>Active <br/><li>Paused                    |

Container 类型 Topology 的具体数据描述如下：

| 节点名称（关键字） | 父节点                         | 描述         | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------ | ------------ | --------- | -------- | ---- |
| Dependencies       | Request.MediaWorkflow.Topology | 节点依赖关系 | Container | 是       | 无   |
| Nodes              | Request.MediaWorkflow.Topology | 节点列表     | Container | 是       | 无   |

Container 类型 Nodes 的具体数据描述如下：

| 节点名称（关键字） | 父节点                               | 描述         | 类型      | 是否<br>必选 | 限制                                               |
| ------------------ | ------------------------------------ | ------------ | --------- | ------------ | -------------------------------------------------- |
| Start              | Request.MediaWorkflow.Topology.Nodes | 开始节点     | Container | 是           | 只有唯一一个开始节点                               |
| Animation_***      | Request.MediaWorkflow.Topology.Nodes | 动图类型节点 | Container | 是           | 节点名称以 Animation 为前缀，可能有多个动图节点      |
| Snapshot_***       | Request.MediaWorkflow.Topology.Nodes | 截图类型节点 | Container | 是           | 节点名称以 Snapshot 为前缀，可能有多个截图节点       |
| SmartCover_***     | Request.MediaWorkflow.Topology.Nodes | 智能封面节点 | Container | 是           | 节点名称以 SmartCover 为前缀，可能有多个智能封面节点 |

Container 类型 Start 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                     | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------ | -------- | --------- | -------- | ---- |
| Type               | Request.MediaWorkflow.Topology.Nodes.Start | 节点类型 | String    | 是       | 无   |
| Input              | Request.MediaWorkflow.Topology.Nodes.Start | 输入信息 | Container | 是       | 无   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                | 描述        | 类型   | 是否必选 | 限制 |
| ------------------ | ----------------------------------------------------- | ----------- | ------ | -------- | ---- |
| ObjectPrefix       | Request.MediaWorkflow.Topology.Nod<br/>es.Start.Input | Object 前缀 | String | 是       | 无   |
| QueueId            | Request.MediaWorkflow.Topology.Nod<br/>es.Start.Input | 队列 ID     | String | 是       | 无   |

Container 类型 Animation_*** 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                  | 描述     | 类型      | 是否必选 | 限制         |
| ------------------ | ------------------------------------------------------- | -------- | --------- | -------- | ------------ |
| Type               | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_*** | 节点类型 | String    | 是       | 动图类型节点 |
| Operation          | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_*** | 操作规则 | Container | 是       | 无           |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_***.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_***.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否<br>必选 | 限制                                                   |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ------------ | ------------------------------------------------------ |
| Region             | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_***.Operation.Output | 存储桶的地域 | String | 是           | 无                                                     |
| Bucket             | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_***.Operation.Output | 存储桶的名称 | String | 是           | 无                                                     |
| Object             | Request.MediaWorkflow.Topology.Nod<br/>es.Animation_***.Operation.Output | 结果文件名称 | String | 是           | <li>bcd/${RunId}/bcd.gif <br><li>bcd/${RunId}/bcd.webp |

Container 类型 Snapshot_*** 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                    | 描述     | 类型      | 是否必选 | 限制         |
| ------------------ | --------------------------------------------------------- | -------- | --------- | -------- | ------------ |
| Type               | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_****** | 节点类型 | String    | 是       | 动图类型节点 |
| Operation          | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_****** | 操作规则 | Container | 是       | 无           |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| TemplateId         | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_***.Operation | 模板 ID  | String    | 是       | 无   |
| Output             | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_***.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否<br>必选 | 限制                                                         |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | ------------ | ------------------------------------------------------------ |
| Region             | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_***.Operation.Output | 存储桶的地域 | String | 是           | 无                                                           |
| Bucket             | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_***.Operation.Output | 存储桶的名称 | String | 是           | 无                                                           |
| Object             | Request.MediaWorkflow.Topology.Nod<br/>es.Snapshot_***.Operation.Output | 结果文件名称 | String | 是           | <li>abc/${RunId}/snapshot-${number}.${Ext}<br><li>bcd/${RunId}/snapshot-${number}.jpg |

Container 类型 SmartCover_*** 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                   | 描述     | 类型      | 是否必选 | 限制         |
| ------------------ | -------------------------------------------------------- | -------- | --------- | -------- | ------------ |
| Type               | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_*** | 节点类型 | String    | 是       | 动图类型节点 |
| Operation          | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_*** | 操作规则 | Container | 是       | 无           |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述     | 类型      | 是否必选 | 限制 |
| ------------------ | ------------------------------------------------------------ | -------- | --------- | -------- | ---- |
| Output             | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_***.Operation | 输出地址 | Container | 是       | 无   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                                       | 描述         | 类型   | 是否必选 | 限制                            |
| ------------------ | ------------------------------------------------------------ | ------------ | ------ | -------- | ------------------------------- |
| Region             | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_***.Operation.Output | 存储桶的地域 | String | 是       | 无                              |
| Bucket             | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_***.Operation.Output | 存储桶的名称 | String | 是       | 无                              |
| Object             | Request.MediaWorkflow.Topology.Nod<br/>es.SmartCover_***.Operation.Output | 结果文件名称 | String | 是       | 必须包含 ${Number} ${RunId}参数 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <MediaWorkflow>
        <Name>demo</Name>
        <MediaWorkflowId></MediaWorkflowId>
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
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                    </Operation>
                </SmartCover_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>

```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型      |
| :----------------- | :----- | :----------------------------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器，同 GET Workflow 中的 Response.MediaWorkflowList | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
POST /workflow HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
    <MediaWorkflow>
        <Name>demo</Name>
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
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                    </Operation>
                </SmartCover_1581665960539>
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
    </MediaWorkflow>
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
    <MediaWorkflow>
        <Name>demo</Name>
        <State></State>
        <WorkflowId></WorkflowId>
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
                <SmartCover_1581665960539>
                    <Type>SmartCover</Type>
                    <Operation>
                        <Output>
                            <Region></Region>
                            <Bucket></Bucket>
                            <Object>abc/${RunId}/cover-${Number}.jpg</Object>
                        </Output>
                    </Operation>
                </SmartCover_1581665960539>
            </Nodes>
        </Topology>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </MediaWorkflow>
</Response>
```
