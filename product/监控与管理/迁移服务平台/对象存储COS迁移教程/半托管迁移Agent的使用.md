## 概述

msp-agent 是一款将数据迁移至 COS 的工具。您可以将 msp-agent 部署在机房服务器或者云上服务器，它将执行您在 msp 控制台创建的半托管迁移任务，轻松将云存储数据迁移至 COS。

## 支持特性

- 支持丰富的数据源，所有控制台支持录入的源服务商均支持。
- 主从结构，支持分布式模式，部署简单，支持大规模数据高效迁移。
- 支持断点续传。
- 支持流量控制。
- 支持控制台可录入的所有特性，与全托管服务特性保持一致。

## 运行环境
Linux 系统

## 系统部署方法

### 安装
msp-agent安装包下载  [msp-agent](https://msp-agent-1258344699.cos.ap-beijing.myqcloud.com/msp-agent-latest.zip)，下载后进行解压，msp-agent 安装包解压后的目录结构：
![](https://qcloudimg.tencent-cloud.cn/raw/f208f788bb8d20cbc192e02b73460ead.png)
>?
>- msp-agent 是采用 master-worker 的分布式架构，一台 master 一般对应一到多台 worker。
>- master目录即为 master, worker 目录即为 worker。
>- 如果需要部署多个 worker，把 worker 目录整体拷贝，然后修改相应参数后，按下面的启动方式启动即可。
>- 单个服务器可以启动多个 worker 进程，但需要注意按下面参数说明修改相应参数，以防止端口冲突。

### 启动

- 启动 master：
cd {path-to-msp-agent}/master && ./bin/start.sh

- 启动 worker：
cd {path-to-msp-agent}/worker && ./bin/start.sh

### 配置参数说明

master 和 worker 目录下都有相同的 configs 结构：
![](https://qcloudimg.tencent-cloud.cn/raw/6e6e0a1baf256531101e627e491cf8df.png)

其中 pl_config.yaml 配置了进程运行的主要参数；app_logger_config.yaml 配置了应用运行日志格式；query_logger_config.yaml 配置了主从 rpc 通信记录日志格式。

#### 日志配置

日志部分基本采用默认的参数即可。但需要注意日志滚动部分配置：如果磁盘空间有限而任务规模巨大，则需要调节一下日志配置以节省磁盘空间（迁移只有存储日志部分使用到磁盘，实际的文件迁移是不使用磁盘的）。

![](https://qcloudimg.tencent-cloud.cn/raw/16464c28d210bf69eadcfd65ff8e6c7f.png)             

#### Master 配置

| 参数               | 含义                             | 说明                                                         |
| ------------------ | -------------------------------- | ------------------------------------------------------------ |
| "*.*.*.*.gRPCPort" | master 监听 gRpc 端口               | 用于接收 worker上报信息，master 机器此端口一定要向 worker 机器开放。 |
| failFilePartSize   | 记录失败文件的文件分块大小       | 用于记录失败文件的文件分块，乘以10000即为最大失败文件记录大小，默认10485760Byte, 即可记录100GB大小的失败文件；如果待迁移文件特别多，失败的也特别多，比如超过2亿，则此处可往上调。 |
| fragMaxSize        | 分发任务单个分片包含文件大小     | 为了降低主从通信压力，master 派发给 worker 的子任务是将多个文件路径打包成一个**分片**后派发，此处 fragMaxSize 即为单个分片能打包的文件最大总字节数。此处设置太小会使主从通信压力加大，浪费服务器资源，太大会使 worker上报分片完成时间拉长，不够及时，同时会造成 worker 负载不均衡。默认值是10737418240，即为100GB。打包时满足 fragMaxSize 或者 fragMaxNum 其中一个即停止加更多文件。 |
| fragMaxNum         | 分发任务单个分片最大包含文件个数 | 为了降低主从通信压力，master 派发给 worker 的子任务是将多个文件路径打包成一个**分片**后派发，此处 fragMaxNum 即为单个分片能打包的文件最大个数。此处设置太小会使主从通信压力加大，浪费服务器资源，太大会使 worker 上报分片完成时间拉长，不够及时，同时会造成 worker 负载不均衡。默认值是1000。打包时满足 fragMaxSize 或者 fragMaxNum 其中一个即停止加更多文件。 |
| secretId           | 用于请求 MSP 云 API 的密钥SecretId   | Master进程需要请求 msp 云 API，以获取用户在控制台创建的任务，因此此处需要填入用户的密钥，此处填密钥中的 secretId。**注意此处密钥是指创建 MSP 任务的用户密钥，与源桶和目标桶的密钥完全无关。** |
| secretKey          | 用于请求 MSP 云 API 的密钥 SecretKey  | Master进程需要请求msp云API，以获取用户在控制台创建的任务，因此此处需要填入用户的密钥，此处填密钥中的 secretKey。**注意此处密钥是指创建 MSP 任务的用户密钥，与源桶和目标桶的密钥完全无关。** |
| listerIp           | 部署 Master 进程的服务器内网 IP     | 客户可能创建多个任务，而且希望多个任务运行到不同集群，因此此处需要填入部署 Master 进程的服务器的内网 IP，这样此 Master 就只会运行在控制台创建任务时分配到这个服务器 IP 的任务。控制台创建任务时**主节点内网 IP** 表单即输入与本配置相同的 IP。![](https://qcloudimg.tencent-cloud.cn/raw/9120edae88ad48d18df39e655b70a5b6.png) |



#### Worker 配置

| 参数                           | 含义                     | 说明                                                         |
| ------------------------------ | ------------------------ | ------------------------------------------------------------ |
| "*.*.*.*.gRPCPort"             | Worker 监听gRpc 端口       | 用于接收 master 调度信息，worker 机器此端口一定要向 worker 机器开放。如果单个服务器启动多个 worker 进程的话，需要修改此处配置与其他 worker 不同，防止端口冲突而造成的进程启动失败。 |
| fileMigrateTryTimes            | 重试次数                 | 单个文件失败后的重试次数。                                     |
| goroutineConcurrentNum         | 协程并发数               | 并发协程数，也可以理解为并发迁移文件数。跟两个因素有直接关系，一是机器配置大小，机器核数越高，此值可设的越大；二是平均文件大小，单个文件平均越大，此值可设的越小，因为较小的并发协程即可达成较大的带宽占用，单个文件越小，越要增大并发以增大总体带宽。 |
| baseWorkerMaxConcurrentFileNum | 缓存的待迁移文件队列     | 为了加快分布式任务派发效率，每个 worker 都会缓存一些待迁移文件分片，当需要迁移的文件较小，即迁移更高的  qps 时，此值可设置的越大，这样缓存就会缓解 worker 消费的饥饿情形。负面影响是此处缓存越大，master 需要保存的状态数据就越大，会造成 master 负载加大与不稳定。因此此数值需要折中设置。 |
| partSize                       | 分块大小                 | 迁移大文件时分块上传的默认分块大小。                         |
| downloadPartTimeout            | 下载超时时间             | 下载文件的超时时间，单位：秒。                                 |
| uploadPartTimeout              | 上传超时时间             | 上传文件的超时时间，单位：秒。                                 |
| perHostMaxIdle                 | http client 并发设置      | 每个host的连接池大小，一般与 goroutineConcurrentNum 一致即可。 |
| addr                           | 对应的master 内网通信地址 | 配置 worker 对应的 master 通信地址，这样 worker 就会像 master 注册，从而组成集群。例如 master 的 listerIp 是10.0.0.1，master配置里监听的 grpc 端口是22011，则此处addr填入`10.0.0.1:22011` |
| sample                         | 是否做抽样检测           | 在概述中说明了迁移后数据一致性校验的几种情况，对于源文件没有内容签名 Content-MD5 或者 crc64 的文件，是无法直接做一致性检验的，所以只能通过抽样检测来降低不一致概率。如果打开此配置为 true, 则对于源文件没有内容签名 Content-MD5 或者 crc64 的文件, 会做抽样检测。 |
| sampleTimes                    | 单个文件抽样片段数       | 对单个文件的抽样片段数，每一个抽样片段均会多一次下载请求，也意味着会多一部分下载流量。 |
| sampleByte                     | 抽样片段字节数           | 每个抽样片段的大小，越大意味着抽样占用的带宽越大。           |

