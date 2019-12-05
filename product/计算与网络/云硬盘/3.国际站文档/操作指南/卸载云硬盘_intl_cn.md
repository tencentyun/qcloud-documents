当您需要将 ***弹性云盘*** 挂载到另一台实例上使用时，您可以主动地从实例断开该弹性云盘，并将其连接到其他实例上。<font color="red">卸载弹性云盘并不会清除该硬盘上的数据。</font>

## 使用控制台卸载弹性云盘

目前支持对作为数据盘的普通弹性云盘云盘进行卸载，不可卸载系统盘。

<font color="red">
卸载数据盘时，请确保您了解以下事项：
</font>

- 在 Windows 操作系统下，为了保证数据完整性，建议您暂停对该磁盘的所有文件系统的读写操作，否则未完成读写的数据会丢失。<font color="red">解挂弹性云盘时需要先将磁盘设为脱机状态，否则在不重启云主机的情况下，您可能将无法再次挂载弹性云盘。</font>
![](//mccdn.qcloud.com/static/img/92a187945b9f4318981ea70b6532e1d6/image.png)

- 在 Linux 操作系统下，您需要先登录实例，并对需要卸载的弹性云硬盘进行` unmount `操作，命令执行成功后再进入控制台对磁盘进行卸载操作。若未进行unmount操作直接被强制解挂后，关机时和开机时可能会出现以下问题： 
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)
![](//mccdn.qcloud.com/static/img/9939fccce6e6d9ead64b5703455d4403/image.png)

1) 登录[腾讯云控制台](https://console.cloud.tencent.com/)。

2) 进入【云服务器】-【云硬盘】选项卡。

3) 在云硬盘列表页，点击状态为<font color="red">已挂载、支持挂载/卸载</font>的云硬盘后的【更多】-【卸载】按钮进行单盘卸载；
或在云硬盘列表页，勾选状态为<font color="red">已挂载、支持挂载/卸载</font>状态的云硬盘，点击顶部【挂载】按钮进行批量挂载。

4) 在弹出的对话框中确认警告事项，点击【确认】按钮。

## 使用 API 卸载弹性云盘
用户可以使用 DetachCbsStorages 接口卸载弹性云盘，具体内容请参考 [解挂弹性云盘接口](https://cloud.tencent.com/doc/api/364/2521)。