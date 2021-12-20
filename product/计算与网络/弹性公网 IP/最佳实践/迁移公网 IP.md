本文为您介绍如何将同一账户内的云服务器上的公网 IP 迁移到另一个云服务器上。

## 操作场景
云服务器 A 发生故障，无法正常提供服务，需迁移云服务器 A 上的公网 IP 到健康的云服务器 B 上，以保障服务的正常提供。迁移的公网 IP，包括普通公网 IP 和弹性公网 IP（EIP）。

## 操作步骤
### 步骤一：将云服务器 A 上的普通公网 IP 转换为 EIP
>?若云服务器 A 上的公网 IP 已是 EIP，请跳过此步骤，执行 [步骤二：云服务器 A 解绑 EIP](#step2)。
>
EIP 拥有普通公网 IP 不具备的灵活绑定与解绑能力，若云服务器 A 上的公网 IP 为普通公网 IP，需转换为 EIP，利用 EIP 的能力进行公网 IP 的迁移。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
2. 在实例的管理页面，选择云服务器 A 的地域，并在所在行单击<img src="https://main.qcloudimg.com/raw/25e8c0e37b73c12da900301f03e57dbc.png" style="margin: -3px 0;"></img>。
>?普通公网 IP 转换为 EIP，IP 地址保持不变，且不中断您的服务，每个账户单个地域 EIP 配额数为20个。
>
![](https://main.qcloudimg.com/raw/93689324c72948a9746a4ab90223dd12.png)
3. 在弹出的 “转换为弹性公网IP” 窗口中，单击**确定**。
![](https://main.qcloudimg.com/raw/471859c38ddc18538b5e342453e37985.png)

### <span id="step2" />步骤二：云服务器 A 解绑 EIP
将云服务器 A 与 EIP 进行解绑，解绑后，云服务器 A 将因为没有公网 IP 而无法访问公网。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
2. 在实例的管理页面，选择云服务器 A 的地域，并在所在行的操作栏下，单击**更多** > **IP/网卡** > **解绑弹性 IP**。
![](https://main.qcloudimg.com/raw/346f3844b9ec334d3081520417ea3236.png)
3. 在弹出的“解绑弹性公网IP”窗口中，单击**确定**。
![](https://main.qcloudimg.com/raw/2934137c578408e591a1d9042b7a3a3c.png)
4. 在弹出的提示框中，单击**确定**，完成 EIP 的解绑操作。
>?EIP 解绑后，请尽快执行步骤三，以节省 IP 资源费，IP 资源费按小时计费，精确到秒级，不足一小时，按闲置时间占比收取费用。

### 步骤三：绑定 EIP 到云服务器 B
将云服务器 A 解绑的 EIP 绑定到云服务器 B 上，完成公网 IP 的迁移。
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 选择云服务器 A 所在地域，并在列表中找到云服务器 A 解绑的 EIP 所在行，单击操作栏下的**更多** > **绑定**。
3. 在弹出的“绑定资源”窗口中，资源类型选择**CVM 实例**，选择需迁移 EIP 的目的云服务器 B，单击**确定**。
![](https://main.qcloudimg.com/raw/e6424cd51bf47208d62ac9414672048f.png)
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



