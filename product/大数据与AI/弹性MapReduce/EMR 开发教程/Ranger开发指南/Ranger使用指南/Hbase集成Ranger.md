## 使用准备
Ranger 安装时，Ranger Admin、Ranger UserSync 都是部署在 Master 节点上，Ranger Plugin 是部署在嵌入组件主守护进程节点上。

创建集群时，在选择集群类型为 Hadoop 时可以在可选组件中选择 Ranger，Ranger 的版本根据您选择的 EMR 版本不同而存在差异。  
>?集群类型为 Hadoop 且选择了可选组件 Ranger 时，EMR-Ranger 默认会为 HDFS、YARN 创建服务并设置默认策略。
>
![](https://qcloudimg.tencent-cloud.cn/raw/34bd0190bda80ae2399d5530f6a6b700.png)

## Ranger Web UI
在访问 Ranger Web UI 之前，请务必确认当前所购买的集群是否配置了公网 IP，然后在集群服务中单击 Ranger 组件的 Web UI 地址链接。
![](https://qcloudimg.tencent-cloud.cn/raw/ee47cd26b3faa48c102bbbe328bfec5a.png)
Web UI 地址链接跳转后，会提示输入用户名及密码，即在购买集群时设置的用户名及密码。
![](https://qcloudimg.tencent-cloud.cn/raw/43ce2c4f958ade5fc4948ff0a22f458f.png)


## Hbase 集成 Ranger
>!请确保 HBase 相关服务运行正常并且当前集群已安装 Ranger。
>
1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger Hbase 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/9050d98797e0a63fb14ca99de69a7722.png)
2. 配置 EMR Ranger Hbase Service 相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/b80c20f337af7a41040f0f258a5cd1d3.png)
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
 - 单击配置好的 EMR Ranger Hbase Service 
![](https://qcloudimg.tencent-cloud.cn/raw/b11a9e939f0de2c7ac37ce465540ea41.png)
 - 配置 Policy 
![](https://qcloudimg.tencent-cloud.cn/raw/4d26c02fea6c8dc0f9f47d4a05ac07e5.png)
上图中的 Users 为 Hbase，它的 Policy Name 是 all-table、column-family、column，也就是 Hbase 用户具有 Region Balance、MemeStore Fluh、Compaction、Split 权限。**请确保创建的 Service 是有这些权限的。**
![](https://qcloudimg.tencent-cloud.cn/raw/424bae73bead9888167fb586243e8023.png)
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
