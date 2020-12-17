数据万象（Cloud Infinite，CI）是腾讯云为客户提供的专业一体化的图片解决方案，涵盖图片上传、下载、存储、处理、识别等功能，将 QQ 空间相册积累的十年图片服务运作经验开放给开发者。目前数据万象提供图片缩放、裁剪、水印、转码、内容审核等多种功能，提供高效准确的图像识别及处理服务，减少人力投入，真正地实现人工智能。

下表为云审计支持的数据万象操作列表：

| 操作名称         | 资源类型 | 事件名称                            |
|--------------|------|---------------------------------|
| 取消任务         | ci   | CancelMediaJob                  |
| 创建语音识别 bucket | ci   | CreateAsrBucket                 |
| 创建审核任务       | ci   | CreateAuditingJobs              |
| 绑定存储桶        | ci   | CreateMediaBucket               |
| 创建任务         | ci   | CreateMediaJobs                 |
| 创建模版         | ci   | CreateMediaTemplate             |
| 创建工作流        | ci   | CreateMediaWorkflow             |
| 解绑语音识别 bucket | ci   | DeleteAsrBucket                 |
| 解绑存储桶        | ci   | DeleteMediaBucket               |
| 删除模版         | ci   | DeleteMediaTemplate             |
| 删除工作流        | ci   | DeleteMediaWorkflow             |
| 获取语音识别存储桶列表  | ci   | DescribeAsrBuckets              |
| 获取语音识别的队列    | ci   | DescribeAsrQueues               |
| 获取审核任务       | ci   | DescribeAuditingJobs            |
| 获取存储桶        | ci   | DescribeMediaBuckets            |
| 获取任务         | ci   | DescribeMediaJob                |
| 获取任务列表       | ci   | DescribeMediaJobs               |
| 获取队列         | ci   | DescribeMediaQueues             |
| 获取模版         | ci   | DescribeMediaTemplates          |
| 获取工作流执行实例    | ci   | DescribeMediaWorkflowExecutions |
| 获取工作流        | ci   | DescribeMediaWorkflows          |
| 修改语音识别队列     | ci   | UpdateAsrQueue                  |
| 修改队列         | ci   | UpdateMediaQueue                |
| 修改模版         | ci   | UpdateMediaTemplate             |
| 更新工作流        | ci   | UpdateMediaWorkflow             |
