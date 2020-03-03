如果您需要通过 NAT 网关使私有网络内子网的资源访问 Internet，则您不仅需要创建 NAT 网关，还需在需要路由转发的子网所关联的路由表中配置路由规则。

### 快速入门
您需要完成以下两个步骤，您可以通过 NAT 网关访问 Internet：
#### 第一步：创建 NAT 网关
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>，选择【私有网络】选项卡，选择【NAT网关】。

2. 单击左上角【新建】按钮，在弹出框中依次输入或确定以下参数：
  - 网关名称：填写您的网关名称。
  - 网关类型：网关类型创建后可更改。
  - 所属网络：选择 NAT 网关服务的私有网络。
  - 为 NAT 网关分配弹性 IP：您可以选择已有的弹性 IP，或者重新购买并分配弹性 IP。

3. 选择结束后单击【确认】按钮，即可完成 NAT 网关的创建。 

4. 创建完 NAT 网关，您需要在私有网络控制台路由表页配置路由规则，以将子网流量指向 NAT 网关。

><b>注意：</b>
>NAT 网关创建时将会冻结 1 小时的租用费用。

#### 第二步：配置相关子网所关联的路由表
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 单击导航条【私有网络】，进入，选择【路由表】。

2. 在路由表列表中，单击需要访问 Internet 的子网所关联的路由表 ID 进入路由表详情页，在路由策略中单击【编辑】按钮。

3. 单击新增一行，填入目的端，下一跳类型选择【NAT网关】，并选择已创建的 NAT 网关 ID。

4. 单击【确定】按钮。完成以上配置后，关联此路由表的子网内的云服务器访问 Intenet 的流量将指向 NAT 网关。

### 修改 NAT 网关配置
NAT 网关创建后，可以对其属性进行修改：
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 单击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，选择【NAT网关】。

2. 在 NAT 网关列表页中单击需要修改的 NAT 网关 ID 进入详情页，在详情页您可以完成以下属性的修改：
- 修改 ```NAT 网关的自定义名称```。
- 更改 ```NAT 网关的规格```。规格更改后实时设定，实时生效（变更规格不会中断原网络连接）。

### 管理 NAT 网关的弹性 IP
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>，单击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，选择【 NAT 网关】。
2. 在 NAT 网关列表中单击 ID 进入 NAT 网关详情页。

3. 在关联弹性 IP 表中，您可以选择【新增】弹性 IP 或者【解绑】弹性 IP。

### 查看 NAT 网关监控信息
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>，单击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，选择【NAT网关】。

2. 在 NAT 网关列表页，单击需要查看的 NAT 网关条目中的监控按钮，即可查看该 NAT 网关的监控信息。
  <b>或者：</b>
  在 NAT 网关列表页，单击需要查看的 NAT 网关 ID 进入详情页，单击监控选项卡查看该 NAT 网关的监控信息。

### 设置告警
1. 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>，单击顶部导航条【云产品】-<a href="https://console.cloud.tencent.com/monitor/overview" target="_blank">【云监控】</a>，选择左导航栏内的【我的告警】-<a href="https://console.cloud.tencent.com/monitor/policylist" target="_blank">【告警策略】</a>，单击【新增告警策略】。

  2)填写 **告警策略名称**，在策略类型中选择【私有网络】-【NAT网关】，然后添加```告警触发条件```。

  3)**关联告警对象**：选择告警接收组，保存后即可在告警策略列表中查看已设置的告警策略。

  4)**查看告警信息**：告警条件被触发后，您将接受到短信/邮件/站内信等通知，同时可以在左导航【我的告警】-【告警列表】中查看。有关告警的更多信息，请参考<a href="https://cloud.tencent.com/doc/product/248/1073" target="_blank">告警配置</a>。

### 删除 NAT 网关
用户可以在不需要 NAT 网关时随时将其删除，删除时会将含有此 NAT 网关的路由表的相关路由策略一并删除，Internet 转发请求将立即中断，请提前做好网络中断准备。

1) 	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>，单击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，选择【NAT网关】。

2) 选中需要删除的 NAT 网关，单击【删除】按钮并确认即可完成删除。


### 开启网关流控明细
开启后，可查看某NAT网关上过去7天内的经过该网关的IP流量指标，。
1)	登录[腾讯云控制台](https://console.cloud.tencent.com/)单击导航条【私有网络】，进入[私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=8)，选择【NAT网关】。
2) 在 NAT 网关列表中单击 ID 进入 NAT 网关详情页。
3) 单击监控tab，开启右上角 开启网关流控明细 开关
开启网关流控名称，需要5-6采集数据、发布数据，一段时间您可在监控图表下方查看监控明细表格。

### 设置网关流控明细
您在开启网关流控明细，可设置某个IP留向某NAT网关的出带宽。
1)	登录[腾讯云控制台](https://console.cloud.tencent.com/)单击导航条【私有网络】，进入[私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=8)，选择【NAT网关】。
2) 在 NAT 网关列表中单击 ID 进入 NAT 网关详情页。
3) 单击监控tab，找到需要设置监控明细的IP，设置其出带宽限制。

### 查看网关流控明细
1)	登录[腾讯云控制台](https://console.cloud.tencent.com/)单击导航条【私有网络】，进入[私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=8)，选择【NAT网关】。
2) 在 NAT 网关列表中单击 ID 进入 NAT 网关详情页。
3) 单击监控tab，在网关流控明细表右上方，单击“查看已限制IP”。
