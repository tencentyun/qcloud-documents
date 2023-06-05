本文为您介绍云数据库 SQL Server 各版本的功能概览以及差异。

## 各版本功能概览及差异列表
<table>
<tr><td width=10% rowspan=2>模块</td><td width=15% rowspan=2>功能</th><td width=30%>双节点（原高可用版及集群版）</td><td width=30%>单节点（原基础版）</td></tr>
<tr>
<td>2008R2 Enterprise<br>2012 Standard/Enterprise<br>2014 Standard/Enterprise<br>2016 Standard/Enterprise<br>2017 Standard/Enterprise<br>2019 Standard/Enterprise</td>
<td>2008R2 Enterprise<br>2012 Enterprise<br>2014 Enterprise<br>2016 Enterprise<br>2017 Enterprise<br>2019 Enterprise</td></tr>
<tr>
<td rowspan=11>生命周期</td>
<td>创建实例</td><td rowspan=11>支持</td><td rowspan=11>支持</td></tr>
<tr><td>重启实例</td></tr>
<tr><td>自动续费</td></tr>
<tr><td>变更计费方式</td></tr>
<tr><td>销毁实例</td></tr>
<tr><td>创建只读实例</td></tr>
<tr><td>发布/订阅</td></tr>
<tr><td>规格升降配</td></tr>
<tr><td>磁盘扩缩容</td></tr>
<tr><td>版本升级</td></tr>
<tr><td>架构升级</td></tr>
<tr>
<td rowspan=7>实例属性</td>
<td>查看实例列表</td><td rowspan=7>支持</td><td rowspan=7>支持</td></tr>
<tr><td>查看实例详情</td></tr>
<tr><td>修改实例名</td></tr>
<tr><td>修改实例备注</td></tr>
<tr><td>设置实例标签</td></tr>
<tr><td>管理可维护时间</td></tr>
<tr><td>管理项目</td></tr>
<tr>
<td rowspan=5>服务可用性</td>
<td>高可用方式</td><td><li>版本 SQL Server 2008R2/2012/2014/2016 Enterprise，SQL Server 2012/2014/2016 Standard 采用 Mirror HA<li>版本 SQL Server 2017/2019 Enterprise 采用 Always On 高可用</td><td>计算节点迁移 + 硬盘快照</td></tr>
<tr><td>跨可用区内容灾</td><td>支持</td><td>不支持</td></tr>
<tr><td>同城容灾</td><td>支持</td><td>不支持</td></tr>
<tr><td>只读实例剔除</td><td>支持</td><td>不支持</td></tr>
<tr><td>跨可用区迁移</td><td>支持</td><td>不支持</td></tr>
<tr>
<td rowspan=19>备份与恢复</td>
<td>全量备份</td><td rowspan=18>支持</td><td rowspan=18>支持</td></tr>
<tr><td>数据备份</td></tr>
<tr><td>增量备份</td></tr>
<tr><td>日志备份</td></tr>
<tr><td>定时备份</td></tr>
<tr><td>手动备份</td></tr>
<tr><td>打包备份</td></tr>
<tr><td>单库备份</td></tr>
<tr><td>实例备份</td></tr>
<tr><td>多库备份</td></tr>
<tr><td>定制备份策略</td></tr>
<tr><td>按备份集恢复</td></tr>
<tr><td>按时间点恢复</td></tr>
<tr><td>按用户备份集恢复</td></tr>
<tr><td>回档至当前实例</td></tr>
<tr><td>回档至已有实例（同地域）</td></tr>
<tr><td>回档至已有实例（跨地域）</td></tr>
<tr><td>备份下载</td></tr>
<td>备实例执行备份任务</td><td><li>版本 SQL Server 2008R2/2012/2014/2016 Enterprise，SQL Server 2012/2014/2016 Standard 不支持<li>版本 SQL Server 2017/2019 Enterprise 支持</td><td>不支持</td></tr>
<tr>
<td rowspan=5>监控与报警</td>
<td>资源监控</td><td rowspan=3>支持</td><td >支持</td></tr>
<tr><td>引擎监控</td><td >支持</td></tr>
<tr><td>秒级监控</td><td >不支持（1分钟粒度）</td></tr>
<tr><td>监控策略定制</td><td>不支持</td><td>支持</td></tr>
<tr><td>告警</td><td>支持</td><td>支持</td></tr>
<tr>
<td rowspan=5>账号管理</td>
<td>创建和删除账号</td><td rowspan=4>支持</td><td rowspan=4>支持</td></tr>
<tr><td>普通账号</td></tr>
<tr><td>高级权限账号</td></tr>
<tr><td>特殊权限账号</td></tr>
<tr><td>超级权限账号</td><td>不支持</td><td>支持</td></tr>
<td rowspan=7>数据库管理</td>
<td>创建数据库</td><td rowspan=7>支持</td><td rowspan=7>支持</td></tr>
<tr><td>删除数据库</td></tr>
<tr><td>克隆数据库</td></tr>
<tr><td>数据库授权</td></tr>
<tr><td>变更数据捕获 CDC</td></tr>
<tr><td>更改跟踪 CT</td></tr>
<tr><td>收缩数据库</td>
<tr>
<td rowspan=4>数据安全</td>
<td>安全组</td><td>支持</td><td>支持</td></tr>
<tr><td>数据库审计</td><td rowspan=2>暂不支持</td><td rowspan=3>不支持</td></tr>
<tr><td>网络加密</td></tr>
<tr><td>TDE 加密</td><td>支持</td></tr>
<tr>
<td rowspan=4>数据通道</td>
<td>数据同步</td><td>暂不支持</td><td>暂不支持</td></tr>
<tr><td>同构数据迁移</td><td>支持</td><td>支持</td></tr>
<tr><td>异构数据迁移</td><td >不支持</td><td rowspan=2>不支持</td></tr>
<tr><td>发布订阅</td><td>支持</td></tr>
<tr>
<td rowspan=4>日志管理</td>
<td>错误日志</td><td>不支持</td><td>不支持</td></tr>
<tr><td>慢日志</td><td>支持</td><td>支持</td></tr>
<tr><td>运行日志</td><td>不支持</td><td>不支持</td></tr>
<tr><td>阻塞及死锁事件</td><td>版本 SQL Server 2012/2014/2016/2017/2019 Enterprise 支持</td><td>版本 SQL Server 2012/2014/2016/2017/2019 Enterprise 支持</td></tr>
<tr>
<td rowspan=3>参数管理</td>
<td>参数更新</td><td rowspan=2>支持</td><td rowspan=2>支持</td></tr>
<tr><td>参数历史</td></tr>
<tr><td>参数模板</td><td>不支持</td><td>不支持</td></tr>
<tr>
<td rowspan=3>性能优化</td>
<td>专家服务</td><td>支持</td><td>支持</td></tr>
<tr><td>资源分析</td><td rowspan=2>不支持</td><td rowspan=2>不支持</td></tr>
<tr><td>引擎分析</td></tr>
<tr>
<td rowspan=3>网络</td>
<td>基础网络</td><td rowspan=2>支持</td><td rowspan=2>支持</td></tr>
<tr><td>私有网络</td></tr>
<tr><td>公网地址</td><td>支持</td><td>支持</td></tr>
</tbody></table>