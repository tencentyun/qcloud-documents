本文介绍如何使用 go2tencentcloud 迁移工具，进行 Linux 系统服务器在线迁移。

## 准备事项

- 已具备腾讯云账号，及目标云服务器。
- 建议暂停源端服务器上的应用程序，以避免迁移时对现有应用程序可能产生的影响。
- [下载](https://go2tencentcloud-1251783334.cos.ap-guangzhou.myqcloud.com/latest/go2tencentcloud.zip) 迁移工具压缩包。
- 在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中创建并获取 `SecretId` 及 `SecretKey`。
- 检查源端主机和目标云服务器是否满足迁移条件。例如，目标云服务器的云硬盘必须具备足够的存储空间用来装载源端的数据。
- 建议您在迁移前，通过下方式进行数据备份：
 - 源端主机：可以选择源服务器快照功能等方式备份数据。
 - 目标云服务器：可以选择 [创建快照](https://cloud.tencent.com/document/product/362/5755) 等方式备份目标云服务器数据。

## 迁移工具包说明

### 压缩包文件说明

`go2tencentcloud.zip` 解压后，文件说明如下：
<table>
	<tr><th width="30%">文件名</th><th>说明</th></tr>
	<tr><td>go2tencentcloud-linux.zip</td><td>Linux 系统的迁移压缩包。</td></tr>
	<tr><td>readme.txt</td><td>目录简介文件。</td></tr>
	<tr><td>release_notes.txt</td><td>迁移工具变更日志。</td></tr>
</table>

`go2tencentcloud-linux.zip` 解压后，文件说明如下：
<table>
	<tr><th width="30%">文件名</th><th>说明</th></tr>
	<tr><td>go2tencentcloud_x64</td><td>64位 Linux 系统的迁移工具可执行程序。</td></tr>
	<tr><td>go2tencentcloud_x32</td><td>32位 Linux 系统的迁移工具可执行程序。</td></tr>
	<tr><td>user.json</td><td>迁移时的用户信息。</td></tr>
	<tr><td>client.json</td><td>迁移工具的配置文件。</td></tr>
	<tr><td>rsync_excludes_linux.txt</td><td>rsync 配置文件，排除 Linux 系统下不需要迁移的文件目录。</td></tr>
</table>

<dx-alert infotype="notice" title="">
不能删除配置文件，并请将配置文件存放在和 go2tencentcloud 可执行程序同级目录下。 
</dx-alert>

### user.json 文件参数说明[](id:userJsonState)

user.json 配置文件说明如下表：

<table>
  <tr>
	<th>参数名称</th>
	<th>类型</th>
	<th>是否必填</th>
	<th>说明</th>
  </tr>
  <tr>
	<td>SecretId</td>
	<td>String</td>
	<td>是</td>
	<td>账户 API 访问密钥 SecretId，详细信息请参考 
	<a href="https://cloud.tencent.com/document/product/598/37140">访问密钥</a>。</td>
  </tr>
  <tr>
	<td>SecretKey</td>
	<td>String</td>
	<td>是</td>
	<td>账户 API 访问密钥 SecretKey，详细信息请参考 
	<a href="https://cloud.tencent.com/document/product/598/37140">访问密钥</a>。</td>
  </tr>
  <tr>
	<td>Region</td>
	<td>String</td>
	<td>是</td>
	<td>目标云服务器的地域，只需填写地域，无需填写可用区，取值请参考 
	<a href="https://cloud.tencent.com/document/product/213/6091">地域</a> 列表。</td>
  </tr>
  <tr>
	<td>InstanceId</td>
	<td>String</td>
	<td>是</td>
	<td>目标云服务器的实例 ID，形如 
	<code>ins-xxxxxxxx</code>。</td>
  </tr>
  <tr>
	<td>DataDisks</td>
	<td>Array</td>
	<td>否</td>
	<td>源端主机待迁移数据盘列表，每一个元素代表一块数据盘，最多支持20块数据盘。</td>
  </tr>
  <tr>
	<td>DataDisks.Index</td>
	<td>Integer</td>
	<td>否</td>
	<td>数据盘序号，取值范围[1,20]，值为<code>1</code>代表该块数据盘将迁移至目标云服务器挂载的第一块数据盘，值为<code>2</code>代表迁移至目标云服务器挂载的第二块数据盘，以此类推。</td>
  </tr>
  <tr>
	<td>DataDisks.Size</td>
	<td>Integer</td>
	<td>否</td>
	<td>源端数据盘大小，单位 GB，取值范围[10,16000]。</td>
  </tr>
  <tr>
	<td>DataDisks.MountPoint</td>
	<td>String</td>
	<td>否</td>
	<td>源端数据盘挂载点，如 
	<code>&quot;/mnt/disk1&quot;</code>。</td>
  </tr>
</table>

您可参考以下的示例，结合实际业务场景修改配置文件。
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

### client.json 文件参数说明[](id:clientJsonState)

client.json 配置文件说明如下表：

<table>
  <tr>
	<th>参数名称</th>
	<th>类型</th>
	<th>是否<br>必填</th>
	<th>说明</th>
  </tr>
  <tr>
	<td>Client.ToolMode</td>
	<td>bool</td>
	<td>否</td>
	<td>工具迁移模式标识参数，默认值为 <code>false</code>。若使用工具模式迁移，请修改为 <code>true</code> 或运行工具时添加 <code>--no-console</code> 参数。</td>
  </tr>
  <tr>
	<td>Client.Net.Mode</td>
	<td>Integer</td>
	<td>是</td>
	<td>迁移模式参数，默认使用公网传输，值为<code>0</code>，取值范围：<code>0</code>（<a href="https://cloud.tencent.com/document/product/213/65714#publicMigration">公网迁移模式</a>）、<code>1</code>（<a href="https://cloud.tencent.com/document/product/213/65714#Scenario1">内网迁移模式：场景1</a>）、<code>2</code>（<a href="https://cloud.tencent.com/document/product/213/65714#Scenario2">内网迁移模式：场景2</a>）、<code>3</code>（<a href="https://cloud.tencent.com/document/product/213/65714#Scenario3">内网迁移模式：场景3</a>）。</td>
  </tr>
  <tr>
	<td>Client.Extra.IgnoreCheck</td>
	<td>Bool</td>
	<td>否</td>
	<td>默认值为 <code>false</code>，迁移工具默认在工具开始运行时自动检查源端主机环境，如需要跳过检查，请设置为 <code>true</code>。</td>
  </tr>
  <tr>
	<td>Client.Rsync.BandwidthLimit</td>
	<td>String</td>
	<td>否</td>
	<td>限速配置项，单位为 KBytes/s，默认值为空，即默认传输时不限速。</td>
  </tr>
  <tr>
	<td>Client.Rsync.Checksum</td>
	<td>Bool</td>
	<td>否</td>
	<td>传输校验项，设为 <code>true</code> 后可加强传输一致性校验，但会提高源端主机 CPU
	负载和减慢传输速度。默认值为 <code>false</code>，即默认不校验。</td>
  </tr>
</table>

如果源端主机和目标云服务器任何一方不能直接访问公网，则可以选择先通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立连接通道，再进行内网模式迁移。请根据您的源端主机和目标云服务器的网络环境，确定适合的迁移模式。

###  rsync\_excludes\_linux.txt 文件说明[](id:_linuxTxtState)

排除 Linux 源端主机中不需要迁移传输的文件，或指定目录下的配置文件。该文件中已经默认排除以下目录和文件，**请勿删改**。
```shellsession
/dev/*
/sys/*
/proc/*
/var/cache/yum/*
/lost+found/*
/var/lib/lxcfs/*
/var/lib/docker-storage.btrfs/root/.local/share/gvfs-metadata/*
```
如果您需要排除其他目录和文件，请在该文件尾部追加内容。例如，排除挂载在 `/mnt/disk1` 的数据盘的所有内容。
```shellsession
/dev/*
/sys/*
/proc/*
/var/cache/yum/*
/lost+found/*
/var/lib/lxcfs/*
/var/lib/docker-storage.btrfs/root/.local/share/gvfs-metadata/*
/mnt/disk1/*
```

### 工具运行参数说明

<table>
<thead>
<tr>
<th width="18%">参数选项</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td><code>--help</code></td>
<td>打印帮助信息。</td>
</tr>
<tr>
<td><code>--no-console</code></td>
<td>仅使用工具模式迁移（非控制台模式迁移）。</td>
</tr>
<tr>
<td><code>--check</code></td>
<td>对源端主机进行检查</td>
</tr>
<tr>
<td><code>--log-file</code></td>
<td>设置日志文件名称，默认为 <code>log</code>。</td>
</tr>
<tr>
<td><code>--log-level</code></td>
<td>日志输出级别，取值范围为<code>1</code>（ERROR 级别），<code>2</code>（INFO 级别）和<code>3</code>（DEBUG 级别），默认值为<code>2</code>。</td>
</tr>
<tr>
<td><code>--clean</code></td>
<td>目标云服务器强制退出迁移模式，清理现场。例如，如果控制台提示 Please execute '--clean' option manually.，则需要使用此选项执行工具使目标云服务器退出迁移模式。</td>
</tr>
<tr>
<td><code>--version</code></td>
<td>打印版本号。</td>
</tr>
</tbody>
</table>


## 迁移步骤

### 备份数据
- 源端主机：可以选择源服务器快照功能等方式备份数据。
- 目标云服务器：可以选择 [创建快照](https://cloud.tencent.com/document/product/362/5755) 等方式备份数据。


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
- 源端主机检查可以使用工具命令自动检查，如 `./go2tencentcloud_x64 --no-console --check`。
- go2tencentcloud 迁移工具在开始运行时，默认自动检查。如果需要略过检查强制迁移，请将 client.json 文件中的 `Client.Extra.IgnoreCheck` 字段配置为 `true`。
</dx-alert>


### 开始迁移

腾讯云提供的 go2tencentcloud 迁移工具支持断点传输，并将整个迁移过程主要划分为以下三个阶段，用户可以在工具运行过程中直观的了解迁移的进度。

- **阶段1**：目标云服务器进入迁移模式，准备迁移
- **阶段2**：目标云服务器处于迁移模式，迁移数据中
- **阶段3**：目标云服务器退出迁移模式，迁移完成

每个阶段均会产生一些子任务去执行相关操作，部分耗时的子任务还将具有默认的最大超时时间。由于传输数据耗时受源端数据大小，网络带宽等因素影响，请耐心等待迁移流程的完成。
<dx-alert infotype="notice" title="">
开始迁移后目标云服务器将进入迁移模式，请不要对目标云服务器进行重装系统、关机、销毁、重置密码等操作，直至迁移完成退出迁移模式。 
</dx-alert>

<dx-tabs>

:::  公网迁移

1. 将迁移工具 go2tencentcloud.zip 下载或上传至源端主机，并执行以下命令进入对应目录。
  1. 依次执行以下命令，解压 go2tencentcloud.zip 并进入目录。
```shellsession
unzip go2tencentcloud.zip
```
```shellsession
cd go2tencentcloud
```
  2. 依次执行以下命令，解压 go2tencentcloud-linux.zip 并进入目录。
```shellsession
unzip go2tencentcloud-linux.zip
```
```shellsession
cd go2tencentcloud-linux
```
<dx-alert infotype="explain" title="">
`go2tencentcloud` 目录下的文件将不会被迁移，请勿将需迁移的文件放置在该目录下。
</dx-alert>
2. 在 `user.json` 文件配置目标云服务器。
请按照 [user.json 文件参数说明](#userJsonState) 配置必填项和所需项的值。
3. 在 `client.json` 文件配置迁移模式和其他项。
将 `client.json` 文件里的 `Client.ToolMode` 值设置为 `true`，即标识工具模式迁移。此外，如果还需要进行其他项设置，请按照 [client.json 文件参数说明](#clientJsonState) 进行配置。
4. （可选）排除源端主机上不需迁移的文件或目录。
若 Linux 源端主机中存在不需要迁移的文件或目录，可将文件或目录添加至 [rsync_excludes_linux.txt 文件](#_linuxTxtState)。
5. 运行工具。
例如，在64位 Linux 源端主机下，以 root 权限执行以下命令运行工具。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改 client.json 中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`，如下：
```shellsession
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
工具运行后，请耐心等待迁移流程的完成。一般公网迁移模式下，迁移成功的控制台输出如下图所示：
![](https://main.qcloudimg.com/raw/b056d6b1d5ac457ff43e48883848af01.png)

:::
:::  内网迁移场景1

1. 建立源端主机和目标云服务器的连接通道。
通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553) / [VPN 连接](https://cloud.tencent.com/document/product/554) / [云联网](https://cloud.tencent.com/document/product/877) 等方式，建立源端主机和目标云服务器的连接通道。
2. 将迁移工具 go2tencentcloud.zip 下载或上传至源端主机，并执行以下命令进入对应目录。
   1. 依次执行以下命令，解压 go2tencentcloud.zip 并进入目录。
```shellsession
unzip go2tencentcloud.zip
```
```shellsession
cd go2tencentcloud
```
   2. 依次执行以下命令，解压 go2tencentcloud-linux.zip 并进入目录。
```shellsession
unzip go2tencentcloud-linux.zip
```
```shellsession
cd go2tencentcloud-linux
```
<dx-alert infotype="explain" title="">
`go2tencentcloud` 目录下的文件将不会被迁移，请勿将需迁移的文件放置在该目录下。
</dx-alert>
3. 在 `user.json` 文件配置目标云服务器。
请按照 [user.json 文件参数说明](#userJsonState) 配置必填项和所需项的值。
4. 在 `client.json` 文件配置迁移模式和其他项。
   - 将 `client.json` 文件里的 `Client.ToolMode` 值设置为 `true`， 即标识工具模式迁移。
   - 将 `client.json` 文件里的 `Client.Net.Mode` 项设置为`1`，即进行 [内网迁移模式：场景1](https://cloud.tencent.com/document/product/213/65714#Scenario1) 的迁移。此外，如果还需要进行其他项设置，请按照 [client.json 文件参数说明](#clientJsonState) 进行配置。
5. （可选）排除源端主机上不需迁移的文件或目录。
若 Linux 源端主机中存在不需要迁移的文件或目录，可将文件或目录添加至 [rsync_excludes_linux.txt 文件](#_linuxTxtState)。
6. [](id:Scenario1_step06)在一台可以访问公网的主机（如网关）上运行工具。
例如，在一台可以访问公网的主机上执行以下命令运行工具，进行阶段1的迁移。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改client.json中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`， 如下：
```shell
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
若提示 `Stage 1 is finished and please run next stage at source machine.`，则说明阶段1已完成。如下图所示：
![](https://main.qcloudimg.com/raw/f861b47c464f58ea184e5cc5a6a30e1c.png)
7. [](id:Scenario1_step07)在待迁移的源端主机上运行工具。
待 [步骤6](#Scenario1_step06)（即阶段1）完成后，需先将阶段1的整个工具目录拷贝至待迁移的源端主机，再运行工具进行阶段2的迁移。
例如，执行以下命令运行工具，进行阶段2的迁移。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改 client.json 中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`， 如下：
```shellsession
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
若提示 `Stage 2 is finished and please run next stage at gateway machine.`，则说明阶段2已完成。如下图所示：
![](https://main.qcloudimg.com/raw/5684fc8aee6ebf8ba01e42deff3b4fc2.png)
8. 在一台可以访问公网的主机（如网关）上运行工具。
待 [步骤7](#Scenario1_step07)（即阶段2）完成后，需先将阶段2的整个工具目录拷贝至刚才阶段1的主机，再运行工具进行阶段3的迁移。
例如，执行以下命令运行工具，进行阶段3的迁移。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改 client.json 中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`， 如下：
```shellsession
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
若提示 `Migrate successfully.`，则说明整个迁移任务已完成。如下图所示：
![](https://main.qcloudimg.com/raw/851e90fdc07fb601d3d158386d524985.png)




:::
:::  内网迁移场景2

1. 建立源端主机和目标云服务器的连接通道。
通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553) / [VPN 连接](https://cloud.tencent.com/document/product/554) / [云联网](https://cloud.tencent.com/document/product/877) 等方式，建立源端主机和目标云服务器的连接通道。
2. 将迁移工具 go2tencentcloud.zip 下载或上传至源端主机，并执行以下命令进入对应目录。
   1. 依次执行以下命令，解压 go2tencentcloud.zip 并进入目录。
```shellsession
unzip go2tencentcloud.zip
```
```shellsession
cd go2tencentcloud
```
    2. 依次执行以下命令，解压 go2tencentcloud-linux.zip 并进入目录。
```shellsession
unzip go2tencentcloud-linux.zip
```
```shellsession
cd go2tencentcloud-linux
```
<dx-alert infotype="explain" title="">
`go2tencentcloud` 目录下的文件将不会被迁移，请勿将需迁移的文件放置在该目录下。
</dx-alert>
3. 在 `user.json` 文件配置目标云服务器。
请按照 [user.json 文件参数说明](#userJsonState) 配置必填项和所需项的值。
4. 在 `client.json` 文件配置迁移模式和其他项。
    - 将 `client.json` 文件里的 `Client.ToolMode` 值设置为 `true`， 即标识工具模式迁移。
    - 将 `client.json` 文件里的 `Client.Net.Mode` 项设置为`2`，即进行 [内网迁移模式：场景2](https://cloud.tencent.com/document/product/213/65714#Scenario2) 的迁移。此外，如果还需要进行其他项设置，请按照 [client.json 文件参数说明](#clientJsonState) 进行配置。
5. （可选）排除源端主机上不需迁移的文件或目录。
若 Linux 源端主机中存在不需要迁移的文件或目录，可将文件或目录添加至 [rsync_excludes_linux.txt 文件](#_linuxTxtState)。
6. 运行工具。
例如，在64位 Linux 源端主机下，以 root 权限执行以下命令运行工具。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改 client.json 中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`， 如下：
```shellsession
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
工具运行后，请耐心等待迁移流程的完成。一般迁移成功的控制台输出信息如下图所示：![](https://main.qcloudimg.com/raw/d32b4be8287d4b06697f0cb03cc6cff8.png)




:::
:::  内网迁移场景3
1. 建立源端主机和目标云服务器的连接通道。
通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553) / [VPN 连接](https://cloud.tencent.com/document/product/554) / [云联网](https://cloud.tencent.com/document/product/877) 等方式，建立源端主机和目标云服务器的连接通道。
2. 将迁移工具 go2tencentcloud.zip 下载或上传至源端主机，并执行以下命令进入对应目录。
    1. 依次执行以下命令，解压 go2tencentcloud.zip 并进入目录。
```shellsession
unzip go2tencentcloud.zip
```
```shellsession
cd go2tencentcloud
```
    2. 依次执行以下命令，解压 go2tencentcloud-linux.zip 并进入目录。
```shellsession
unzip go2tencentcloud-linux.zip
```
```shellsession
cd go2tencentcloud-linux
```
<dx-alert infotype="explain" title="">
`go2tencentcloud` 目录下的文件将不会被迁移，请勿将需迁移的文件放置在该目录下。
</dx-alert>
3. 在 `user.json` 文件配置目标云服务器。
请按照 [user.json 文件参数说明](#userJsonState) 配置必填项和所需项的值。
4. 在 `client.json` 文件配置迁移模式和其他项。
    - 将 `client.json` 文件里的 `Client.ToolMode` 值设置为 `true`， 即标识工具模式迁移。
    - 将 `client.json` 文件里的 `Client.Net.Mode` 项设置为`3`，即进行 [内网迁移模式：场景3](https://cloud.tencent.com/document/product/213/65714#Scenario3) 的迁移。
    - 将 `client.json` 文件里的 `Client.Net.Proxy.Ip` 和 `Client.Net.Proxy.Port` 项设置为网络代理的 IP 地址和端口。如您的网络代理还需认证，则请在 `Client.Net.Proxy.User` 和 `Client.Net.Proxy.Password` 项填写网络代理的用户名和密码。如不需要认证，则不填。 
		此外，如果还需要进行其他项设置，请按照 [client.json 文件参数说明](#clientJsonState) 进行配置。
5. （可选）排除源端主机上不需迁移的文件或目录。
若 Linux 源端主机中存在不需要迁移的文件或目录，可将文件或目录添加至 [rsync_excludes_linux.txt 文件](#_linuxTxtState)。
6. 运行工具。
例如，在64位 Linux 源端主机下，以 root 权限执行以下命令运行工具。
```shellsession
sudo ./go2tencentcloud_x64 
```
<dx-alert infotype="notice" title="">
若您未修改 client.json 中的 `Client.ToolMode` 为 `true` ，则运行工具时需要添加参数 `--no-console`， 如下：
```shellsession
sudo ./go2tencentcloud_x64 --no-console
```
</dx-alert>
工具运行后，请耐心等待迁移流程的完成。一般迁移成功的控制台输出信息如下图所示：
![](https://main.qcloudimg.com/raw/2195589176d3669f08fbb5745901040b.png)

:::

</dx-tabs>


### 迁移后的检查

- 若迁移结果失败，则请检查日志文件（默认为迁移工具目录下的 log 文件）的错误信息输出、指引文档或者 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 进行排查和修复问题。
- 若迁移结果成功，则请检查目标云服务器能否正常启动、目标云服务器数据与源端主机是否一致、网络是否正常或者其他系统服务是否正常等。

如有任何疑问、迁移异常等问题请查看 [服务迁移类常见问题](https://cloud.tencent.com/document/product/213/32962) 或者 [联系我们](https://cloud.tencent.com/document/product/213/39047) 解决。
