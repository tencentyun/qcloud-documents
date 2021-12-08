## 操作场景
本文介绍如何在 M6p 实例上配置持久内存。


## 实例配置
本文使用了以下配置的云服务器实例，获取的相关信息请以实际情况为准：
 - **实例规格**：内存型 M6p 实例 M6p.LARGE16（4核16GB）。其他规格配置请参见 [内存型 M6p](https://cloud.tencent.com/document/product/213/11518#M6p)。
 - **操作系统**： TencentOS Server 3.1（TK4）。
<dx-alert infotype="explain" title="">
建议您的实例使用以下操作系统：
 - TencentOS Server 3.1
 - CentOS 7.6及更高版本
 - Ubuntu 18.10及更高版本
</dx-alert>

## 前提条件
已创建并登录 [M6p 实例](https://cloud.tencent.com/document/product/213/11518#M6p)。
- 如何创建实例，请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 如何登录实例，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。


## 英特尔® 傲腾™ DC BPS 硬件（PMEM）模式介绍

### Memory 模式
在 Memory 模式下，常规 DRAM 充当最常访问数据的缓存，而持久内存作为后备内存使用，高速缓存管理操作由内存控制器自动处理。

### AD 模式
M6p 机型采用该模式，在 M6p 机型中，平台侧将 BPS 硬件配置为 AD 模式透传给云服务器使用。在 AD 模式下，应用程序可以把 PMEM 设备作为内存使用，或作为本地 SSD 盘使用。


## 操作步骤

### PMEM 初始化
首次使用实例时请依次执行以下命令，对 PMEM 设备初始化。若您已执行过 PMEM 初始化，则请跳过该步骤。
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

您可按照实际需求，将持久内存作为内存或本地 SSD 盘使用：

<dx-tabs>
::: 作为内存使用
PMEM 可作为字符设备提供给上层应用（例如 redis）进行持久内存的分配，可借助 memkind 等 PMDK 框架来使用。其配置方法如下：
1. 执行以下命令，生成字符设备。
```
ndctl create-namespace -r region0 -m devdax
```
返回结果如下图所示，表示已生成 `dax0.0` 字符设备。
![](https://qcloudimg.tencent-cloud.cn/raw/e25e7a26c05b4d09507f571105d5e7c2.png)
最大规格实例具有两个 region，若您使用最大规格实例，请同时执行以下命令。
```
ndctl create-namespace -r region1 -m devdax -f
```
配置完成后，`/dev` 目录下已生成 `dax0.0` 字符设备，可映射持久化内存。
2. 执行以下命令，查看持久内存大小。
```
ndctl list -R
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b454a36bf3baf0361fe6154639b6c4da.png)


#### 扩展功能（可选）
您可通过该步骤进行功能扩展，依次执行以下命令，使用 PMEM 扩充云服务器的内存。
1. 在高版本的内核（5.1 以上且使用了 KMEM DAX 的驱动，如 TencentOS Server 3.1 的内核）支持下，可将 devdax 模式的 PMEM 进一步配置为 kmemdax，可使用 PMEM 扩充云服务器的内存。
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
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6cc731b4e6e08be343c284683ac75721.png)
2. 执行以下命令，查看系统内存扩充的情况。
```
numactl -H
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6cbeee0aeb1bf7d4527297d5eaa747bc.png)
:::
::: 作为本地 SSD 盘使用
AD 模式的 PMEM 也可配置为高速块设备，可用作一般的块设备，进行创建文件系统，裸盘读写等操作。其配置方法如下：
1. 执行以下命令，在 `/dev` 目录下生成 pmem0 块设备。
```
ndctl create-namespace -r region0 -m fsdax
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/010dbd1f35b3dfdff08d39546f0ce06e.png)
最大规格实例具有两个 region，若您使用最大规格实例，请同时执行以下命令。
```
ndctl create-namespace -r region1 -m fsdax -f
```
2. 依次执行以下命令，创建文件系统或挂载使用。
    1. 创建文件系统。
```
mkfs.ext4 /dev/pmem0
```
返回结果如下图所示，表示已成功创建文件系统。
![](https://qcloudimg.tencent-cloud.cn/raw/e1c39d0122b4d6bff535d22dd9af0c18.png)
    2. 挂载至 `/mnt/`。
```
mount -o dax,noatime /dev/pmem0 /mnt/
```


:::
</dx-tabs>






## 参考资料
- [Intel® Optane™ DC Persistent Memory](https://www.intel.com/content/dam/support/us/en/documents/memory-and-storage/data-center-persistent-mem/Intel-Optane-DC-Persistent-Memory-Quick-Start-Guide.pdf)
- [Linux Provisioning for Intel® Optane™ Persistent Memory](https://www.intel.com/content/www/us/en/developer/articles/technical/qsg-part2-linux-provisioning-with-optane-pmem.html)
