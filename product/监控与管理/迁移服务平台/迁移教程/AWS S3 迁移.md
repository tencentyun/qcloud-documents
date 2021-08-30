
## 操作场景

Agent 半托管迁移模式中，用户需要手工在源数据云厂商的服务上部署 Agent，Agent 通过内网拉取源数据，并推送到腾讯云对象存储 COS。
如果源数据厂商与腾讯云 COS 间已经拉通专线，Agent 半托管迁移模式不会产生出流量费用，因此建议已经部署了专线的用户采用此模式进行迁移。
下文将详细介绍当源对象存储部署在 AWS S3 时，如何配置 Agent 半托管迁移任务，实现数据迁移。

>?“AWS 海外站迁移”，需要登录国际站控制台。



## 准备工作
#### AWS S3
1. 专线准备确认：
Agent 半托管模式如果是通过专线迁移，需要确保AWS云侧主机上使用的 COS SDK，可经过专线访问 COS，迁移前请与商务经理确认。
2. 创建 AWS IAM 账号并授予相关权限：
	1.	登录 AWS 控制台。
	2.	在导航窗格中，选择用户，然后选择添加用户。为新用户键入用户名。
	3.	选择此组用户将拥有的访问权限类型。选择以编程方式访问和访问 AWS 管理控制台。
	4.	单击**Next: Permissions**（下一步：权限）。在 Set permissions 页面上，指定您要向新用户分配权限的方式。授予IAM账号存储空间读写权限。
	5.	单击**Create user**。
	6.	要查看用户的访问密钥（访问密钥 ID 和秘密访问密钥），请选择您要查看的每个密码和访问密钥旁边的显示。要保存访问密钥，请选择下载` .csv`，获取 AccessKeyID 和 AccessKeySecret。

#### 腾讯云对象存储 COS
1. 创建目标存储空间：
创建目标存储空间，用于存放迁移的数据。详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 创建用于迁移的子用户并授予相关权限：
	1. 登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
	2. 在左导航栏中单击 **用户** > **用户列表**， 进入用户列表页面。
	3. 新建子用户，勾选编程访问及腾讯云控制台访问。
	4. 搜索并勾选 QcloudCOSAccessForMSPRole 及 QcloudCOSFullAccess 策略。
	5. 完成子用户创建并保存子用户名，访问登录密码，SecretId，SecretKey。
	6. 单击 [这里](https://migrate-1256125716.cos.ap-guangzhou.myqcloud.com/agent/agent.zip) 下载 Agent。


>?迁移服务也可以使用主账号操作，但是出于安全考虑，建议新建子账号并使用子账号 API 密钥进行迁移，迁移完成后删除。



## 迁移限速
MSP 迁移工具提供了限制 QPS（对象存储模式）和带宽限速（URL 列表模式）。用户在使用 Agent 迁移的情况下，也可以在迁移服务器上进行限速操作，同时在 MSP 中创建任务时选择“不限速”。

1.	执行如下命令，查看网卡序列号。
```
[root@VM_10_12_centos ~]# ifconfig
```
2.	执行如下命令，测试限速前的下载速度。
```
[root@VM_10_12_centos ~]# wget https://msp-test-src-1200000000.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
```
3.	执行如下命令，安装 iproute 工具（默认 Centos 7.x 已安装，此步可跳过）。
```
[root@VM_10_12_centos ~]# yum -y install iproute
```
4.	执行如下命令，将 eth0 网卡限速为50kbit。
```
[root@VM_10_12_centos ~]# /sbin/tc qdisc add dev eth0 root tbf rate 50kbit latency 50ms burst 1000
```
>?
>- eth0 为网卡序号，由第1步查看网卡获取。
>- 如果需要限速10M，则将50kbit改为10Mbit。
5.	限速后测试，执行如下命令，验证下载速度是否已被限制。
```
[root@VM_10_12_centos ~]# wget https://msp-test-src-1200000000.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
```
6.	若您需要解除限速，则可以执行如下命令，即可解除限速。
```
[root@VM_10_12_centos ~]# /sbin/tc qdisc del dev eth0 root tbf
```

## 实施迁移

1.	在迁移源一侧建立用于迁移的临时服务器（主控服务器）。
因为建立迁移任务时需要填写 Agent 主控服务器的 IP 地址（内网 IP 地址，用于与迁移集群中的 Worker 服务器通信），因此在建立迁移任务之前，需先在 AWS 上准备一台操作系统为 CentOS 7.x 64位的云服务器。
2.	在 [腾讯云 MSP](https://console.cloud.tencent.com/msp/v2file) 中建立迁移任务。
i.	在**选择迁移模式**中的“模式选择”部分，选择**新建迁移任务后手动下载 Agent 启动迁移**。
ii.	在“主节点内网 IP”部分，填写 AWS 上创建的服务器内网 IP 地址（例如：172.XXX.XXX.94）。
![](https://main.qcloudimg.com/raw/a6c87ea2574d2b0355fafa3834f7502b.jpg)
>! 
>- 若迁移源与目标源有内容不同，名称相同的文件，建议在**同名文件**配置处选择**跳过（保留目标桶中已有的同名文件）**，系统默认选择**覆盖（源桶中的文件会覆盖目标桶中的同名文件）**。
>- 若在迁移过程中对象（文件）内容有变化，需要进行二次迁移。
3.	所有参数填写完毕后，单击**新建并启动**。需要注意的是，在 Agent 模式下，此时任务虽已创建成功但并未运行，需要按以下步骤在 AWS 主控服务器上手工启动 Agent。
4.	在主控服务器上部署和启动 Agent。
i.	解压 Agent 工具包（目录无特殊要求）。
ii.	修改配置文件。
```
./agent/conf/agent.toml
# 此处填写腾讯云用于迁移的云 API 密钥对
secret_id = '此处填写腾讯云 API 密钥 AccessKey'
secret_key = '此处填写腾讯云 API 密钥 SecretKey'
```
iii.	启动 Agent。
```
# chmod +x ./agent/bin/agent
# cd agent/bin  //必须在 bin 目录中启动 agent 程序（否则会找不到配置文件）
#./agent
Agent 会定时自动从 MSP 平台获取任务的详细配置信息，如果创建多个迁移任务无需重复启动 Agent。
```
5.	扩充迁移集群（增加 Worker 服务器）。
Agent 模式支持分布式迁移（多服务器协同），如果希望进一步提高迁移速度，在有可用带宽的情况下可以增加 Worker 服务器加入到迁移：
	- Worker 服务器必须与 master 服务器互通。
	- 如果使用专线迁移，需要确保 Worker 服务器可通过专线直接访问 COS。
Worker 服务器可以是任意配置，但建议与 master 保持一致。部署和启动 Agent 的方式与 master 服务器完全相同（同样需要修改 agent.toml 中的 secret_id 和 secret_key），因新建任务的时候已经指定了 master 服务器，新加入的 agent 均被作为 Worker 节点与 master 服务器通信获得任务。
Worker 服务器可以随时加入迁移集群，但建议创建任务之前将所有的 Worker 服务器与 master 一同创建并配置和启动 Agent，以便 master 启动任务时可以更有效的进行分片调度。


## 预估文件迁移时间
迁移速度由迁移过程中涉及到的每一个环节的最低速度决定，同时受到网络传输速度和最大并发数影响。影响因素有：


| 影响因素               | 说明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 迁出源的读取速度       | 数据源的读取速度因不同的服务商而不同，通常：<br><li>传输速度在50Mbps - 200Mbps之间。<br><li>文件读取并发在500 - 3000之间（大量小文件的传输受并发限制）。 |
| MSP 平台的传输速度               | MSP 平台提供最大200Mbps的迁移带宽。             |
| 迁入目标位置的写入速度 | 腾讯云对象存储 COS：写入传输速度200Mbps，写入并发500 - 800之间。<br>整体迁移速度会是6MByte - 25MByte（即21GB/小时 - 87GB/小时）之间。 |


