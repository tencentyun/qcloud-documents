## 操作场景
Agent 半托管迁移模式中，客户需要手工在源数据云厂商的服务上部署 Agent，Agent 通过内网拉取源数据，并推送到腾讯云对象存储 COS。
如果源数据厂商到腾讯云 COS 间已经拉通专线，Agent 半托管迁移模式不会产生出流量费用。因此建议已经有专线的用户采用此模式进行迁移。

## 操作步骤
1. 专线准备确认。
Agent半托管模式如果是通过专线迁移，需要确保友商云侧主机上使用COS SDK可经过专线访问COS，迁移前请与商务经理确认。 

2. 迁移限速。
MSP 迁移工具提供了限制 QPS（对象存储模式）和带宽限速（URL 列表模式）。在使用 Agent 迁移的情况下，也可以在迁移服务器上进行限速操作，同时在MSP中创建任务时选择“不限速”

 

2.1. 查看网卡
```bash
[root@VM_10_12_centos ~]# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
inet 10.0.10.12  netmask 255.255.255.0  broadcast 10.0.10.255
ether 52:54:00:bb:49:0f  txqueuelen 1000  (Ethernet)
RX packets 13361  bytes 19400520 (18.5 MiB)
RX errors 0  dropped 0  overruns 0  frame 0
TX packets 1001  bytes 67101 (65.5 KiB)
TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
inet 127.0.0.1  netmask 255.0.0.0
loop  txqueuelen 1000  (Local Loopback)
RX packets 0  bytes 0 (0.0 B)
RX errors 0  dropped 0  overruns 0  frame 0
TX packets 0  bytes 0 (0.0 B)
TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
 

2.2. 限速前测试
```bash
[root@VM_10_12_centos ~]# wget https://msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
--2019-04-08 10:47:41--  https://msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
Resolving msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com (msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com)... 211.159.131.23, 211.159.131.24, 211.159.130.21, ...
Connecting to msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com (msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com)|211.159.131.23|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1574565066 (1.5G) [application/octet-stream]
Saving to: ‘bkce_src-5.0.2.tar.gz’
5% [========>] 86,299,969  14.2MB/s  eta 94s 
```
 

2.3. 安装 iproute 工具（默认 centos 7.x 已安装，此步可跳过）
```
[root@VM_10_12_centos ~]# yum -y install iproute
Loaded plugins: fastestmirror, langpacks
Determining fastest mirrors
Package iproute-4.11.0-14.el7.x86_64 already installed and latest version
Nothing to do
```
 

 

2.4. 限速
```
[root@VM_10_12_centos ~]# /sbin/tc qdisc add dev eth0 root tbf rate 50kbit latency 50ms burst 10000
```
 

如果需要限速10M，可以将50kbit改为10Mbit

 

2.5. 限速后测试
```
[root@VM_10_12_centos ~]# wget https://msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
--2019-04-08 10:49:15--  https://msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com/bkce_src-5.0.2.tar.gz
Resolving msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com (msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com)... 139.199.41.140, 119.29.47.254, 211.159.130.20, ...
Connecting to msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com (msp-test-src-1256125716.cos.ap-guangzhou.myqcloud.com)|139.199.41.140|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1574565066 (1.5G) [application/octet-stream]
Saving to: ‘bkce_src-5.0.2.tar.gz.1’
 0% [                  ] 155,313      359KB/s
```

 

2.6. 解除限速
```
[root@VM_10_12_centos ~]# /sbin/tc qdisc del dev eth0 root tbf
```
 



3. 实施迁移
3.1 在迁移源一侧建立用于迁移的临时服务器（主控服务器）
因为建立迁移任务时需要填写Agent主控服务器的IP地址（内网IP地址，用于与迁移集群中的worker服务器通信），因此在建立迁移任务之前，先在友商云上准备一台服务器。操作系统CentOS 7.x 64位

例如：在友商云上先创建一台主控服务器，内网IP地址172.19.97.94

3.2 在腾讯云MSP中建立迁移任务
在“选择迁移模式”中的“模式选择”部分，选择“新建迁移任务后手动下载Agent启动迁移” 
在“主节点内网IP”部分，填写友商云上创建的服务器内网IP地址（172.19.97.94）


所有参数填写完毕后，按下“新建并启动”按钮。需要注意的是，在Agent模式下任务已创建成功但并未运行，需要按以下步骤在阿里云主机上手工启动Agent。

 

3.3. 在主控服务器上部署和启动Agent
3.3.1. 将Agent工具解压到合适的目录（目录无特殊要求）

3.3.2. 修改配置文件
```
./agent/conf/agent.toml
# 此处填写腾讯云用于迁移的云API密钥对
secret_id = '此处填写腾讯云API密钥AccessKey'
secret_key = '此处填写腾讯云API密钥SecretKey'
```

3.3.3. 启动Agent
```
# chmod +x ./agent/bin/agent
# cd agent/bin
#./agent
```
必须在bin目录中启动agent程序（否则会找不到配置文件）

 

Agent会定时自动从MSP平台获取任务的详细配置信息，如果创建多个迁移任务无需重复启动Agent。

3.4. 扩充迁移集群（增加worker服务器）
Agent模式支持分布式迁移（多服务器协同），如果希望进一步提高迁移速度，在有可用带宽的情况下可以增加worker服务器加入到迁移：
- worker服务器必须与master服务器互通。
- 如果使用专线迁移，需要确保worker服务器可通过专线直接访问COS。

worker 服务器可以是任意配置，但建议与master保持一致。部署和启动Agent的方式与master服务器完全相同（同样需要修改agent.toml中的secret_id和secret_key），因新建任务的时候已经指定了master服务器，新加入的agent均被作为worker节点与master服务器通信获得任务。 

Worker服务器可以随时加入迁移集群，但建议创建任务之前将所有的worker服务器与master一同创建并配置和启动Agent，以便master启动任务时可以更有效的进行分片调度。
