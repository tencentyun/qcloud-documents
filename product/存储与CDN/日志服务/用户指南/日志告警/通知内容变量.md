用户配置自定义告警内容时可以插入系统变量，告警发送时系统将自动解析变量。

## 变量列表

| 变量                     | 说明               |
|--------------------------|------------------|
| {{.UIN}}                  | 用户账户           |
| {{.Nickname}}             | 用户名称           |
| {{.AlertID}}              | 告警策略 ID         |
| {{.AlertName}}            | 告警策略名称       |
| {{.Trigger}}              | 触发条件           |
| {{.HappenThreshold}}      | 连续触发次数       |
| {{.AlertThreshold}}       | 告警间隔时间       |
| {{.Region}}               | 地域               |
| {{.NotifyTime}}           | 通知时间           |
| {{.ConsecutiveAlertNums}} | 连续告警次数       |
| {{.TopicName}}            | 日志主题名称       |
| {{.TopicId}}              | 日志主题 ID         |
| {{.LogsetName}}           | 日志集名称         |
| {{.LogsetId}}             | 日志集 ID           |
| {{.FireTime}}             | 第一次告警触发时间 |
| {{.Duration}}             | 告警持续时间       |
| {{.TriggerParams}}        | 告警触发时参数     |
| {{.Query}}                | 监控语句           |
| {{.DetailUrl}}   | 免登录详情页面链接   |
| {{.QueryUrl}}   | 第一个查询语句的检索链接   |
| {{.AlertHistoryUrl}}   | 告警历史记录查询链接   |
