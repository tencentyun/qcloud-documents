通常情况下，多数 Linux 系统类问题可通过 VNC 方式及救援模式进行排查及修复。本文介绍如何使用这两种方式排查 Linux 实例无法 SSH 登录、系统失败问题。您可通过本文了解并在遇到实例问题时，进行排查及修复。


## 排查工具
- VNC 登录是通过 Web 浏览器远程连接云服务器的方式，一般在无法正常 SSH 远程登录实例时使用。使用 VNC 登录方式可直接观察云服务器状态，或进行修改系统内配置文件等操作。
- 救援模式一般在 Linux 系统无法正常启动，或无法通过 VNC 登录时使用。常见使用场景例如 fstab 配置异常、系统关键文件缺失、lib 动态库文件损坏/缺失等。

## 问题定位及处理

<dx-accordion>
::: VNC 方式排查 SSH 无法登录问题[](id:cantSSHlogin)
#### 现象描述
使用 SSH 登录 Linux 实例时，出现报错信息 “ssh_exchange_identification: Connection closed by remote host”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4cfe14beb79b3b7b1b617fce540a53a0.png)



#### 可能原因
kex_exchange_identification 阶段的 connection reset 报错，一般代表 ssh 相关进程已启动，但是配置可能存在异常，例如 sshd 配置文件权限被修改。


#### 解决思路
参考 [处理步骤](#ProcessingSteps1)，检查 sshd 进程，定位并解决问题。


#### 处理步骤[](id:ProcessingSteps1)
1. [](id:ProcessingSteps1Step1)参考以下步骤，使用 VNC 登录 Linux 实例：
   1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，找到需要登录的 Linux 云服务器，单击右侧的**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/e82e7f4b606fc59d26990285d7bdbaa3.png)
 2. 在打开的“标准登录 | Linux 实例”窗口，单击 **VNC登录**。如下图所示：
![](https://main.qcloudimg.com/raw/600264310b8e778ffadaa164a597faae.png)
 3. 在 “login” 后输入用户名，按 **Enter**，在 “Password” 后输入密码，按 **Enter**。如下图所示即为登录成功：
 ![](https://main.qcloudimg.com/raw/69bd64692fdaffc0cbbbdd0b9d307722.png)
2. 执行以下命令，查看 sshd 进程是否正常运行。
```shellsession
ps -ef | grep sshd
```
返回结果如下图所示，sshd 进程正常。
![](https://qcloudimg.tencent-cloud.cn/raw/c1024ca17237af64df91503164854983.png)
3. 执行以下命令，查看报错原因。
```shellsession
sshd -t
```
返回类似如下图所示信息 “/var/empty/sshd must be owned by root and not group or world-writable.
”，可定位错误原因为 `/var/empty/sshd/` 权限问题导致。
![](https://qcloudimg.tencent-cloud.cn/raw/19912fbd3406488556cf2e2937a6c2de.png)
您还可通过查看 `/var/log/secure` 日志中的报错信息来辅助排查。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a696b1ce175631aebcfb92037680b506.png)
4. 执行以下命令，查看 `/var/empty/sshd` 目录权限。
```shellsession
ll -d /var/empty/sshd/
```
返回结果如下图所示，可知权限被修改为777。
![](https://qcloudimg.tencent-cloud.cn/raw/952ac209bb81e882474f413b31bedfc1.png)
5. 执行以下命令，修改 `/var/empty/sshd/` 文件权限。
```shellsession
chmod 711 /var/empty/sshd/
```
参考 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 测试后，可正常远程登录实例。


:::
::: VNC 方式排查 Linux 系统启动失败问题[](id:OSStartupFailed)

#### 现象描述[](id:symptom)
无法成功登录云服务器，且使用 VNC 方式登录后，查看系统启动失败且提示信息 “Welcome to emergency mode”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dea541a48d2a01503c1dbbc85b0d396f.png)


#### 可能原因
可能由于 `/etc/fstab` 配置不当导致。
例如，已在 `/etc/fstab` 中配置使用设备名称自动挂载磁盘，但云服务器重启时设备名称发生改变，导致系统无法正常启动。


#### 解决思路
参考 [处理步骤](#ProcessingSteps2) 修复 `/etc/fstab` 配置文件，重启服务器后再进行核验。


#### 处理步骤[](id:ProcessingSteps2)
1. 参考 [处理步骤1](#ProcessingSteps1Step1)，使用 VNC 登录 Linux 实例。
2. 进入 VNC 界面后，查看到如 [现象描述](#symptom) 中所示界面，请输入 root 帐户密码并按 **Enter** 登录服务器。输入的密码默认不显示，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7b9a8cdc6fe38ca6cb1e571790a54894.png)
3. 进入系统后，执行以下命令，查看 fstab 文件中盘符信息是否正确。
```shellsession
lsblk
```
返回结果如下图所示，文件中盘符信息有误：
![](https://qcloudimg.tencent-cloud.cn/raw/be6158d53fcb6e261be719f523cacb93.png)
4. 执行以下命令，备份 fstab 文件。
```shellsession
cp /etc/fstab /home
```
5. 执行以下命令，使用 VI 编辑器打开 `/etc/fstab` 文件。
```shellsession
vi /etc/fstab
```
6. 按 **i** 进入编辑模式，将光标移动至错误配置行首，并输入 `#` 注释该行配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a2d9e675d6586341e6b5e3a221ee7906.png)
7. 按 **Esc** 输入 **:wq** 后，按 **Enter** 保存设置并退出编辑器。
8. 通过控制台重启实例，详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
9. 在启动后验证是否可正常启动及登录


:::
::: 救援模式排查 Linux 系统启动失败问题[](id:rescueModeStartupFailed)
#### 现象描述

Linux 系统重启之后无法正常启动，提示信息有诸多 FAILED 启动失败项。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ac026f0cbea1eab4761a8557d5078cde.png)



#### 可能原因
可能由于关键系统文件缺失导致启动失败，例如 bin 或 lib 文件缺失。


#### 解决思路
参考 [处理步骤](#ProcessingSteps3)，通过控制台进入实例救援模式，进行问题排查及修复。


#### 处理步骤[](id:ProcessingSteps3)

1. 进入救援模式前，强烈建议您对实例进行备份，以防止由于出现误操作等造成的影响。云硬盘可通过 [创建快照](https://cloud.tencent.com/document/product/362/5755) 备份，本地系统盘可通过 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 镜像备份。
2. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，在“实例”页面中，选择实例所在行右侧的**更多** > **运维与检测** > **进入救援模式**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c2aea04a88c0f7bca94738d85eb295ff.png)
3. [](id:step3)在弹出的“进入救援模式”窗口中，设置救援模式期间登录实例的密码。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d427eda6067ce07fe4ff6cedcbe20732.png)
4. 单击**进入救援模式**，此时实例状态会变为“进入救援模式”。如下图所示，该过程一般会在几分钟内完成：
![](https://qcloudimg.tencent-cloud.cn/raw/21669f60fd5334176de2866f5a237abc.png)
正常进入救援模式后实例的状态会变为红色叹号的“救援模式”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ec6a90921d8472dafd7580fed9699851.png)
5. 使用 `root` 帐户及 [步骤3](#step3) 中设置的密码，通过以下方式登录实例。
 - 若实例有公网 IP，则请参考 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)。
 - 若实例无公网 IP，则请参考 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 本文以 VNC 方式登录为例，登录成功后，依次执行以下命令挂载系统盘根分区。
<dx-alert infotype="explain" title="">
救援模式下实例系统盘设备名为 vda，根分区为 vda1，默认未挂载。
</dx-alert>
```shellsession
mkdir -p /mnt/vm1
```
```shellsession
mount /dev/vda1 /mnt/vm1
```
执行完成后，返回结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/c48cd3e7b83abfc17cff3aedbf6dbfa2.png"/>
7. 挂载成功后，即可操作原系统根分区中的数据。
您也可使用 `mount -o bind` 命令，挂载原文件系统的一部分子目录，并通过 `chroot` 命令用来在指定的根目录下运行指令，具体操作命令如下：
```shellsession
mount -o bind /dev /mnt/vm1/dev
mount -o bind /dev/pts /mnt/vm1/dev/pts
mount -o bind /proc /mnt/vm1/proc
mount -o bind /run /mnt/vm1/run
mount -o bind /sys /mnt/vm1/sys
chroot /mnt/vm1 /bin/bash
```
执行 `chroot` 命令时：
 - 若无报错信息，可继续执行 `cd /` 命令。
 - 若出现如下图所示报错信息，说明无法正常切换根目录，此时可执行 `cd /mnt/vm1` 查看根分区数据。
![](https://qcloudimg.tencent-cloud.cn/raw/12e2bccf5c19edb4d248ac26d257c31e.png)
8. 通过命令，可查看原系统根分区中 `/usr/bin` 目录下的所有文件被删除。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0f2820f10b457378d26c9a6efaf14966.png)
9. 此时，可创建一台同操作系统的正常机器，并执行以下命令将正常系统 `/usr/bin` 目录下的文件压缩后远程拷贝至异常机器上。
 - 正常机器：依次执行以下命令
```shellsession
cd /usr/bin/ && tar -zcvf bin.tar.gz *
```
```shellsession
scp bin.tar.gz root@异常实例ip：/mnt/vm1/usr/bin/
```
<dx-alert infotype="explain" title="">
有公网 IP 可通过公网拷贝，无公网 IP 需通过内网拷贝。
</dx-alert>
执行结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/937f1d97edda8a2b2786b856750dfb5e.png"/>
  - 异常机器：在救援模式下依次执行以下命令
```shellsession
cd /mnt/vm1/usr/bin/
```
```shellsession
tar -zxvf bin.tar.gz
```
```shellsession
chroot /mnt/vm1 /bin/bash
```
执行结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/90e4c3d4c06806f07401ec01863dcdfa.png)
10. 实例修复完成后，选择实例所在行右侧的**更多** > **运维与检测** > **退出救援模式**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f23ffc9ce833d11699e8d857d77555a0.png)
11. 退出救援模式后实例处于关机状态，开机后进行系统验证。如下图所示，系统已恢复。
![](https://qcloudimg.tencent-cloud.cn/raw/705c27323e74f424b775f88567d7252c.png)






:::
</dx-accordion>




