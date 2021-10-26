## 操作场景
本文介绍如何在 M6p 实例上配置持久内存。


## 前提条件
已创建并登录 M6p 实例。
- 如何创建实例，请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 如何登录实例，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。

<dx-alert infotype="explain" title="">
本文以操作系统为 TencentOS Server 3.1（TK4）的云服务器为例。建议您的实例使用以下内核版本：
 - CentOS 7.6及更高版本
 - Ubuntu 18.10及更高版本
 - TencentOS Server 3.1
</dx-alert>




## 英特尔® 傲腾™ DC BSP 硬件（PMEM）模式介绍

### Memory mode
在 Memory mode 模式下，常规 DRAM 充当最常访问数据的缓存，而持久内存作为后备内存使用，高速缓存管理操作由内存控制器自动处理。

### AD mode
M6p 机型采用该模式，在 M6p 机型中，平台侧将 BPS 硬件配置为 AD 模式透传给云服务器使用。在 AD 模式下，应用程序可以把 PMEM 设备作为内存使用，或作为本地 SSD 盘使用。


## 操作步骤

### PMEM 初始化
依次执行以下命令，对 PMEM 设备初始化。
```
yum install -y ndctl
```
```
ndctl destroy-namespace all --force
```
<dx-alert infotype="explain" title="">
最大规格实例具有两个 region，执行以下命令后，请将 region0 替换为 region1 并再次执行命令。
</dx-alert>
```
ndctl disable-region region0
```
```
ndctl init-labels all
```
```
ndctl enable-region region0
```

### 在 AD 模式下配置 PMEM

#### 将持久内存作为内存使用

PMEM 可作为字符设备提供给上层应用，例如 redis 进行持久内存的分配，可借助 memkind 等 PMDK 框架来使用。其配置方法如下：
1. 依次执行以下命令，生成字符设备。
```
ndctl create-namespace -r region0 -m devdax
```
```
ndctl create-namespace -r region1 -m devdax -f
```
<dx-alert infotype="explain" title="">
最大规格实例具有两个 region，执行以上命令后，请将 region0 替换为 region1 并再次执行命令。
</dx-alert>
配置完成后，`/dev` 目录下已生成 `dax0.0` 字符设备，可映射持久化内存。
2. 执行以下命令，查看持久内存大小。
```
ndctl list -R
```
3. 依次执行以下命令，使用 PMEM 扩充云服务器的内存。
在高版本的内核（如 TencentOS Server 3.1 的内核）支持下，可将 devdax 模式的 PMEM 进一步配置为 kmemdax，可使用 PMEM 扩充云服务器的内存。
```
yum install -y daxctl
```
```
daxctl migrate-device-model
```
```
reboot
```
```
daxctl reconfigure-device --mode=system-ram --no-online dax0.0
```
4. 执行以下命令，查看系统内存扩充的情况。
```
numactl -H
```

#### 将持久内存作为本地 SSD 盘使用
AD 模式的 PMEM 也可配置为高速块设备，可用作一般的块设备，进行创建文件系统，裸盘读写等操作。其配置方法如下：
1. 执行以下命令，在 `/dev` 目录下生成 pmem0 块设备。
```
ndctl create-namespace -r region0 -m fsdax
```
最大规格实例具有两个 region，若您使用了最大规格的实例，则请执行以下命令。
```
ndctl create-namespace -r region1 -m fsdax -f
```
2. 依次执行以下命令，创建文件系统或挂载使用。
```
mkfs.ext4 /dev/pmem0
```
```
mount -o dax,noatime /dev/pmem0 /mnt/
```

## 参考资料
- [Intel® Optane™ DC Persistent Memory](https://www.intel.com/content/dam/support/us/en/documents/memory-and-storage/data-center-persistent-mem/Intel-Optane-DC-Persistent-Memory-Quick-Start-Guide.pdf)
- [Linux Provisioning for Intel® Optane™ Persistent Memory](https://www.intel.com/content/www/us/en/developer/articles/technical/qsg-part2-linux-provisioning-with-optane-pmem.html)
