云数据库 MySQL 于北京时间2018年01月01日全面升级了 API 接口服务至 3.0 版本，当前基于 API 2.0 版本接口访问的时延较高且使用较复杂考虑，云数据库 MySQL 的 API 2.0 版本接口服务将不再提供技术支持，并将于北京时间2023年03月31日起下线。

如果您的业务还在使用云数据库 MySQL 的 API 2.0 版本相关接口，建议尽快将服务升级至云数据库 MySQL API 3.0 版本，以免对您的业务造成影响。

使用 API 3.0 版本接口服务时，建议使用 [云产品 SDK 中心](https://cloud.tencent.com/document/sdk)，获取到 API 3.0 版本配套的多种编程语言的 SDK，[API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cdb&Version=2017-03-20&Action=DescribeDBInstances) 可以直接生成 SDK 的调用代码，方便您实现代码调用。

请您参照下方的 API 2.0 切换 3.0 接口表找到您需要升级的新接口，完成升级。

## API 2.0 切换 3.0 接口列表
<table>
<thead><tr><th>API 2.0 接口</td><th>API 3.0 接口</td><th>API 3.0 文档</td><th>接口传参变化</td></tr></thead>
<tbody>
<tr>
<td>DescribeCdbInstances</td>
 <td>DescribeDBInstances</td>
 <td>查询实例列表 <a href="https://cloud.tencent.com/document/api/236/15872">单击了解</a>。</td>
 <td>为降低使用复杂度，部分参数有变化，请参考相关 <a href="https://cloud.tencent.com/document/api/236/15872">API 文档</a>。</td>
 </tr>
 <tr>
<td>QueryCdbStatisticsInfo</td>
 <td>GetAppStat</td>
 <td>下线该接口，停止调用，如需获取实例监控信息，可以调用 GetMonitorData 接口获取<a href="https://cloud.tencent.com/document/product/248/31014"> 单击了解</a>。</td>
 <td>接口传参无变化。</td>
 </tr>
 <tr>
<td>DescribeDBInstancesV3</td>
 <td>DescribeDBInstances</td>
 <td>查询实例列表 <a href="https://cloud.tencent.com/document/api/236/15872">单击了解</a>。</td>
  <td>接口传参无变化。</td>
 </tr>
 <tr>
<td>GetCdbExportLogUrl</td>
 <td>GetDownloadUrl</td>
 <td>该接口可通过现网接口进行替换<br><li>type = slowlog_day 查询慢日志 DescribeSlowLogs <a href="https://cloud.tencent.com/document/product/236/15845">单击了解</a>。<br><li>type = errlog_day 查询实例错误日志 DescribeErrorLogData <a href="https://cloud.tencent.com/document/product/236/43041">单击了解</a>。<br><li>type = coldbackup 查询数据备份列表 DescribeBackups <a href="https://cloud.tencent.com/document/product/236/15842">单击了解</a>。<br><li>type = binlog 查询日志备份列表 DescribeBinlogs <a href="https://cloud.tencent.com/document/product/236/15843">单击了解</a>。</td>
   <td>为降低使用复杂度，部分参数有变化，请参考相关 API 文档：<li><a href="https://cloud.tencent.com/document/product/236/15845">查询慢日志</a>。<li><a href="https://cloud.tencent.com/document/product/236/43041">查询实例错误日志</a>。<li><a href="https://cloud.tencent.com/document/product/236/15842">查询数据备份列表</a>。<li><a href="https://cloud.tencent.com/document/product/236/15843">查询日志备份列表</a>。</td>
 </tr>
 <tr>
<td>RenewCdb</td>
 <td>RenewDBInstance</td>
 <td>续费云数据库实例 <a href="https://cloud.tencent.com/document/api/236/30160">单击了解</a>。</td>
 <td>为降低使用复杂度，部分参数有变化，请参考相关 <a href="https://cloud.tencent.com/document/api/236/30160">API 文档</a>。</td>
 </tr>
</tbody></table>

