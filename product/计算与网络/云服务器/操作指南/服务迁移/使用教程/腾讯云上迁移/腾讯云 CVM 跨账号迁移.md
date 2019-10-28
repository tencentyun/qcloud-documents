在线迁移工具支持腾讯云两个不同主机之间的迁移。跨账号迁移是指两个不同账号下的主机之间的迁移。

## 1. 获取迁移工具  
 [点此获取](https://go2tencentcloud-1251783334.cos.ap-guangzhou.myqcloud.com/v2.0.0/go2tencentcloud.zip) 迁移工具压缩包。

## 2. 根据网络环境确定迁移模式
请根据您的源端主机和目标云服务器的网络环境，确定适合的迁移模式。
目前迁移工具支持默认模式和内网迁移模式。其中，内网迁移模式细分为3种场景。不同迁移模式/场景，对源端主机和目标云服务器的网络要求不一致。如果源端主机和目标云服务器均可以访问公网，则可以直接进行默认模式迁移。如果源端主机和目标云服务器任何一方不能直接访问公网，则可以选择先通过 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立连接通道，再进行内网模式迁移。

## 3. 备份数据
可以选择创建快照等方式备份数据。

## 4. 迁移前检查
迁移前，需要分别检查源端主机和目标云服务器。源端主机和目标云服务器需要检查的内容如下：
<table>
	<tr><th style="width: 15%;">目标云服务器</th><td><ol  style="margin: 0;"><li>目标云服务器系统盘的存储空间：迁移后，目标云服务器的系统盘会存放源端主机根目录的数据。</li><li>是否限制443端口和80端口：使用默认模式迁移时，需要公网访问能力，安全组中不能限制443端口和80端口。</li><li>带宽设置：建议尽可能调大两端的带宽，以便更快迁移。迁移过程中，会产生约等于数据量的流量消耗，如有必要请提前调整网络计费模式。</li><li>目标云服务器和源端主机的操作系统类型是否一致：操作系统不一致会造成后续制作的镜像的信息与实际操作系统不符，建议目标云服务器的操作系统尽量和源端主机的操作系统类型一致。例如，CentOS 7 系统的对源端主机迁移时，选择一台 CentOS 7 系统的云服务器作为迁移目标。</li></ol></td></tr>
	<tr><th>Linux 源端主机</th><td><ol  style="margin: 0;"><li>检查和安装 Virtio，操作详情可参考 <a href="https://cloud.tencent.com/document/product/213/9929">Linux 系统检查 Virtio 驱动</a>。</li><li>检查是否安装了 rsync 和 grub2-install（或 grub-install）。</li><li>检查 SELinux 是否已打开。如果 SELinux 已打开，请关闭 SELinux。</li><li>向腾讯云 API 发起迁移请求后，云 API 会使用当前 UNIX 时间检查生成的 Token，请确保当前系统时间无误。</li></ol></td></tr>
</table>

>? 
> - 源端主机检查可以使用工具命令自动检查，如 `sudo ./go2tencentcloud_x64 --check`。
> - go2tencentcloud 迁移工具在开始运行时，默认自动检查。如果需要略过检查强制迁移，请将 client.json 文件中的`Client.Extra.IgnoreCheck`字段配置为`true`。
> 

## 5. 开始迁移
 
1. 建立源端主机和目标云服务器的连接通道。（可选）  
 - 如果您选择内网迁移模式，则需要通过使用 [VPC 对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[云联网](https://cloud.tencent.com/document/product/877) 或者 [专线接入](https://cloud.tencent.com/document/product/216) 等方式建立源端主机与目标云服务器的连接通道。
 - 如果您选择默认模式，则请跳过此步骤。
2. 配置 user.json 文件。
user.json 是配置源端主机和目标云服务器的文件。该文件的配置项如下：
 - 您的账户 API 访问密钥 SecretId 和 SecretKey，详细信息请参考 [访问密钥](https://cloud.tencent.com/document/product/598/37140)。
 - 目标云服务器所在地域。
 - 目标云服务器的实例 ID。
 - 源端主机的数据盘配置。（可选）  
3. 配置 client.json 文件。
client.json 是配置迁移模式和其他迁移配置项的文件。无论选择哪种迁移模式/场景，均需在 client.json 里的`Client.Net.Mode`项中设置相应的参数值。
4. 排除源端主机上不需迁移的文件和目录。（可选）  
 在 Linux 源端主机编辑 rsync\_excludes\_linux.txt 文件，排除不需要迁移的文件和目录。
5. 运行工具。
以 [内网迁移模式：场景1](https://cloud.tencent.com/document/product/213/38654#Scenario1) 进行跨账号迁移为例：  
 1. 在一台可以访问公网的主机上，执行以下命令，运行工具，进行初始化远程实例的迁移。
```
sudo ./go2tencentcloud_x64
```
若返回`Stage 1 is finished and please run next stage at source machine.`，则说明初始化远程实例已完成。 
 ![](https://main.qcloudimg.com/raw/afeceabbdaad10f348cd0805b209e5cb.png)
 2. 待上一步骤（即初始化远程实例）完成后，需先将初始化远程实例的整个工具目录拷贝至待迁移的源端主机，再运行工具进行传输数据的迁移。
 例如，执行以下命令运行工具，进行传输数据的迁移。
```
sudo ./go2tencentcloud_x64
```
若返回`Stage 2 is finished and please run next stage at gateway machine.`，则说明传输数据已完成。
 ![](https://main.qcloudimg.com/raw/be35753f3f8f3a30b8d6364a1052991f.png)
 3. 待上一步骤（即传输数据）完成后，需先将传输数据的整个工具目录拷贝至刚才初始化远程实例的主机，再运行工具进行传输数据的迁移。
 例如，执行以下命令运行工具，进行传输数据的迁移。
```
sudo ./go2tencentcloud_x64
```
若返回`Migrate successfully.`，则说明整个迁移任务已完成。
 ![](https://main.qcloudimg.com/raw/1cf4ef72cebab8b42440608643cedade.png)
 
 
