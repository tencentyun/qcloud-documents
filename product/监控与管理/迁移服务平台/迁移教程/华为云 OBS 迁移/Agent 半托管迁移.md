## 操作场景

Agent 半托管迁移模式中，用户需要手工在源数据云厂商的服务上部署 Agent，Agent 通过内网拉取源数据，并推送到腾讯云对象存储（Cloud Object Storage，COS）。

如果源数据厂商与腾讯云 COS 间已经拉通专线，Agent 半托管迁移模式不会产生流量费用，因此建议已经部署了专线的用户采用此模式进行迁移。

下文将详细介绍当源对象存储部署在华为云 OBS 时，如何配置 Agent 半托管迁移任务，实现数据迁移。


## 准备工作
#### 华为云对象存储 OBS

1. 专线准备确认（如无专线环境，通过公网迁移可忽略此步骤）：
Agent 半托管模式如果是通过专线迁移，需要确保华为云侧主机上使用的 COS SDK，可经过专线访问 COS，迁移前请与商务经理确认。
2. 创建 IAM 子账号并授予相关权限：
	1. 登录 IAM 控制台。
	2. 选择**人员管理** > **用户** > **新建用户**。
	3. 勾选控制台密码登录和编程访问，之后填写用户账号信息。
	4. 保存生成的账号、密码、AccessKeyID 和 AccessKeySecret。
	5. 勾选用户登录名称，单击**添加权限**，授予子账号存储空间读写权限（OBSOperateAccess）。

#### 腾讯云对象存储 COS

1. 创建目标存储空间，用于存放迁移的数据，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 创建用于迁移的子用户并授予相关权限：
	1.	登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
	2.	在左导航栏中选择**用户** > **用户列表**，进入用户列表页面。
	3.	新建子用户，勾选编程访问及腾讯云控制台访问。
	4.	搜索并勾选 QcloudCOSAccessForMSPRole 及 QcloudCOSFullAccess 策略。
	5.	完成子用户创建并保存子用户名，访问登录密码，SecretId，SecretKey。
3. 单击 [这里](https://migrate-1256125716.cos.ap-guangzhou.myqcloud.com/agent/agent.zip) 下载 Agent。

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
>
5.	限速后测试，执行如下命令，验证下载速度是否已被限制。
```
[root@VM_10_12_centos ~]# wget https://msp-test-src-1200000000.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
```
6.	若您需要解除限速，则可以执行如下命令，即可解除限速。
```
[root@VM_10_12_centos ~]# /sbin/tc qdisc del dev eth0 root tbf
```

## 实施迁移
1. 建立用于迁移的临时服务器（主控服务器）。
因为建立迁移任务时需要填写 Agent 主控服务器的 IP 地址（内网 IP 地址，用于与迁移集群中的 Worker 服务器通信），因此在建立迁移任务之前，需先准备一台操作系统为 CentOS 7.x 64位的云服务器。
>?
>- 如果通过专线迁移，建议服务器在迁移源侧。
>- 如果通过公网迁移，建议服务测使用腾讯云 [云服务器（Cloud Virtual Machine，CVM）](https://cloud.tencent.com/document/product/213)。
2. 在腾讯云 MSP 中建立迁移任务。
 1. 在“选择迁移模式”中的“模式选择”部分，选择“新建迁移任务后手动下载 Agent 启动迁移”。
 2. 在“主节点内网 IP”部分，填写华为云上创建的服务器内网 IP 地址（例如 172.XXX.XXX.94）。
 3. 在“OBS内网EndPoint”部分，填写华为云对象存储桶的“EndPoint（地域节点）”。
![](https://main.qcloudimg.com/raw/e1b2cc7d0ff4a584587ea8dacd8173d3.jpg)
>!
>- 若迁移源与目标源有内容不同，名称相同的文件，建议在**同名文件**配置处选择**跳过（保留目标桶中已有的同名文件）**，系统默认选择**覆盖（源桶中的文件会覆盖目标桶中的同名文件）**。
>- 若在迁移过程中对象（文件）内容有变化，需要进行二次迁移。
>
3. 所有参数填写完毕后，单击**新建并启动**。需要注意的是，在 Agent 模式下，此时任务虽已创建成功但并未运行，需要按以下步骤在华为云主控服务器上手工启动 Agent。
4. 在主控服务器上部署和启动 Agent。
 1. 解压 Agent 工具包（目录无特殊要求）。
 2. 修改配置文件。
```
./agent/conf/agent.toml
# 此处填写腾讯云用于迁移的云 API 密钥对
secret_id = '此处填写腾讯云 API 密钥 AccessKey'
secret_key = '此处填写腾讯云 API 密钥 SecretKey'
```
iii. 启动 Agent。
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

## 查看迁移状态和进度
在文件迁移工具主界面中，可以查看所有文件迁移任务的状态和进度：
 - “任务完成”状态，绿色是任务完成并且所有文件都迁移成功，黄色是迁移任务完成但部分文件迁移失败。
 - 单击“重试失败任务”链接后，该任务中失败的文件将会重试迁移，已经成功迁移的文件不会重传。
 - 单击“导出”链接可以导出迁移过程中失败的文件列表。

