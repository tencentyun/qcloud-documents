## 操作场景
Bottleneck Bandwidth and Round-trip propagation time（BBR），是 Google 在2016年开发的 TCP 拥塞控制算法，可以使 Linux 服务器显著地提高吞吐量和减少 TCP 连接的延迟。由于开启 BBR 需 4.10 以上版本 Linux 内核，如果您的 Linux 服务器内核低于4.10，可参考本文进行操作。

本文以 CentOS 7.5 操作系统的云服务器为例，指导您如何在 Linux 系统中手动更换内核，开启 BBR。

## 操作步骤

### 更新内核包
1. 执行以下命令，查看当前 Kernel 版本。
```
uname -r
```
2. 执行以下命令，更新软件包。
```
yum update -y
```
3. 执行以下命令，导入 ELRepo 公钥。
```
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
```
4. 执行以下命令，安装 ELRepo 的 yum 源。
```
yum install https://www.elrepo.org/elrepo-release-7.0-4.el7.elrepo.noarch.rpm
```


### 安装新内核
1. 执行以下命令，查看 ELRepo 仓库下当前系统支持的内核包。
```
yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
```
2. 执行以下命令，安装最新的主线稳定内核。
```
yum --enablerepo=elrepo-kernel install kernel-ml
```

### 更改 grub 配置
1. 执行以下命令，打开 `/etc/default/grub` 文件。
```
vim /etc/default/grub
```
2. 按 **i** 切换至编辑模式，将 `GRUB_DEFAULT=saved` 修改为 `GRUB_DEFAULT=0`。
![](https://main.qcloudimg.com/raw/484e7a6e818dc44c2d4debb9230e0b46.png)
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，重新生成 Kernel 配置。
```
grub2-mkconfig -o /boot/grub2/grub.cfg
```
5. 执行以下命令，重启机器。
```
reboot
```
6. 执行以下命令，检查是否更改成功。
```
uname -r
```

### 删除多余内核
1. 执行以下命令，查看所有的 Kernel。
```
rpm -qa | grep kernel
```
2. 执行以下命令，删除旧版本的内核。
```
yum remove kernel-old_kernel_version
```
例如：
```
yum remove kernel-3.10.0-957.el7.x86_64
```

### 开启 BBR
1. 执行以下命令，编辑 `/etc/sysctl.conf` 文件。
```
vim /etc/sysctl.conf
```
2. 按 **i** 切换至编辑模式，添加如下内容。
```
net.core.default_qdisc=fq
net.ipv4.tcp_congestion_control=bbr
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，从`/etc/sysctl.conf`配置文件中加载内核参数设置。
```
sysctl -p
```
5. 依次执行以下命令，验证是否成功开启了 BBR。
```
sysctl net.ipv4.tcp_congestion_control
# 显示如下内容即可：
# net.ipv4.tcp_congestion_control = bbr
```
```
sysctl net.ipv4.tcp_available_congestion_control
# 显示如下内容即可：
# net.ipv4.tcp_available_congestion_control = reno cubic bbr
```
6. 执行以下命令，查看内核模块是否加载。
```
lsmod | grep bbr
```
返回如下信息，表示开启成功。
![](https://main.qcloudimg.com/raw/7d736afd8ce22f421315e149a86527e5.png)



