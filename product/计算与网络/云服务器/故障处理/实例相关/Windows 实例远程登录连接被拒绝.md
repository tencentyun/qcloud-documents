## 现象描述
[](id:FaultPhenomenon1)
- **现象1**：Windows 使用远程桌面连接 Windows 实例时，提示**连接被拒绝，因为没有授权此用户帐户进行远程登录**。如下图所示：

![连接被拒绝](https://main.qcloudimg.com/raw/9ce749a2481cabf30cccdefeb00ae770.png)

[](id:FaultPhenomenon2)
- **现象2**：Windows 使用远程桌面连接 Windows 实例时，提示**要远程登录，您需要具有通过远程桌面服务进行登录的权限。默认情况下，远程桌面用户组的成员有这项权限。如果您所属的组没有这项权限，或者远程桌面用户组中已经删除了这项权限，那么需要手动为您授予这一权限**。如下图所示：

![错误提示](https://main.qcloudimg.com/raw/52a79c81015d7e6b2f5299f98474348d.png)

## 可能原因
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
    <td>未配置允许远程登录的权限</td>
    <td><a href="#ConfigurationToAllowAccess"> 检查并配置允许远程登录的权限</a></td>
  </tr>
  <tr>
    <td>未修改拒绝远程登录的权限</td>
    <td><a href="#ModifyLoginAuthority">检查并修改拒绝远程登录的权限</a></td>
  </tr>
</tbody>
</table>


## 故障处理

### 通过 VNC 方式登录云服务器[](id:tcpPacketLoss)

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作，具体操作请参见：[使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。


### [检查并配置允许远程登录的权限](id:ConfigurationToAllowAccess)

如果您远程桌面连接 Windows 实例时，遇到 [现象1](#FaultPhenomenon1) 的情况，则需要将用户账号添加至 Windows 实例设置的允许通过远程桌面服务登录的列表中。具体的操作请参见 [检查并配置允许远程登录的权限](#ConfigurationToAllowAccess)。

<dx-alert infotype="explain" title="">
以下操作以 Windows Server 2016 为例。
</dx-alert>

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开**本地组策略编辑器**。
2. 在左侧导航树中，选择**计算机配置** > **Windows 设置** > **安全设置** > **本地策略** > **用户权限分配**，双击打开**允许通过远程桌面服务登录**。如下图所示：
![](https://main.qcloudimg.com/raw/0a9f64957539a37d3c930932e24213c0.png)
3. 在打开的**允许通过远程桌面服务登录**属性窗口中，检查允许通过远程桌面服务登录的用户列表是否存在需要登录的账号。如下图所示：
![允许通过远程桌面服务登录](https://main.qcloudimg.com/raw/acd4d3cb6204a34c612b32c777308f9f.png)
 - 如果该用户不在允许通过远程桌面服务登录的列表中，请执行 [步骤4](#step04)。
 - 如果该用户已经在允许通过远程桌面服务登录的列表中，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213) 反馈。
4. [](id:step04)单击**添加用户或组**，打开**选择用户或组**窗口。
5. 输入需要进行远程登录的账号，单击**确定**。
6. 单击**确定**，并关闭本地组策略编辑器。
7. 重启实例，重新尝试使用该账号远程桌面连接 Windows 实例。


### [检查并修改拒绝远程登录的权限](id:ModifyLoginAuthority)

如果您远程桌面连接 Windows 实例时，遇到 [现象2](#FaultPhenomenon2) 的情况，则需要将用户账号从 Windows 实例设置的不允许通过远程桌面服务登录的列表中删除。具体的操作请参见 [检查并修改拒绝远程登录的权限](#ModifyLoginAuthority)。
<dx-alert infotype="explain" title="">
以下操作以 Windows Server 2016 为例。
</dx-alert>

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开**本地组策略编辑器**。
2. 在左侧导航树中，选择**计算机配置** > **Windows 设置** > **安全设置** > **本地策略** > **用户权限分配**，双击打开**拒绝通过远程桌面服务登录**。如下图所示：
![拒绝通过远程桌面服务登录](https://main.qcloudimg.com/raw/aaea1d8c0dadb73676a926ed0ed56367.png)
3. 在打开的**拒绝通过远程桌面服务登录**属性窗口中，检查拒绝通过远程桌面服务登录的用户列表是否存在需要登录的账号。
 - 如果该用户在拒绝通过远程桌面服务登录的列表中，请将需要登录的账号从列表中删除，并重启实例。
 - 如果该用户不在拒绝通过远程桌面服务登录的列表中，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213) 反馈。
 
 
