## 操作场景
本文以操作系统为 CentOS 8.0 的腾讯云云服务器为例，介绍如何使用开源工具 [Extundelete](https://sourceforge.net/projects/extundelete/) 快速恢复被误删除的数据。
Extundelete 支持文件系统类型为 ext3 及 ext4 的文件误删恢复，但具体恢复程度与删除后是否被写覆盖、元数据是否存留在 journal 等因素有关。若需恢复数据的文件系统位于系统盘，且一直有业务进程或系统进程在写入文件，则恢复可能性较低。

<dx-alert infotype="explain" title="">
腾讯云提供了 [创建快照](https://cloud.tencent.com/document/product/362/5755)、[创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 及 [对象存储](https://cloud.tencent.com/document/product/436/6222) 等存储数据的方式，建议您定期进行数据备份，以提高数据安全性。
</dx-alert>




## 准备工作
在执行恢复数据相关操作前，请完成以下准备工作：
- 参考 [创建快照](https://cloud.tencent.com/document/product/362/5755) 及 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 进行数据备份，以确保出现问题时可恢复至初始状态。
- 停止相关业务程序继续写数据到该文件系统。若需执行恢复操作的为数据盘，则可先对数据盘执行 `umount` 操作。


## 操作步骤

1. 安装 Extundelete，通过以下两种方式：
<dx-tabs>
::: 下载已编译好的二进制程序（推荐）
1. 执行以下命令，可直接下载已编译好的二进制程序。
```
wget https://github.com/curu/extundelete/releases/download/v1.0/extundelete
```
2. 执行以下命令，授予文件权限。
```
chmod a+x extundelete
```
:::
::: 手动编译安装

<dx-alert infotype="explain" title="">
该步骤以 CentOS 7 操作系统为例，不同系统环境下步骤有一定区别，请您结合实际参考文档进行操作。
</dx-alert>



1. 依次执行以下命令，安装 Extundelete 所需依赖及库。
```shell
yum install libcom_err e2fsprogs-devel
```
```shell
yum install gcc gcc-c++ 
```
2. 执行以下命令，下载 Extundelete 源码。
```
wget https://github.com/curu/extundelete/archive/refs/tags/v1.0.tar.gz
```
3. 执行以下命令，解压 v1.0.tar.gz 文件。
```
tar  xf v1.0.tar.gz
```
4. 依次执行以下命令，进行编译安装。
```
cd extundelete-1.0
```
```
./configure
```
```
make
```
5. 执行以下命令，进入 src 目录，可查看已编译好的 Extundelete 文件。
```
cd ./src
```
:::
</dx-tabs>
2. 执行以下命令，尝试恢复数据。
```
./extundelete  --restore-all  /dev/对应盘
```
恢复后的文件位于同级目录的 `RECOVERED_FILES` 文件夹下，请确实是否有所需文件。


