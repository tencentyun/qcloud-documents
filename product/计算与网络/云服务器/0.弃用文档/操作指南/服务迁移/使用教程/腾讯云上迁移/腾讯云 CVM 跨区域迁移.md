跨区域迁移数据，指在腾讯云某个地域下某个可用区的云服务器数据迁移至另一个地域下某个可用区的目标云服务器，也可以指在腾讯云同一个地域下不同可用区的云服务器之间的数据迁移。

## 1. 获取迁移工具  
 [点此获取](https://go2tencentcloud-1251783334.cos.ap-guangzhou.myqcloud.com/latest/go2tencentcloud.zip) 迁移工具压缩包。

## 2. 根据网络环境确定迁移场景
请根据您的源端主机和目标云服务器的网络环境，确定适合的迁移模式。
目前迁移工具支持默认模式和内网迁移模式。其中，内网迁移模式细分为3种场景。不同迁移模式/场景，对源端主机和目标云服务器的网络要求不一致。如果源端主机和目标云服务器均可以访问公网，则可以直接进行默认模式迁移。如果源端主机和目标云服务器任何一方不能直接访问公网，则可以选择先通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立连接通道，再进行内网模式迁移。

## 3. 备份数据
可以选择 [创建快照](https://cloud.tencent.com/document/product/362/5755) 等方式备份数据。

## 4. 迁移前的检查
迁移前，需要分别检查源端主机和目标云服务器。源端主机和目标云服务器需要检查的内容如下：
<table>
	<tr><th style="width: 15%;">目标云服务器</th><td><ol  style="margin: 0;"><li>存储空间：目标云服务器的云硬盘（包括系统盘和数据盘）必须具备足够的存储空间用来装载源端的数据。</li><li>安全组：安全组中不能限制443端口和80端口。</li><li>带宽设置：建议尽可能调大两端的带宽，以便更快迁移。迁移过程中，会产生约等于数据量的流量消耗，如有必要请提前调整网络计费模式。</li><li>目标云服务器和源端主机的操作系统类型是否一致：操作系统不一致会造成后续制作的镜像的信息与实际操作系统不符，建议目标云服务器的操作系统尽量和源端主机的操作系统类型一致。例如，CentOS 7 系统的对源端主机迁移时，选择一台 CentOS 7 系统的云服务器作为迁移目标。</li></ol></td></tr>
	<tr><th>Linux 源端主机</th><td><ol  style="margin: 0;"><li>检查和安装 Virtio，操作详情可参考 <a href="https://cloud.tencent.com/document/product/213/9929">Linux 系统检查 Virtio 驱动</a>。</li><li>检查是否安装了 rsync，可执行 <code>which rsync</code> 命令进行验证。</li><li>检查 SELinux 是否已打开。如果 SELinux 已打开，请关闭 SELinux。</li><li>向腾讯云 API 发起迁移请求后，云 API 会使用当前 UNIX 时间检查生成的 Token，请确保当前系统时间无误。</li></ol></td></tr>
</table>



<dx-alert infotype="explain" title="">
- 源端主机检查可以使用工具命令自动检查，如 `sudo ./go2tencentcloud_x64 --check`。
- go2tencentcloud 迁移工具在开始运行时，默认自动检查。如果需要略过检查强制迁移，请将 client.json 文件中的 `Client.Extra.IgnoreCheck` 字段配置为 `true`。
-  go2tencentcloud 迁移工具详细信息，请参见 [迁移工具说明](https://cloud.tencent.com/document/product/213/38783)。
</dx-alert>



## 5. 开始迁移

1. 建立源端主机和目标云服务器的连接通道。（可选） 
 - 如果您选择内网迁移模式，则需要通过使用 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立源端主机与目标云服务器的连接通道。
 - 如果您选择默认模式，则请跳过此步骤。
2. 配置 user.json 文件。
user.json 是配置源端主机和目标云服务器的文件。该文件的配置项如下：
 - 您的账户 API 访问密钥 SecretId 和 SecretKey，详细信息请参考 [访问密钥](https://cloud.tencent.com/document/product/598/37140)。
 - 目标云服务器所在地域和实例 ID。云服务器支持地域请参见 [地域和可用区](https://cloud.tencent.com/document/product/213/6091)，实例 ID 可前往 [实例列表](https://console.cloud.tencent.com/cvm/instance/index?rid=1) 页面查看。
 - 源端主机的数据盘配置。（可选）  
3. 配置 client.json 文件。
client.json 是配置迁移场景和其他迁移配置项的文件。无论选择哪种迁移模式/场景，均需在 client.json 里的`Client.Net.Mode`项中设置相应的参数值。
4. 排除源端主机上不需迁移的文件和目录。（可选）  
 在 Linux 源端主机编辑 rsync\_excludes\_linux.txt 文件，排除不需要迁移的文件和目录。
5. 运行工具。
例如，在64位 Linux 源端主机下，以 root 权限执行以下命令运行工具。
```
sudo ./go2tencentcloud_x64
```
例如，您使用 [内网迁移模式：场景2](https://cloud.tencent.com/document/product/213/38783#Scenario2) 进行迁移，迁移成功的控制台输出如下所示：
 ![](https://main.qcloudimg.com/raw/3d5c45ccb9f5350bb30cf3d3fce29590/console-cross-region.png)
