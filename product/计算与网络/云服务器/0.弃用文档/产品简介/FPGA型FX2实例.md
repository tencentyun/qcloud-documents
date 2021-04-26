## FPGA型 FX2 概述
**FPGA型 FX2 实例** 是基于 FPGA（Field Programmable Gate Array）现场可编程阵列的计算服务。具有高吞吐量、低延时、低功耗的特点。从硬件层面加速云计算在各个场景中的应用。
> **注意：**
> 内测阶段，腾讯云提供的公共开发镜像为 CentOS 7.2 64 位 + FPGA 驱动 + 硬件编程工具。

## 适用场景
非常适用于有非常大量的重复性、需要并行计算且时延低的工作。
 - 机器学习计算；
 - 自然语言处理与语音识别；
 - 计算金融；
 - 实时视频处理；
 - 图像压缩；
 - 基因组学研究计算。


## 硬件规格
- **处理器：**Xilinx Kintex UltraScale KU115 FPGA 。
- **内存：**DDR4 ，配有专用 PCle x8 连接。
- **存储：**SSD 云硬盘。 
- **网络：**默认网络增强，万兆网络。

**FX2 实例提供三种配置：**

| 实例规格 | FPGA | DDR4 规格（GiB）| vCPU | 内存（GiB）| 数据盘 | 网络|
|---------|---------|---------|------|------------|------|----|
| &nbsp;FX2.7xlarge60 | &nbsp;1 | &nbsp;2 * 8| &nbsp;14 | &nbsp;60 | &nbsp;SSD 云硬盘 | &nbsp;万兆网络|
| &nbsp;FX2.14xlarge120 | &nbsp;2 | &nbsp;4 * 8 | &nbsp;28 | &nbsp;120 | &nbsp;SSD 云硬盘 | &nbsp;万兆网络|
| &nbsp;FX2.28xlarge240 | &nbsp;4 | &nbsp;8 * 8 | &nbsp;56 | &nbsp;240 | &nbsp;SSD 云硬盘 | &nbsp;万兆网络|
	
