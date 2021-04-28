## 使用准备
仅支持在购买集群时选择了可选组件 Ranger 的集群，若是在已创建的集群上新增 Ranger 组件，可能会出现 Web UI 无法访问的情况。默认 Ranger 安装时，Ranger Admin、Ranger UserSync 都是部署在 Master 节点上，Ranger Plugin 是部署嵌入组件主守护进程节点上。

创建集群时，在选择集群类型为 Hadoop 时可以在可选组件中选择 Ranger，Ranger 的版本根据您选择的 EMR 版本不同而存在差异。
>?集群类型为 Hadoop 且选择了可选组件 Ranger 时，EMR-Ranger 默认会为 HDFS、YARN 创建服务并设置默认策略。
>
![](https://main.qcloudimg.com/raw/e744dc5ce95b1a2dc17f2765b4abe721.png)

## Ranger Web UI
在访问 Ranger Web UI 之前，请务必确认当前所购买的集群是否配置了公网 IP，然后在集群服务中单击 Ranger 组件的 Web UI 地址链接。
![](https://main.qcloudimg.com/raw/002d2aeeb1349f12b3c811b1bbae7ea4.png)
Web UI 地址链接跳转后，会提示输入用户名及密码，即在购买集群时设置的用户名及密码。
![](https://main.qcloudimg.com/raw/a0b4159c09c674773b2f3705abbd7d38.png)

## 组件集成
### HDFS 集成 Ranger
>!请确保 HDFS 相关服务运行正常并且当前集群已安装 Ranger。
>
1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger HDFS 服务。
![](https://main.qcloudimg.com/raw/74f103c458aa2327cd3eb8c7ad2009ef.png)
2. 配置 EMR Ranger HDFS Service 相关参数。
![](https://main.qcloudimg.com/raw/c73a4fa6907df6be4bc1f2b6fac87106.png)
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
<td>服务名称，Ranger Web UI 主 HDFS 组件显示服务名称</td>
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
<td>Passwrod</td>
<td>是</td>
<td>用户密码</td>
</tr>
<tr>
<td>NameNode URL</td>
<td>是</td>
<td>HDFS 地址</td>
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
3.  EMR Ranger HDFS 资源权限配置。
 - 点击配置好的 EMR Ranger HDFS Service 
![](https://main.qcloudimg.com/raw/3c2d2defa092584909a3d1b2a2021eff.png)
 - 配置 Policy 
![](https://main.qcloudimg.com/raw/4e103c65e9de153c4c1cd8d77dcaf33c.png)
![](https://main.qcloudimg.com/raw/a22709846886c938b2b9aa2222e445ed.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以对 HDFS 文件系统的 /user 进行读写操作。

### YARN 集成 Ranger
>!请确保 YARN 相关服务运行正常并且当前集群已安装 Ranger。
>
EMR Ranger YARN 目前仅支持 Capacity Scheduler 队列的 ACL，不支持 Fair Scheduler 队列的 ACL。Ranger YARN 队列 ACL 与 YARN 自带的 Capacity Scheduler 配置共同生效，且优先级低于 Capacity Scheduler 配置，只有在 YARN 自带的 Capacity Scheduler 配置拒绝校验时才会校验 Ranger YARN 权限。**建议不要在配置文件设置 ACL，而是使用 Ranger 设置 ACL**。

1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger YARN 服务。
![](https://main.qcloudimg.com/raw/b574991466eb89ebb990c4c9dc56a236.png)
2. 配置 EMR Ranger YARN Service 相关参数。
![](https://main.qcloudimg.com/raw/40ee44b63186f88216f0c657b7a9f018.png)
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
<td>Passwrod</td>
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
 - 点击配置好的 EMR Ranger HDFS Service 
![](https://main.qcloudimg.com/raw/57b34f9adde606c40f52bf76f1e43c36.png)
 - 配置 Policy 
![](https://main.qcloudimg.com/raw/68cceaed942cea8da21222b3d6903a19.png)
![](https://main.qcloudimg.com/raw/374ad719611ded0872a0aa51c5dcf6dd.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以向 YARN 的 root.default 队列中提交、杀死、查询作业等操作。

>!在配置 Ranger YARN Service 以及 Policy 时请务必确保期间没有 YARN 作业，否则会出现某些用户作业提交权限问题。

### Hbase 集成 Ranger
>!请确保 HBase 相关服务运行正常并且当前集群已安装 Ranger。
>
1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger Hbase 服务。
![](https://main.qcloudimg.com/raw/acc3b5af5f1c4b7186427cb8cc7a837f.png)
2. 配置 EMR Ranger Hbase Service 相关参数。
![](https://main.qcloudimg.com/raw/bf5058d18d9865a9421821a6dc46fac5.png)
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
<td>服务名称，Ranger Web UI 主 HBase 组件显示服务名称</td>
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
<td>Passwrod</td>
<td>是</td>
<td>用户密码</td>
</tr>
<tr>
<td>Hbase.zookeeper.property.clientPort</td>
<td>是</td>
<td>ZK 客户端请求端口</td>
</tr>
<tr>
<td>Hbase.zookeeper.quorum</td>
<td>是</td>
<td>ZK 集群 IP</td>
</tr>
<tr>
<td>Zookeeper.znode.parent</td>
<td>是</td>
<td>ZK 节点信息</td>
</tr>
</tbody></table>
3. EMR Ranger Hbase 资源权限配置。
 - 点击配置好的 EMR Ranger Hbase Service 
![](https://main.qcloudimg.com/raw/d235d5dff25704fa68e634d268cd7c72.png)
 - 配置 Policy 
![](https://main.qcloudimg.com/raw/9b84df03567605e44664fda64473aae0.png)
上图中的 Users 为 Hbase，它的 Policy Name 是 all-table、column-family、cloumn，也就是 Hbase 用户具有 Region Balance、MemeStore Fluh、Compaction、Split 权限。**请确保创建的 Service 是有些这些权限的。**
![](https://main.qcloudimg.com/raw/17839f58a557bd44bcc4dc4db4e02603.png)
<table>
<thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>是否必选项</strong></th>
<th><strong>解释</strong></th>
</tr>
</thead>
<tbody><tr>
<td>HBase Table</td>
<td>是</td>
<td>HBase 表名</td>
</tr>
<tr>
<td>HBase Column-family</td>
<td>是</td>
<td>HBase 表中的列簇</td>
</tr>
<tr>
<td>HBase Column</td>
<td>是</td>
<td>HBase 表中的列簇下的限定符</td>
</tr>
</tbody></table>
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以对 Hbase 的 order 表相关列簇和限定符进行相关操作。

### Presto 集成 Ranger
>!请确保 Presto 相关服务运行正常并且当前集群已安装 Ranger。
>
1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger Presto 服务。
![](https://main.qcloudimg.com/raw/53202d00bdc86897c076caf1fdb139b8.png)
2. 配置 EMR Ranger Presto Service 相关参数。
![](https://main.qcloudimg.com/raw/6f096bcccb58a5c52e7e0a4b258d6c9a.png)
<table>
<thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>是否必填项</strong></th>
<th><strong>解释</strong></th>
</tr>
</thead>
<tbody><tr>
<td>Service Name</td>
<td>是</td>
<td>服务名称，Ranger Web UI 主 Predo 组件显示服务名称</td>
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
<td>Passwrod</td>
<td>是</td>
<td>用户密码</td>
</tr>
<tr>
<td>JDBC.driverClassName</td>
<td>是</td>
<td>驱动的类名全路径</td>
</tr>
<tr>
<td>jdbc.url</td>
<td>是</td>
<td>Presto jdbc 连接形式的地址，例如 jdbc:presto://ip/hostname:port</td>
</tr>
</tbody></table>
3. EMR Ranger Presto 资源权限配置
 - 点击配置好的 EMR Ranger Presto Service
![](https://main.qcloudimg.com/raw/c47fa2c22c26241a855fa07aaec53e7c.png)
 - 配置 Policy 
![](https://main.qcloudimg.com/raw/4e7f4d64de70f3dc20a8dd266156d490.png)
![](https://main.qcloudimg.com/raw/41ca3e0a1be965d9b6d7ee84c9a8e146.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以对 Presto 的 catalog 进行查看和使用。
