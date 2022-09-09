您可以指定子账号拥有特定资源的数据万象（Cloud Infinite，CI）接口权限。数据万象的授权粒度分为资源级和接口级：

- 资源级接口：此类型接口支持对某一个具体特定的资源进行授权。
- 接口级接口：此类型接口不支持对某一个特定的资源进行授权。

资源级接口在鉴权时，数据万象会将具体的资源六段式传给访问管理（Cloud Access Management，CAM）鉴权，故支持对某一个具体特定的资源进行授权和鉴权。

接口级接口在鉴权时，数据万象不会将具体的资源六段式传给 CAM 鉴权，只会传递任意资源`*`。因此授权时策略语法若限定了具体的资源，鉴权时此接口不传递该资源，CAM 会判断此接口不在授权范围，会判断为无权限。

数据万象的所有接口权限列表如下：

## 列表操作

| 接口名               | 接口描述                                 | 授权粒度 | 资源六段式 |
| :------------------- | ---------------------------------------- | :------- | :--------- |
| DescribeMediaBuckets | 查看开通了媒体处理功能的存储桶列表       | 接口级   | *          |
| DescribeRiskLibImage | 查看内容审核预设风险图库中的图片列表     | 接口级   | *          |
| DescribeRiskLibText  | 查看内容审核预设风险文本库中的关键词列表 | 接口级   | *          |

## 写操作

### 基础功能

| 接口名               | 接口描述                           | 授权粒度 | 资源六段式 |
| :------------------- | ---------------------------------- | :------- | :--------- |
| CreateCIBucket               | 存储桶绑定数据万象 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteCIBucket               | 存储桶解绑数据万象 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetDomain                    | 设置数据万象域名 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetCDNAccelerate             | 设置数据万象 CDN 加速域名 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| Set4XXResponse               | 设置数据万象4xx图片配置 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetRefer                     | 设置数据万象存储桶防盗链功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetOriginProtect             | 设置数据万象原图保护功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### 内容审核

| 接口名                    | 接口描述                             | 授权粒度 | 资源六段式                                                   |
| :------------------------ | ------------------------------------ | :------- | :----------------------------------------------------------- |
| SetAuditingPicture        | 设置图片自动审核                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetAuditingVideo          | 设置视频自动审核                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetAuditingAudio          | 设置音频自动审核                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetAuditingText           | 设置文本自动审核                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetAuditingDocument       | 设置文档自动审核                     | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| CreateAuditingJobs        | 创建视频审核任务                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateAuditingPictureJob  | 调用图片审核                         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateAuditingTextJob     | 创建文本审核任务                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateAuditingAudioJob    | 创建音频审核任务                     | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateAuditingWebpageJob  | 创建网页审核任务                     | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/${bucket}/*            |
| CreateAuditingDocumentJob | 创建文档审核任务                     | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateAuditingExistTask   | 创建存量审核任务                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CancelAuditingExistTask   | 终止存量审核任务                     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteRiskLibText         | 删除内容审核预设风险文本库           | 接口级   | *                                                            |
| DeleteRiskLibImage        | 删除内容审核预设风险图库中的图片     | 接口级   | *                                                            |
| CreateRiskLibText         | 在内容审核预设风险文本库中添加关键词 | 接口级   | *                                                            |
| CreateRiskLibImage        | 在内容审核预设风险图库中添加图片     | 接口级   | *                                                            |
| CreateAuditingVirusJob    | 创建云查毒任务                       | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/${bucket}/*            |

### 媒体处理

| 接口名              | 接口描述               | 授权粒度 | 资源六段式                                                   |
| :------------------ | ---------------------- | :------- | :----------------------------------------------------------- |
| CreateMediaBucket   | 开通存储桶媒体处理功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaBucket   | 关闭存储桶媒体处理功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaTemplate | 创建媒体处理模板       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaTemplate | 更新媒体处理模板       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaTemplate | 删除媒体处理模板       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaQueue    | 更新媒体处理队列       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaJobs     | 创建媒体处理任务       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CancelMediaJob      | 取消媒体处理任务       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| GenerateSnapshot    | 生成视频截帧           | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| GenerateMediaInfo   | 查看视频信息           | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaWorkflow | 删除工作流             | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaWorkflow | 更新工作流             | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaWorkflow | 创建工作流             | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### 图片处理

| 接口名                      | 接口描述            | 授权粒度 | 资源六段式                                                   |
| :-------------------------- | ------------------- | :------- | :----------------------------------------------------------- |
| SetImageGuetzli             | 开启图片 Guetzli 压缩 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetImageAdvancedCompression | 开启图片高级压缩    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetImageBlindWatermark      | 开启图片盲水印      | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetImageStyleSeparator      | 设置图片样式分隔符  | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SetImageStyle               | 设置图片样式        | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |


### 文档处理

| 接口名                 | 接口描述               | 授权粒度 | 资源六段式                                                   |
| :--------------------- | ---------------------- | :------- | :----------------------------------------------------------- |
| CreateDocProcessBucket | 开通存储桶文档预览功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateDocProcessQueue  | 更新文档预览队列       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteDocProcessBucket | 关闭存储桶文档预览功能 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CancelDocProcessJob    | 取消文档预览任务       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateDocProcessJobs   | 创建文档预览任务       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### AI 内容识别

| 接口名                       | 接口描述                        | 授权粒度 | 资源六段式                                                   |
| :--------------------------- | ------------------------------- | :------- | :----------------------------------------------------------- |
| CreateDetectQRcodeJob        | 调用二维码识别接口              | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateDetectLabelJob         | 调用图片标签识别接口            | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateFaceEffectJob          | 调用人脸特效接口                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateAsrQueue               | 更新语音识别队列                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteAsrBucket              | 关闭存储桶语音识别功能          | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateAsrBucket              | 开通存储桶语音识别功能          | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateAsrJobs                | 创建语音识别任务                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateGetActionSequenceJob   | 调用人脸核身-获取动作顺序接口   | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateGetLiveCodeJob         | 调用人脸核身-获取数字验证码接口 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateLivenessRecognitionJob | 调用人脸核身接口                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateIDCardOCRJob           | 调用身份证识别接口              | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateQRcodeGenerateJob      | 调用二维码生成接口              | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| TriggerMediaWorkflow         | 触发工作流                      | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreatePetDetectJob           | 调用宠物识别接口                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteImage                  | 删除以图搜图图库中的图片        | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| AddImage                     | 添加图片至以图搜图图库          | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateImageSearchBucket      | 开通存储桶为以图搜图的图库      | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateContentAnalysisJob     | 调用图片标签识别接口            | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateBodyJointsDetectJob    | 调用人体关键点分析接口          | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateOCRJob                 | 调用图片 OCR 识别接口             | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateLicensePlateJob        | 调用车牌识别接口                | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| CreateDetectFaceJob          | 调用人脸检测接口                | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateAssessQualityJob       | 调用图片质量分析接口            | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| CreateAiRecognitionJob       | 调用 AI 多合一接口                | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| CreateEnhanceImageJob        | 调用图片清晰度增强接口          | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/${bucket}/*            |
| CancelPicProcessJob          | 取消图片处理任务                | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| CreatePicProcessJobs         | 创建图片处理任务                | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| UpdatePicProcessQueue        | 更新图片处理任务队列            | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DeletePicProcessBucket       | 关闭存储桶图片处理任务功能      | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| CreatePicProcessBucket       | 开通存储桶图片处理任务功能      | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |

## 读操作

### 基础功能

| 接口名                | 接口描述                         | 授权粒度 | 资源六段式                                                   |
| :-------------------- | -------------------------------- | :------- | :----------------------------------------------------------- |
| DescribeCIBuckets     | 查看存储桶绑定数据万象的状态     | 接口级   | *                                                            |
| DescribeDomain        | 查看数据万象域名信息            | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeOriginProtect | 查询数据万象原图保护功能开通状态 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeCDNAccelerate | 查询数据万象 CDN 加速域名绑定状态  | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| Describe4XXResponse   | 查询数据万象4xx图片配置状态      | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeRefer         | 查询数据万象存储桶防盗链状态     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### 内容审核

| 接口名                        | 接口描述                     | 授权粒度 | 资源六段式                                                   |
| :---------------------------- | ---------------------------- | :------- | :----------------------------------------------------------- |
| DescribeAuditingJobs          | 查看视频审核任务             | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingVideo         | 查看是否开启视频自动审核     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingAudio         | 查看是否开启音频自动审核     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingPicture       | 查看是否开启图片自动审核     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingText          | 查看是否开启文本自动审核     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingDocument      | 查看是否开启文档自动审核     | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DescribeAuditingCallback      | 查询内容审核回调设置接口权限 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingBlockRule     | 查看内容审核冻结规则接口权限 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingPictureFiles  | 查询图片审核文件列表         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingVideoFiles    | 查询视频审核文件列表         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingAudioFiles    | 查询音频审核文件列表         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingTextFiles     | 查询文本审核文件列表         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingExistTasks    | 查看历史数据审核任务         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingTextJob       | 查看文本审核任务结果         | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAuditingAudioJob      | 查看音频审核任务结果         | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| DescribeAuditingDocumentJob   | 查看文档审核任务结果         | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/examplebucket-1250000000/* |
| DescribeAuditingWebpageJob    | 查看网页审核任务结果         | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/${bucket}/*            |
| DescribeAuditingDocumentFiles | 查看文档审核任务结果         | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DescribeAuditingVirusJob      | 查看云查毒任务结果           | 资源级   | qcs::ci:${region}:uid/${appid}:bucket/${bucket}/*            |

### 媒体处理

| 接口名                          | 接口描述             | 授权粒度 | 资源六段式                                                   |
| :------------------------------ | -------------------- | :------- | :----------------------------------------------------------- |
| DescribeMediaTemplates          | 查看媒体处理模板     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaQueues             | 查看媒体处理队列     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaJob                | 查看媒体处理任务     | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaJobs               | 查看媒体处理任务列表 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaWorkflowExecutions | 查看工作流执行实例   | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaWorkflows          | 查看工作流状态       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| GetPrivateM3U8                  | 生成私有m3u8视频     | 接口级   | *                                                            |
| GenerateMediaInfo               | 获取媒体信息    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| GenerateSnapshot               | 调用截帧任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| ModifyM3U8Token                 | 刷新 hls 加密 token    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaTemplate             | 创建媒体处理模板    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaTemplate             | 更新媒体处理模板    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaTemplate             | 删除媒体处理模板    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaWorkflow             | 创建媒体处理工作流    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaWorkflow             | 更新媒体处理工作流    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaWorkflow             | 删除媒体处理工作流    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| TriggerMediaWorkflow            | 触发媒体处理工作流    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateMediaQueue                | 更新媒体处理队列    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| AddMediaQueue                   | 添加媒体处理队列    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaBucket               | 绑定媒体处理服务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeMediaBuckets            | 查询媒体处理服务状态    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DeleteMediaBucket               | 解绑媒体处理服务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateMediaJobs                 | 提交媒体处理任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CancelMediaJob                  | 取消媒体处理任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateInventoryTriggerJob       | 发起媒体处理批量任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeInventoryTriggerJob     | 查询媒体处理批量任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeInventoryTriggerJobs    | 批量拉取批量任务状态    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CancelInventoryTriggerJob       | 取消批量处理任务    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| UpdateSpeedTranscodingProcessQueue  | 更新倍速转码队列    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeSpeedTranscodingProcessQueues | 查询倍速转码队列    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| CreateSpeedTranscodingProcessQueues   | 创建倍速转码队列    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### 图片处理

| 接口名                           | 接口描述                          | 授权粒度 | 资源六段式                                                   |
| :------------------------------- | --------------------------------- | :------- | :----------------------------------------------------------- |
| DescribeImageGuetzli             | 查看存储桶图片 Gurtzli 压缩开通状态 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeImageAdvancedCompression | 查看存储桶图片高级压缩开通状态    | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeImageBlindWatermark      | 查看存储桶盲水印开通状态          | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeImageStyleSeparator      | 查看图片样式分隔符                | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeImageStyles              | 查看图片样式                      | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### 文档处理

| 接口名                   | 接口描述                   | 授权粒度 | 资源六段式                                                   |
| :----------------------- | -------------------------- | :------- | :----------------------------------------------------------- |
| DescribeDocProcessQueues | 查看文档预览队列           | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeDocProcessBucket | 查看存储桶文档预览开通状态 | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeDocProcessJobs   | 查看文档预览任务列表       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeDocProcessJob    | 查看文档预览任务           | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |

### AI 内容识别

| 接口名                   | 接口描述                       | 授权粒度 | 资源六段式                                                   |
| :----------------------- | ------------------------------ | :------- | :----------------------------------------------------------- |
| DescribeAsrQueues        | 查看语音识别队列               | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAsrBuckets       | 查看存储桶语音识别功能开通状态 | 接口级   | *                                                            |
| DescribeAsrJobs          | 查看语音识别任务               | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribeAsrJob           | 查看语音识别任务列表           | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| SearchImage              | 搜索以图搜图图库中的图片       | 资源级   | qcs::ci:ap-shanghai:uid/1250000000:bucket/examplebucket-1250000000/* |
| DescribePicProcessJobs   | 查看图片处理任务列表           | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DescribePicProcessJob    | 查看图片处理任务               | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DescribePicProcessQueues | 查看图片处理队列               | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
| DescribePicProcessBucket | 查看图片处理存储桶列表         | 资源级   | qcs::ci::uid/${appid}:bucket/examplebucket-1250000000/*        |
