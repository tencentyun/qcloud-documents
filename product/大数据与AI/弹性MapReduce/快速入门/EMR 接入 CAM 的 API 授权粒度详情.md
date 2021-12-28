## 支持资源级授权的 API 列表
EMR 支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

>!不排除后续接口新增时出现操作报错，如遇到权限报错情况，可根据报错提示缺少对应接口权限进行策略中补充。

支持资源级授权的接口列表如下：
<table>
<thead>
<tr>
<th width="25%">API 名</th>
<th width="30%">API 描述</th>
<th width="45%">资源类型/资源六段式示例</th>
</tr>
</thead>
<tbody>
<tr>
<td >DescribeKeyTabFile</td>
<td >导出 Keytab 文件（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeShowUserManagerTab</td>
<td >是否显示用户管理的 Tab 页（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeResourceSchedule</td>
<td >获取 Yarn 资源调度页面的数据</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeCamUserList</td>
<td >查询 Cam 用户列表</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeClusterServiceInfo</td>
<td >查询服务信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeUserManagerUserList</td>
<td >查询用户列表（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyUserManagerPwd</td>
<td >修改用户密码（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResourcePools</td>
<td >刷新动态资源池</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteUserManagerUserList</td>
<td >删除用户列表（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResourceScheduler</td>
<td >修改了 Yarn 的资源调度器，点击部署生效</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResourceScheduleSwitch</td>
<td >开启开关后，需要同步资源调度的配置文件到资源调度器才能看见资源调度器的页面，才能进行页面的相关操作</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddUserManagerUserList</td>
<td >新增用户列表（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyUserManagerInfo</td>
<td >修改用户信息（用户管理）</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResourceScheduleConfig</td>
<td >修改 Yarn 资源调度的资源配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResourceScheduleConfigForRollback</td>
<td >取消保存 Yarn 资源调度的资源配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquirePriceRefundEmr</td>
<td >销毁节点退费金额查询</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeModifyPayModeNodes</td>
<td >集群按量转包年包月资源查询</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifySecurityGroup</td>
<td >修改集群安全组</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstanceRenewNodes</td>
<td >EMR 集群续费节点查询</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquirePriceRenewEmr</td>
<td >续费集群询价</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstancesList</td>
<td >EMR 集群实例列表查询</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyFlowStatus</td>
<td >修改流程状态</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyMasterIp</td>
<td >更新 ERM 集群 IP</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >CheckFlowCanBeCancelled</td>
<td >确认流程是否支持取消</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeModifySpec</td>
<td >查询变配规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddShellScriptTask</td>
<td >生成集群脚本任务</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeShellScriptTaskList</td>
<td >查询集群脚本任务列表</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeShellScriptNodes</td>
<td >查询单个集群脚本任务的节点列表</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeNodeList</td>
<td >查看节点信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeNodeList</td>
<td >查看节点信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeShellScriptNodeDetails</td>
<td >查询集群脚本任务的单个节点详细执行结果</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteShellScriptList</td>
<td >删除集群脚本任务记录</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeMasterIp</td>
<td >获取 ERM 集群实例 IP</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeEKSInstances</td>
<td >查询 TKE 集群接口信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddServiceConfFile</td>
<td >新增用户自定义配置文件</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteServiceConfFile</td>
<td >删除用户自定义配置文件</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyBootScript</td>
<td >修改引导脚本</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstanceAlias</td>
<td >获取别名</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeBootScript</td>
<td >获取引导脚本</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeSubJobFlowStatus</td>
<td >描述 EMR 子任务流程</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ListConfLogs</td>
<td >获取配置下发日志</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >GenerateScaleoutGoodsDetail</td>
<td >生成扩容订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >GenerateRenewGoodsDetail</td>
<td >生成续费订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >GenerateModifyGoodsDetail</td>
<td >生成变配订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyAutoScaleGlobalConf</td>
<td >更新自动扩缩容全局配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeFlowStatusDetail</td>
<td >查询 EMR 任务运行详情状态 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeFileIps</td>
<td >查询指定配置文件所在的 IP 列表 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeExportConfsList</td>
<td >查询支持导出配置文件的列表 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeFlowStatus</td>
<td >查询 EMR 实例流程状态 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeFlowNum</td>
<td >查询 EMR 集群流程个数 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeClusterNodes</td>
<td >查询 EMR 集群的硬件节点信息 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ClearMetadata</td>
<td >清理 EMR 集群元数据信息并销毁集群 </td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeAutoScaleGlobalConf</td>
<td >获取自动扩缩容全局配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeAutoScaleSpecs</td>
<td >获取自动扩缩容规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyAutoScaleSpecs</td>
<td >修改自动扩缩容规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddMetricScaleStrategy</td>
<td >添加指标负载扩缩容规则</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteAutoScaleSpec</td>
<td >删除自动扩缩容规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeAutoScaleRecords</td>
<td >获取自动扩缩容历史记录</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteAutoScaleStrategy</td>
<td >删除自动扩缩容规则</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyStrategyPriority</td>
<td >修改规则优先级</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeAutoScaleMetaRange</td>
<td >获取自动扩缩容元数据</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeAutoScaleStrategies</td>
<td >获取自动扩缩容规则</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyAutoScaleStrategy</td>
<td >修改自动扩缩容规则</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddAutoScaleSpec</td>
<td >添加自动扩缩容规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >TerminateAutoScaleNodes</td>
<td >销毁所有自动扩缩容节点</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeCbsEncrypt</td>
<td >描述 cbs 加密</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyConfigGroup</td>
<td >修改配置组</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteConfigGroup</td>
<td >删除配置组</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddConfigGroup</td>
<td >添加配置组</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeConfigGroup</td>
<td >描述配置组</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >SynchronizeGroupConfCheck</td>
<td >同步配置检查</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >UnbindInstanceAndNodesTags</td>
<td >解绑集群标签</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeNodeResourceConfigFast</td>
<td >快速获取节点规格配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InstallCos</td>
<td >后开启 Cos</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeScaleoutableService</td>
<td >描述可扩容的服务</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeNodeResourceConfig</td>
<td >获取节点规格配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DeleteNodeResourceConfig</td>
<td >删除节点规格配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AddNodeResourceConfig</td>
<td >增加节点规格配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >SetNodeResourceConfigDefault</td>
<td >设置节点规格配置默认属性</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeHbaseTableMetricDataOverview</td>
<td >获取 HBase 表级监控数据概览接口</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstanceNode</td>
<td >【标签控制台】拉取节点资源</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >UpdateWebproxyPassword</td>
<td >更新代理组件密码</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >TerminateTasks</td>
<td >缩容 Task 节点</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >TerminateNodes</td>
<td >销毁节点</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >TerminateInstance</td>
<td >销毁 EMR 实例</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >StopService</td>
<td >停止组件服务</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >StopMonitor</td>
<td >停止组件监控</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >StartService</td>
<td >启动组件服务</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >StartMonitor</td>
<td >启动组件监控</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ScaleOutRouter</td>
<td >扩容 Router 节点</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeDestroyInfo</td>
<td >查询 EMR 集群/节点销毁信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ScaleOutInstance</td>
<td >实例扩容</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >RollBackConf</td>
<td >回滚配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >RestartService</td>
<td >重启组件服务</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyServiceParams</td>
<td >修改服务组件参数</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyResource</td>
<td >变配实例</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >AssignInstancesProject</td>
<td >将 EMR 集群分配到指定项目</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyOptionalSpecStatus</td>
<td >修改备选规格状态</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyOptionalSpec</td>
<td >修改备选规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeSelectedOptionalSpec</td>
<td >查询已选备选规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >ModifyInstanceBasic</td>
<td >修改集群名称</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InstallSoftware</td>
<td >安装组件</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquiryPriceAddRouter</td>
<td >获取添加 Router 价格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquiryPriceRenewInstance</td>
<td >续费询价</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquiryPriceUpdateInstance</td>
<td >变配询价</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >InquiryPriceScaleOutInstance</td>
<td >扩容询价</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribleClusterNodes</td>
<td >查询 EMR 集群的硬件节点信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeServiceNodeInfos</td>
<td >查询 EMR 集群服务进程信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeServiceGroups</td>
<td >查询 EMR 集群服务组信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeServiceConfs</td>
<td >查询 EMR 集群服务的所有配置信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeScaleoutGoodsDetail</td>
<td >查询扩容订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeRouterGoodsDetail</td>
<td >查询 Router 节点订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeRenewGoodsDetail</td>
<td >查询续费订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeOptionalSpec</td>
<td >查询 EMR 实例节点的备选规格</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeModifyGoodsDetail</td>
<td >查询变配订单</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeMetricsDimension</td>
<td >查询不同级别监控的监控维度值</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeMetricMeta</td>
<td >查询 EMR 集群监控元数据</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstanceOplog</td>
<td >查询 EMR 实例操作日志</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeExecCustomScript</td>
<td >查询用户自定义脚本信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstanceAlerts</td>
<td >查询 EMR 集群告警信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstances</td>
<td >查询 EMR 实例信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeInstallSoftwareInfo</td>
<td >查询 EMR 集群安装和未安装的组件信息</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr><tr>
<td >DescribeExportConfs</td>
<td >查询导出配置</td>
<td >emr-instance|qcs::emr:${region}:uin/${uin}:emr-instance/$emrInstanceId</td>
</tr>
</tbody>
</table>

## 支持接口级授权的 API 列表
<table>
<thead>
<tr>
<th width="50%">API 名</th>
<th width="50%">API 描述</th>
</tr>
</thead>
<tbody>
<tr>
<td >RunJobFlow</td>
<td >创建运行作业</td>
</tr><tr>
<td >DescribeJobFlow</td>
<td >查询运行作业</td>
</tr><tr>
<td >DescribeK8sResourcePrice</td>
<td >查询 K8s 资源价格</td>
</tr><tr>
<td >DescribePodSpecs</td>
<td >描述 Pod 规格</td>
</tr><tr>
<td >GenerateCreateGoodsDetail</td>
<td >生成创建集群订单</td>
</tr><tr>
<td >DescribeLogSearchFileNames</td>
<td >获取日志搜索文件列表</td>
</tr><tr>
<td >DescribeInstanceServiceRoleNames</td>
<td >获取服务角色表名称</td>
</tr><tr>
<td >DescribeCompareMetricsList</td>
<td >获取对比指标列表</td>
</tr><tr>
<td >DescribeHeatMapMetricList</td>
<td >返回集群主机聚合维度指标列表</td>
</tr><tr>
<td >DescribeHBaseRegionList</td>
<td >获取 HBase Region 列表</td>
</tr><tr>
<td >DescribeClusterOverview</td>
<td >查询集群概览</td>
</tr><tr>
<td >DescribeEMRNodeOverview</td>
<td >查询节点各进程部署状态</td>
</tr><tr>
<td >DescribeNodeHardwareInfo</td>
<td >查询主机基本配置</td>
</tr><tr>
<td >DescribeTopNMeta</td>
<td >获取 topn 元数据信息</td>
</tr><tr>
<td >DescribeMetricDataAutoGranularity</td>
<td >获取监控数据，自动设置时间粒度</td>
</tr><tr>
<td >DescribeLogSearchTabs</td>
<td >获取日志搜索 tab 标签开关</td>
</tr><tr>
<td >DescribeEMRHostOverview</td>
<td >主机详情页查询进程状态</td>
</tr><tr>
<td >DescribeLogSearchRecords</td>
<td >获取日志搜索内容</td>
</tr><tr>
<td >DescribeTopNByProcess</td>
<td >获取 topn 进程</td>
</tr><tr>
<td >DescribeDiskInfo</td>
<td >返回磁盘具体信息</td>
</tr><tr>
<td >DescribeTopNByHost</td>
<td >查询概览页主机维度的 TopN</td>
</tr><tr>
<td >DescribeHeatMapDistribution</td>
<td >返回集群热力图数据</td>
</tr><tr>
<td >DescribeInstanceServiceRoleTable</td>
<td >获取服务角色表数据</td>
</tr><tr>
<td >DescribeNodeAlias</td>
<td >获取 EMR 节点别名</td>
</tr><tr>
<td >DescribeInstanceNodes</td>
<td >获取集群主机信息</td>
</tr><tr>
<td >DescribeKeyPairs</td>
<td >查询密钥对信息</td>
</tr><tr>
<td >DescribeHbaseTableMetricData</td>
<td >查询 HBase 表级监控数据</td>
</tr><tr>
<td >DescribeKeyPairs</td>
<td >查询密钥对信息</td>
</tr><tr>
<td >DescribeEmrMetaDB</td>
<td >获取 Hive 统一元数据库信息</td>
</tr><tr>
<td >ModifyEmrRole</td>
<td >更新 EmrRole 信息</td>
</tr><tr>
<td >DescribeDisasterRecoverGroup</td>
<td >获取分散置放群组信息</td>
</tr><tr>
<td >DescribeTags</td>
<td >拉取集群所有标签</td>
</tr><tr>
<td >InquiryPriceCreateInstance</td>
<td >创建实例询价</td>
</tr><tr>
<td >DescribleAccountBalance</td>
<td >查询账户余额</td>
</tr><tr>
<td >DescribeSecurityGroup</td>
<td >获取 EMR 安全组信息</td>
</tr><tr>
<td >DescribeCvmSpec</td>
<td >查询云服务器规格</td>
</tr><tr>
<td >DescribeCdbPrice</td>
<td >查询 CDB 价格</td>
</tr><tr>
<td >CreateInstance</td>
<td >创建 EMR 实例</td>
</tr><tr>
<td >GetMetricDataForMcController</td>
<td >【控制台】详情页监控信息接口</td>
</tr><tr>
<td >DescribeVpcList</td>
<td >查询 vpc 列表信息</td>
</tr><tr>
<td >DescribeSceneProductInfo</td>
<td >获取购买页集群场景、类型、产品及组件信息</td>
</tr><tr>
<td >DescribeRegionAndZoneSaleInfo</td>
<td >获取控制台及购买页的地域和可用区</td>
</tr><tr>
<td >DescribeCgwProjects</td>
<td >获取 CGW 项目列表</td>
</tr>
</tbody>
</table>

资源级和接口级别具体授权方案详见：[授权粒度方案](https://tcloud-doc.isd.com/document/product/589/66673)。
