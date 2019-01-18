> **注意：**
> 本说明仅适用于 Windows Server 2008 R2 和 Windows Server 2012 系统，如果有批量修改 SID 的需求，可通过制作自定义镜像（选择“执行 sysprep 制作镜像”）解决。

## 背景介绍
微软操作系统使用安全标识符（SID）对计算机和用户进行识别。如果需要搭建 Windows 域环境，由于基于同一镜像生产的云主机 SID 相同，会引起无法入域的问题，此时需要通过修改 SID 以达到入域的目的。

## 操作说明
1. 使用控制台 VNC 登录到云主机。[点击查看操作指南](https://cloud.tencent.com/doc/product/213/2155)
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
