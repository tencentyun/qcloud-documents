
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
      <td class="div-td-1">内存 OOM</td>
      <td class="div-td-2 div-td-el">OutOfMemory</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">数据库内存使用过载</td>
      <td class="div-td-7">评估当前数据库内存规格是否满足业务需求，如果需要更大的内存建议升级 MySQL 的内存配置</td>
   </tr>
   <tr>
      <td class="div-td-1">主从切换</td>
      <td class="div-td-2 div-td-el">Switch</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">无</td>
      <td class="div-td-6">主实例和从实例发生切换</td>
      <td class="div-td-7">当物理机故障时可能会触发该事件，请确认实例状态是否正常</td>
   </tr>
   <tr>
      <td class="div-td-1">只读实例剔除</td>
      <td class="div-td-2 div-td-el">RORemoval</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">只读实例故障或超过延迟阈值</td>
      <td class="div-td-7">若只读组仅一个只读实例，只读实例被剔除后，请及时对读流量进行切换，避免因只读实例出现单点故障，建议为只读组至少购买两个只读实例</td>
   </tr>
   <tr>
      <td class="div-td-1">服务器故障导致实例迁移</td>
      <td class="div-td-2 div-td-el">ServerfailureInstanceMigration</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">服务器故障发起的实例迁移</td>
      <td class="div-td-7">迁移切换时间以维护时间窗为准，若需要更改切换时间，请及时调整，切换时间将以调整后的维护时间窗为准
      </td>
   </tr>
	    <tr>
      <td class="div-td-1">审计功能关闭</td>
      <td class="div-td-2 div-td-el">Auditclose</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">无</td>
      <td class="div-td-6">该事件已废弃，不再使用</td>
      <td class="div-td-7">该事件已废弃，不再使用 </td>
   </tr>
	    <tr>
      <td class="div-td-1">实例复制状态</td>
      <td class="div-td-2 div-td-el">InstRepStatus</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">RO 实例和主实例之间的主从同步是否正常，需配置 RO 实例</td>
      <td class="div-td-7">受限于只读实例的规格或主实例存在大事务易导致该异常。可以适当增加只读实例配置或减少大事务
      </td>
   </tr>
	    <tr>
      <td class="div-td-1">数据库代理挂载节点剔除</td>
      <td class="div-td-2 div-td-el">ProxyNodeRemoval</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">满足保留最小只读节点数以及延迟剔除时间的只读节点，由于延迟过大、出现异常无法连接、I/O 线程、SQL 线程异常，将只读节点剔除</td>
      <td class="div-td-7">若数据库代理仅有一个只读实例，只读实例被剔除后，避免因只读实例出现单点故障，建议为数据库代理至少配置两个只读实例
      </td>
   </tr>
	    <tr>
      <td class="div-td-1">数据库代理异常</td>
      <td class="div-td-2 div-td-el">ProxyNotAvailable</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">Proxy 代理节点出现故障，故障节点无法提供代理服务</td>
      <td class="div-td-7">当数据库代理异常后，无法通过数据库代理 VIP 访问数据库实例，请确保打开数据库代理故障转移能力
      </td>
   </tr>
		    <tr>
      <td class="div-td-1">实例只读（硬盘超限）     </td>
      <td class="div-td-2 div-td-el">Outofstorage</td>
      <td class="div-td-3">异常<br>事件</td>
      <td class="div-td-4">云数据库 MySQL 实例维度</td>
      <td class="div-td-5">有</td>
      <td class="div-td-6">数据库磁盘使用过载</td>
      <td class="div-td-7">评估当前数据库磁盘规格是否满足业务需求，如果需要更大的磁盘空间建议扩容 MySQL 的磁盘容量
      </td>
   </tr>
</tbody>
</table>
