## 操作场景
本文介绍如何修改轻量应用服务器 Windows 实例的显示分辨率，您可参考本文进行操作。

## 操作步骤
您可根据所使用的登录方式，选择对应操作步骤：
<dx-tabs>
::: 使用\sVNC\s方式登录\sWindows\s实例
>? 本文以系统镜像 Windows Server 2012 R2为例，不同版本的操作系统步骤有一定区别，请结合您的实际情况参考本文进行设置。
>
1. [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)。
2. 在操作系统界面，单击鼠标右键，选择【屏幕分辨率】。如下图所示：
![](https://main.qcloudimg.com/raw/4078cc166eb9532e1db18930b46c6ff8.png)
3. 在“屏幕分辨率窗口”中，设置“分辨率”的大小，并单击【应用】。如下图所示：
![](https://main.qcloudimg.com/raw/c9d63ed48f4f15625d3ff3eb7efae525.png)
4. 在弹出的提示框中，单击【保留更改】。
5. 单击【确定】，关闭屏幕分辨率窗口。
:::
::: 使用远程桌面连接登录\sWindows\s实例
使用远程桌面连接登录 Windows 实例后，无法在系统内部调整桌面的分辨率。您需在登录前使用远程桌面工具，设置实例分辨率。以下操作步骤中，本地系统以 Windows 10 为例：
1. 在本地 Windows 计算机上，选择 <img src="https://main.qcloudimg.com/raw/19cdc57ebc3fc56da3ff6d77010a6e3a.png" style="margin:-5px 0px"> 后单击【运行】。
2. 在“运行”窗口中，输入 mstsc 并单击【确定】，打开远程桌面连接对话框。
3. 在“远程桌面连接”窗口中，选择【显示选项】。如下图所示：
![](https://main.qcloudimg.com/raw/8499ae42b8707bf4dad640475bbfc34b.png)
4. 选择“显示”，在“显示配置”中调节分辨率。如下图所示：
![](https://main.qcloudimg.com/raw/2d15df46d98e25445bf5f4ca34886e11.png)
5. 单击【连接】，[使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44579)。
:::
</dx-tabs>

