NVIDIA GPU 系列实例提供了监控 GPU 使用率，显存使用量，功耗以及温度等参数的能力。
## GPU 监控工作条件

GPU 监控是通过在 GPU 云服务上部署安装相关 [GPU 驱动](https://cloud.tencent.com/document/product/560/8048) 和 [云服务器监控组件](https://cloud.tencent.com/document/product/248/6211) 来实现的，使用不同的镜像需要不同的处理方式：
- 使用公共镜像：公共镜像默认包含云服务器监控组件，只需安装 GPU 驱动。
- [使用镜像市场GPU驱动预装镜像](https://cloud.tencent.com/document/product/560/30129)：无需任何安装。
- 使用导入镜像：需手动安装云服务器监控组件和 GPU 驱动。

## 查看 GPU 工作参数
单击 GPU 列表中的 “<img style="margin:0;" src="https://main.qcloudimg.com/raw/99d10268805b09f693477afd664e05fb.png"/>” 监控图标， 访问 [控制台](https://cloud.tencent.com/login) GPU 实例的监控页面，查看 GPU 监控，移动鼠标到指标曲线上将显示对应 GPU 设备的 BDF 和监控数据。如下图所示：
![](https://main.qcloudimg.com/raw/13ae6f53519093601fbeba86971ec7a0.jpg)
参数说明：
<table>
			<tr>
				<th>指标名称</th>
				<th>含义</th>
				<th>单位</th>
				<th>维度</th>
			</tr>
			<tr>
				<td>GPU 使用率</td>
				<td>评估负载所消耗的计算能力，非空闲状态百分比</td>
				<td>%</td>
				<td>per-GPU</td>
			</tr>
			<tr>
				<td>GPU 显存使用量</td>
				<td>评估负载对显存占用</td>
				<td>MBytes</td>
				<td>per-GPU</td>
			</tr>
			<tr>
				<td>GPU 功耗</td>
				<td>评估 GPU 耗电情况</td>
				<td>W</td>
				<td>per-GPU</td>
			</tr>
			<tr>
				<td>GPU 温度</td>
				<td>评估 GPU 散热状态</td>
				<td>摄氏度</td>
				<td>per-GPU</td>
			</tr>
		</table>


## 无监控数据原因
- 只支持 NVIDIA GPU 实例。
- 只支持 Linux 操作系统。
- 没有安装 GPU 驱动或监控组件。
- 其他原因分析可参考 [云服务器无监控数据](https://cloud.tencent.com/document/product/248/17468)。



