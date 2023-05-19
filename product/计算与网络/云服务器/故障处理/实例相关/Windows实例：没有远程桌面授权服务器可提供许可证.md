## 现象描述

使用 Windows 远程桌面连接 Windows 实例时，提示**由于没有远程桌面授权服务器可以提供许可证，远程会话连接已断开。请跟服务器管理员联系**。如下图所示：
![](https://main.qcloudimg.com/raw/4bfce19b16c2920adefccd123f2a021d.png)

## 可能原因
<table>
<thead>
  <tr>
    <th>可能原因</th>
    <th>处理措施</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>远程桌面会话主机角色授权到期</td>
    <td><a href="#step01">检查并删除远程桌面会话主机角色</a></td>
  </tr>
  <tr>
    <td>未在微软购买 License</td>
    <td><a href="#step02">检查并确保已购买 License</a></td>
  </tr>
</tbody>
</table>

## 故障处理
### 通过 VNC 方式登录云服务器[](id:eax)
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作，具体操作请参见：[使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。

### 检查并删除远程桌面会话主机角色[](id:step01)
<dx-alert infotype="explain" title="">
如果您不想删除**远程桌面会话主机**角色，可跳过此方案，前往 [微软官网](https://www.microsoft.com/zh-cn/) 购买与配置相应的证书授权。
</dx-alert>


1. 在操作系统界面，单击<img style="width:20px; max-width: inherit;" src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" />，打开**服务器管理器**。
2. 单击**服务器管理器**右上方的**管理**，选择**删除角色和功能**。如下图所示：
<img style="width:700px; max-width: inherit;" src="https://main.qcloudimg.com/raw/c50d1df5fdf65abd3f301ba904e80817.png" />
3. 在**删除角色和功能向导**窗口中，单击**下一步**。
4. 在**删除服务器角色**界面，取消勾选**远程桌面服务**，并在弹出的提示框中，选择**删除功能**。如下图所示：
![](https://main.qcloudimg.com/raw/974994d5cb387ea3aa8baec6ffdc9d7f.png)
5. 单击两次**下一步**。
6. 勾选**如果需要，自动重新启动目标服务器**，并在弹出的提示框中单击**是**。如下图所示：
<img style="width:700px; max-width: inherit;" src="https://main.qcloudimg.com/raw/bb3b938d970a225884ec36e61e18b526.png" />
7. 单击**删除**，待云服务器重新启动即可。

### 检查并确保已购买 License[](id:step02)

Windows Server 默认允许2个用户同时登录，可满足大多数需求。如果您需要超过2个用户同时登录，需要联系微软或微软合作伙伴等正规渠道购买多用户登录 RDS 授权。具体您可拨打微软市场部热线：**400-820-3800** 拨通之后再按提示选择对应按键，进行咨询购买。

<dx-alert infotype="notice" title="">
微软市场部热线电话可能会变化，也请您根据实际情况随机应变，谢谢您的理解。
</dx-alert>

