## 操作场景
本文以操作系统为 CentOS 7.7 的腾讯云云服务器为例，介绍如何使用开源工具 Extundelete 快速恢复被误删除的数据。Extundelete 支持 ext3 及 ext4 双格式分区恢复，功能强大。本文适用于误删数据盘文件的用户，且误操作后未对磁盘进行写入等操作。
腾讯云还提供了 [创建快照](https://cloud.tencent.com/document/product/362/5755)、[创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 及 [对象存储](https://cloud.tencent.com/document/product/436/6222) 等存储数据的方式，建议您定期进行数据备份，以提高数据安全性。

## 示例软件版本
- Linux：Linux 操作系统，本文以 CentOS 7.7 为例。
- Extundelete：开源数据恢复工具，本文以 Extundelete 0.2.4 为例。


## 操作步骤


<dx-alert infotype="notice" title="">
在执行操作步骤前，请参考 [创建快照](https://cloud.tencent.com/document/product/362/5755) 及 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 进行数据备份，以确保出现问题时可恢复至初始状态。
</dx-alert>


### 安装 Extundelete
1. 执行以下命令，安装 Extundelete 所需依赖及库。
<dx-alert infotype="notice" title="">
- Extundelete 需 libext2fs 1.39或更高版本。
- 如需支持 ext4 格式，请确保安装 e1fsprogs 1.41或更高版本。可执行 `dumpe2fs` 命令查看版本。 
</dx-alert>
```
yum -y install  bzip2  e2fsprogs-devel  e2fsprogs  gcc-c++  make
```
2. 下载 [Extundelete](https://sourceforge.net/projects/extundelete/) 安装包。
3. 依次执行以下命令，解压 Extundelete 安装包并进入程序目录。
```
tar -xvjf extundelete-0.2.4.tar.bz2
```
```
cd extundelete-0.2.4 
```
4. 依次执行以下命令，编译安装 Extundelete。
```
./configure   
```
```
make && make install
```
安装成功后，您可前往 `usr/local/bin` 目录下查看 extundelete 可执行文件。

### 数据恢复测试
您可参考以下步骤，了解数据恢复过程并结合实际情况进行操作。
1. 参考 [在分区上构建文件系统](https://cloud.tencent.com/document/product/362/6734#CreateFileSystemOnPartition) 对数据盘进行初始化及分区，并执行以下命令，检查现有磁盘及可用分区。
```
fdisk -l
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/34abb1b0c7a1f6fb4ff233a42a781123.png)
2. 依次执行以下命令，新建挂载点并挂载分区。本文以将分区 `/dev/vdb1`  挂载至 `/test` 为例。
```
mkdir /test
```
```
mount /dev/vdb1 /test
```
3. 依次执行以下命令，在挂载点创建测试文件 hello。
```
cd /test
```
```
echo test > hello
```
4. <span id="Step4"></span>执行以下命令，记录 hello 文件 md5 的值。md5 值可用于校验删除前和恢复后的两个文件。
```
md5sum hello
```
返回结果如下所示：
![](https://main.qcloudimg.com/raw/230d4c9a4456df8b3623c0bd401d878a.png)
5. 依次执行以下命令，删除 hello 文件。
```
rm -rf hello
```
```
cd ~
```
```
fuser -k /test
```
6. 执行以下命令，卸载挂载的分区。
```
umount /dev/vdb1
```
7. 执行以下命令，搜索分区内误删文件。
```
extundelete --inode 2 /dev/vdb1
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/97a64a2e0de658f4ed55500f162b1eb7.png)
8. 执行以下命令，使用 Extundelete 恢复文件。
```
/usr/local/bin/extundelete  --restore-inode 12  /dev/vdb1
```
恢复完成后，会在同级目录下出现 `RECOVERED_FILES` 文件夹。
9. 进入 `RECOVERED_FILES` 文件夹，查看恢复的文件，并执行以下命令。
```
md5sum 已恢复文件
```
若获取的 md5 值与 [步骤4](#Step4) 中 hello 文件的 md5 值相等，则说明数据恢复成功。
