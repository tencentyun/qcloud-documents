

[NVIDIA GPU 实例](https://cloud.tencent.com/document/product/560/19700) 需要安装驱动后才可以正常使用，您可通过腾讯云提供购买页自动安装驱动功能，或已预装驱动的镜像创建实例。创建实例后十分钟内初始化完毕即可开展您的业务，免除了手动下载部署 GPU 驱动所需要的数小时繁琐流程。您可参考本文，为您的实例选择适合的驱动类型及安装方式。



## 安装方式


### 自动安装 GPU 驱动[](id:autoInstall)
1. 在云服务器 [购买页](https://buy.cloud.tencent.com/?tab=custom&regionId=8&zoneId=800005&instanceType=GN7.5XLARGE80) 创建实例的过程中，[选择镜像](https://cloud.tencent.com/document/product/560/30211#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E9.80.89.E6.8B.A9.E9.95.9C.E5.83.8F) 步骤请选择 CentOS 或 Ubuntu 镜像。
选择后即出现“后台自动安装GPU驱动”选项，勾选后即可按需选择 CUDA 和 cuDNN 版本。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/352d7b636f81cb97362fdb0ee0333ae9.gif)
各实例支持自动安装的镜像版本请参考 [各实例支持的 GPU 驱动版本及安装方式](#supportList)。
3. 购买页其他配置选择请参考 [购买 GPU 实例](https://cloud.tencent.com/document/product/560/30211)，创建完成后请前往控制台，找到实例并等待10分钟左右驱动安装完成。
4. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录实例。
5. 执行以下命令，验证驱动是否安装成功。
```shell
nvidia-smi
```
如返回类似下图中的 GPU 信息，则说明驱动安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/1b5e3bcd39038e82e9a3faf9655ea59d.png)




### 使用预装 GPU 驱动的镜像

<dx-tabs>
::: 渲染型实例

如果您的业务类型属于图形图像处理（3D 渲染，视频编解码），需要使用 DirectX 和 OpenGL 等图形 API，推荐您选择 [渲染型实例](https://cloud.tencent.com/document/product/560/63854)。
腾讯云提供预装 GRID 驱动的镜像，您在 [购买页](https://buy.cloud.tencent.com/?tab=custom&regionId=8&zoneId=800005&instanceType=GN7.5XLARGE80) 中选择对应镜像版本后，在 [控制台](https://console.cloud.tencent.com/cvm/instance) 等待创建完成即可使用渲染型实例。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5e492284a4d1252acef79fb5fda94ff1.gif)
各个实例支持 GRID 版本请参考 [各实例支持的 GPU 驱动版本及安装方式](#supportList)。


:::
::: 计算型实例

- 若您使用直通卡 [计算型实例](https://cloud.tencent.com/document/product/560/19700)，推荐使用 [自动安装 GPU 驱动](#autoInstall) 方式。您也可在 [购买页](https://buy.cloud.tencent.com/?tab=custom&regionId=8&zoneId=800005&instanceType=GN7.5XLARGE80) 的“镜像”中选择**镜像市场**，以使用预装 GPU 驱动的镜像，详情请参见 [使用预装 GPU 驱动的镜像](https://cloud.tencent.com/document/product/560/30129)。
- [vGPU 计算型实例](https://cloud.tencent.com/document/product/560/19700#.E8.AE.A1.E7.AE.97.E5.9E.8B-gn7.3Ca-id.3D.22gn7.22.3E.3C.2Fa.3E) 在公共镜像中已提供驱动，您无需单独安装。vGPU 实例的驱动版本可参考 [各实例支持的 GPU 驱动版本及安装方式](#supportList)。


#### 相关概念
- **直通卡实例类型**：GPU 卡数大于或等于 1 的实例规格为 GPU 直通卡实例类型，使用直通模式的虚拟化技术。
- **vGPU 计算型实例**：实现1/2卡，1/4卡的 GPU 算力切分，vGPU 的类型为 vCS（vComputeServer），只支持 CUDA 计算 API，不支持 DirectX 和 OpenGL 等图形 API。vCS 实例需 GRID 驱动，在公共镜像中可选，且 vCS 的实例不支持 Windows 操作系统。
- **vGPU 渲染型实例**：配置 vDWS/vWS License 服务器并安装 GRID 驱动，支持图形图像处理（3D 渲染，视频编解码）场景，各实例驱动支持版本可参考 [各实例支持的 GPU 驱动版本及安装方式](#supportList)。



:::
</dx-tabs>









## 如何进行 GPU 驱动类型选型

<table>
<tr>
<th width="25%">实例类型</th>
<th width="13%">场景</th>
<th width="13%">驱动类型</th>
<th>推荐安装方式</th>
</tr>
<tr>
<td rowspan=2>计算型实例 - 直通卡型</td>
<td>通用计算</td>
<td>Tesla 驱动</td>
<td><a href="#autoInstall">自动安装 GPU 驱动</a>
</td>
</tr>
<tr>
<td>图形渲染</td>
<td>GRID 驱动</td>
<td>在购买页<b>镜像市场</b>中选择已预装 GRID 驱动的付费镜像，详情请参见 <a href="https://cloud.tencent.com/document/product/560/30129">使用预装 GPU 驱动的镜像</a>
</td>
</tr>
<tr>
<td>计算型实例 - vGPU - vCS</td>
<td>通用计算</td>
<td>GRID 驱动</td>
<td>选择已预装 GRID 驱动的公共镜像</td>
</tr>
<tr>
<td>渲染型实例 - vGPU - vDWS/vWS</td>
<td>图形渲染</td>
<td>GRID 驱动</td>
<td>选择已预装 GRID 驱动的公共镜像</td>
</tr>
</table>


<dx-alert infotype="explain" title="">
如您需手动安装 GPU 驱动，请参考 [安装 NVIDIA Tesla 驱动](https://cloud.tencent.com/document/product/560/8048) 和 [安装 NVIDIA GRID 驱动](https://cloud.tencent.com/document/product/560/30060) ，各实例驱动支持版本可参考  [各实例支持的 GPU 驱动版本及安装方式](#supportList)。

</dx-alert>





## 各实例支持的 GPU 驱动版本及安装方式[](id:supportList)

<table>
<thead>
    <tr>
      <th style="
    width: 11%;
">实例</th>
      <th style="
    width: 11%;
">支持驱动类型</th>
      <th style="
    width: 20%;
">自动安装支持驱动版本</th>
      <th style="
    width: 33%;
">可用带驱动镜像</th>
      <th style="
    width: 25%;
">手动安装驱动版本限制</th>
    </tr>
  </thead>
  <tbody>
	<tr>
	  <td>计算型<br>PNV4</td>
	  <td rowspan="8">Tesla 驱动
	  <br />GRID 驱动</td>
	  <td>
		<b>CentOS 7.2 - 8.2 64位、Ubuntu 18.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 470.82.01</li>
		  <li>Tesla 驱动 460.106.00</li>
		</ul>
	  </td>
	  <td rowspan="8">
		<b>镜像市场付费镜像</b>
		<ul class="params">
		  <li>Windows Server 2019中文版GPU基础镜像（预装 GRID13 驱动，vDWs/vWs License）64位</li>
		  <li>Windows Server 2019中文版GPU基础镜像（预装GRID 11驱动，vDWs/vWs License）64位</li>
		</ul>
		<br />
		<b>镜像市场免费镜像</b>
		<ul class="params">
		  <li>CentOS 7.6 NVIDIA GPU基础镜像（预装驱动和CUDA 10.2）64位</li>
		  <li>CentOS 7.5 NVIDIA GPU基础镜像（预装驱动和CUDA 9.2）64位</li>
		  <li>CentOS 7.2 NVIDIA GPU基础镜像（预装驱动和CUDA 9.2）64位</li>
		  <li>GPU服务器CentOS 7.6带CUDA 10.0 32位</li>
		  <li>GPU服务器CentOS 7.6带Tensorflow 32位</li>
		  <li>GPU服务器CentOS 7.6带Pytorch 32位</li>
		  <li>GPU服务器Ubuntu 18.04带Pytorch 64位</li>
		</ul>
	  </td>
	  <td rowspan="8">
	  <b>Tesla 驱动</b>
	  <br />无特殊要求，官方支持版本即可。
	  <br />  <br />
	  <b>GRID 驱动</b>
	  <ul class="params">
		<li>GRID14 驱动</li>
		<li>GRID13 驱动</li>
		<li>GRID11 驱动</li>
	  </ul>
	  <br />
	  <b>说明：</b>手动安装 GRID 驱动需要您前往 NVIDIA 官网下载并购买 license。版本选择可参考 
	  <a href="https://docs.nvidia.com/grid/index.html">GRID 驱动版本说明</a>。</td>
	</tr>
	<tr>
	  <td>计算型<br>GT4</td>
	  <td>
		<b>CentOS 8.0 - 8.2 64位</b>
		<ul class="params">
		  <li>GPU Tesla 驱动 470.82.01</li>
		  <li>GPU Tesla 驱动 460.106.00</li>
		</ul>
		<br />
		<b>Ubuntu 20.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		</ul>
		<br />
		<b>CentOS 7.2 - 7.9 64位、Ubuntu 18.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		  <li>Tesla 驱动 470.82.01</li>
		  <li>Tesla 驱动 460.106.00</li>
		</ul>
	  </td>
	</tr>
	<tr>
	  <td>计算型<br>GN10Xp</td>
	  <td rowspan="2">
		<b>CentOS 7.2 - 8.2 64位、Ubuntu 18.04/20.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		  <li>Tesla 驱动 470.82.01</li>
		  <li>Tesla 驱动 460.106.00</li>
		</ul>
	  </td>
	</tr>
	<tr>
	  <td>计算型<br>GN7-直通卡</td>
	</tr>
	<tr>
	  <td>推理型<br>GI3X</td>
	  <td>
		<b>CentOS 7.2 - 8.2 64位、Ubuntu 18.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		  <li>Tesla 驱动 470.82.01</li>
		  <li>Tesla 驱动 460.106.00</li>
		</ul>
	  </td>
	</tr>
	<tr>
	  <td>计算型<br>GN10X</td>
	  <td rowspan="3">
		<b>CentOS 7.2 - 8.2 64位、Ubuntu 18.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		  <li>Tesla 驱动 470.82.01</li>
		  <li>Tesla 驱动 460.106.00</li>
		</ul>
		<br />
		<b>Ubuntu 20.04 LTS 64位</b>
		<ul class="params">
		  <li>Tesla 驱动 450.102.04</li>
		</ul>
	  </td>
	</tr>
	<tr>
	  <td>计算型<br>GN8</td>
	</tr>
	<tr>
	  <td>计算型<br>GN6/GN6S</td>
	</tr>
	<tr>
	  <td>计算型<br>GN7-vGPU</td>
	  <td rowspan="4">GRID 驱动</td>
	  <td rowspan="4">-</td>
	  <td>
		<ul class="params">
		  <li>CentOS 8.0 64位 GRID11.1</li>
		  <li>Ubuntu Server 20.04 LTS 64位 GRID11.1</li>
		</ul>
	  </td>
	  <td>Linux- GRID11.1 450.80.02</td>
	</tr>
	<tr>
	  <td>渲染型<br>GNV4v</td>
	  <td rowspan="2">Windows Server 2019 数据中心版 64位 中文版 GRID13</td>
	  <td rowspan="2">Windows-GRID13 驱动 471.68</td>
	</tr>
	<tr>
	  <td>渲染型<br>GNV4</td>
	</tr>
	<tr>
	  <td>渲染型<br>GN7vw</td>
	  <td>
		<ul class="params">
		  <li>CentOS 8.0 64位 GRID11.1</li>
		  <li>Ubuntu 20.04 LTS 64位 GRID 11.1</li>
		  <li>Windows Server 2019 数据中心版 64位 中文版 GRID11.1</li>
		</ul>
	  </td>
	  <td>
		<ul class="params">
		  <li>Linux-GRID11.1 驱动 450.80.02</li>
		  <li>Windows-GRID11.1 驱动 452.39</li>
		</ul>
	  </td>
	</tr>
  </tbody>
</table>

<style>
 .params{ margin-bottom:0px !important}
</style>
