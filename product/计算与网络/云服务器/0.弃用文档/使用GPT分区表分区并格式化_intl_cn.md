新购买的 Linux 云服务器，由于数据盘未做分区和格式化，无法使用。
>**注意：**
>数据盘中的数据在格式化后将全部被清空。请在格式化之前，确保数据盘中没有数据或已对重要数据进行备份。为避免服务发生异常，格式化前请确保云服务器已停止对外服务。

### 非 FreeBSD 系统操作方法
#### 1. 查看磁盘列表
使用命令 `fdisk –l` 查看磁盘设备列表。
![](https://mc.qcloudimg.com/static/img/cd614ab9441c731539cda705bce12f4a/27.png)
#### 2. 创建 GPT 分区
使用 parted 工具，创建 GPT 分区。
1）. 输入 `parted /dev/vdb` 命令。
2）. 输入 `mklabel gpt` 命令，再输入 `print` 将信息打印出来，此时会显示磁盘大小。
3）. 输入 `mkpart primary 0 磁盘大小` 命令，并在提示警告时选择 ignore 忽视。
4）. 输入 `print` 将信息打印出来。
![](https://mc.qcloudimg.com/static/img/7a2dbc0db11c035e13049581b3a53923/28.png)

#### 3. 查看新分区消息
分区创建完成后，可使用 `fdisk -l` 语句查看新分区信息。
![](https://mc.qcloudimg.com/static/img/21931bce6b1bad88454da272cb4d9520/29.png)

#### 4. 格式化分区
使用 mkfs 工具格式化分区：执行 `mkfs.ext4 -T largefile 磁盘`
![](https://mc.qcloudimg.com/static/img/a647e6efee27611461c3b687b7db73cc/30.png)

#### 5. 挂载新分区
格式化完成后，执行命令 `mount 文件系统 分区路径 挂载点` 挂载新分区。
此时使用命令 `df –h` 可以查看到磁盘剩余容量。
![](https://mc.qcloudimg.com/static/img/984ff3b2d4c56e84057573643ac0009a/31.png)

#### 6. 设置自动挂载
修改 fstab 文件，设置系统重启时自动挂载新分区。
执行命令 `vi /etc/fstab` ，进入编辑页面，键入`i`进入编辑模式；
将 `/dev/vdb1      /data           ext4         defaults     0 0` 添加至文本末端，再按 Esc 键，输入`:wq`保存并返回到命令行，此时已成功修改 fstab 文件。
![](https://mc.qcloudimg.com/static/img/dfaf4ce2855059ba9da9f18e0da1b260/32.png)
 
### FreeBSD 系统操作方法
#### 1. 查看磁盘列表
使用命令 `diskinfo -v /dev/vtbd1` 查看磁盘设备列表。
![](//mccdn.qcloud.com/img56a616a9911da.png)

#### 2. 创建 GPT 分区
1）. 执行命令 `gpart create -s gpt vtbd1`。
![](//mccdn.qcloud.com/img56a6171206c80.png)
2）. 执行命令 `gpart add -t freebsd-ufs -a 1M vtbd1`。
![](//mccdn.qcloud.com/img56a6172bb39c0.png) 

#### 3. 查看新分区消息
使用命令 `diskinfo -v /dev/vtbd1` 查看新分区消息。

#### 4. 格式化分区
使用 newfs 工具格式化分区。执行命令 `newfs -j /dev/vtbd1p1`。

#### 5. 挂载新分区
格式化完成后，执行命令 `mount 文件系统 分区路径 挂载点` 挂载新分区。
此时使用命令 `df –h` 可以查看到磁盘剩余容量。

#### 6. 设置自动挂载
修改 /etc/fstab 文件，设置系统重启时自动挂载新分区。
执行命令 `vi /etc/fstab` ，进入编辑页面，键入`i`进入编辑模式；
将 `/dev/vtbd1p1       /ufs     rw       0        0` 添加至文本末端，再按 Esc 键，输入`:wq`保存并返回到命令行，此时已成功修改 fstab 文件。
![](//mccdn.qcloud.com/img56a6188004bac.png)
