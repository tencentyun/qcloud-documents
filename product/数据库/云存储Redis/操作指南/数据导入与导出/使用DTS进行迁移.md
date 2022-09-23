## 背景简介
腾讯云 [数据传输服务](https://cloud.tencent.com/document/product/571)（Data Transmission Service，DTS）是提供数据迁移、数据同步、数据订阅于一体的数据库数据传输服务，可帮助用户在业务不停服的前提下轻松完成数据库迁移上云，利用实时同步通道轻松构建高可用的数据库容灾架构，通过数据订阅来满足商业数据挖掘、业务异步解耦等场景需求。 

DTS for Redis 目前支持数据迁移功能，可一次性将数据迁移到云上数据库，迁移过程中不停机，并且支持全量 + 增量数据的迁移，即迁移前源库的历史数据，和迁移过程中源库新增的写入数据都支持一起迁移。 

## 适用场景

DTS 支持 Redis 数据迁移的源端和目标端部署形态如下：

| 源端                                            | 目标端       | 说明                                                         |
| ----------------------------------------------- | ------------ | ------------------------------------------------------------ |
| 自建数据库 Redis（IDC 自建、腾讯云 CVM 上自建） | 腾讯云 Redis | -                                                            |
| 第三方云厂商 Redis                              | 腾讯云 Redis | 前提条件是云厂商需要提供 SYNC 或者 PSYNC 命令权限            |
| 腾讯云 Redis                                    | 腾讯云 Redis | 支持相同腾讯云账号下数据库实例之间的数据迁移，如版本升级、跨地域迁移等。 |

## 迁移支持说明
>?单机版迁移内存版（集群架构）兼容性问题请参见 [单机版迁移集群版说明](https://cloud.tencent.com/document/product/239/43697)。

#### 支持版本
- DTS 迁移服务支持的版本包括 Redis 2.8、3.0、3.2、4.0、5.0、6.0，其中6.0版本如需体验请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行申请。建议目标库版本大于或等于源库版本，否则会存在兼容性问题。
- 标准架构和集群架构支持相互迁移，但异构迁移（如集群架构 > 标准架构）可能会存在兼容性问题。
- 支持的架构包括单节点、redis cluster、codis、twemproxy。
- 迁移权限要求：DTS 迁移数据需要源实例支持 SYNC 或者 PSYNC 命令。

#### 支持网络
DTS 迁移服务支持常见的网络迁移，包括公网、CVM 自建、专线接入、VPN 接入、云联网场景下的数据迁移。

- 公网：源数据库可以通过公网 IP 访问。
- 云主机自建：源数据库部署在 [腾讯云服务器 CVM](https://cloud.tencent.com/document/product/213) 上。
- 专线接入：源数据库可以通过 [专线接入](https://cloud.tencent.com/document/product/216) 方式与腾讯云私有网络打通。 
- VPN 接入：源数据库可以通过 [VPN 连接](https://cloud.tencent.com/document/product/554) 方式与腾讯云私有网络打通。 
- 云联网：源数据库可以通过 [云联网](https://cloud.tencent.com/document/product/877) 与腾讯云私有网络打通。

#### 迁移限制
- 为保障迁移效率，CVM 自建实例迁移不支持跨地域迁移。
- 外网实例迁移时，需确保源实例服务在外网环境下可访问。
- 进行迁移任务时，只允许迁移正常运行状态下的实例，未初始化密码或者有其他任务在执行中的实例，不能迁移。
- 目标实例必须是没有数据的空实例，迁移过程中，目标实例会被设置为只读，不能对实例进行写入操作。
- 迁移成功时，由业务侧验证数据后，可断开源实例连接，将连接切换到目标实例。

## 环境要求
### 系统检查
> ?DTS 系统会在启动迁移任务前进行如下校验，不符合要求的系统会报错提示，用户也可提前进行自查，报错后的处理方法请参考 [Redis 校验项](https://cloud.tencent.com/document/product/571/61639#redis)。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源库要求</td>
<td>
<li>源库和目标库网络能够连通。</li><li>源库中的数据库个数需要小于或等于目标库的数据库个数。</li><li>Redis 源实例版本需要大于等于2.2.6，2.2.6以下版本不支持 DTS 迁移。</li><li>源库必须为 Slave 节点，否则校验项会报警告。</li></td></tr>
<tr> 
<td>目标库要求</td>
<td>
<li>建议目标库的版本大于或等于源实例的版本，否则校验时会报警告，提示兼容性问题。</li><li>目标端 Redis 的 Proxy 版本为最新版本。</li>
<li>目标库的空间必须大于等于源库待迁移数据所占空间的1.5倍。</li>
<li>目标库必须为空。</li></td></tr>
</table>

### [用户自查](id:zxjc)
如下检查需要用户在迁移前自行排查，否则可能会出现迁移失败。

#### 检查源端是否存在大 Key
迁移之前，请检查源端数据库中是否存在大 Key。在迁移过程中，大 Key 可能引起缓冲区 client-output-buffer-limit 溢出，导致迁移失败。
- 腾讯云数据库，请使用数据库智能管家（TencentDB for DBbrain，DBbrain）的诊断优化功能快速分析大 Key。具体操作，请参见 [内存分析](https://cloud.tencent.com/document/product/239/73524)。
- 非腾讯云数据库，请使用 rdbtools 分析 Redis 大 Key。具体操作，请参见 [如何使用 rdbtools 分析 Redis 大 Key](https://cloud.tencent.com/developer/article/1981133)。

评估大 Key 进行拆分或清理，如果保留大 Key，请设置源端缓冲区的大小 client-output-buffer-limit 为无限大。
```
config set client-output-buffer-limit 'slave 0 0 0' 
```

#### 检查源端 Linux 内核 TCP 连接数的限制
如果业务并发请求比较大，迁移之前，请检查 Linux 内核对连接数的限制，如果业务请求连接数超出内核限制的连接数，Linux 服务器将会主动断开与 DTS 的连接。
```
echo "net.ipv4.tcp_max_syn_backlog=4096" >> /etc/sysctl.conf
echo "net.core.somaxconn=4096" >> /etc/sysctl.conf
echo "net.ipv4.tcp_abort_on_overflow=0" /etc/sysctl.conf
sysctl -p
```

#### 检查源端 RDB 文件目录的访问权限
迁移之前，请务必检查源端存放 RDB 文件目录的访问权限是否为可读，否则将会因 RDB 文件不可读而引起迁移失败。

如果RDB文件所在目录不可读，请在源端执行如下命令，设置“无盘复制”，直接发送 RDB 文件给 DTS 落盘，而不需要保存在源端的磁盘再发送。 
```
config set repl-diskless-sync yes
```

#### 标准架构迁移到集群架构，请检查命令兼容性问题
标准架构迁移至内存版（集群架构）面临的最大问题为命令是否兼容内存版（集群架构）的使用规范。

- 多 Key 操作
  腾讯云数据库 Redis 内存版（集群架构）仅支持 mget、mset、 del 、 exists 命令的跨 SLOT 多 Key 访问， 源端数据库可以通过 Hash Tag 的方式，将需要进行多 Key 运算的 Key 聚合至相同 SLOT，Hash Tag 的使用方式请参考 [Redis Cluster 文档](https://redis.io/topics/cluster-spec)。 
- 事务操作
  内存版（集群架构）支持事务，但是事务中的命令不能跨 SLOT 访问 Key。

具体操作，请参见 [标准架构迁移集群架构检查](https://cloud.tencent.com/document/product/239/43697) 进行静态评估与动态评估。

## 迁移步骤
#### 1. 新建迁移任务
1）登录 [DTS 控制台](https://console.cloud.tencent.com/dts )，在数据迁移页，单击**新建迁移任务**。
2）在新建迁移任务页面，选择源数据库和目标数据库的类型、地域信息，然后单击**立即购买**。

#### 2. 设置源和目标数据库
填写源库设置和目标库设置，单击**连通性测试**，测试通过后，单击**保存**进入下一步。
![](https://qcloudimg.tencent-cloud.cn/raw/96df8c4fb4ab868be8f6f6bde8145701.png)
<table>
<thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
<tbody>
<tr>
<td rowspan=3>任务设置</td>
<td>任务名称</td>
<td>设置一个具有业务意义的名称，便于任务识别。</td></tr>
<tr>
<td>运行模式</td>
<td>可以设置立即执行任务或者定时执行。<ul><li>修改定时任务，校验通过后，需要重新单击<b>定时启动</b>，任务才会定时启动。</li><li>如果任务过了定时启动的时间，定时启动会变为立即启动，单击<b>立即启动</b>，会立刻启动任务。
</li></ul></td></tr>
<tr>
<td>标签</td>
<td>标签用于从不同维度对资源分类管理。如现有标签不符合您的要求，请前往控制台管理标签。</td></tr>
<tr>
<td rowspan=7>源库设置</td>
<td>源库类型</td><td>购买时选择的源数据库类型，不可修改。</td></tr>
<tr>
<td>所属地域</td><td>购买时选择的地域，不可修改。</td></tr>
<tr>
<td>接入类型</td><td>对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。<br>本场景选择“专线接入”或“VPN接入”，该场景需要 <a href="https://cloud.tencent.com/document/product/571/60604">配置 VPN 和 IDC 之间的互通</a>，其他接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。
<ul><li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li></ul></td></tr>
<tr>
<td>私有网络专线网关</td><td>专线接入时只支持私有网络专线网关，请确认网关关联网络类型。</td></tr>
<tr>
<td>私有网络</td><td>选择私有网络专线网关关联的私有网络和子网。</td></tr>
<tr>
<td>节点类型</td><td>支持单节点迁移和集群版迁移。此处以“集群迁移”为例进行介绍。<br>目前 Redis 集群版迁移到集群版时，对分片数量和副本数量没有限制。</td></tr>
<tr>
<td>节点信息</td><td>填写源库集群的所有分片节点地址和密码（IP:端口:密码 或 IP:端口），多个节点请换行处理。<br>强烈建议从源库的副本节点（从节点）进行数据迁移，避免影响源库的业务访问。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>购买时选择的目标库类型，不可修改。</td></tr>
<tr>
<td>所属地域</td><td>购买时选择的目标库地域，不可修改。</td></tr>
<tr>
<td>接入类型</td><td>根据您的场景选择，本场景选择“云数据库”。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标库的实例 ID。</td></tr>
</tbody></table>

#### 3. 校验和启动任务
在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。

- 校验结果为失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。  
- 校验结果为警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。

返回数据迁移任务列表，任务进入准备运行状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。

#### 4. 完成迁移任务 
1）（可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
2）当源库和目标库的 key 同步一致时，在**操作**列单击**完成**，结束数据迁移任务。
![](https://qcloudimg.tencent-cloud.cn/raw/b553ad8c8b40da22906ce72286e5f7d6.png)
3）当迁移任务状态变为**任务成功**时，请先在目标数据库上验证数据，如果验证无误，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。
![](https://qcloudimg.tencent-cloud.cn/raw/327f36c3bafef9fb8010221839228928.png)

## 事件告警和指标监控
1）DTS 支持迁移中断自动上报事件告警，以便及时了解到迁移任务的异常，详细步骤请参考 [配置数据迁移告警](https://cloud.tencent.com/document/product/571/59192)。
2）DTS 支持查看迁移过程中的各项指标监控， 以便了解系统的各项指标性能，请参考 [查看监控指标](https://cloud.tencent.com/document/product/571/59202)。


