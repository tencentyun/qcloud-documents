## 功能描述

Describe WorkflowExecution 接口用于获取工作流实例详情。

## 请求

#### 请求示例

```shell
GET /workflowexecution/<RunId> HTTP/1.1
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

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <WorkflowExecution>
    <RunId>37145b2919714156bd97f91dc03fa2b4</RunId>
    <WorkflowId>we65e4d260e1042debdfb7e4560a19d3d</WorkflowId>
    <WorkflowName></WorkflowName>
    <State>Success</State>
    <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
    <Object>https://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/mars_white_test.mp4</Object>
    <Topology>
        <Dependencies>
            <Start>Snapshot_1581665960536,Animation_1581665960538</Start>
            <Snapshot_1581665960536>End</Snapshot_1581665960536>
            <Animation_1581665960538>End</Animation_1581665960538>
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
        </Nodes>
    </Topology>
    <Tasks>
        <Type>Start</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Success</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Start</Name>
    </Tasks>
    <Tasks>
        <Type>Snapshot</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Success</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Snapshot_1581665960536</Name>
    </Tasks>
    <Tasks>
        <Type>Animation</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Failed</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Animation_1581665960538</Name>
    </Tasks>
  </WorkflowExecution>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述               | 类型      |
| :----------------- | :------- | :----------------- | :-------- |
| WorkflowExecution  | Response | 工作流实例详细信息 | Container |

Container 节点 WorkflowExecution 的内容：

| 节点名称（关键字） | 父节点                     | 描述                                                         | 类型      |
| :----------------- | :------------------------- | :----------------------------------------------------------- | :-------- |
| RunId              | Response.WorkflowExecution | 工作流实例 ID                                                | string    |
| WorkflowId         | Response.WorkflowExecution | 工作流 ID                                                    | string    |
| WorkflowName       | Response.WorkflowExecution | 工作流名称                                                   | string    |
| State              | Response.WorkflowExecution | 工作流实例状态                                               | string    |
| CreateTime         | Response.WorkflowExecution | 创建时间                                                     | string    |
| Object             | Response.WorkflowExecution | COS 对象地址                                                 | string    |
| Topology           | Response.WorkflowExecution | 拓扑信息，同 GetWorkflow 的 Response.MediaWorkflowList.Topology | Container |
| Tasks              | Response.WorkflowExecution | 工作流实例任务                                               | Container |

Container 节点 Tasks 的内容：

| 节点名称（关键字） | 父节点                           | 描述             | 类型   |
| :----------------- | :------------------------------- | :--------------- | :----- |
| Type               | Response.WorkflowExecution.Tasks | 任务所属节点类型 | string |
| CreateTime         | Response.WorkflowExecution.Tasks | 创建时间         | string |
| EndTime            | Response.WorkflowExecution.Tasks | 结束时间         | string |
| State              | Response.WorkflowExecution.Tasks | 任务状态         | string |
| JobId              | Response.WorkflowExecution.Tasks | 任务 ID          | string |
| Name               | Response.WorkflowExecution.Tasks | 节点name         | string |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```shell
GET /workflowexecution/37145b2919714156bd97f91dc03fa2b4 HTTP/1.1
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
  <WorkflowExecution>
    <RunId>37145b2919714156bd97f91dc03fa2b4</RunId>
    <WorkflowId>we65e4d260e1042debdfb7e4560a19d3d</WorkflowId>
    <WorkflowName></WorkflowName>
    <State>Success</State>
    <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
    <Object>https://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/mars_white_test.mp4</Object>
    <Topology>
        <Dependencies>
            <Start>Snapshot_1581665960536,Animation_1581665960538</Start>
            <Snapshot_1581665960536>End</Snapshot_1581665960536>
            <Animation_1581665960538>End</Animation_1581665960538>
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
        </Nodes>
    </Topology>
    <Tasks>
        <Type>Start</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Success</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Start</Name>
    </Tasks>
    <Tasks>
        <Type>Snapshot</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Success</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Snapshot_1581665960536</Name>
    </Tasks>
    <Tasks>
        <Type>Animation</Type>
        <CreateTime>2019-07-07T12:12:12+0800</CreateTime>
        <EndTime></EndTime>
        <State>Failed</State>
        <JobId>f9ddcf74ebfd4f0caa0bb78692432d69</JobId>
        <Name>Animation_1581665960538</Name>
    </Tasks>
  </WorkflowExecution>
</Response>
```
