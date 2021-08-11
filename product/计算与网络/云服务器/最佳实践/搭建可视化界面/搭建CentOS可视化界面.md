## 操作场景
本文以操作系统为 CentOS 8.2 及 CentOS 7.9 的腾讯云云服务器为例，介绍如何搭建 CentOS 可视化界面。

## 说明事项
- 基于性能及通用性考虑，腾讯云提供的 Linux 公共镜像默认不安装图形化组件。
- 如安装不当可能造成实例无法正常启动，建议您通过 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 或 [创建快照](https://cloud.tencent.com/document/product/362/5755) 进行数据备份。

## 操作步骤
请对应您实际使用的云服务器操作系统，参考以下步骤进行操作：
<dx-tabs>
::: CentOS\s8.2
1. 登录实例，详情请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装图形化界面组件。
```
yum groupinstall "Server with GUI" -y
```
3. 执行以下命令，设置默认启动图形化界面。
```
systemctl set-default graphical
```
4. 执行以下命令，重启实例。
```
reboot
```
5. 以 VNC 方式登录实例，详情请参见 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
登录实例后查看可视化界面即表示搭建成功，根据界面提示进行配置进入桌面后，可按需进行相关操作。如下图所示：
![](https://main.qcloudimg.com/raw/58e12a33b38e0114f5b3116b31f7b026.png)
:::
::: CentOS\s7.9
1. 登录实例，详情请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，安装图形化界面组件。
```
yum groupinstall "GNOME Desktop" "Graphical Administration Tools" -y
```
3. 执行以下命令，设置默认启动图形化界面。
```
ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target
```
4. 执行以下命令，重启实例。
```
reboot
```
5. 以 VNC 方式登录实例，详情请参见 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
登录实例后查看可视化界面即表示搭建成功，根据界面提示进行配置进入桌面后，可按需进行相关操作。如下图所示：
![](https://main.qcloudimg.com/raw/ae361df3eb2c224a92a754e1f693c06d.png)
:::
</dx-tabs>
