>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

欢迎使用云服务器（Cloud Virtual Machine）。

腾讯云服务器（Cloud Virtual Machine，以下又称CVM）运行在腾讯数据中心，它提供了可以弹性伸缩的计算服务，可以根据业务需要来构建和托管软件系统。

云服务器向用户提供弹性的计算、存储和网络资源。用户可以使用本文档介绍的 API，并参照相应的示例，对云服务器进行相关操作：如创建、销毁、更改带宽、重启等；支持的全部操作可参见[API概览页](/doc/api/229/569)。

请确保在使用这些接口前，已充分了解了[云服务器产品说明](/doc/product/213/495)。


## 1. 术语表
本文档涉及的一些常用术语如下：

| 术语 | 全称  | 中文 | 说明 |
|---------|---------|---------|---------|
| Instance | Instance |[实例](https://cloud.tencent.com/doc/product/213/4939) | 指代一台云服务器。
| Image | Image | [镜像](https://cloud.tencent.com/doc/product/213/4940) | CVM实例上软件环境的拷贝，一般包括操作系统和已安装的软件；我们使用镜像来创建实例。 |
| SecurityGroup | Security Group | [安全组](https://cloud.tencent.com/doc/product/213/5221) | 一种有状态的包过滤功能的虚拟防火墙，用于控制CVM实例的网络访问， 是一种重要的网络安全隔离手段。 |
| EIP | Elastic IP | [弹性IP](https://cloud.tencent.com/doc/product/213/5733) | 弹性IP是公网IP的一种。与普通公网IP不同的是，弹性IP归属于用户账户而不是实例；实例与公网IP的映射关系随时可以更改。 |
| Zone | Zone | [可用区](https://cloud.tencent.com/doc/product/213/6091) | 指腾讯云在同一[地域](https://cloud.tencent.com/doc/product/213/6091)内电力和网络互相独立的物理数据中心。目标是能够保证可用区之间故障相互隔离，不出现故障扩散，使得用户的业务持续在线服务。 |
|无 | 无 | 包年包月 |	一种计费模式，参看[计费模式说明](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88)。|
|无| 无| 按量计费 |	一种计费模式，参看[计费模式说明](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9)。|

#### 输入参数与返回参数释义
* limit 和 offset

	>用来控制分页的参数；当相应结果是列表形式时，如果数量超过了 limit 所限定的值，那么只返回limit个值。用户可以通过 limit 和 offset 两个参数来控制分页：limit 为单次返回的最多条目数量，offset 为偏移量。
	>举例来说，参数 offset=0&limit=20 返回第0到20项，offset=20&limit=20 返回第20到40项，offset=40&limit=20 返回第40到60项；以此类推。
	
* id.n

	>同时输入多个参数的格式。当遇到形如这样的格式时，那么该输入参数可以同时传多个。例如：
	
	> id.0=10.12.243.21&id.1=10.11.243.21&id.2=10.12.243.21&id.3=10.13.243.21...
	
	> 以此类推（以下标0开始）。


## 2. API快速入门

CVM API的使用方式这里针对几个典型的使用场景来说明：

1. 通过使用 [创建实例](https://cloud.tencent.com/doc/api/229/1350) API，提供可用区ID、镜像ID、CPU内存组合及数据盘大小等一些必要的信息，即可立刻创建一个按量计费的实例。
2. 如需修改配置，可以使用 [调整配置](https://cloud.tencent.com/doc/api/229/1344) API调整为更高的配置。可调整的内容如内存大小，CPU核数等。
3. 如需关闭实例，可以使用 [关闭实例](https://cloud.tencent.com/doc/api/229/1250) API。关闭后，实例将不再运行。
4. 在不使用此实例时使用 [退还实例](https://cloud.tencent.com/doc/api/229/1347) API销毁它。退还实例后，将不再收费。

## 3. 使用限制 
* CVM API 调用配额为：1000次/分钟；且单一API不超过100次/分钟。
* API创建的机器遵循[CVM实例购买限制](https://cloud.tencent.com/doc/product/213/2664)文档所描述的数量限制，和官网所创建的机器共用配额。
* 更具体的限制请参考每个API接口文档或是产品文档。



