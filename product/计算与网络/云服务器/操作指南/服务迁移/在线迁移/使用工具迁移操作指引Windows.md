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

1. 在 `user.json` 文件中配置目标云服务器。
请按照 [user.json 文件参数说明](https://cloud.tencent.com/document/product/213/65714#userJsonState) 配置必填项和所需项的值。请将对应参数值替换为您实际的配置参数，参考示例如下。
将一台 Windows 源端主机迁移至腾讯云广州地域的一台云服务器中，`user.json` 文件配置为以下内容：
```json
{  
	"SecretId": "your secretId",
	"SecretKey": "your secretKey",  
	"Region": "ap-guangzhou",  
	"InstanceId": "your instance id"
} 
```
2. （可选）在 `client.json` 文件中配置迁移模式和其他项。
请按照 [client.json 文件参数说明](https://cloud.tencent.com/document/product/213/65714#clientJsonState) 进行配置。如果源端主机和目标云服务器任何一方不能直接访问公网，则可以选择先通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立连接通道，再进行内网模式迁移，详情请参见 [内网迁移教程](https://cloud.tencent.com/document/product/213/65715)。

### 迁移前的检查

迁移前，需要分别检查源端主机和目标云服务器。检查内容如下表：

<table>
  <tr>
	<th style="width: 15%;">目标云服务器</th>
	<td>
	  <ol style="margin: 0;">
		<li>
		存储空间：目标云服务器的云硬盘（包括系统盘和数据盘）必须具备足够的存储空间用来装载源端的数据。</li>
		<li>安全组：安全组中不能限制3389端口和80端口。</li>
		<li>
		带宽设置：建议尽可能调大两端的带宽，以便更快迁移。迁移过程中，会产生约等于数据量的流量消耗，如有必要请提前调整网络计费模式。</li>
		<li>
		目标云服务器和源端主机的操作系统类型是否一致：操作系统不一致会造成后续制作的镜像的信息与实际操作系统不符，建议目标云服务器的操作系统尽量和源端主机的操作系统类型一致。例如，CentOS
		7 系统的对源端主机迁移时，选择一台 CentOS 7 系统的云服务器作为迁移目标。</li>
	  </ol>
	</td>
  </tr>
  <tr>
	<th>Windows 源端主机</th>
	<td>
	  <ol style="margin: 0;">
		<li>检查和安装 Virtio。Windows 系统默认未安装 Virtio 驱动，您可在安装 Windows Virtio 驱动后导出本地镜像。<a href="http://mirrors.tencent.com/install/windows/virtio_64_1.0.9.exe">点击此处</a> 下载 Windows Virtio 驱动 。
		<li>检查和安装 Cloudbase-Init，详情请参见 <a href="https://cloud.tencent.com/document/product/213/30000">Windows 操作系统安装 Cloudbase-Init</a>。您可以选择迁移前在源端主机安装，也可迁移后在目标实例安装。若在迁移前安装，则迁移后将会进行自动配置网络、激活等初始化操作。若未在迁移前安装，您可能需要 <a href="https://cloud.tencent.com/document/product/213/35704">使用 VNC 登录实例</a> 并手动修改网络配置。</li>
	  </ol>
	</td>
  </tr>
</table>
<dx-alert infotype="explain" title="">
源端主机的所有磁盘都将迁移，若有多块磁盘（这里指的并非分区），那么您需要按顺序购买对应数量和大小的磁盘挂载至目标云服务器。
</dx-alert>



### 发起迁移
1. 使用 Administrator 用户登录源端主机，并以管理员权限运行 cmd.exe。
2. 在打开的 cmd 窗口中，进入 go2tencentcloud 文件目录，并执行以下命令，运行工具。
```sh
go2tencentcloud_windows_x64.exe
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

迁移成功将会输出 Migrate successfully 信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/96525aa2e9ffa861fd244ca20734d7f3.png)
此时，您可以按任意键退出迁移模式，并登录目标服务器检查是否迁移完成。


### 迁移后的检查

- 若迁移结果失败，则请检查日志文件（默认为迁移工具目录下的 log 文件）的错误信息输出、指引文档或者 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 进行排查和修复问题。
- 若迁移结果成功，则请检查目标云服务器能否正常启动、目标云服务器数据与源端主机是否一致、网络是否正常或者其他系统服务是否正常等。

如有任何疑问、迁移异常等问题请查看 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 或者 [联系我们](https://cloud.tencent.com/document/product/213/39047) 解决。
