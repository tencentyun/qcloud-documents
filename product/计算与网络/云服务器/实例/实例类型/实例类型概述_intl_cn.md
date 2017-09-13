
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;创建腾讯云云服务器时，用户指定的***实例类型*** 决定了实例的主机硬件配置。每个实例类型提供不同的计算、内存和存储功能。用户可基于需要部署运行的应用规模，选择一种适当的实例类型。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPU、内存、存储和网络等相关资源均是该CVM实例专用的。但实例间也会存在共享某些资源的情况，例如[共享网络](https://www.qcloud.com/doc/product/213/509#2.-.E5.85.B1.E4.BA.AB.E7.BD.91.E7.BB.9C)等。

## 硬件规格
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有关每种实例类型的具体硬件规格的更多信息，请参考 [CVM 实例配置](https://www.qcloud.com/doc/product/213/2177)。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要确定最适合您需求的实例类型，我们建议启动一个按量计费实例，并使用自己的基准测试应用程序。由于是按实例使用量付费，因而您能够在做出决策前方便而经济地测试不同的实例类型。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在购买并使用了某一实例后，当用户的需求发生变化时，仍可以调整实例的大小，更多信息请参考[调整 CVM 硬件配置](/doc/product/213/5730)。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面分别介绍各种实例系列和实例类型。需要注意的是，一台已经创建好的云服务器实例 ***不能*** 转换成其他类型，需要新类型的实例时请重新创建。

## 可用实例类型
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据底层硬件的不同，腾讯云目前提供了 *系列 1* 和 *系列 2* （下文也称为 *上一代实例* 和 *当前一代实例* ）两种不同的实例系列，不同的实例系列提供如下实例类型：

**当前一代实例类型**：[标准型S2](https://www.qcloud.com/doc/product/213/7154)，[高IO型I2](https://www.qcloud.com/doc/product/213/7155)，[内存型M2](https://www.qcloud.com/doc/product/213/7156)，[计算型C2](https://www.qcloud.com/doc/product/213/7157)
**上一代实例类型**：标准型S1，高IO型I1，内存型M1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为获得最佳性能，我们建议您在新建实例时使用当前一代实例类型。

### 当前一代实例
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;系列 2 采用 Intel E5-Xeon Broadwell（v4） CPU、搭配 DDR4 内存，拥有更好的内存计算能力；**全面**搭配网络增强，网络转发能力最高可达30w pps。整数和浮点运算能力提升了40%，整体计算能力更强。


### 上一代实例
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;系列 1 采用 Intel Xeon CPU，搭配 DDR3 内存。

## 实例限制

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实例系列2支持 广州二区、广州三区、上海一区、上海二区、北京二区的购买。如需购买，请参考[CVM购买配置](https://www.qcloud.com/document/product/213/2177)。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在一个区域中可以启动的实例总数存在限制，有关限制的更多信息，请参阅 [CVM 实例购买限制](https://www.qcloud.com/doc/product/213/2664)






