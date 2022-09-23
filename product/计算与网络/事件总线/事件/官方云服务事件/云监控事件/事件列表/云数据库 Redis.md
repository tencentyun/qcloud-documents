
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
      <td class="div-td-1">主备切换</td>
      <td class="div-td-2 div-td-el">MasterSlaveSwitched</td>
      <td class="div-td-3">状态<br>变更</td>
      <td class="div-td-4">云数据库 Redis 实例维度</td>
      <td class="div-td-5">无</td>
      <td class="div-td-6">云数据库 Redis 发生故障切换</td>
      <td class="div-td-7">故障会导致连接 Redis 服务的访问断开和短暂的不可用，请关注业务是否有自动重连机制，以确保业务快速恢复</td>
   </tr>
   <tr>
      <td class="div-td-1">服务不可用</td>
      <td class="div-td-2 div-td-el">ServiceNotAvailable</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 Redis 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">云数据库 Redis 发生故障导致服务不可用</td>
      <td class="div-td-7">我们将第一时间恢复服务，并且发送服务恢复通知，如果您有灾备实例，请尝试将业务切换到灾备实例</td>
   </tr>
   <tr>
      <td class="div-td-1">只读副本故障切换</td>
      <td class="div-td-2 div-td-el">ReadonlyReplicaSwitched</td>
      <td class="div-td-3">状态<br>变更</td>
      <td class="div-td-4">云数据库 Redis 实例维度</td>
      <td class="div-td-5">无</td>
      <td class="div-td-6">云数据库 Redis 发生只读副本故障切换</td>
      <td class="div-td-7">我们将第一时间恢复服务，并且发送服务恢复通知，如果您有灾备实例，请尝试将业务切换到灾备实例，或者新增只读副本</td>
   </tr>
   <tr>
      <td class="div-td-1">只读副本不可用</td>
      <td class="div-td-2 div-td-el">ReadonlyReplicaNotAvailable</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 Redis 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">云数据库 Redis 发生只读副本故障</td>
      <td class="div-td-7">我们将第一时间恢复服务，并且发送服务恢复通知，如果您有灾备实例，请尝试将业务切换到灾备实例，或者新增只读副本
      </td>
   </tr>
</tbody>
</table>
