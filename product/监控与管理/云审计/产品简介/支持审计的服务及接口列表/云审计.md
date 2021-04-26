使用腾讯云云审计（CloudAudit），可以获取您腾讯云账号下 API 调用历史记录，包括通过腾讯云管理控制台，腾讯云 SDK，命令行工具和其他腾讯云服务进行的API调用，监控腾讯云中的任何部署行为。可以确定哪些子用户、协作者使用腾讯云 API 时，从哪个源 IP 地址进行调用，以及何时发生调用。您可以设置多个不同的跟踪集用以跟踪不同的日志，随时控制何时打开和关闭 CloudAudit 日志记录。

下表为云审计支持的云审计操作列表：

| 操作名称 | 资源类型 | 事件名称       |
|------|------|--------------|
| 检索日志 | ca   | LookUpEvents |
| 创建云审计               | cloudaudit | CreateAudit             |
| 删除云审计               | cloudaudit | DeleteAudit             |
| 获取事件的检索范围           | cloudaudit | GetEventNameSearchValue |
| GetSearchValueRange | cloudaudit | GetSearchValueRange     |
| 拉取云审计列表             | cloudaudit | ListAudits              |
| 检索日志                | cloudaudit | LookupEvents            |
| 检索日志                | cloudaudit | LookUpEvents            |
| 检索敏感操作记录            | cloudaudit | LookupSensitiveEvents   |
| 开启日志采集              | cloudaudit | StartLogging            |
| 关闭日志采集              | cloudaudit | StopLogging             |
| 更新云审计               | cloudaudit | UpdateAudit             |
