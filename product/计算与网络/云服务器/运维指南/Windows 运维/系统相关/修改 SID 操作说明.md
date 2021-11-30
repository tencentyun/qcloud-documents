## 操作场景

安全标识符（SID）被微软操作系统对于计算机和用户进行识别。由于基于同一镜像生产的云服务器实例 SID 相同，会引起无法入域的问题。如果您需要搭建 Windows 域环境，则需要通过修改 SID 以达到入域的目的。
本文档以 Windows Server 2012 操作系统云服务器为例，介绍如何使用系统自带 sysprep 以及 sidchg 工具修改 SID。

## 注意事项

- 本说明仅适用于 Windows Server 2008 R2 、Windows Server 2012 以及Windows Server 2016。
- 如果有批量修改 SID 的需求，可通过制作自定义镜像（选择 “执行 sysprep 制作镜像”）解决。
- 修改 SID 可能导致数据丢失或系统损坏，建议您提前做好系统盘快照或者镜像。

## 操作方式

### 使用 sysprep 修改 SID



<dx-alert infotype="notice" title="">
- 使用 sysprep 修改 SID 后，系统参数很多都被重新设置，包括 IP 配置信息等，您必须手动重新设置。
- 使用 sysprep 修改 SID 后，C:\Users\Administrator 将会被重置，系统盘部分数据将被清理，请注意做好数据备份。
</dx-alert>


1. [使用 VNC 方式登录云服务器](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"> > **运行**，输入 **cmd**，按 **Enter**，打开管理员命令行工具。
3. [](id:step_03)在管理员命令行工具中，执行以下命令，保存当前网络配置。
```
ipconfig /all
```
4. 在管理员命令行工具中，执行以下命令，打开 sysprep 工具。
```
C:\Windows\System32\Sysprep\sysprep.exe
```
5. 在打开的 “系统准备工具 3.14” 窗口中，进行以下设置。如下图所示：
![](https://main.qcloudimg.com/raw/d94e4a96b8ca82052d91e9bb9d8fecbf.png)
 - 将**系统清理操作**设置为**进入系统全新体验 (OOBE)**，并勾选“通用”。
 - 将**关机选项**设置为**重新启动**。
6. 单击**确定**，系统自动重新启动。
7. 待完成启动后，按照向导完成配置（选择语言、重设密码等）。
8. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"> > **运行**，输入 **cmd**，按 **Enter**，打开管理员命令行工具。
9. 执行以下命令，验证 SID 是否已修改。
```
whoami /user
```
返回类似如下信息，则表示 SID 已完成修改。
![](https://main.qcloudimg.com/raw/656f5974a213347edc75c49c6e7ec166.png)
10. 根据 [步骤3](#step_03) 保存的网络配置信息，重新设置网卡相关信息（如 IP 地址、网关地址、DNS 等）。


### 使用 sidchg 修改 SID

1. 登录云服务器。
2. 通过 IE 浏览器访问和下载 sidchg 工具。
sidchg 工具下载地址：`http://www.stratesave.com/html/sidchg.html`
3. 使用管理员命令行工具，执行以下命令，打开 sidchg 工具。如下图所示：
例如，sidchg 工具保存在 C: 盘中，其名称为 sidchg64-2.0p.exe。
![](https://main.qcloudimg.com/raw/284926ae1eae88228fb009f247b82068.png)
其中，`/R` 表示修改后自动重启，`/S` 表示修改后关闭，使用详情请参照 [SIDCHG 官方说明](http://www.stratesave.com/html/sidchg.html)。
4. 根据界面提示，输入 license key 或者  trial key，按 **Enter**。
5. 根据界面提示，输入 **Y**，按 **Enter**。如下图所示：
![](https://main.qcloudimg.com/raw/43c19634475517b183402d15fa32e962.png)
6. 在修改 SID 的提示框中，单击**确定**，进行 SID 重置。如下图所示：
重置过程中，系统将会被重启。
![](https://main.qcloudimg.com/raw/406a1669402ecc33e85f7c42a51bc25d.png)
7. 待完成启动后，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;"> > **运行**，输入 **cmd**，按 **Enter**，打开管理员命令行工具。
8. 执行以下命令，验证 SID 是否已修改。
```
whoami /user
```
返回类似如下信息，则表示 SID 已完成修改。
![](https://main.qcloudimg.com/raw/656f5974a213347edc75c49c6e7ec166.png)

