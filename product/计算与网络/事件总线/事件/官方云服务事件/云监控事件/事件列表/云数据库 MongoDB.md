
由客户云上购买和使用的资源实例与产品产生的监控事件包括：


<style type="text/css">
.div-table-1 {width:100%;}
.div-table-1 td{white-space:pre-wrap; }
.div-td-el{word-wrap:break-word;word-break:break-all;}
.div-td-1{width:12%}
.div-td-2{width:12%}
.div-td-3{width:8%}
.div-td-4{width:12%}
.div-td-5{width:8%}
.div-td-6{width:20%}
.div-td-7{width:28%}
</style>



<table class="div-table-1">
<thead>
	<tr>
      <th class="div-td-1">事件<br>中文名称</th>
      <th class="div-td-2">事件<br>英文名称</th>
      <th class="div-td-3">事件<br>类型</th>
      <th class="div-td-4">从属维度</th>
      <th class="div-td-5">有无<br>恢复概念</th>
      <th class="div-td-6">事件描述</th>
      <th class="div-td-7">处理方法和建议</th>
	</tr>
	</thead>
	<tbody>
	<tr>
      <td class="div-td-1">备份 oplog 不足</td>
      <td class="div-td-2 div-td-el">oplogInsufficient</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">无</td>
      <td class="div-td-6">云数据库 MongoDB 在备份时，无法读取到上次备份到本次备份的完整 oplog，这将影响您的数据库回档到 7 天内的任意时间点 </td>
			<td class="div-td-7">建议在 <a href="https://console.cloud.tencent.com/mongodb">MongoDB 控制台</a> 调整云数据库 MongoDB oplog 的大小或备份频率；如您不需要该事件通知，可以在 <a href="https://console.cloud.tencent.com/mongodb">MongoDB 控制台</a> 备份界面进行设置以关闭该事件通知</td>
    </tr>
    <tr>
      <td class="div-td-1">连接数超限</td>
      <td class="div-td-2 div-td-el">connectionOverlimit</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">实例连接数使用超过限制</td>
      <td class="div-td-7">评估当前实例所配置连接数是否满足业务需求，如果需要更大的连接配置建议，升级腾讯云 MongoDB 数据库实例配置</td>
    </tr>
    <tr>
      <td class="div-td-1">主从切换</td>
      <td class="div-td-2 div-td-el">primarywitch</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">实例 Primary 和 Secondary 切换</td>
      <td class="div-td-7">当物理机故障时可能会触发该事件，请确认实例状态是否正常</td>
    </tr>
    <tr>
      <td class="div-td-1">磁盘空间已耗尽</td>
      <td class="div-td-2 div-td-el">instanceOutOfDisk </td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">磁盘空间写满，造成实例只读</td>
      <td class="div-td-7">清理磁盘空间</td>
    </tr>
    <tr>
      <td class="div-td-1">实例 Rollback </td>
      <td class="div-td-2 div-td-el">instanceRollback </td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">实例数据 rollback</td>
      <td class="div-td-7">当主节点有部分数据还没有及时同步到从节点时主节点故障并发生主从切换可能会触发该事件，请确认实例状态是否正常</td>
    </tr>
		<tr>
      <td class="div-td-1">节点 CPU 异常 </td>
      <td class="div-td-2 div-td-el">NodeCPUAbnormal</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MongoDB 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">集群中有任一节点 CPU 使用率达到 80%，即触发告警</td>
      <td class="div-td-7">单次告警仅代表实例有单个节点负载较高，可结合连接数和慢查询等其他实例运行状态升级综合评估，必要时升级腾讯云 MongoDB 数据库实例配置</td>
    </tr>
</tbody>
</table>
