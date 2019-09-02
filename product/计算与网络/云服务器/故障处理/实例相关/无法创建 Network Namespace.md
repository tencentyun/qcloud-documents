## 问题描述
当执行创建一个新的网络命名空间（Network Namespace）的命令时，命令卡住，无法继续。Dmesg 信息提示：“unregister_netdevice: waiting for lo to become free. Usage count = 1”

## 问题原因
该问题为一个内核 bug。目前，以下内核版本都存在该 bug：
- Ubuntu 16.04 x86_64 内核版本为 4.4.0-91-generic
- Ubuntu 16.04 x86_32 内核版本为 4.4.0-92-generic

## 解决方案

将内核版本升级到 4.4.0-98-generic 版本，该版本已经修复此 bug。

## 处理步骤
1. 执行以下命令，查看当前内核版本。
```
uname -r
```
2. 执行以下命令，查看是否有 4.4.0-98-generic 版本的内核可升级。
```
sudo apt-get update
sudo apt-cache search linux-image-4.4.0-98-generic
```
若显示如下信息，则表示源中存在该版本，可进行升级：
```
linux-image-4.4.0-98-generic - Linux kernel image for version 4.4.0 on 64 bit x86 SMP
```
3. 执行以下命令，安装新版本内核和对应的 Header 包。
```
sudo apt-get install linux-image-4.4.0-98-generic linux-headers-4.4.0-98-generic
```
4. 执行以下命令，重启系统。
```
sudo reboot
```
5. 执行以下命令，进入系统，检查内核版本。
```
uname -r
```
若显示如下结果，则表示版本更新成功：
```
4.4.0-98-generic
```
