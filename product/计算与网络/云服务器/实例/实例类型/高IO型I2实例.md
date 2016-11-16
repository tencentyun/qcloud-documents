# 高 IO 型 I2 实例
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;高IO型 I2 实例经过了优化，可以向应用程序提供每秒上万次低延迟性随机 I/O 操作 (IOPS)，是高磁盘IO的最佳选择，它们非常适合用于下列情况：

- NoSQL 数据库（例如MongoDB）
- 群集化数据库
- 联机事务处理 (OLTP) 系统

等需要低时延的I/O密集型应用。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;高 IO 型 I2 机器采用主频 2.4 GHz 的 Intel E5-Xeon Broadwell（v4） CPU处理器和 DDR4 内存，其中所有配置的系统盘均为SSD本地盘。搭载网络增强，包转发能力高达30w。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有关高 IO 型 I2 实例支持购买配置，请参阅[CVM实例配置](https://www.qcloud.com/doc/product/213/2177)。 
## 硬件规格
高 IO 型 I2 实例硬件规格如下：

- 2.4 GHz  Intel Xeon  E5-2680 Broadwell（v4） 处理器，DDR4 内存
- CPU性能相比系列 1 高 IO 型 I1 提升20%
- 采用 SSD 的实例存储
	- 高随机 IOPS，典型场景下随机读 IOPS 可达 40000 （blocksize =4k ，iodepth =32）；
	- 高吞吐量，典型场景下随机读吞吐可达 300MB/s（blocksize =4k ，iodepth =32）；
- 默认网络增强型，无需额外付费，包转发率可高达30w pps。


## 高 IO 型 I2 实例功能
以下是 I2 实例功能的摘要：

- I2 实例数据存储是基于 SSD 的实例存储。I2实例的系统盘和数据盘只在实例生命周期内存在。当实例到期或您主动销毁实例时，将擦除其实例存储中的应用程序和数据。我们建议您定期备份或复制您存储在实例存储中的数据。
- I2 实例默认网络增强型，可以显著提高每秒数据包数 (PPS) 性能，降低网络抖动，并减少延迟。

## 高 IO 型 I2 实例要求
以下是 I2 实例的要求：

- I2 实例可以用作[包年包月](https://www.qcloud.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88)实例和[按量计费](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9)实例，也可以用作专用宿主机中高IO型宿主机生产的实例；
- 支持在基础网络和[私有网络](https://www.qcloud.com/doc/product/215/535#.E8.85.BE.E8.AE.AF.E4.BA.91.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E6.98.AF.E4.BB.80.E4.B9.88.EF.BC.9F)中启动 I2 实例；
- 高 IO 型 I2 实例支持购买配置，请参阅[CVM实例配置](https://www.qcloud.com/doc/product/213/2177)。


