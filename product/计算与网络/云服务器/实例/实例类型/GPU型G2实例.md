## GPU型 G2 概述
**GPU型 G2 实例** 适用于通用 GPU 计算应用程序。是基于 GPU 的应用于视频编解码、深度学习、科学计算等多种场景的快速、稳定、弹性的计算服务，腾讯云提供和标准云服务器一致的管理方式。

## 适用场景
非常适用于高图形处理能力要求和高性能计算能力要求的服务器端 GPU 计算工作负载。
 - 深度学习；
 - 图形数据库；
 - 高性能数据库；
 - 计算流体动力学；
 - 计算金融；
 - 地震分析；
 - 分子建模；
 - 基因组学及其他。

## 硬件规格
- **CPU：**高频 Intel Xeon E5-2680 (Broadwell) 。
- **GPU：** NVIDIA Tesla M40 GPU 。
- **内存：**DDR4 。
- **存储：**系统盘与数据盘都为本地 SSD 磁盘，如需扩容可 [购买弹性云盘](/doc/product/362/2732) 进行挂载。	 
- **网络：**默认网络增强， 无额外收费。

	
**G2 实例提供两种配置：**
<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=11%>GPU<br>(Tesla M40)</th>
			<th width=11%>GPU 内存<br>(GDDR5)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>内存<br>(DDR4)</th>
			<th>数据盘<br>(本地 SSD 硬盘)</th>
			<th>性能指标</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>G2.large</td>
					<td>&nbsp;1 颗</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;28 核</td>
					<td>&nbsp;&nbsp;&nbsp;60 GB</td>
					<td>&nbsp;1650 GB</td>
					<td>单机峰值计算能力突破：<br/>&nbsp;&nbsp;&nbsp;&nbsp;7 T Flops 单精度浮点运算；<br/>&nbsp;&nbsp;0.2T Flops 双精度浮点运算。</td>
					</tr>
				<tr>
				<td>G2.2xlarge</td>
				<td>&nbsp;2 颗</td>
				<td>&nbsp;48 GB</td>
				<td>&nbsp;56 核</td>
				<td>&nbsp;120 GB</td>
				<td>&nbsp;3300 GB</td>
				<td>单机峰值计算能力突破：<br/>&nbsp;&nbsp;&nbsp;&nbsp;14 T Flops 单精度浮点运算；<br/>&nbsp;&nbsp;&nbsp;0.4 T Flops 双精度浮点运算。</td>
				</tr>
			</tbody>
</table>

## 支持范围
- 支持 [包年包月](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) 和 [按量计费]( /doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) 。
- 支持在 基础网络 和 [私有网络](/doc/product/213/5227) 中启动。
- 支持 [负载均衡](/doc/product/214/524) 等的业务对接，不增加额外的管理和运维成本，内网流量免费。
