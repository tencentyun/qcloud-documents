非弹性云硬盘(即生命周期跟随 CVM 实例的云硬盘)在创建时将自动连接至创建的 CVM 实例上，且不可以更改；同时用户可以手动将弹性云盘挂载到同一可用区中的任意实例上，可以在挂载时确定每个实例还能挂载多少云硬盘。有关挂载数量的更多信息，请参阅[使用约束](/doc/product/362/5145)。有关弹性云盘和非弹性云硬盘的更多内容，请参阅 [云硬盘的分类](/doc/product/362/2353)。

## 使用控制台将弹性云硬盘连接到实例
目前支持对作为<font color="red">数据盘</font>的普通弹性云硬盘云盘进行挂载，不可挂载系统盘。

1) 登录[腾讯云控制台](https://console.cloud.tencent.com/)。

2) 进入【云服务器】-【云硬盘】选项卡。

3) 在云硬盘列表页，点击状态为<font color="red">待挂载、支持挂载/卸载</font>的云硬盘后的【更多】-【挂载到云主机】按钮进行单盘挂载；
或在云硬盘列表页，勾选状态为<font color="red">待挂载、支持挂载/卸载</font>的云硬盘，点击顶部【挂载】按钮进行批量挂载。

4) 在弹出框中选择需要挂载到的云服务器，点击【确定】按钮，等待挂载完毕即可登录云服务器查看云硬盘挂载状况。

云硬盘在挂载完后并不能马上使用，需要进行分区、格式化等一系列操作。具体操作方式请见：[Windows 系统分区、格式化及创建文件系统](https://cloud.tencent.com/document/product/362/6734
)、[Linux 系统分区、格式化、挂载及创建文件系统](/document/product/362/6735)、

## 使用 API 将弹性云硬盘连接到实例
请参考 [AttachCbsStorages 接口](https://cloud.tencent.com/doc/api/364/2520)。

## 部分已创建的云服务器实例无法识别弹性云盘的解决方案

目前提供的所有镜像已经支持弹性云盘的连接/解挂操作。<font color="red">请注意，拔盘（卸载）前请先执行umount（Linux）或脱机（Windows）操作，否则可能出现再次挂载时无法识别的问题。</font>

但若您在此时间之前购买了下面类型的云服务器并计划向云服务器中添加弹性云盘时：

<table>
<tbody>
<tr><th>云服务器操作系统类型</th><th>版本</th>
<tr><td rowspan="4">CentOS</td><td>5.11 64位</td>
<tr><td>5.11 32位</td>
<tr><td>5.8 64位</td>
<tr><td>5.8 32位</td>
<tr><td >Debian</td><td>6.0.3 32位</td>
<tr><td rowspan="2">Ubuntu</td><td>10.04 64位</td>
<tr><td>10.04 32位</td>
<tr><td rowspan="2">OpenSuse</td><td>12.3 64位</td>
<tr><td>12.3 32位</td>
</tbody>
</table>

建议您在购买弹性云盘之前在实例中执行如下命令添加驱动来获得热插拔功能：

```
modprobe acpiphp
```
　　
另外，当您在关机或者重新启动该云服务器后，仍然需要再次加载 `acpiphp` 驱动模块，建议您将 `acpiphp` 模块设置成开机自动加载，各个系列的设置方法如下：

**CentOS 5系列**

执行以下命令创建文件:

```
vi /etc/sysconfig/modules/acpiphp.modules
```

并在文件中添加如下内容：

```
 #!/bin/bash
 modprobe acpiphp >& /dev/null
```

执行以下命令添加可执行权限，设置完成后此脚本即可开机加载：

```
chmod a+x /etc/sysconfig/modules/acpiphp.modules
```

**Debian 6系列、Ubuntu 10.04系列**

执行以下命令修改文件：

```
vi /etc/modules
```
并写入以下内容：

```
acpiphp
```
 	  
**OpenSUSE 12.3系列**

执行以下命令修改文件：

```
vi /etc/sysconfig/kernel
```
并写入以下内容：

```
MODULES_LOADED_ON_BOOT="acpiphp"
```　
	   