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


## Hbase 集成 Ranger
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
<td>Password</td>
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
