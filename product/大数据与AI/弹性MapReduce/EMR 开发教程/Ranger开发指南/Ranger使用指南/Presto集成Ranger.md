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

## Presto 集成 Ranger
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
 - 点击配置好的 EMR Ranger Presto Service
![](https://main.qcloudimg.com/raw/c47fa2c22c26241a855fa07aaec53e7c.png)
 - 配置 Policy 
![](https://main.qcloudimg.com/raw/4e7f4d64de70f3dc20a8dd266156d490.png)
![](https://main.qcloudimg.com/raw/41ca3e0a1be965d9b6d7ee84c9a8e146.png)
4. 添加完 Policy 后，稍等约半分钟等待 Policy 生效。生效后使用 user1 就可以对 Presto 的 catalog 进行查看和使用。
