## 实例概述

**NVIDIA 系列 GPU 实例 GN**\* 不仅适用于深度学习、科学计算等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景；腾讯云以和 **[云服务器CVM](https://cloud.tencent.com/product/cvm) 一致的管理方式**，提供快速、稳定、弹性的计算服务。

>! GN\* 系列实例用作 3D 图形渲染（GN2 不支持）需要安装 GRID Driver 和配置 License Server，安装方法参考 [安装 NVIDIA GRID 驱动](https://cloud.tencent.com/document/product/560/30060)。

## 适用场景
适用于数据吞吐量大且对计算速度有要求的工作场景，例如：
- 深度学习
- 图形图像处理
- 视频编解码
- 图形数据库
- 高性能数据库
- 计算流体动力学
- 计算金融
- 地震分析
- 分子建模
- 基因组学及其他

## 硬件规格
基本硬件规格如下图所示：
![](https://main.qcloudimg.com/raw/3facef30152a1700147e457a5f40b0e3.png)

**规格说明**：
- GPU 性能：主要指标为 GPU 的浮点运行能力，TF 代表 T Flops，SP 代表 single-precision 单精度浮点运算，DP 代表 double-precision 双精度浮点运算，INT8 代表 INT8 整数运算，DL 代表 Tensor Core 的深度学习加速能力（仅适用 V100）。
- 存储/网络：存储列表展示了当前实例所支持购买的存储类型，增强型 SSD 云盘目前在内测阶段；网络带宽是指该类型实例所在物理机的网络带宽，某一类型具实例所分配的网络带宽详见购买页。
>!GN2，GN8 实例提供基于 SSD 的本地存储（GN2 实例的存储默认强制选择固定容量的 SSD 本地磁盘，详见购买页）。采用本地存储时，这些实例的系统盘和数据盘只在实例生命周期内存在；当实例到期或您主动销毁实例时，将擦除其实例存储中的应用程序和数据。我们建议您定期备份存储在实例存储中的数据。

## 选型推荐
腾讯云提供了类型丰富的 GPU 计算实例，满足不同业务应用场景的需求。如何结合实际需求选择合适的计算实例，可参考 [选型推荐](https://cloud.tencent.com/document/product/560/30130)。

## 支持范围
- 支持 [包年包月](https://cloud.tencent.com/document/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) 和 [按量计费](https://cloud.tencent.com/document/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) 。
- 支持在基础网络和 [私有网络](https://cloud.tencent.com/document/product/213/5227) 中启动。
- 支持 [负载均衡](https://cloud.tencent.com/document/product/214/524) 等的业务对接，不增加额外的管理和运维成本，内网流量免费。
