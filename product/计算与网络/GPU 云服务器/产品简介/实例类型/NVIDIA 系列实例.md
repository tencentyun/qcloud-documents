

**NVIDIA 系列 GPU 实例 GN\*** 能够提供强大的计算能力，从容应对高实时、高并发的海量计算场景。不仅适用于深度学习、科学计算等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。腾讯云 GPU 云服务器以和 **[云服务器 CVM](https://cloud.tencent.com/product/cvm) 一致的管理方式**，提供快速、稳定、弹性的计算服务。



## NVIDIA 系列实例总览

NVIDIA 系列实例包括计算型和渲染型两类。其中：
- **渲染型**：适用于 3D 渲染、视频编解码、CAD 等。
- **计算型**：适用于深度学习、科学计算、CAE 等。

**GPU 云服务器 NVIDIA 系列提供以下实例：**

<table>
        <thead>
        <tr>
            <th width="11%">类型</th>
            <th width="3%">实例</th>
            <th width="17%">GPU 类型</th>
            <th width="34%">可用镜像</th>
            <th style="width: 38%;">可用区域</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="9">计算型</td>
								<td><a href="#GT4">GT4</a></td> 
                <td>Tesla A100 NVLink 40G</td>
                                <td><ul class="params"><li>CentOS 7.2 及以上</li><li>Ubuntu 16.04 及以上</li><li>Windows Server 2016 及以上</li></ul></td>
                <td>广州、上海、北京</td>
            </tr>
						<td><a href="#GN10XGN10Xp">GN10X<br>GN10Xp</a></td> 
                <td>Tesla V100 NVLink 32G</td>
                <td><ul class="params"><li>CentOS 7.2 及以上</li><li>Ubuntu 14.04 及以上</li><li>Windows Server 2012 及以上</li></td>
                <td><ul class="params"><li>GN10X：广州、上海、南京、北京、成都、重庆、新加坡、硅谷、法兰克福、孟买</li><li>GN10Xp：广州、上海、南京、北京、成都、重庆、香港、法兰克福</li></ul></td>
            </tr>
         <tr>
					</tr>
					<tr>
						    <td><a href="#GN8">GN8</a></td> 
                <td>Tesla P40</td>
								 <td  rowspan=3><ul class="params"><li>CentOS 7.2 及以上</li><li>Ubuntu 14.04 及以上</li><li>Windows Server 2012 及以上</li></td>
							  <td>广州、上海、北京、成都、重庆、香港、硅谷</td>
					</tr>
				  <tr>
					   <td><a href="#GI3X">GI3X</a></td> 
             <td>Tesla T4</td>
             <td>广州、上海、北京、南京</td>
          </tr>
	        <tr>
					<td rowspan="2"><a href="#GN7">GN7</a></td> 
                <td>Tesla T4</td>
                <td>广州、上海、南京、北京、成都、重庆、香港、新加坡、硅谷、孟买、弗吉尼亚、法兰克福</td>
            </tr><tr>
				<td>vGPU - Tesla T4</td> 
                <td>CentOS 8.0 64位 GRID11.1</td>
                <td>广州、上海、南京、北京、成都、重庆、香港、硅谷</td>
			</tr><tr>
            </tr><tr>
						<td><a href="#GN6GN6S">GN6<br>GN6S</a></td> 
                <td>Tesla P4</td>
            	<td><ul class="params"><li>CentOS 7.2 及以上</li><li>Ubuntu 14.04 及以上</li><li>Windows Server 2012 及以上</li></td>
                <td><ul class="params"><li>GN6：成都</li><li>GN6S：广州、上海、北京</li></ul></td>
            </tr>
            <tr>
                <td>渲染型</td>
								<td><a href="#GN7vw">GN7vw</a></td> 
                <td>Tesla T4</td>
                <td><ul class="params"><li>CentOS 8.0 64位 GRID11.1</li><li>Windows Server 2019 数据中心版 64位 中文版 GRID11.1</li></td>
                <td>北京、上海、广州、南京、成都、重庆、香港、新加坡、孟买、硅谷、弗吉尼亚、法兰克福</td>
            </tr>
        </tbody>
</table>


>?**可用区域**：精确到城市级，细分区域详见下文中的实例配置信息。



## NVIDIA 系列选型推荐

腾讯云提供了类型丰富的 GPU 计算实例，可满足不同业务应用场景的需求。请参考下表，并结合实际需求选择合适的计算实例。

**GPU 云服务器 NVIDIA 系列选型推荐**如下表，其中 **✓** 为支持，**★** 为推荐。

<table>
        <thead>
        <tr>
            <th width="20%">功能\实例</th>
            <th width="11.5%">GN6<br>GN6S</th>
            <th width="11.5%">GN7</th>
						<th width="11.5%">GN8</th>
						<th width="11.5%">GI3X</th>
            <th width="11.5%">GN10X<br>GN10Xp</th>
            <th width="11.5%">GN7vw</th>
            <th width="11.5%">GT4</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <td>图形图像处理</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
								<td>✓</td>
                <td>✓</td>
                <td>★</td>
                 <td>-</td> 
            </tr>
            <tr>
                <td>视频编解码</td>
                <td>✓</td>
                <td>★</td>
                <td>✓</td>
								<td>★</td>
								<td>✓</td>
                <td>★</td>
                <td>-</td> 
            </tr>
            <tr>
                <td>深度学习训练</td>
                <td>✓</td>
                <td>✓</td>
								<td>★</td>
								<td>✓</td>
                <td>★</td>
                <td>-</td>
                <td>★</td>
            </tr>
            <tr>
                <td>深度学习推理</td>
                <td>★</td>
                <td>★</td>
                <td>★</td>
                <td>★</td>
								<td>✓</td>
                <td>-</td>
                <td>✓</td>
            </tr>
            <tr>
                <td>科学计算</td>
								<td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
								<td>★</td>
                <td>-</td>
                <td>★</td>
            </tr>
        </tbody>
</table>


### 图形图像处理
推荐使用 GN7vw，免除了 vDWS License 申请及搭建服务器步骤，是图形图像处理应用场景的首选。目前 GN7vw 处于限量购买阶段，如需使用，请前往 [申请](https://cloud.tencent.com/apply/p/l133eutcwd9) 页面。

NVIDIA GN* 系列其他实例可以通过安装 GRID Driver 的方式来支持图形图像处理，但是需要额外购买 License，详情请参见 [安装 NVIDIA GRID 驱动](https://cloud.tencent.com/document/product/560/30060)。

### 视频编解码

推荐使用 GN7 实例。GN7 采用 T4 GPU，性能好且单路视频转码成本最低，适用于视频编解码的产品。 

### 深度学习训练

推荐使用 GN8/GN10X/GN10Xp/GT4 实例。 GN8/GN10Xp/GT4 实例采用 P40、V100、A100 中高端 GPU，具有强大的单精度浮点运算能力，并具备较大的 GPU 板载内存，是深度学习训练的首选。

### 深度学习推理

推荐使用 GN6/GN6S/GN7/GI3X/GN8 实例。GN6/GN6S/GN7/GI3X/GN8 实例采用 P4、T4、P40 GPU，具备 INT8 计算能力，性价比高 ，适合大规模部署。

### 科学计算

推荐使用 GN10X/GN10Xp/GT4 实例。GN10X/GN10Xp/GT4 实例采用 V100、A100 GPU，具有强大的双精度浮点运算能力，可为科学与工程计算相关的应用软件提供最好的加速能力。

>!
>- 以上推荐用途仅供参考，请根据实际需要进行选择。
>- NVIDIA 系列 GPU 实例如用作通用计算，则需安装 Tesla Driver + CUDA，安装方法请参考 [安装 NVIDIA Tesla 驱动指引](https://cloud.tencent.com/document/product/560/8048) 和 [安装 CUDA 驱动指引](https://cloud.tencent.com/document/product/560/8064)。
>- NVIDIA 系列 GPU 实例如用作 3D 图形渲染任务（高性能图形处理，视频编解码等），则需安装 GRID Driver 和配置 License Server，安装方法请参考 [安装 NVIDIA GRID 驱动](https://cloud.tencent.com/document/product/560/30060)。
>

##  支持范围
- 支持 [包年包月](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) 和 [按量计费]( /doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9)。
- 支持在 [私有网络](/doc/product/213/5227) 中启动。
- 支持与 [负载均衡](/doc/product/214/524) 等产品的业务对接，不增加额外的管理和运维成本，内网流量免费。


## 计算型 GT4[](id:GT4) 

**NVIDIA 实例 GT4** 适用于深度学习、科学计算等 GPU 通用计算场景。

### 适用场景

GT4 具有强大的双精度浮点运算能力 ，适用于大规模深度学习训练，推理和科学计算场景。例如：
  - 深度学习
  - 高性能数据库
  - 计算流体动力学
  - 计算金融
  - 地震分析
  - 分子建模
  - 基因组学及其他



### 硬件规格

- **CPU：**GT4 配置 AMD EPYC™ ROME 处理器，主频2.6GHz。
- **GPU：**NVIDIA<sup>®</sup>  A100 NVLink 40GB（19.5TFLOPS单精度浮点计算，9.7TFLOPS双精度浮点计算，600GB/s NVLink）。
- **内存：**DDR4，内存计算性能稳定。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**最高可支持50Gbps内网带宽，超高网络收发包能力，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GT4 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla A100 NVLink 40G）</th>
            <th width=12%>GPU 显存<br>（HBM2）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
        <tr>
			<td>GT4.4XLARGE96</td>
			<td>1颗</td> 
            <td>1 * 40GB</td>
			<td>16核</td>
			<td>96GB</td>
            <td>5Gbps</td>
			<td>120万PPS</td>
            <td>4</td>
            <td rowspan="4">广州四区，上海四区，北京五区</td>
		</tr>
		<tr>
			<td>GT4.8XLARGE192</td>
			<td>2颗</td> 
            <td>2 * 40GB</td>
			<td>32核</td>
			<td>192GB</td>
            <td>10Gbps</td>
			<td>235万PPS</td>
            <td>8</td>
		</tr>
        <tr>
			<td>GT4.20XLARGE474</td>
			<td>4颗</td> 
            <td>4 * 40GB</td>
			<td>82核</td>
			<td>474GB</td>
            <td>25Gbps</td>
			<td>600万PPS</td>
            <td>16</td>
		</tr>
        <tr>
			<td>GT4.41XLARGE948</td>
			<td>8颗</td> 
            <td>8 * 40GB</td>
			<td>164核</td>
			<td>948GB</td>
            <td>50Gbps</td>
			<td>1200万PPS</td>
            <td>32</td>
		</tr>
		</tbody>
</table>

>?**GPU 驱动**：NVIDIA A100 系列需要安装 NVIDIA Tesla 450 版本以上驱动，推荐您安装 460.32.03(Linux)/461.33(Windows) 版本驱动，驱动版本信息请参见 [NVIDIA 官方文档](https://docs.nvidia.com/datacenter/tesla/index.html#nvidia-driver-documentation)。


## 计算型 GN10X/GN10Xp[](id:GN10XGN10Xp) 
**NVIDIA 实例 GN10X/GN10Xp** 不仅适用于深度学习、科学计算等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。

### 适用场景
GN10X/GN10Xp 具有强大的双精度浮点运算能力 ，适用于如下场景：
- 大规模深度学习训练，推理和科学计算场景。例如：
	- 深度学习
	- 高性能数据库
	- 计算流体动力学
	- 计算金融
	- 地震分析
	- 分子建模
	- 基因组学及其他
- 图形图像处理场景。例如：
	- 图形图像处理
	- 视频编解码
	- 图形数据库



### 硬件规格

- **CPU：**GN10X 配置 Intel<sup>®</sup> Xeon<sup>®</sup> Gold 6133 CPU，主频2.5GHz。GN10Xp 配置 Intel<sup>®</sup> Xeon<sup>®</sup> Platinum 8255C CPU，主频2.5GHz。
- **GPU：**NVIDIA<sup>®</sup> Tesla<sup>®</sup> V100 NVLink 32GB（15.7TFLOPS 单精度浮点计算，7.8TFLOPS 双精度浮点计算，125TFLOPS Tensor Core 深度学习加速，300GB/s NVLink）。
- **内存：**DDR4，内存带宽达2666MT/s。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GN10X/GN10Xp 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla V100 NVLink 32G）</th>
            <th width=12%>GPU 显存<br>（HBM2）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
            <tr>
				<td>GN10X.2XLARGE40</td>
				<td>1颗</td> 
                <td>1 * 32GB</td>
				<td>8核</td>
				<td>40GB</td>
                <td>4Gbps</td>
				<td>80万PPS</td>
                <td>2</td>
                <td rowspan="3">广州三、四区，上海二、三区，南京一区，北京四、五区，成都一区，重庆一区，新加坡一区，硅谷二区，法兰克福一区，孟买二区</td>
			</tr>
            <tr>
				<td>GN10X.9XLARGE160</td>
				<td>4颗</td> 
                <td>4 * 32GB</td>
				<td>36核</td>
				<td>160GB</td>
                <td>13Gbps</td>
				<td>250万PPS</td>
                <td>9</td>
			</tr>
            <tr>
				<td>GN10X.18XLARGE320</td>
				<td>8颗</td> 
                <td>8 * 32GB</td>
				<td>72核</td>
				<td>320GB</td>
                <td>25Gbps</td>
				<td>490万PPS</td>
                <td>16</td>
			</tr>
            <tr>
				<td>GN10X.4XLARGE80</td>
				<td>2颗</td> 
                <td>2 * 32GB</td>
				<td>18核</td>
				<td>80GB</td>
                <td>7Gbps</td>
				<td>150万PPS</td>
                <td>4</td>
                <td rowspan="1">广州三、四区，南京一区，成都一区，重庆一区</td>
			</tr>
      <tr>
			<td>GN10Xp.2XLARGE40</td>
			<td>1颗</td> 
            <td>1 * 32GB</td>
			<td>10核</td>
			<td>40GB</td>
            <td>4Gbps</td>
			<td>80万PPS</td>
            <td>10</td>
            <td rowspan="4">广州三、四区，上海二区，南京一区，北京五区，成都一区，重庆一区，香港二区，法兰克福一区</td>
		</tr>
		<tr>
			<td>GN10Xp.5XLARGE80</td>
			<td>2颗</td> 
            <td>2 * 32GB</td>
			<td>20核</td>
			<td>80GB</td>
            <td>7Gbps</td>
			<td>150万PPS</td>
            <td>16</td>
		</tr>
        <tr>
			<td>GN10Xp.10XLARGE160</td>
			<td>4颗</td> 
            <td>4 * 32GB</td>
			<td>40核</td>
			<td>160GB</td>
            <td>13Gbps</td>
			<td>250万PPS</td>
            <td>16</td>
		</tr>
        <tr>
			<td>GN10Xp.20XLARGE320</td>
			<td>8颗</td> 
            <td>8 * 32GB</td>
			<td>80核</td>
			<td>320GB</td>
            <td>25Gbps</td>
			<td>490万PPS</td>
            <td>16</td>
		</tr>
		</tbody>
</table>

## 计算型 GN8[](id:GN8) 

**NVIDIA 实例 GN8** 不仅适用于深度学习等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。

### 适用场景

适用于如下场景：
- 深度学习的推理和训练场景。例如：
	- 大吞吐量的 AI 推理
	- 深度学习
- 图形图像处理场景。例如：
	- 图形图像处理
	- 视频编解码
	- 图形数据库


### 硬件规格

- **CPU：**Intel<sup>®</sup> Xeon<sup>®</sup> E5-2680 v4 CPU，主频2.4GHz。
- **GPU：**NVIDIA<sup>®</sup> Tesla<sup>®</sup> P40（12TFLOPS 单精度浮点计算，47INT8 TOPS）。
- **内存：**DDR4，内存带宽达2666MT/s。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GN8 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla P40）</th>
            <th width=12%>GPU 显存<br>（GDDR5）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
            <tr>
				<td>GN8.LARGE56</td>
				<td>1颗</td> 
                <td>24GB</td>
				<td>6核</td>
				<td>56GB</td>
                <td>1.5Gbps</td>
				<td>45万PPS</td>
                <td>6</td>
                <td rowspan="4">香港二区，广州三区，上海三区，北京二、四区，成都一区，重庆一区，硅谷一区</td>
			</tr>
            <tr>
                <td>GN8.3XLARGE112</td>
				<td>2颗</td> 
                <td>48GB</td>
				<td>14核</td>
				<td>112GB</td>
                <td>2.5Gbps</td>
				<td>50万PPS</td>
                <td>8</td>
			</tr>
			<tr>
				<td>GN8.7XLARGE224</td>
				<td>4颗</td> 
        <td>96GB</td>
				<td>28核</td>
				<td>224GB</td>
         <td>5Gbps</td>
				<td>70万PPS</td>
        <td>8</td>
			</tr>
            <tr>
				<td>GN8.14XLARGE448</td>
				<td>8颗</td> 
        <td>192GB</td>
				<td>56核</td>
				<td>448GB</td>
        <td>10Gbps</td>
				<td>70万PPS</td>
        <td>8</td>
			</tr>
		</tbody>
</table>

## 推理型 GI3X[](id:GI3X) 

**NVIDIA 实例 GI3X** 适用于深度学习等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。

### 适用场景
GI3X 性价比高 ，适用于如下场景：
- 深度学习的推理场景和小规模训练场景。例如：
  - 大规模部署的 AI 推理
  - 深度学习小规模训练
- 图形图像处理场景。例如：
  - 图形图像处理
  - 视频编解码
  - 图形数据库

### 硬件规格
- **CPU：**2.6GHz AMD EPYC™ ROME 处理器，睿频3.3GHz。
- **GPU：**NVIDIA<sup>®</sup> Tesla<sup>®</sup> T4（8.1 TFLOPS 单精度浮点计算，130 INT8 TOPS，260 INT4 TOPS）。
- **内存：**搭配最新八通道 DDR4，内存计算性能稳定。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GI3X 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla T4）</th>
            <th width=12%>GPU 显存<br>（GDDR6）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
            <tr>
				<td>GI3X.8XLARGE64</td>
				<td>1颗</td> 
        <td>1 * 16GB</td>
				<td>32核</td>
				<td>64GB</td>
        <td>5Gbps</td>
				<td>140万PPS</td>
        <td>8</td>
                <td rowspan="3">广州三区，上海四区，南京一、二区，北京五区</td>
			</tr>
            <tr>
				<td>GI3X.22XLARGE226</td>
				<td>2颗</td> 
        <td>2 * 16GB</td>
				<td>90核</td>
				<td>226GB</td>
        <td>13Gbps</td>
				<td>375万PPS</td>
        <td>16</td>
			</tr>
            <tr>
				<td>GI3X.45XLARGE452</td>
				<td>4颗</td> 
        <td>4 * 16GB</td>
				<td>180核</td>
				<td>452GB</td>
        <td>25Gbps</td>
				<td>750万PPS</td>
         <td>32</td>
			</tr>
		</tbody>
</table>


## 计算型 GN7[](id:GN7) 
**NVIDIA 实例 GN7** 不仅适用于深度学习等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。

### 适用场景
性价比高 ，适用于如下场景：
- 深度学习的推理场景和小规模训练场景。例如：
	- 大规模部署的 AI 推理
	- 深度学习小规模训练
- 图形图像处理场景。例如：
	- 图形图像处理
	- 视频编解码
	- 图形数据库

### 硬件规格

- **CPU：**Intel<sup>®</sup> Xeon<sup>®</sup> Platinum 8255C CPU，主频 2.5 GHz。
- **GPU：**NVIDIA<sup>®</sup> Tesla<sup>®</sup> T4（8.1 TFLOPS 单精度浮点计算，130 INT8 TOPS，260 INT4 TOPS）。
- **内存：**DDR4，内存带宽达2666MT/s。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GN7 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla T4）</th>
            <th width=12%>GPU 显存<br>（GDDR6）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
            <tr>
				<td>GN7.LARGE20</td>
				<td>1/4颗</td> 
        <td>4GB vGPU</td>
				<td>4核</td>
				<td>20GB</td>
        <td>1.5Gbps</td>
				<td>50万PPS</td>
         <td>4</td>
         <td rowspan="2">广州三、四区，上海二、四区，南京一、二区，北京三，五区，成都一区，重庆一区，硅谷二区</td>
			</tr>
            <tr>
				<td>GN7.2XLARGE40</td>
				<td>1/2颗</td> 
        <td>8GB vGPU</td>
				<td>10核</td>
				<td>40GB</td>
        <td>3Gbps</td>
				<td>70万PPS</td>
        <td>10</td>
			</tr>
            <tr>
				<td>GN7.2XLARGE32</td>
				<td>1颗</td> 
                <td>1 * 16GB</td>
				<td>8核</td>
				<td>32GB</td>
                <td>3Gbps</td>
				<td>60万PPS</td>
                <td>8</td>
                <td rowspan="5">广州三、四区，上海二、四区，南京一、二区，北京三、五区，成都一区，重庆一区，新加坡一区，硅谷二区，香港二区，孟买二区，弗吉尼亚二区，法兰克福一区</td>
			</tr>
			<tr>
				<td>GN7.5XLARGE80</td>
				<td>1颗</td> 
                <td>1 * 16GB</td>
				<td>20核</td>
				<td>80GB</td>
                <td>7Gbps</td>
				<td>140万PPS</td>
                <td>16</td>
			</tr>
            <tr>
				<td>GN7.8XLARGE128</td>
				<td>1 颗</td> 
        <td>1 * 16GB</td>
				<td>32核</td>
				<td>128GB</td>
        <td>10Gbps</td>
				<td>240万PPS</td>
        <td>16</td>
			</tr>
            <tr>
				<td>GN7.10XLARGE160</td>
				<td>2颗</td> 
        <td>2 * 16GB</td>
				<td>40核</td>
				<td>160GB</td>
        <td>13Gbps</td>
				<td>280万PPS</td>
        <td>16</td>
			</tr>
            <tr>
				<td>GN7.20XLARGE320</td>
				<td>4颗</td> 
        <td>4 * 16GB</td>
				<td>80核</td>
				<td>320GB</td>
        <td>25Gbps</td>
				<td>560万PPS</td>
         <td>16</td>
			</tr>
		</tbody>
</table>


>?**vGPU**：
>- GN7 实例簇支持 vGPU 的实例类型。vGPU 的类型为 vComputeServer，只支持 CUDA 计算 API。
>- vCS 实例需安装 GRID 驱动，且 vCS 的实例不支持 Windows 操作系统。


## 计算型 GN6/GN6S[](id:GN6GN6S) 

**NVIDIA 实例 GN6/GN6S** 不仅适用于深度学习等 GPU 通用计算场景，也适用于图形图像处理（3D 渲染，视频编解码）场景。

### 适用场景

性价比高 ，适用于如下场景：
- 深度学习的推理场景和小规模训练场景。例如：
	- 大规模部署的 AI 推理
	- 深度学习小规模训练
- 图形图像处理场景。例如：
	- 图形图像处理
	- 视频编解码
	- 图形数据库


### 硬件规格

- **CPU：**GN6 配置 Intel<sup>®</sup> Xeon<sup>®</sup> E5-2680 v4 CPU，主频2.4GHz。GN6S 配置 Intel<sup>®</sup> Xeon<sup>®</sup> Silver 4110 CPU，主频2.1GHz。
- **GPU：**NVIDIA<sup>®</sup> Tesla<sup>®</sup> P4（5.5TFLOPS 单精度浮点计算，22INT8 TOPS）。
- **内存：**DDR4，内存带宽达2666MT/s。
- **存储：**可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：**默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GN6/GN6S 实例提供以下配置：**

<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=14%>GPU<br>（NVIDIA<br>Tesla P4）</th>
            <th width=10%>GPU 显存<br>（GDDR5）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
            <tr>
				<td>GN6.7XLARGE48</td>
				<td>1颗</td> 
         <td>8GB</td>
				<td>28核</td>
				<td>48GB</td>
        <td>5Gbps</td>
				<td>120万PPS</td>
        <td>16</td>
        <td rowspan="2">成都一区</td>
			</tr>
            <tr>
         <td>GN6.14XLARGE96</td>
				<td>2颗</td> 
        <td>16GB</td>
				<td>56核</td>
				<td>96GB</td>
        <td>10Gbps</td>
				<td>120万PPS</td>
        <td>16</td>
			</tr>
			<tr>
				<td>GN6S.LARGE20</td>
				<td>1颗</td> 
        <td>8GB</td>
				<td>4核</td>
				<td>20GB</td>
         <td>7Gbps</td>
				<td>50万PPS</td>
        <td>2</td>
        <td rowspan="2">广州三区，上海二、三、四区，北京四、五区</td>
			</tr>
            <tr>
				<td>GN6S.2XLARGE40</td>
				<td>2颗</td> 
        <td>16GB</td>
				<td>8核</td>
				<td>40GB</td>
        <td>13Gbps</td>
				<td>80万PPS</td>
        <td>2</td>
			</tr>
		</tbody>
</table>



## 渲染型 GN7vw[](id:GN7vw)

**NVIDIA 实例 GN7vw** 是在 GN7 基础上配置 vDWS License 服务器并安装 GRID driver 的渲染型实例，适用于图形图像处理（3D 渲染，视频编解码）场景。使用该实例，您可免除手动配置 GPU 图形图像处理基础环境。
>!GPU 渲染型 GN7vw 现处于限量购买阶段，如需使用，请前往 [申请](https://cloud.tencent.com/apply/p/l133eutcwd9) 页面。
>





### 适用场景
适用于图形图像处理。例如：
- 图形图像处理
- 视频编解码
- 图形数据库

### 硬件规格

- **CPU：**Intel<sup>®</sup> Xeon<sup>®</sup> Platinum 8255C CPU，主频 2.5 GHz。
- **GPU：** NVIDIA<sup>®</sup> Tesla<sup>®</sup> T4（8.1 TFLOPS 单精度浮点计算，130 INT8 TOPS，260 INT4 TOPS）。
- **内存：** DDR4 ，内存带宽达2666MT/s。
- **存储：** 可选择 [云硬盘类型](https://cloud.tencent.com/document/product/362/2353)，如需 [扩容](https://cloud.tencent.com/document/product/362/32539) 可新建弹性云盘进行挂载。	 
- **网络：** 默认网络优化，实例网络性能与规格对应。[公网网络](https://cloud.tencent.com/document/product/213/10578) 可按需配置。

**GN7vw实例提供以下配置：**
<table>
		<thead>
		<tr>
			<th width=10%>型号</th>
			<th width=10%>GPU<br>（NVIDIA<br>Tesla T4）</th>
            <th width=12%>GPU 显存<br>（GDDR6）</th>
			<th width=8%>vCPU</th>
			<th>内存<br>（DDR4）</th>
            <th width=10%>内网带宽</th>
            <th>网络收发包</th>
            <th>队列数</th>
			<th>可用区</th>
		</tr>
		</thead>
		<tbody>
			<tr>
				<td>GN7vw.LARGE16</td>
				<td>1/4颗</td> 
        <td>4GB vGPU</td>
				<td>4核</td>
				<td>16GB</td>
        <td>2Gbps</td>
				<td>50万PPS</td>
        <td>4</td>
        <td rowspan="4">广州三、四区，上海二、四、五区，南京一、二区，北京五区，成都一区，重庆一区，香港二区，新加坡一区，孟买二区，硅谷二区，弗吉尼亚二区，法兰克福一区</td>
			</tr>
            <tr>
				<td>GN7vw.2XLARGE32</td>
				<td>1/2颗</td> 
        <td>8GB vGPU</td>
				<td>8核</td>
				<td>32GB</td>
        <td>4Gbps</td>
				<td>80万PPS</td>
        <td>8</td>
			</tr>
            <tr>
				<td>GN7vw.4XLARGE64</td>
				<td>1颗</td> 
        <td>1 * 16GB</td>
				<td>16核</td>
				<td>64GB</td>
        <td>7Gbps</td>
				<td>150万PPS</td>
        <td>16</td>
			</tr>
		</tbody>
</table>


>?**vGPU**：GN7、GN7vw 实例簇提供支持 vGPU 的实例类型。其中 GN7vw vGPU 的类型为 vDWS，仅支持 DirectX 和 OpenGL 等图形 API。


<style>
	.params{margin:0px !important}
</style>
