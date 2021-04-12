语音识别（ASR）支持资源级授权、按标签授权两种方式。
- 资源级授权：您可以通过策略语法给子账号单个资源的管理的权限。
- 按标签授权：您可以通过给资源标记标签，实现给子账号对应的标签下资源的管理权限。

## 资源级授权的 API 列表
ASR 支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

支持资源级授权的接口列表如下（列表请按升序排列）：

| API 名 | API 描述 | 资源类型 | 资源六段式示例 |
|---------|---------|---------|---------|
| DeleteAsrVocab | 删除热词表 | 热词表 | `qcs::asr::uin/$account:vocab/$VocabId` |
| DeleteCustomization | 删除自学习模型 | 自学习模型 | `qcs::asr::uin/$account:model/$ModelId` |
| DeleteModelsByAppid | 根据 AppId 删除自学习模型 | 自学习模型 | `qcs::asr::uin/$account:model/$ModelId` |
| DownloadAsrVocab | 下载热词表 | 热词表 | `qcs::asr::uin/$account:vocab/$VocabId` |
| DownloadCustomization | 下载自学习模型语料 | 自学习模型 | `qcs::asr::uin/$account:model/$ModelId` |
| GetAsrVocab | 获取热词表 | 热词表 | `qcs::asr::uin/$account:vocab/$VocabId` |
| GetAsrVocabList | 获取热词表列表 | 热词表 | `qcs::asr::uin/$account:vocab/*` |
| GetCustomizationList | 获取自学习列表 | 自学习模型 | `qcs::asr::uin/$account:model/*` |
| ModifyCustomization | 修改自学习模型 | 自学习模型 | `qcs::asr::uin/$account:model/$ModelId` |
| ModifyCustomizationState | 修改自学习模型状态 | 自学习模型 | `qcs::asr::uin/$account:model/$ModelId` |
| SetVocabState | 设置热词表状态 | 热词表 | `qcs::asr::uin/$account:vocab/$VocabId` |
| UpdateAsrVocab | 更新热词表 | 热词表 | `qcs::asr::uin/$account:vocab/$VocabId` |


## 接口级授权的 API 列表
针对支持操作级权限的 API 操作，您仍可以向用户授予使用该操作的权限，但是策略语句的资源元素必须指定为 * 。

| API 名 | API 描述 |
|---------|---------|
| CreateAsrUser | 为用户开通 ASR 服务 |
| CreateAsrVocab | 创建热词表 |
| CreateCustomization | 创建自学习模型 |
| CreateRecTask | 录音文件识别 |
| DescribeResource | 查询资源包 |
| DescribeStatistics | 查询统计数据 |
| DescribeTaskStatus | 查询录音文件识别任务状态 |
| DescribeUserStatus | 查询用户 ASR 服务开通状态 |
| RealtimeRecognition | 实时识别 |
| SentenceRecognition | 一句话识别 |
| StartStreamTranscription | 国际语音识别 |
