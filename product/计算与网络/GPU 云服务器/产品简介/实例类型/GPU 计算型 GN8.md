## GN8 实例概述
**GPU 计算型 GN8 实例** 适用于通用 GPU 计算应用程序。是基于 GPU 的应用于深度学习、科学计算等多种场景的快速、稳定、弹性的计算服务，腾讯云提供和标准云服务器一致的管理方式。

>**注意：**
>GPU 计算型 GN8 实例数据存储可基于 SSD 的实本地存储。基于 SSD 的本地存储，GN8 实例的系统盘和数据盘只在实例生命周期内存在。当实例到期或您主动销毁实例时，将擦除其实例存储中的应用程序和数据。我们建议您定期备份或复制您存储在实例存储中的数据。

## 适用场景
非常适用于高性能计算能力要求的服务器端 GPU 计算工作负载。
 - 深度学习；
 - 图形数据库；
 - 高性能数据库；
 - 计算流体动力学；
 - 计算金融；
 - 地震分析；
 - 分子建模；
 - 基因组学及其他。

## 硬件规格
- **CPU：**高频 Intel Xeon E5-2680v4 (Broadwell) 。
- **GPU：**NVIDIA Tesla P40 GPU 。
- **内存：**DDR4 。
- **存储：**系统盘：普通云盘／SSD云盘／SSD本地盘； 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据盘：普通云盘／高性能云盘（在高性能云盘白名单内的即可购买）／SSD云盘／SSD本地盘。
- **网络：**默认网络增强， 无额外收费。

	
**GN8 实例提供三种配置：**
<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=11%>GPU<br>(Tesla P40)</th>
			<th width=11%>GPU 显存<br>(GDDR5 @346GB/s)</th>
			<th width=12%>vCPU<br>(Xeon E5 v4)</th>
			<th>内存<br>(DDR4)</th>
			<th>性能指标</th>
		</tr>
		</thead>
			<tbody>
					<tr>
					<td>GN8.LARGE56</td>
					<td>&nbsp;1 颗</td>
					<td>&nbsp;24 GB</td>
					<td>&nbsp;6 核</td>
					<td>&nbsp;&nbsp;&nbsp;56 GB</td>
					<td>&nbsp;&nbsp;&nbsp;&nbsp;12 TFLOPS 单精度浮点运算能力；<br/>&nbsp;&nbsp;&nbsp;&nbsp;47 TOPS 整数运算能力（INT8）。</td>
					</tr>
				<tr>
				<td>GN8.7XLARGE224</td>
				<td>&nbsp;4 颗</td>
				<td>&nbsp;96 GB</td>
				<td>&nbsp;28 核</td>
				<td>&nbsp;224 GB</td>
				<td>&nbsp;&nbsp;&nbsp;&nbsp;48 TFLOPS 单精度浮点运算能力；<br/>&nbsp;&nbsp;&nbsp;&nbsp;188 TOPS 整数运算能力（INT8）。</td>
				</tr>
				<tr>
				<td>GN8.14XLARGE448</td>
				<td>&nbsp;8 颗</td>
				<td>&nbsp;192 GB</td>
				<td>&nbsp;56 核</td>
				<td>&nbsp;448 GB</td>
				<td>&nbsp;&nbsp;&nbsp;&nbsp;96 TFLOPS 单精度浮点运算能力；<br/>&nbsp;&nbsp;&nbsp;&nbsp;376 TOPS 整数运算能力（INT8）。</td>
				</tr>
			</tbody>
</table>

## 支持范围
- 支持 [包年包月](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) 和 [按量计费]( /doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) 。
- 支持在 基础网络 和 [私有网络](/doc/product/213/5227) 中启动。
- 支持 [负载均衡](/doc/product/214/524) 等的业务对接，不增加额外的管理和运维成本，内网流量免费。












