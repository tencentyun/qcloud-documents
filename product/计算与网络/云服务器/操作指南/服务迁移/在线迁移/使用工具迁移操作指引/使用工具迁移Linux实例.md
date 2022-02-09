本文介绍如何使用 go2tencentcloud 迁移工具，进行服务器在线迁移。


## 迁移流程
使用工具迁移流程如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b779202f27976ee40a746e8e1ae77381.png)

## 准备事项

- 已具备腾讯云账号，及目标云服务器。
- 建议暂停源端服务器上的应用程序，以避免迁移时对现有应用程序可能产生的影响。
- [下载](https://go2tencentcloud-1251783334.cos.ap-guangzhou.myqcloud.com/latest/go2tencentcloud.zip) 迁移工具压缩包。
- 在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中创建并获取 `SecretId` 及 `SecretKey`。
- 检查源端主机和目标云服务器是否满足迁移条件。例如，目标云服务器的云硬盘必须具备足够的存储空间用来装载源端的数据。
- 建议您在迁移前，通过下方式进行数据备份：
 - 源端主机：可以选择源服务器快照功能等方式备份数据。
 - 目标云服务器：可以选择 [创建快照](https://cloud.tencent.com/document/product/362/5755) 等方式备份目标云服务器数据。

## 迁移步骤


### 修改配置文件[](id:modifyConfiguration)

1. 将迁移工具 go2tencentcloud.zip 下载或上传至源端主机，并执行以下命令进入对应目录。
    1. 依次执行以下命令，解压 go2tencentcloud.zip 并进入目录。
```sh
unzip go2tencentcloud.zip
```
```sh
cd go2tencentcloud
```
    2. 依次执行以下命令，解压 go2tencentcloud_tool.zip 并进入目录。
```sh
unzip go2tencentcloud_tool.zip
```
```sh
cd go2tencentcloud_tool
```
<dx-alert infotype="explain" title="">
`go2tencentcloud` 目录下的文件将不会被迁移，请勿将需迁移的文件放置在该目录下。
</dx-alert>
2. 在 `user.json` 文件中配置目标云服务器。
请按照 [user.json 文件参数说明](https://cloud.tencent.com/document/product/213/65714#userJsonState) 配置必填项和所需项的值。请将对应参数值替换为您实际的配置参数，参考示例如下：
 - 示例1：将一台 Linux 源端主机迁移至腾讯云广州地域的一台云服务器中，`user.json` 文件配置为以下内容：
```json
{  
	"SecretId": "your secretId",
	"SecretKey": "your secretKey",  
	"Region": "ap-guangzhou",  
	"InstanceId": "your instance id"
} 
```
 - 示例2：将一台 Linux 源端主机（包含一块数据盘，挂载点为 `/mnt/disk1`，大小为`10GB`）迁移至腾讯云广州地域的一台目标云服务器（至少挂载一块数据盘），`user.json` 文件配置为以下内容：
```json
{  
	"SecretId": "your secretId",
	"SecretKey": "your secretKey",  
	"Region": "ap-guangzhou",  
	"InstanceId": "your instance id",
	"DataDisks": [
		{
			"Index": 1,
			"Size": 10,
			"MountPoint": "/mnt/disk1"
		}
	]
}
```
 - 示例3：将一台 Linux 源端主机（包含两块数据盘，盘1挂载点为 `/mnt/disk1`，大小为`10GB`，欲迁移至目标云服务器的第一块数据盘，盘2挂载点为 `/mnt/disk2`，大小为`20GB`，欲迁移至目标云服务器的第二块数据盘）迁移至腾讯云广州地域的一台目标云服务器（至少挂载两块数据盘），`user.json` 文件配置为以下内容：
```json
{  
	"SecretId": "your secretId",
	"SecretKey": "your secretKey",  
	"Region": "ap-guangzhou",  
	"InstanceId": "your instance id",
	"DataDisks": [
		{
			"Index": 1,
			"Size": 10,
			"MountPoint": "/mnt/disk1"
		},
		{
			"Index": 2,
			"Size": 20,
			"MountPoint": "/mnt/disk2"
		}
	]
}  
```
2. （可选）在 `client.json` 文件中配置迁移模式和其他项。
请按照 [client.json 文件参数说明](https://cloud.tencent.com/document/product/213/65714#clientJsonState) 进行配置。如果源端主机和目标云服务器任何一方不能直接访问公网，则可以选择先通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立连接通道，再进行内网模式迁移，详情请参见 [内网迁移教程](https://cloud.tencent.com/document/product/213/65715)。
3. （可选）排除源端主机上不需迁移的文件或目录。
若 Linux 源端主机中存在不需要迁移的文件或目录，可将文件或目录添加至 [rsync\_excludes\_linux.txt 文件](https://cloud.tencent.com/document/product/213/65714#_linuxTxtState)。

### 迁移前的检查

迁移前，需要分别检查源端主机和目标云服务器。检查内容如下表：

<table>
  <tr>
	<th style="width: 15%;">目标云服务器</th>
	<td>
	  <ol style="margin: 0;">
		<li>
		存储空间：目标云服务器的云硬盘（包括系统盘和数据盘）必须具备足够的存储空间用来装载源端的数据。</li>
		<li>安全组：安全组中不能限制443端口和80端口。</li>
		<li>
		带宽设置：建议尽可能调大两端的带宽，以便更快迁移。迁移过程中，会产生约等于数据量的流量消耗，如有必要请提前调整网络计费模式。</li>
		<li>
		目标云服务器和源端主机的操作系统类型是否一致：操作系统不一致会造成后续制作的镜像的信息与实际操作系统不符，建议目标云服务器的操作系统尽量和源端主机的操作系统类型一致。例如，CentOS
		7 系统的对源端主机迁移时，选择一台 CentOS 7 系统的云服务器作为迁移目标。</li>
	  </ol>
	</td>
  </tr>
  <tr>
	<th>Linux 源端主机</th>
	<td>
	  <ol style="margin: 0;">
		<li>检查和安装 Virtio，操作详情可参考 
		<a href="https://cloud.tencent.com/document/product/213/9929">Linux 系统检查 Virtio 驱动</a>。</li>
		<li>执行 
		<code>which rsync</code> 命令检查是否安装了 rsync。如未安装，请参考 <a href="https://cloud.tencent.com/document/product/213/32962#installRsync">如何安装 Rsync</a> 进行安装。</li>
		<li>检查 SELinux 是否已打开。如果 SELinux 已打开，请参考 <a href="https://cloud.tencent.com/document/product/213/32962#closeSELinux">如何关闭 SELinux</a> 进行关闭。</li>
		<li>向腾讯云 API 发起迁移请求后，云 API 会使用当前 UNIX 时间检查生成的
		Token，请确保当前系统时间无误。</li>
	  </ol>
	</td>
  </tr>
</table>
<dx-alert infotype="explain" title="">
- 源端主机检查可以使用工具命令自动检查，如 `sudo ./go2tencentcloud_x64 --check`。
- go2tencentcloud 迁移工具在开始运行时，默认自动检查。如果需要略过检查强制迁移，请将 client.json 文件中的 `Client.Extra.IgnoreCheck` 字段配置为 `true`。
</dx-alert>



### 发起迁移

执行以下命令，运行工具。
本文以64位 Linux 源端主机为例，进入 go2tencentcloud_tool 文件目录，并以 root 权限执行以下命令运行工具。
```sh
sudo ./go2tencentcloud_x64
```

### 等待迁移结束

腾讯云提供的 go2tencentcloud 迁移工具支持断点传输，并将整个迁移过程主要划分为以下三个阶段，用户可以在工具运行过程中直观的了解迁移的进度。

- **阶段1**：目标云服务器进入迁移模式，准备迁移
- **阶段2**：目标云服务器处于迁移模式，迁移数据中
- **阶段3**：目标云服务器退出迁移模式，迁移完成

每个阶段均会产生一些子任务去执行相关操作，部分耗时的子任务还将具有默认的最大超时时间。由于传输数据耗时受源端数据大小，网络带宽等因素影响，请耐心等待迁移流程的完成。

<dx-alert infotype="notice" title="">
开始迁移后目标云服务器将进入迁移模式，请不要对目标云服务器进行重装系统、关机、销毁、重置密码等操作，直至迁移完成退出迁移模式。 
</dx-alert>

一般公网迁移模式下，迁移成功的控制台输出如下：
![](https://main.qcloudimg.com/raw/b056d6b1d5ac457ff43e48883848af01.png)

### 迁移后的检查

- 若迁移结果失败，则请检查日志文件（默认为迁移工具目录下的 log 文件）的错误信息输出、指引文档或者 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 进行排查和修复问题。
- 若迁移结果成功，则请检查目标云服务器能否正常启动、目标云服务器数据与源端主机是否一致、网络是否正常或者其他系统服务是否正常等。

如有任何疑问、迁移异常等问题请查看 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 或者 [联系我们](https://cloud.tencent.com/document/product/213/39047) 解决。
