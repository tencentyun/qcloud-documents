云数据库 Redis 内存版（集群架构）是腾讯云基于社区版 Redis Cluster 打造的全新版本，兼容Redis 4.0 和 Redis 5.0 版本命令，采用分布式架构，支持分片和副本的扩缩容，拥有高度的灵活性、可用性和高达千万级 QPS 的高性能。Redis 内存版（集群架构）支持1分片 - 128分片的水平方向扩展，1个 - 5个副本集的副本扩展，扩容、缩容、迁移过程业务几乎无感知，做到最大的系统可用性。
![](https://main.qcloudimg.com/raw/77c61a22ab02087ecbe9e36c9aec7cc5.png)

## 适用场景
**主从高可用场景**
选择单个节点并为节点选择1个副本集，从而达到主从高可用，提供双机热备，故障自动切换的能力，保证 Redis 服务的高可靠和高可用。
 **读写分离场景**  
节点副本数大于等于1，可开启云数据库 Redis 自动读写分离能力，提供单节点读性能扩充，最大支持5个副本集，支持配置主节点以及各副本节点的读访问权重。 
**多分片高性能场景**
内存版（集群架构）自动启动分片模式，通过将不同的 Key 分配到多个节点达到水平扩充系统性能的能力。

## 集群规格
- 分片规格（GB）：2、4、8、12、16、20、24、32、40、48、64
- 分片数量：1、3、5、8、12、16、24、32、40、48、64、80、96、128
- 副本数量：1、2、3、4、5 

## 集群模式
- 集群模式数据将会自动分片，系统将提供数据均衡，数据迁移功能。
- 集群模式支持的分片规格为2GB - 64GB。
- 集群模式的命令相对于非集群模式有一定的兼容性，主要体现在跨 Slot（槽位）数据访问，详细说明请参见 [命令兼容性说明](#xianzhi)。

## 副本说明
- 副本数等于1时，Redis 提供数据主从实时热备，提供数据高可靠和高可用（同一可用区内，跨服务器高可用），HA 系统监测到节点故障后，会将请求切换到从节点，并且新增一个从节点加入到系统。
- 副本数大于1时，Redis 提供数据主从实时热备，并且提供从节点只读功能。

## 功能特性
**灵活性** 
内存版（集群架构）支持最小1个节点到最大128个节点的水平扩容和缩容，支持1个副本集到5个副本集的副本扩容和缩容，通过实例的调整支持多种应用场景。
**可用性** 
内存版（集群架构）的分片数量和副本数量的扩容、缩容对业务完全无感知，做到高度的系统可用性。
 **兼容性**
内存版（集群架构）在应用场景中，支持社区版原生 Cluster 的使用场景，兼容 Jedis 等智能客户端使用场景，兼容 Codis 使用场景。
 **可运维**
内存版（集群架构）将最大程度的开放系统的能力，提供分片级的监控和管理，分片数据迁移和均衡，以及大 Key 监控、热 Key 监控的高级功能，做到系统完整的可管理，可运维。

## [命令兼容性说明](id:xianzhi)
命令支持详情请参见 [命令兼容性概览](https://cloud.tencent.com/document/product/239/76287)。
