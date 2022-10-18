## 操作场景
分片集群实例开通 Mongos 访问地址之后，您可以通过 Mongos 地址访问实例，在**实例详情**页您可以看到 Mongos 的访问连接串（提供 Mongos 内网访问地址）。

## 使用须知
- 在实例当前的 VIP 下面，将给不同的 Mongos 节点绑定不同的 VPORT。
- Mongos 故障后系统将重新绑定新的 Mongos 进程，VIP 和 VPORT 地址不会变化。
- 开通 Mongos 访问地址不影响原有的负载均衡访问地址。

## 版本说明
MongoDB 4.4、4.2、4.0版本支持开通 Mongos 访问地址。

## 前提条件
- 实例类型：分片实例。
- 实例状态：运行中。

## 操作步骤
1. 登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)。
2. 在左侧导航栏 **MongoDB** 的下拉列表中，选择**分片实例**。
3. 在右侧**实例列表**页面上方，选择地域。
4. 在实例列表中，找到需查看节点的目标实例。
5. 单击其实例 ID，进入**实例详情**页面，单击**节点管理**页签。
6. 在**节点管理**页面，单击 **Mongos 节点**页签。
7. 在 **Mongos 节点**页签，单击**开通 Mongos 访问地址**。
8. 在弹出的对话框，了解开通访问地址的影响，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/8e894465d269aaf2f49b7b7f4ab23e08.png" style="zoom:80%;" />
7. 在左侧导航栏，选择**任务管理**，在任务列表中，根据实例 ID 找到**任务类型**为**开启节点访问地址**的实例，等待**任务执行状态**为**完成**。
8. 在左侧导航栏，选择**分片实例**，在实例列表找到已开启节点访问地址的实例，单击其实例 ID，进入**实例详情**页面，在**网络配置**区域的**访问地址**中，可查看 Mongos 访问地址，将鼠标放在访问地址的连接串上，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/036d66791d6ca5688900c92d7dc9a2cc.png" style="zoom:33%;" />，可直接复制连接串去访问 Mongos 节点。
![](https://qcloudimg.tencent-cloud.cn/raw/7d5250bd32c27f6d74bc90dbacf59a50.png)

