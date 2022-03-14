 **[容器服务 API 2.0 ](https://cloud.tencent.com/document/product/457/9458) 将于2020年3月下线， 建议您使用 [容器服务 API 3.0](https://cloud.tencent.com/document/product/457/31853)。3.0版本接口定义更加规范，访问时延下降显著，您可参考下文 API 接口对照映射表开始使用。**

>?下表中部分容器服务 API 3.0 接口及 Kubernetes API 文档将于近期上线，请注意官方文档变化。

<table>
	<tr>		<th colspan=2>模块</th>		<th>API 2.0</th>		<th>API 3.0</th>	</tr>
	<tr>
		<td rowspan=20 colspan=2>集群相关</td>
		<td><a href="https://cloud.tencent.com/document/product/457/9444">创建集群（CreateCluster）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/34527">创建集群（CreateCluster）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9445"> 删除集群（DeleteCluster）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/36704"> 删除集群（DeleteCluster）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9448">查询集群列表（DescribeCluster）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/31862">查询集群列表（DescribeCluster）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9447">扩展集群节点（ AddClusterInstances）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/36707">扩展集群节点（CreateClusterInstances）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9450">添加已存在云服务器到集群（AddClusterInstancesFromExistedCvm）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/31865">添加已经存在的实例到集群（AddExistedInstances）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9446">删除集群节点（DeleteClusterInstances）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/31864">删除集群中的节点（DeleteClusterInstances）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9449">查询集群节点列表（DescribeClusterInstances）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/31863">查询集群节点信息（DescribeClusterInstances）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17560">获取集群外网访问凭据（DescribeClusterSecurityInfo ）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/36703">集群的密钥信息（DescribeClusterSecurity）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18159">校验 CIDR（CheckClusterCIDR）</a></td>
		<td>检查集群的 CIDR 是否冲突（CheckClusterCIDR）</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18321">查询加入集群的主机列表（DescribeExistedCvmForAddClusterInstances）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/36706">查询已经存在的节点（DescribeExistedInstances）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18333">查询集群 Request 和 Limit 信息（DescribeClusterRequestLimitInfo）</a></td>
		<td rowspan=2><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
	</tr>
	<tr>
			<td><a href="https://cloud.tencent.com/document/product/457/13999">修改节点 Label（ModifyClusterNodeLabel）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17558">修改集群属性（ModifyClusterAttributes）</a></td>
		<td rowspan=2>修改集群属性（ ModifyClusterAttribute）</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18337">修改集群所属项目（ModifyProjectId）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18429">修改集群命名空间描述（ModifyNamespaceDescription）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
	</tr>
	<tr>
		<td><ul class="params"><li><a href="https://cloud.tencent.com/document/product/457/18433">操作集群外网访问地址（OperateClusterVip） </a></li><li><a href="https://cloud.tencent.com/document/product/457/9426">查询异步任务结果（DescribeClusterTaskResult）</a></li></td>
		<td><ul class="params"><li><a href="https://cloud.tencent.com/document/product/457/39413">创建托管集群外网访问端口（CreateClusterEndpointVip）</a></li><li><a href="https://cloud.tencent.com/document/product/457/39411">删除托管集群外网访问端口（DeleteClusterEndpointVip）</a></li><li><a href="https://cloud.tencent.com/document/product/457/39409">查询托管集群开启外网端口流程状态（ DescribeClusterEndpointVipStatus）</a></li><li><a href="https://cloud.tencent.com/document/product/457/39408">修改托管集群外网端口的安全策略（ModifyClusterEndpointSP）</a></li></ul></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18323">驱逐集群节点（ DrainClusterNode）</a></td>
		<td>驱逐节点（DrainClusterNode）</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18322">设置集群节点为是否可调度（ModifyClusterNodeSchedulable）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17559">添加第三方私有镜像仓库（AddHubInfo）</a></td>
		<td rowspan=2>功能下线</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18338">查询集群第三方镜像仓库（DescribeHubInfo） </a></td>
	</tr>
	<tr>
		<td rowspan=9  colspan=2>集群自动扩缩容相关</td>
		<td><a href="https://cloud.tencent.com/document/product/457/15491">创建集群伸缩组（CreateClusterAsg）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/37539">创建集群的伸缩组（CreateClusterAsGroup）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15494">启用集群伸缩组（EnableClusterAsg）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/40470">修改集群伸缩组属性（ModifyClusterAsGroupAttribute）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15495">查询集群伸缩组列表（DescribeClusterAsg）</a></td>
	 <td><a href="https://cloud.tencent.com/document/product/457/40471">集群关联的伸缩组列表（DescribeClusterAsGroups）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15488">修改集群伸缩组是否启用缩容（ModifyClusterAsgScaleDown）</a></td>
	 <td>修改集群弹性伸缩属性（ModifyClusterAsGroupOptionAttribute）</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15487">修改集群伸缩组 label（ModifyClusterAsgLabel）</a></td>
	 <td rowspan=3>功能下线</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15496">重置集群伸缩组 label（ResetClusterAsgLabel）</a></td>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15493">删除集群伸缩组 label（DeleteClusterAsgLabel）</a></td>
	</tr>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15490">停用集群伸缩组（DisableClusterAsg）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/40470">修改集群伸缩组属性（ModifyClusterAsGroupAttribute）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/15492">删除集群伸缩组（DeleteClusterAsg）</a></td>
		<td><a href="https://cloud.tencent.com/document/product/457/37978">删除集群伸缩组（DeleteClusterAsGroups）</a></td>
	</tr>
	<tr>
		<td rowspan=14  colspan=2>服务相关</td>
		<td><a href="https://cloud.tencent.com/document/product/457/9436">创建服务（CreateClusterService）</a></td>
		<td rowspan=25><a href="https://cloud.tencent.com/document/product/457/46276">Kubernetes API</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9440">查询服务列表（DescribeClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9441">查询服务详情（DescribeClusterServiceInfo）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9443">获取服务事件列表（DescribeServiceEvent）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17557">获取服务的 yaml 文本信息（DescribeClusterServiceText）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9434">修改服务（ModifyClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9435">修改服务描述（ModifyServiceDescription）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9630">修改服务镜像（ModifyClusterServiceImage）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17556">修改服务的标签（Label）信息（ModifyServiceLabels）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9438">回滚服务（RollBackClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9685">服务重部署（RedeployClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9439">暂停服务更新（PauseClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9442">继续服务更新（ResumeClusterService）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9437">删除服务（DeleteClusterService）</a></td>
	</tr>
	<tr>
        <td rowspan=4  colspan=2>服务实例相关</td>
        <td><a href="https://cloud.tencent.com/document/product/457/9433">查询服务实例列表（DescribeServiceInstance）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9431">修改服务实例副本数（ModifyServiceReplicas）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17555">获取服务实例日志（DescribeInstanceLog）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9432">删除服务实例（DeleteInstances）</a></td>
	</tr>
	<tr>
        <td rowspan=3  colspan=2>命名空间相关</td>
        <td><a href="https://cloud.tencent.com/document/product/457/9430">查询集群命名空间（DescribeClusterNameSpaces）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9428">创建集群命名空间（CreateClusterNamespace）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/9429">删除集群命名空间（DeleteClusterNamespace）</a></td>
	</tr>
	<tr>
        <td rowspan=4  colspan=2>Ingress 相关</td>
        <td><a href="https://cloud.tencent.com/document/product/457/17544">创建 Ingress（CreateIngress）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17546">查询 Ingress 列表（DescribeIngress）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17543">修改 Ingress（MosifyIngress）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17545">删除 Ingress（DeleteIngress）</a></td>
	</tr>
	<tr>
        <td rowspan=8  colspan=2>日志相关</td>
        <td><a href="https://cloud.tencent.com/document/product/457/17551">启用集群日志收集服务（GetLogDaemonStatus）</a></td>
        <td rowspan=8>功能下线</td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17548">创建集群日志收集规则（CreateLogCollector）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17553">列出日志收集规则（ListLogCollector）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17550">更新日志收集规则（UpdateLogCollector）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17554">获取日志收集器信息（GetLogCollector）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/18255">获取日志收集器状态信息（GetLogDaemonStatus）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17552">检查日志收集器名称（CheckIfLogCollectorName）</a></td>
	</tr>
	<tr>
		<td><a href="https://cloud.tencent.com/document/product/457/17549">删除日志收集规则（DeleteLogCollector）</a></td>
	</tr>
	<tr>
        <td  colspan=2 >监控相关</td>
        <td><a href="https://cloud.tencent.com/document/product/457/9505">查询容器服务监控信息（GetMonitorData）</a></td>
        <td><ul class="params"><li><a href="https://cloud.tencent.com/document/product/248/35805">容器服务-实例维度监控接口（GetMonitorData）</a></li><li><a href="https://cloud.tencent.com/document/product/248/35806">容器服务-容器维度监控接口（GetMonitorData）</a></li><li><a href="https://cloud.tencent.com/document/product/248/35807">容器服务-服务维度监控接口（GetMonitorData）</a></li></ul></td>
	</tr>
    <tr>       
        <td rowspan=28 >镜像仓库相关</td>
        <td rowspan=3>用户及密码管理</td>
        <td><a href="https://cloud.tencent.com/document/product/457/18954">用户注册（无需指定 Namespace）（RegisterRepositoryAccountNew）</a></td>
        <td >创建个人用户（CreateUserPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14654">查询用户配额（GetLimit）</a></td>
        <td >查询个人用户配额（DescribeUserQuotaPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14643">修改密码（ChangePassword）</a></td>
        <td >修改个人用户登录密码（ ModifyUserPasswordPersonal）</td>
    </tr>
    <tr>
    	<td rowspan=4>命名空间</td>
        <td><a href="https://cloud.tencent.com/document/product/457/18547">创建命名空间（CreateCCRNamespace）</a></td>
        <td >创建命名空间（CreateNamespacePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/18549">查询命名空间（GetNamespaceInfo）</a></td>
        <td >查询命名空间（DescribeNamespacePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/18550">查询命名空间是否存在（NamespaceIsExists）</a></td>
        <td >检查命名空间是否存在（ValidateNamespaceExistPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/18548">删除命名空间（DeleteUserNamespace）</a></td>
        <td >删除命名空间（DeleteNamespacePersonal）</td>
    </tr>
    <tr>
    	<td rowspan=9>镜像仓库</td>
        <td><a href="https://cloud.tencent.com/document/product/457/14646">创建镜像仓库（CreateRepository）</a></td>
        <td >创建镜像仓库（CreateRepositoryPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14656">查询镜像仓库信息（GetRepositoryInfo）</a></td>
        <td >查询镜像仓库（DescribeRepositoryPersonal）</td>
    </tr>
    <tr>
        <td>-</td>
        <td >删除镜像仓库（DeleteRepositoryPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14650">批量删除仓库（BatchDeleteRepository）</a></td>
        <td >批量删除镜像仓库（BatchDeleteRepositoryPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14662">镜像仓库是否存在（RepositoryisExists）</a></td>
        <td >检查镜像仓库是否存在（ValidateRepositoryExistPersonal）</td>
    </tr>
    <tr>
        <td><a href="">获取用户自身的所有仓库列表（GetUserRepositoryList）</a></td>
        <td >查询用户创建的镜像仓库（DescribeRepositoryOwnerPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14653">查询用户仓库列表（SearchUserRepository）</a></td>
        <td >查询指定条件的镜像仓库（DescribeRepositoryFilterPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14652">更新镜像仓库访问属性（UpdateRepositoryPublic）</a></td>
        <td >修改镜像仓库公开属性（ModifyRepositoryAccessPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14651">更改镜像仓库描述内容（UpdateRepositoryDesc）</a></td>
        <td >修改镜像仓库描述信息（ModifyRepositoryInfoPersonal）</td>
    </tr>
    <tr>
    	<td rowspan=8>镜像仓库</td>
        <td><a href="https://cloud.tencent.com/document/product/457/14658">获取 tag 列表（GetTagList）</a></td>
        <td >查询镜像版本（DescribeImagePersonal）</td>
    </tr>
    <tr>
        <td>-</td>
        <td >查询指定条件的镜像版本（DescribeImageFilterPersonal）</td>
    </tr>
    <tr>
        <td>-</td>
        <td >删除镜像版本（DeleteImagePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14649">批量删除  tag（BatchDeleteTag）</a></td>
        <td >批量删除镜像版本（BatchDeleteImagePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14648">复制镜像版本（DuplicateImage）</a></td>
        <td >复制镜像版本（DuplicateImagePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14661">设置仓库 tag 超额保留策略（SetAutoDelStrategy）</a></td>
        <td >创建镜像版本生命周期配置（CreateImageLifecyclePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14659">获取仓库 tag 超额保留策略（GetAutoDelStrategy）</a></td>
        <td >查询镜像版本生命周期配置（DescribeImageLifecyclePersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14645">关闭仓库 tag 超额保留策略（CloseAutoDelStrategy）</a></td>
        <td >删除镜像版本生命周期配置（DeleteImageLifecyclePersonal）</td>
    </tr>
    <tr>
    	<td rowspan=4>触发器</td>
        <td><a href="https://cloud.tencent.com/document/product/457/14657">添加触发器（AddUpdateWorkloadTrigger）</a></td>
        <td >创建应用更新触发器（CreateApplicationTriggerPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14644">修改服务更新触发器（ModifyUpdateServiceTrigger）</a></td>
        <td >修改应用更新触发器（ModifyApplicationTriggerPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/14660">获取触发器（ListTrigger）</a></td>
        <td >查询应用更新触发器（DescribeApplicationTriggerPersonal）</td>
    </tr>
    <tr>
        <td><a href="https://cloud.tencent.com/document/product/457/18552">获取触发记录（ListTriggerLog）</a></td>
        <td >查询应用更新触发器触发日志（DescribeApplicationTriggerLogPersonal ）</td>
    </tr>
</table>


<style>
	.params{margin-bottom:0px !important;}
</style>






