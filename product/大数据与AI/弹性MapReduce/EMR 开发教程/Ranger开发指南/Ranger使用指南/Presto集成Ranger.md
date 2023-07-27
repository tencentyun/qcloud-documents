## 使用准备
Ranger 安装时，Ranger Admin、Ranger UserSync 都是部署在 Master 节点上，Ranger Plugin 是部署在嵌入组件主守护进程节点上。  

创建集群时，在选择集群类型为 Hadoop 时可以在可选组件中选择 Ranger，Ranger 的版本根据您选择的 EMR 版本不同而存在差异。
>?集群类型为 Hadoop 且选择了可选组件 Ranger 时，EMR-Ranger 默认会为 HDFS、YARN 创建服务并设置默认策略。
>
![](https://qcloudimg.tencent-cloud.cn/raw/c80ea1ec27340de0788d59a85fbc1762.png)

## Ranger Web UI
在访问 Ranger Web UI 之前，请务必确认当前所购买的集群是否配置了公网 IP，然后在集群服务中单击 Ranger 组件的 Web UI 地址链接。
![](https://qcloudimg.tencent-cloud.cn/raw/edb1a5ee9c1c89c511c9598f3a61d375.png)
Web UI 地址链接跳转后，会提示输入用户名及密码，即在购买集群时设置的用户名及密码。
![](https://qcloudimg.tencent-cloud.cn/raw/e8679c01f804c608011a6d34ae58291c.png)

## Presto 集成 Ranger
>!请确保 Presto 相关服务运行正常并且当前集群已安装 Ranger。
>
1. 使用 EMR Ranger Web UI 页面添加 EMR Ranger Presto 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/4c59168f9e7e6539516bece37ec36fdf.png)
2. 配置 EMR Ranger Presto Service 相关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/bb2377b1effe9568ce37441a9529221e.png)
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
<td>Password</td>
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
 - 单击配置好的 EMR Ranger Presto Service
![](https://qcloudimg.tencent-cloud.cn/raw/174c3407bf8728f8168dcc8fdf90f081.png)
 - 配置 Policy 
![](https://qcloudimg.tencent-cloud.cn/raw/67777bb5461737923c8feab408facbd3.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ae9bf3401dd7dfae9059c01c76a656df.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以对 Presto 的 catalog 进行查看和使用。
