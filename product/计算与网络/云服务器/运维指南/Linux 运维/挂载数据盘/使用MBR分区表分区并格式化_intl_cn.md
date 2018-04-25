<font color="red">本方法仅适用于小于2TB的硬盘进行分区及格式化，大于2TB的硬盘请使用GPT方式。</font>

<br>

新购买的Linux云服务器，数据盘未做分区和格式化，无法使用。

可以通过脚本格式化和手动格式化两种方式对Linux云服务器数据盘进行格式化。

>注：

> <font color="red">格式化后，数据盘中的数据将被全部清空。请在格式化之前，确保数据盘中没有数据或对重要数据已进行备份。为避免服务发生异常，格式化前请确保云服务器已停止对外服务。</font>

## 1. 脚本格式化（仅限非Ubuntu操作系统）
本脚本格式化仅适用于默认用户名为root的机器。默认用户名为ubuntu的机器，请采用手动格式化。

1) 将需要操作的云主机的ip，ssh端口号和root账号的密码写到hosts.txt文件中，每一行代表一个主机，比如：
```
10.0.0.1 22 my_password
```
2) [点击此处](http://cos.myqcloud.com/11001086/deldiskscript/batch-mkfs.tgz?res_content_disposition=attachement;&secretId=AKIDj1rrU6Cio35u8xTdWIVIUorgnHhxqyjw&time=1440581110)下载格式化脚本。

3) 在终端执行以下命令
```
./batch-mkfs.py
```

另外，如果用户想自己在云主机的shell中执行相同的操作，请直接在shell里输入如下命令：

```
if grep -q /data /etc/fstab ; then uuid=notneed; echo /data already in fstab; else uuid=`mkfs.ext3 /dev/vdb
 > /dev/null 2>&1 && blkid /dev/vdb | awk '{print $2}'`;fi;if [[ $uuid == UUID* ]]; then echo $uuid /data 
ext3 noatime,acl,user_xattr 1 0 >> /etc/fstab; mount -a; else echo mkfs failed; fi;
```

## 2. 手动格式化
请根据以下步骤对数据盘进行分区以及格式化，并挂载分区使数据盘可用。

>注：
- 执行以下命令时，请注意修改数据盘符，可以使用”fdisk -l”查看盘符等相关信息，以下均以vdb为例，若是其他盘符，仅需将vdb替换为该盘符即可。如fdisk /dev/vdb替换为fdisk /dev/xvdb
- 请确认路径为“/dev/vdb”,若错填为“/dev/vda”,将会造成云主机崩溃 

### 2.1. 查看数据盘信息

登录Linux云服务器后，可以使用“fdisk -l”命令查看数据盘相关信息。
>注：使用“df -h”命令，无法看到未分区和格式化的数据盘。 

![](//mccdn.qcloud.com/img56a60467e297b.png)

### 2.2. 数据盘分区
执行以下命令，对数据盘进行分区。
```
fdisk /dev/vdb
```
按照界面的提示，依次输入“n”(新建分区)、“p”(新建扩展分区)、“1”(使用第1个主分区)，两次回车(使用默认配置)，输入“w”(保存分区表)，开始分区。
这里是以创建1个分区为例，开发者也可以根据自己的需求创建多个分区。

![](//mccdn.qcloud.com/img56a604c2b886f.png)

### 2.3. 查看新分区
使用“fdisk -l”命令，即可查看到，新的分区vdb1已经创建完成。
![](//mccdn.qcloud.com/img56a605027a966.png)

### 2.4. 格式化新分区
在进行分区格式化时，开发者可以自行决定文件系统的格式，如ext2、ext3等。本例以“ext3”为例：

使用下面的命令对新分区进行格式化。 

```
mkfs.ext3 /dev/vdb1
```
![](//mccdn.qcloud.com/img56a6053fb5aa0.png)

### 2.5. 挂载新分区
使用以下命令创建mydata目录：
```
mkdir /mydata
```
再通过以下命令手动挂载新分区：
```
mount /dev/vdb1 /mydata
```
最后用以下命令查看
```
df -h
```
出现如图信息则说明挂载成功，即可以查看到数据盘了。
![](//mccdn.qcloud.com/img56a60615c0984.png)

### 2.6. 添加分区信息
如果希望云服务器在重启或开机时能自动挂载数据盘，必须将分区信息添加到/etc/fstab中。如果没有添加，则云服务器重启或开机后，都不能自动挂载数据盘。

>注：请确认分区路径是否为 “/dev/vdb1”,若路径错误，将会造成云主机重启失败。

使用以下命令添加分区信息：
```
echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
```

使用以下命令查看
```
cat /etc/fstab
```

出现如图信息则说明添加分区信息成功。
![](//mccdn.qcloud.com/img56a606ad3180c.png)