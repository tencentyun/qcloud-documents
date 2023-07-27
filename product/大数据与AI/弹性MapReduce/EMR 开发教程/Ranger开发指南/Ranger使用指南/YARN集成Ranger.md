## 使用准备
Ranger 安装时，Ranger Admin、Ranger UserSync 都是部署在 Master 节点上，Ranger Plugin 是部署在嵌入组件主守护进程节点上。

创建集群时，在选择集群类型为 Hadoop 时可以在可选组件中选择 Ranger，Ranger 的版本根据您选择的 EMR 版本不同而存在差异。
>?集群类型为 Hadoop 且选择了可选组件 Ranger 时，EMR-Ranger 默认会为 HDFS、YARN 创建服务并设置默认策略。
>
![](https://qcloudimg.tencent-cloud.cn/raw/93e385e006b82b746283769796dec2d5.png)

## Ranger Web UI
在访问 Ranger Web UI 之前，请务必确认当前所购买的集群是否配置了公网 IP，然后在集群服务中单击 Ranger 组件的 Web UI 地址链接。
![](https://qcloudimg.tencent-cloud.cn/raw/9d5f3693a9f6a82c96b7645a44d2d5ca.png)
Web UI 地址链接跳转后，会提示输入用户名及密码，即在购买集群时设置的用户名及密码。
![](https://qcloudimg.tencent-cloud.cn/raw/7bf28c9efc42e599966f4ffa803af5c9.png)
 
## YARN 集成 Ranger
>!请确保 YARN 相关服务运行正常并且当前集群已安装 Ranger。
>
EMR Ranger YARN 目前仅支持 Capacity Scheduler 队列的 ACL，不支持 Fair Scheduler 队列的 ACL。Ranger YARN 队列 ACL 与 YARN 自带的 Capacity Scheduler 配置共同生效，且优先级低于 Capacity Scheduler 配置，只有在 YARN 自带的 Capacity Scheduler 配置拒绝校验时才会校验 Ranger YARN 权限。**建议不要在配置文件设置 ACL，而是使用 Ranger 设置 ACL**。

1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger YARN 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/5b219330ef8da448dbf5e87031d7e9fa.png)
2. 配置 EMR Ranger YARN Service 相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/e14eec9e502f0100557c026cf44e5683.png)
<table>
<thead>
<tr>
<th><strong>参数名</strong></th>
<th><strong>是否必填项</strong></th>
<th><strong>解释</strong></th>
</tr>
</thead>
<tbody><tr>
<td>Service Name</td>
<td>是</td>
<td>服务名称，Ranger Web UI 主 YARN 组件显示服务名称</td>
</tr>
<tr>
<td>Description</td>
<td>否</td>
<td>服务描述信息</td>
</tr>
<tr>
<td>Active Status</td>
<td>默认</td>
<td>服务启用状态，默认启用</td>
</tr>
<tr>
<td>UserName</td>
<td>是</td>
<td>资源使用的用户名</td>
</tr>
<tr>
<td>Password</td>
<td>是</td>
<td>用户密码</td>
</tr>
<tr>
<td>NameNode URL</td>
<td>是</td>
<td>YARN 地址</td>
</tr>
<tr>
<td>Authorization Enable</td>
<td>默认</td>
<td>标准集群选择 No；高安全集群选择 Yes</td>
</tr>
<tr>
<td>Authorization Type</td>
<td>是</td>
<td>Simple：标准集群；Kerberos：高安全集群</td>
</tr>
</tbody></table>
3. EMR Ranger YARN 资源权限配置。
 - 单击配置好的 EMR Ranger HDFS Service 
![](https://qcloudimg.tencent-cloud.cn/raw/1d7e2e42823c4271179bc0e36728a385.png)
 - 配置 Policy 
![](https://qcloudimg.tencent-cloud.cn/raw/e291dda6423091557beca98ecfcc2154.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ca47a1e18e2ae77852d979155e36addc.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以向 YARN 的 root.default 队列中提交、删除、查询作业等操作。

>!在配置 Ranger YARN Service 以及 Policy 时请务必确保期间没有 YARN 作业，否则会出现某些用户作业提交权限问题。
