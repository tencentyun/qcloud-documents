## 操作场景

部分 Linux 系统镜像的 VNC 默认显示分辨率较小，如 CentOS 6 的 VNC 默认分辨率只有 720 \* 400。您可以通过修改  grub 参数，将 Linux 系统镜像的 VNC 分辨率设置为1024 \* 768。
对于 Window 系统镜像，当 VNC 分辨率过低时，可能会影响某些项目的正常显示或者导致某些应用无法打开。您可以通过进行修改分辨率，避免这些问题。

本文档将引导您调整云服务器的 VNC 显示分辨率。

## 操作步骤

### 修改 Windows 实例的 VNC 分辨率

>? 下面以 Windows Server 2012 中文版系统镜像为例，引导您修改 Windows 实例的 VNC 分辨率。
>

1. [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，单击鼠标右键，选择**屏幕分辨率**。如下图所示：
![](https://main.qcloudimg.com/raw/1543dadac81f8b0491062902c69ff1a5.png)
3. 在打开的屏幕分辨率窗口中，设置**分辨率**的大小，单击**应用**。如下图所示：
![](https://main.qcloudimg.com/raw/89b188408b7c9668270326d5a53c16ae.png)
4. 在弹出的提示框中，单击**保留更改**。
5. 单击**确定**，关闭屏幕分辨率窗口。

### 修改 Linux 实例的 VNC 分辨率

Linux 系统镜像有许多类型，其中如 CentOS 7、CentOS 8、Ubuntu、Debian 9.0 等较新的系统镜像，VNC 默认分辨率为1024 \* 768，无需修改 VNC 分辨率。下面以 CentOS 6 和 Debian 7.8 为例，引导您修改 VNC 分辨率。

#### CentOS 6

针对 CentOS 6 系统镜像，VNC 默认分辨率为 720 \* 400。通过修改 grub 启动参数，可以将 VNC 分辨率设置为 1024 \* 768。其设置方式如下：
1. [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
 - [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
 - [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
 - [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)
2. 在操作系统界面，执行以下命令，打开 `grub.conf` 文件。
```
vim /etc/grub.conf
```
3. 按 **i** 切换至编辑模式，并在 `grub` 参数值中添加 `vga=792`。如下图所示：
![](https://main.qcloudimg.com/raw/3c2193fa370c48a7af149c63720da077.png)
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，重启云服务器。
```
reboot
```

#### Debian 7.8

Debian 7.8 和 Debian 8.2 系统镜像的 VNC 默认分辨率为 720 \* 400。通过修改 grub 启动参数，可以将 VNC 分辨率设置为 1024 \* 768。其设置方式如下：
1. [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
 - [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
 - [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
 - [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)
2. 在操作系统界面，执行以下命令，打开 grub 文件。
```
vim /etc/default/grub
```
3. 按 **i** 切换至编辑模式，并在 `GRUB_CMDLINE_LINUX_DEFAULT` 参数值后面添加 `vga=792`。如下图所示：
![](https://main.qcloudimg.com/raw/f8e275c35b65b7b2d26cfbd7a8ae4dd6.png)
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，更新 `grub.cfg` 文件。
```
grub-mkconfig -o /boot/grub/grub.cfg
```
6. 执行以下命令，重启云服务器。
```
reboot
```


## 附录

Linux 实例分辨率与 VGA 的参数对照表如下：
<table>
	<tr><th>分辨率</th><td>640 * 480</td><td>800 * 600</td><td>1024 * 768</td></tr>
	<tr><th>VGA</th><td>786</td><td>789</td><td>792</td></tr>
</table>
