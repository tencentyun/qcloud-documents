## 功能说明

数据万象支持自定义设置回调 URL，在工作流开启状态下，每执行一个实例后，系统会向该 URL 发送 HTTP POST 请求，请求体中包含通知内容。您可通过配置的回调地址及时了解工作流实例处理的进展和状态，以便进行其他业务操作。

## 回调内容

任务完成后，系统会向您设置的回调地址发送回调内容，该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <EventName>WorkflowFinish</EventName>
    <WorkflowExecution>
        <WorkflowId>web6ac56c1ef54dbfa44d7f4103203be9</WorkflowId>
        <WorkflowName>workflow-3</WorkflowName>
        <RunId>i166ee19017b011eda8a5525400c540df</RunId>
        <State>Success</State>
        <BucketId>test-1234567890</BucketId>
        <Object>wk-test/game.mp4</Object>
        <CreateTime>2022-08-09 14:54:17+0800</CreateTime>
        <CosHeaders>
            <Key>Content-Type</Key>
            <Value>video/mp4</Value>
        </CosHeaders>
        <CosHeaders>
            <Key>x-cos-request-id</Key>
            <Value>NjJiZDYwYTFfNjUzYTYyNjRfZjEwZl8xMmZhYzY5</Value>
        </CosHeaders>
        <Tasks>
            <Type>Snapshot</Type>
            <CreateTime>2022-08-09 14:54:40+0800</CreateTime>
            <EndTime>2022-08-09 14:54:42+0800</EndTime>
            <State>Success</State>
            <JobId>j23c11e1e17b011edaab4ab15ec33d076</JobId>
            <Name>Snapshot_1581665960536</Name>
            <TemplateId>t07740e32081b44ad7a0aea03adcffd54a</TemplateId>
            <TemplateName>snapshot_1280*720_3</TemplateName>
        </Tasks>
        <Tasks>
            <Type>Transcode</Type>
            <CreateTime>2022-08-09 14:54:18+0800</CreateTime>
            <EndTime>2022-08-09 14:54:39+0800</EndTime>
            <State>Success</State>
            <JobId>j168668b217b011ed8efb27bb229e2d11</JobId>
            <Name>Transcode_1581665960537</Name>
            <TemplateId>t01e57db1c2d154d2fb57aa5de9313a897</TemplateId>
            <TemplateName>MP4-265-SD</TemplateName>
        </Tasks>
    </WorkflowExecution>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| EventName          | Response | 固定值，为 WorkflowFinish | String |
| WorkflowExecution  | Response | 工作流的详细信息           | Container |

Container 节点 WorkflowExecution 的内容：

| 节点名称（关键字） | 父节点                     | 描述                                                         | 类型      |
| :----------------- | :------------------------- | :----------------------------------------------------------- | :-------- |
| WorkflowId         | Response.WorkflowExecution | 工作流 ID                                                    | String    |
| WorkflowName       | Response.WorkflowExecution | 工作流的名称                                                 | String    |
| RunId              | Response.WorkflowExecution | 工作流实例的 ID                                              | String    |
| State              | Response.WorkflowExecution | 实例的状态，值为 Success、Failed 其中一个。Tasks 存在一个 Failed，则此实例视为 Failed | String    |
| BucketId           | Response.WorkflowExecution | 被处理文件所属的存储桶                                       | String    |
| Object             | Response.WorkflowExecution | 该实例处理的文件名                                           | String    |
| CreateTime         | Response.WorkflowExecution | 实例的创建时间                                               | String    |
| CosHeaders         | Response.WorkflowExecution | 该 Object 上传时设定的自定义 Header 列表，没有设置时无此内容 | Container 数组 |
| Tasks              | Response.WorkflowExecution | 任务信息列表                                                 | Container 数组 |

Container 节点 CosHeaders 的内容：

| 节点名称（关键字） | 父节点                                | 描述                 | 类型   |
| :----------------- | :------------------------------------ | :------------------- | :----- |
| Key                | Response.WorkflowExecution.CosHeaders | 自定义 Header 的名称 | String |
| Value              | Response.WorkflowExecution.CosHeaders | 自定义 Header 的值   | String |

Container 节点 Tasks 的内容：

| 节点名称（关键字） | 父节点                           | 描述                                                      | 类型   |
| :----------------- | :------------------------------- | :-------------------------------------------------------- | :----- |
| Type               | Response.WorkflowExecution.Tasks | 任务类型                                                | String |
| Createtime         | Response.WorkflowExecution.Tasks | 任务的创建时间                                            | String |
| StartTime          | Response.WorkflowExecution.Tasks | 任务开始时间                                             | String |
| EndTime            | Response.WorkflowExecution.Tasks | 任务的完成时间                                            | String |
| State              | Response.WorkflowExecution.Tasks | 任务的状态，值为 Success、Failed 等                        | String |
| JobId              | Response.WorkflowExecution.Tasks | 任务的 ID                                                 | String |
| Name               | Response.WorkflowExecution.Tasks | 任务在工作流中的节点名称                                   | String |
| TemplateId         | Response.WorkflowExecution.Tasks | 任务使用的模板 ID                                         | String |
| TemplateName       | Response.WorkflowExecution.Tasks | 任务使用的模板名称                                        | String |

## 实际案例

### 案例 1 (XML)
```plaintext
<Response>
    <EventName>WorkflowFinish</EventName>
    <WorkflowExecution>
        <WorkflowId>web6ac56c1ef54dbfa44d7f4103203be9</WorkflowId>
        <WorkflowName>workflow-3</WorkflowName>
        <RunId>i166ee19017b011eda8a5525400c540df</RunId>
        <State>Success</State>
        <BucketId>test-1234567890</BucketId>
        <Object>wk-test/game.mp4</Object>
        <CreateTime>2022-08-09 14:54:17+0800</CreateTime>
        <CosHeaders>
            <Key>Content-Type</Key>
            <Value>video/mp4</Value>
        </CosHeaders>
        <CosHeaders>
            <Key>x-cos-request-id</Key>
            <Value>NjJiZDYwYTFfNjUzYTYyNjRfZjEwZl8xMmZhYzY5</Value>
        </CosHeaders>
        <Tasks>
            <Type>Snapshot</Type>
            <CreateTime>2022-08-09 14:54:40+0800</CreateTime>
            <EndTime>2022-08-09 14:54:42+0800</EndTime>
            <State>Success</State>
            <JobId>j23c11e1e17b011edaab4ab15ec33d076</JobId>
            <Name>Snapshot_1581665960536</Name>
            <TemplateId>t07740e32081b44ad7a0aea03adcffd54a</TemplateId>
            <TemplateName>snapshot_1280*720_3</TemplateName>
        </Tasks>
        <Tasks>
            <Type>Transcode</Type>
            <CreateTime>2022-08-09 14:54:18+0800</CreateTime>
            <EndTime>2022-08-09 14:54:39+0800</EndTime>
            <State>Success</State>
            <JobId>j168668b217b011ed8efb27bb229e2d11</JobId>
            <Name>Transcode_1581665960537</Name>
            <TemplateId>t01e57db1c2d154d2fb57aa5de9313a897</TemplateId>
            <TemplateName>MP4-265-SD</TemplateName>
        </Tasks>
    </WorkflowExecution>
</Response>
```

### 案例 2 (JSON)

```plaintext
{
    "EventName": "WorkflowFinish",
    "WorkflowExecution": {
        "WorkflowId": "web6ac56c1ef54dbfa44d7f4103203be9",
        "WorkflowName": "workflow-3",
        "RunId": "i166ee19017b011eda8a5525400c540df",
        "State": "Success",
        "BucketId": "test-1234567890",
        "Object": "wk-test/game.mp4",
        "CreateTime": "2022-08-09 14:54:17+0800",
        "CosHeaders": [{
                "Key": "Content-Type",
                "Value": "video/mp4"
            },
            {
                "Key": "x-cos-request-id",
                "Value": "NjJiZDYwYTFfNjUzYTYyNjRfZjEwZl8xMmZhYzY5"
            }
        ],
        "Tasks": [{
                "Type": "Snapshot",
                "CreateTime": "2022-08-09 14:54:40+0800",
                "EndTime": "2022-08-09 14:54:42+0800",
                "State": "Success",
                "JobId": "j23c11e1e17b011edaab4ab15ec33d076",
                "Name": "Snapshot_1581665960536",
                "TemplateId": "t07740e32081b44ad7a0aea03adcffd54a",
                "TemplateName": "snapshot_1280*720_3"
            },
            {
                "Type": "Transcode",
                "CreateTime": "2022-08-09 14:54:18+0800",
                "EndTime": "2022-08-09 14:54:39+0800",
                "State": "Success",
                "JobId": "j168668b217b011ed8efb27bb229e2d11",
                "Name": "Transcode_1581665960537",
                "TemplateId": "t01e57db1c2d154d2fb57aa5de9313a897",
                "TemplateName": "MP4-265-SD"
            }
        ]
    }
}
```
