## 问题描述
当执行创建一个新的网络命名空间（Network Namespace）的命令时，命令卡住，无法继续。dmesg 信息：“unregister_netdevice: waiting for lo to become free. Usage count = 1”

## 问题原因
这是一个内核 Bug。
当前，以下内核版本都存在该 Bug：
- Ubuntu 16.04 x86_64 内核版本为 4.4.0-91-generic；
- Ubuntu 16.04 x86_32 内核版本为 4.4.0-92-generic。

## 解决方案
升级内核版本到 4.4.0-98-generic，该版本已经修复该 Bug。
### 操作流程
1. 查看当前内核版本。
```
uname -r
```

2. 查看是否有版本 4.4.0-98-generic 可升级。
```
sudo apt-get update
sudo apt-cache search linux-image-4.4.0-98-generic
```
显示如下信息表示源中存在该版本，可进行升级：
```
linux-image-4.4.0-98-generic - Linux kernel image for version 4.4.0 on 64 bit x86 SMP
```

3. 安装新版本内核和对应的 Header 包。
```
sudo apt-get install linux-image-4.4.0-98-generic linux-headers-4.4.0-98-generic
```

4. 重启系统。
```
sudo reboot
```

5. 进入系统，检查内核版本。
```
uname -r
```
显示如下结果，表示版本更新成功：
```
4.4.0-98-generic
```
