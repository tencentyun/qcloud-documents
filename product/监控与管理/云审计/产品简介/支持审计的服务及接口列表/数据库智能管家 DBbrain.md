## 健康报告邮件发送相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57811">AddUserContact</a></td>
    <td>添加联系人信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57802">CreateDBDiagReportTask</a></td>
    <td>创建健康报告生成任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57810">CreateDBDiagReportUrl</a></td>
    <td>创建健康报告浏览地址</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57809">CreateMailProfile</a></td>
    <td>创建邮件配置</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57808">CreateSchedulerMailProfile</a></td>
    <td>创建定期生成的邮件发送配置</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57807">DescribeAllUserContact</a></td>
    <td>获取邮件发送中联系人信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57806">DescribeAllUserGroup</a></td>
    <td>获取邮件发送中联系组信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57805">DescribeDBDiagReportTasks</a></td>
    <td>查询健康报告生成任务列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57804">DescribeMailProfile</a></td>
    <td>获取邮件配置</td>
  </tr>
</tbody>
</table>

## kill 会话相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72836">CancelKillTask</a></td>
    <td>终止中断会话任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/67783">CreateKillTask</a></td>
    <td>创建中断会话的任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/67782">CreateProxySessionKillTask</a></td>
    <td>创建中止代理节点会话的任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/69205">DescribeProxySessionKillTasks</a></td>
    <td>查询代理节点 kill 会话任务执行状态</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/61129">KillMySqlThreads</a></td>
    <td>中断MySql会话线程</td>
  </tr>
</tbody>
</table>

## 安全审计相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57801">CreateSecurityAuditLogExportTask</a></td>
    <td>创建安全审计日志导出任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57800">DeleteSecurityAuditLogExportTasks</a></td>
    <td>删除安全审计日志导出任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57796">DescribeSecurityAuditLogDownloadUrls</a></td>
    <td>查询安全审计日志导出文件下载链接</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57795">DescribeSecurityAuditLogExportTasks</a></td>
    <td>查询安全审计日志导出任务列表</td>
  </tr>
</tbody>
</table>

## 其他接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57798">DescribeDiagDBInstances</a></td>
    <td>获取实例信息列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57797">DescribeHealthScore</a></td>
    <td>获取健康得分</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57824">DescribeMySqlProcessList</a></td>
    <td>查询实时线程列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72833">DescribeNoPrimaryKeyTables</a></td>
    <td>查询实例无主键表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72832">DescribeRedisTopBigKeys</a></td>
    <td>查询redis实例大key列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/80213">DescribeRedisTopKeyPrefixList</a></td>
    <td>查询redis实例top key前缀列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72830">DescribeSqlTemplate</a></td>
    <td>查询SQL模板</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57790">ModifyDiagDBInstanceConf</a></td>
    <td>修改实例巡检开关状态</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72828">VerifyUserAccount</a></td>
    <td>验证用户数据库账号权限</td>
  </tr>
</tbody>
</table>

## 慢日志分析相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57785">DescribeSlowLogTimeSeriesStats</a></td>
    <td>获取慢日志统计柱状图</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57784">DescribeSlowLogTopSqls</a></td>
    <td>按照Sql模板查询指定时间段内的慢日志统计结果</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57783">DescribeSlowLogUserHostStats</a></td>
    <td>获取慢日志来源地址统计分布图</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57782">DescribeUserSqlAdvice</a></td>
    <td>获取SQL优化建议</td>
  </tr>
</tbody>
</table>

## SQL限流相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72835">CreateSqlFilter</a></td>
    <td>创建实例SQL限流任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72834">DeleteSqlFilters</a></td>
    <td>删除实例SQL限流任务</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72831">DescribeSqlFilters</a></td>
    <td>查询实例SQL限流任务列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/72829">ModifySqlFilters</a></td>
    <td>更改实例限流任务状态</td>
  </tr>
</tbody>
</table>

## 异常检测相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57788">DescribeDBDiagEvent</a></td>
    <td>获取诊断事件详情</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/65947">DescribeDBDiagEvents</a></td>
    <td>获取诊断事件列表</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57787">DescribeDBDiagHistory</a></td>
    <td>获取实例诊断历史</td>
  </tr>
</tbody>
</table>

## 空间分析相关接口
<table>
<thead>
  <tr>
    <th>接口名称</th>
    <th>接口功能</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57799">DescribeDBSpaceStatus</a></td>
    <td>获取指定时间段内的实例空间使用概览</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57794">DescribeTopSpaceSchemaTimeSeries</a></td>
    <td>获取Top库在指定时间段内的每日空间统计信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57793">DescribeTopSpaceSchemas</a></td>
    <td>获取Top库的空间统计信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57792">DescribeTopSpaceTableTimeSeries</a></td>
    <td>获取Top表在指定时间段内的每日空间统计信息</td>
  </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/1130/57791">DescribeTopSpaceTables</a></td>
    <td>获取Top表的空间统计信息</td>
  </tr>
</tbody>
</table>
