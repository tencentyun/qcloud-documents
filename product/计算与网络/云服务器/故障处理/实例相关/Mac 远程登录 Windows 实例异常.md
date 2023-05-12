您的 Mac 通过 Microsoft Remote Desktop 远程连接登录 Windows 时遇到的常见故障现象如下。
## 现象现象

- Mac 通过 Microsoft Remote Desktop 远程连接登录 Windows 时，提示 **The certificate couldn't be verified back to a root certificate**。
<img style="width:950px; max-width: inherit;" src="https://main.qcloudimg.com/raw/070b9c862d6928988768b266461bc816.png" data-nonescope="true" />
- Mac 远程桌面连接（Remote Desktop Connection）时，提示**远程桌面连接无法验证您希望连接的计算机的身份**。
<img src="https://main.qcloudimg.com/raw/32f0444a47b2e4c90f6657ec9686afcb.png" data-nonescope="true">

## 可能原因：
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
    <td>系统未修改实例本地组策略</td>
    <td><a href="#inodeFull"> 检查系统是否修改实例本地组策略</a></td>
  </tr>
</tbody>
</table>

## 故障处理

<dx-alert infotype="explain" title="">
以下操作以 Windows Server 2016 为例。
</dx-alert>


### 通过 VNC 方式登录云服务器[](id:diskSpaceFull)
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。具体操作请参见：[使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。

### 检查系统是否修改实例本地组策略[](id:inodeFull)

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/330624bafb194914948c8ebd9e47334d.png" style="margin: 0;">，输入 **gpedit.msc**，按 **Enter**，打开**本地组策略编辑器**。
<dx-alert infotype="explain" title="">
也可使用 **Win+R** 快捷键打开运行界面。
</dx-alert>
2. 在左侧导航树中，选择**计算机配置** > **管理模板** > **Windows组件** > **远程桌面服务** > **远程桌面会话主机** > **安全**，双击**远程（RDP）连接要求使用指定的安全层**。如下图所示：
![](https://main.qcloudimg.com/raw/cfcb737815f047d5542ced1658eb354f.png)
3. 在打开的 **远程（RDP）连接要求使用指定的安全层** 窗口中，选择**已启用**，并将**安全层**设置为 **RDP**。如下图所示：
![](https://main.qcloudimg.com/raw/25245ed985e5317078c80fa82d375a59.png)
4. 单击**确定**，完成设置。
5. 重启实例，重新尝试连接是否成功。
如果还是无法成功，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213) 进行反馈。

