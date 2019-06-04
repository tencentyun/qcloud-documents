## 操作场景

安全标识符（SID）被微软操作系统对于计算机和用户进行识别。如果需要搭建 Windows 域环境，由于基于同一镜像生产的云服务器实例 SID 相同，会引起无法入域的问题，此时需要通过修改 SID 以达到入域的目的。
下面将介绍如何使用系统自带 sysprep 以及 sidchg 工具修改 SID 的方法。

> **注意：**
> - 本说明仅适用于 Windows Server 2008 R2 、Windows Server 2012 以及Windows Server 2016。
> - 如果有批量修改 SID 的需求，可通过制作自定义镜像（选择 “执行 sysprep 制作镜像”）解决。
> - 修改 SID 可能导致数据丢失或系统损坏，建议您提前做好系统盘快照或者镜像。

## 操作方式

### 使用 sysprep 修改 SID

> **注意：**
> - 使用 sysprep 修改 SID 后，系统参数很多都被重新设置，包括 IP 配置信息等，您必须手动重新设置。
> - 使用 sysprep 修改 SID 后，C:\Users\Administrator 将会被重置，系统盘部分数据将被清理，请注意做好数据备份。

1. 使用控制台 VNC 登录到云服务器实例。单击 [查看操作指南](https://cloud.tencent.com/doc/product/213/2155)。
2. 保存当前网络配置。
单击【开始】>【运行】，输入命令 `cmd` 打开命令行界面，执行命令 `ipconfig /all` ，将结果信息记录或截图保存。
3. 打开 sysprep 工具。
 运行位于 `C:\windows\system32\sysprep` 文件夹下的 `sysprep.exe` 程序。
【系统清理操作】选择 **进入系统全新体验（OOBE）**，同时勾选【通用】选项，【关机选项】选择 **重新启动**。
 ![](//mccdn.qcloud.com/static/img/1dfa18a861c0a70b880b5130ff40d572/image.png)
4. 单击 **确定** 后系统重新启动，启动后按照向导完成配置（选择语言、重设密码等）。
5. 验证 SID。
单击【开始】>【运行】，输入 `cmd` 打开命令行界面，执行命令 `whoami /user `，验证 SID 是否已修改。
 ![](//mccdn.qcloud.com/static/img/6c1c0784b3e51b5dca3a19f381ea2e02/image.png)
6. 参照步骤 2 保存的配置信息重新设置网卡相关信息（IP 地址、网关地址、DNS 等）。

### 使用 sidchg 修改 SID
1. 下载 [sidchg](http://www.stratesave.com/html/sidchg.html) 工具。
2. 命令行执行 sidchg64-2.0n.exe /R. 根据提示输入 Trial key 或者 license，然后回车。sidchg 提供了多个启动选项，其中 /R 表示修改后自动重启，/S 表示修改后关闭，使用详情请参照 [官方说明](http://www.stratesave.com/html/sidchg.html)。
注：sidchg64-2.0n.exe 为 64位 版本。
 ![](https://main.qcloudimg.com/raw/18884c02b7775a138e5fc1d45eddf3a9.png)
3. 提示修改 SID 可能引发数据丢失或者系统损坏，是否继续？输入 Y，回车进行设置。
 ![](https://main.qcloudimg.com/raw/2ddf9c5f9a66703ac1a20f3eaeb94ed6.png)
4. 单击确认。将会进行 SID 重置，系统将会被重启。
![](https://main.qcloudimg.com/raw/406a1669402ecc33e85f7c42a51bc25d.png)
5. 验证 SID。系统重启完成后，重新登录。
单击【开始】>【运行】，输入 `cmd` 打开命令行界面，执行命令 `whoami /user `，验证 SID 是否已修改。
 ![](//mccdn.qcloud.com/static/img/6c1c0784b3e51b5dca3a19f381ea2e02/image.png)
