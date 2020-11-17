数据库智能管家（TencentDB for DBbrain，DBbrain）是腾讯云推出的一款为用户提供数据库性能、安全、管理等功能的数据库自治云服务。DBbrain 利用机器学习、大数据手段、专家经验引擎快速复制资深数据库管理员的成熟经验，将大量传统手动的数据库运维工作自运维，服务于云上和云下企业，有效保障数据库服务的安全、稳定及高效运行。

下表为云审计支持的数据库智能管家操作列表：

| 操作名称                   | 资源类型    | 事件名称                                |
|------------------------|---------|-------------------------------------|
| 创建审计日志分析任务             | dbbrain | CreateAuditLogStatsTask             |
| 创建健康报告分析任务             | dbbrain | CreateDBDiagReportTask              |
| CreateDBDiagReportUrl  | dbbrain | CreateDBDiagReportUrl               |
| 删除审计日志分析任务             | dbbrain | DeleteAuditLogStatsTask             |
| 删除健康诊断报告分析任务           | dbbrain | DeleteDBDiagReportTasks             |
| 获取给定任务的时间轴统计图表数据 | dbbrain | DescribeAuditLogSeriesForSqlTime    |
| 获取当前任务列表               | dbbrain | DescribeAuditLogStatsTasks          |
| 获取给定任务的 Top SQL         | dbbrain | DescribeAuditLogTopSqls             |
| 获取异常诊断事件详情             | dbbrain | DescribeDBDiagEvent                 |
| 获取实例异常诊断历史             | dbbrain | DescribeDBDiagHistory               |
| 查询健康诊断报告               | dbbrain | DescribeDBDiagReport                |
| 获取实例性能曲线数据             | dbbrain | DescribeDBPerfTimeSeries            |
| 获取给定时间段空间使用概览          | dbbrain | DescribeDBSpaceStatus               |
| 获取健康打分详情               | dbbrain | DescribeHealthScore                 |
| 获取健康打分曲线               | dbbrain | DescribeHealthScoreTimeSeries       |
| 获取 Processlist          | dbbrain | DescribeProcessList                 |
| 获取慢日志柱状图统计             | dbbrain | DescribeSlowLogTimeSeriesStats      |
| 获取慢日志 TopSql 列表          | dbbrain | DescribeSlowLogTopSqls              |
| 创建审计日志分析任务             | dbbrain | DescribeSqlAdvice                   |
| 获取 SQL 执行计划              | dbbrain | DescribeSqlExplain                  |
| 获取 Top 库最新定时采集的空间数据      | dbbrain | DescribeTopSpaceSchemaLatestRecords |
| 获取 Top 库在指定时间段内的每日空间统计信息 | dbbrain | DescribeTopSpaceSchemaTimeSeries    |
| 获取 Top 表最新定时采集的空间数据      | dbbrain | DescribeTopSpaceTableLatestRecords  |
| 获取 Top 表的统计信息,默认按大小排序    | dbbrain | DescribeTopSpaceTables              |
| 获取 Top 表在指定时间段内的每日空间统计信息 | dbbrain | DescribeTopSpaceTableTimeSeries     |
