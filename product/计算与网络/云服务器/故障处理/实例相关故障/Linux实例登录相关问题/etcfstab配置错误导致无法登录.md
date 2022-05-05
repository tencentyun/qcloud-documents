## 现象描述[](id:symptom)
无法成功登录云服务器，且使用 VNC 方式登录后，查看系统启动失败且提示信息 “Welcome to emergency mode”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dea541a48d2a01503c1dbbc85b0d396f.png)


## 可能原因
可能由于 `/etc/fstab` 配置不当导致。
例如，已在 `/etc/fstab` 中配置使用设备名称自动挂载磁盘，但云服务器重启时设备名称发生改变，导致系统无法正常启动。


## 解决思路
参考 [处理步骤](#ProcessingSteps) 修复 `/etc/fstab` 配置文件，重启服务器后再进行核验。


## 处理步骤[](id:ProcessingSteps)

您可通过以下2种方式进入实例并处理该问题：

<dx-tabs>
::: 方式1：使用 VNC 登录（推荐）[](id:useVNC)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 进入 VNC 界面后，查看到如 [现象描述](#symptom) 中所示界面，请输入 root 帐户密码并按 **Enter** 登录服务器。
 - 输入的密码默认不显示。
 - 若您不具备或忘记 root 帐户密码，则请参考方式2进行处理。
3. [](id:Step3)执行以下命令，备份 `/etc/fstab` 文件。本文以备份到 `/home` 目录下为例：
```shellsession
cp /etc/fstab /home
```
4. 执行以下命令，使用 VI 编辑器打开 `/etc/fstab` 文件。
```shellsession
vi /etc/fstab
```
5. 按 **i** 进入编辑模式，将光标移动至错误配置行首，并输入 `#` 注释该行配置。如下图所示：
<dx-alert infotype="explain" title="">
若您无法确定错误配置，则建议先注释除系统盘外的所有挂载盘配置，待服务器恢复正常后再参考 [步骤8](#Step7) 进行配置。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/1c238789186d7f24c0244e0307bc3a22.png"/>
6. [](id:Step6)按 **Esc** 输入 **:wq** 后，按 **Enter** 保存设置并退出编辑器。
7. 通过控制台重启实例，并在启动后验证是否可正常启动及登录。
<dx-alert infotype="explain" title="">
通过控制台重启实例具体步骤请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
</dx-alert>
8. [](id:Step8)登录成功后，若您需设置磁盘自动挂载，则请参考 [配置 /etc/fstab 文件](https://cloud.tencent.com/document/product/362/53951#ConfigurationFile) 进行对应配置。

:::
::: 方式2：使用救援模式[](id:useRescue)
1. 参考 [使用救援模式](https://cloud.tencent.com/document/product/213/66678)，进入实例救援模式。
<dx-alert infotype="notice" title="">
需执行 [使用救援模式进行系统修复](https://cloud.tencent.com/document/product/213/66678#.E4.BD.BF.E7.94.A8.E6.95.91.E6.8F.B4.E6.A8.A1.E5.BC.8F.E8.BF.9B.E8.A1.8C.E7.B3.BB.E7.BB.9F.E4.BF.AE.E5.A4.8D) 步骤中的 `mount` 及 `chroot` 相关命令，且确保已进入业务本身的系统。
</dx-alert>
2. 按照方式1中的 [步骤3](#Step3) - [步骤6](#Step6)，修复 `/etc/fstab` 文件。
3. 参考 [退出救援模式](https://cloud.tencent.com/document/product/213/66678#.E9.80.80.E5.87.BA.E6.95.91.E6.8F.B4.E6.A8.A1.E5.BC.8F)，退出实例救援模式。
4. 实例退出救援模式后将处于关机状态，请参考 [开机实例](https://cloud.tencent.com/document/product/213/47929) 开机，并在启动后验证系统是否可正常启动及登录。
5. 登录成功后，若您需设置磁盘自动挂载，则请参考 [配置 /etc/fstab 文件](https://cloud.tencent.com/document/product/362/53951#ConfigurationFile) 进行对应配置。

:::
</dx-tabs>







