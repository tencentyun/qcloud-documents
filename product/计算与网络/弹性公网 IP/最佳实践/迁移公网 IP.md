本文为您介绍如何将同一账户内的云服务器上的公网 IP 迁移到另一个云服务器上。

## 操作场景
云服务器 A 发生故障，无法正常提供服务，需迁移云服务器 A 上的公网 IP 到健康的云服务器 B 上，以保障服务的正常提供。迁移的公网 IP，包括普通公网 IP 和弹性公网 IP（EIP）。

## 操作步骤
### 步骤一：将云服务器 A 上的普通公网 IP 转换为 EIP
>?
>- 若云服务器 A 上的公网 IP 已是 EIP，请跳过此步骤，执行 [步骤二：云服务器 A 解绑 EIP](#step2)。
>- 当前普通公网 IP 仅支持常规 BGP IP 线路类型。
>- 若您的账户为标准账户类型，则按带宽包年包月计费的普通公网 IP 暂不支持转换为 EIP。您可以将网络计费模式切换为按流量计费或带宽按小时后付费。注意切换网络计费模式后，代金券及购买优惠折扣不退还。若您后续重新变更计费模式为**包月带宽**，则需要重新按官网刊例价购买。若您无法确定账户类型，请参见 [判断账户类型](https://cloud.tencent.com/document/product/1199/49090#judge)。
>
EIP 拥有普通公网 IP 不具备的灵活绑定与解绑能力，若云服务器 A 上的公网 IP 为普通公网 IP，需转换为 EIP，利用 EIP 的能力进行公网 IP 的迁移。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
2. 在实例的管理页面，选择云服务器 A 的地域，并在所在行单击<img src="https://main.qcloudimg.com/raw/25e8c0e37b73c12da900301f03e57dbc.png" style="margin: -3px 0;"></img>。
>?普通公网 IP 转换为 EIP，IP 地址保持不变，且不中断您的服务，每个账户单个地域 EIP 配额数为20个。
>
![](https://main.qcloudimg.com/raw/93689324c72948a9746a4ab90223dd12.png)
3. 在弹出的 “转换为弹性公网 IP” 窗口中，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/05831183789dc337ee51d3f41ea44881.png" width="65%"> 


### <span id="step2" />步骤二：云服务器 A 解绑 EIP
将云服务器 A 与 EIP 进行解绑，解绑后，云服务器 A 将因为没有公网 IP 而无法访问公网。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
2. 在实例的管理页面，选择云服务器 A 的地域，并在所在行的操作栏下，单击**更多** > **IP/网卡** > **解绑弹性 IP**。
![](https://main.qcloudimg.com/raw/346f3844b9ec334d3081520417ea3236.png)
3. 在弹出的**解绑 EIP** 窗口中，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9218a431dc4bf59f82219e468e6b7319.png" width="65%">
4. 在弹出的提示框中，单击**确定**，完成 EIP 的解绑操作。
>?EIP 解绑后，请尽快执行步骤三，以节省 IP 资源费，IP 资源费按小时计费，精确到秒级，不足一小时，按闲置时间占比收取费用。

### 步骤三：绑定 EIP 到云服务器 B
将云服务器 A 解绑的 EIP 绑定到云服务器 B 上，完成公网 IP 的迁移。
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 选择云服务器 A 所在地域，并在列表中找到云服务器 A 解绑的 EIP 所在行，单击操作栏下的**更多** > **绑定**。
3. 在弹出的**绑定资源**窗口中，资源类型选择**CVM 实例**，选择需迁移 EIP 的目的云服务器 B，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/eaf5c4724e540cc945a291d81efca32a.png)
4. 在弹出的提示框中，单击**确定**。

### 步骤四：验证迁移结果
完成迁移后，您可以在云服务器列表页或 EIP 列表页中查看，该公网 IP 已经绑定到目的云服务器 B 上。
- **云服务器列表页**
 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
 2. 在实例的管理页面，选择云服务器 B 的地域，并在列表中找到云服务器 B 所在行，即可查看到已成功迁移公网 IP。
![](https://main.qcloudimg.com/raw/fe61e09338c810039ac0d240c8757e9d.png)
- **EIP 列表页**
 1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
 2. 选择云服务器 B 所在地域，并在列表中找到迁移的 EIP 所在行，即可查看到该 EIP 已成功绑定云服务器 B。
![](https://qcloudimg.tencent-cloud.cn/raw/59a000151dd937ae55e31cbcbbaf0c24.png)
