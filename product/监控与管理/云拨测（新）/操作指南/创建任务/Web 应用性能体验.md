本文将为您介绍如何新建 Web 应用性能体验场景的拨测任务。

## 操作场景

“Web 应用性能体验任务”专注于网页的性能和可用性，您只需要输入您的网页地址，分布全国的拨测点将自动对您的网站发起探测，并记录拨测情况。根据高频的探测，获取用户在不同的运营商、城市地域、浏览器版本、操作系统、设备等环境下，访问 Web 页面的体验数据，支持实时告警，并提供详细数据指标供您了解网页的体验情况。
Web 应用性能体验监控帮助您快速了解网页运行情况，快速发现并定位问题。


>?Web 应用性能体验提供免费体验版，仅限体验一次，如需购买请参见 [计费概述](https://cloud.tencent.com/document/product/280/52110)。

## 操作步骤

1. 登录 [云拨测控制台](https://console.cloud.tencent.com/catpro)。
2. 单击左侧菜单栏中的【场景化监控】，进入场景化监控页面。
3. 单击【新建任务】，进入新建任务页，选择“Web应用性能体验”任务场景。其它配置请参见下表。
	- **基本信息**
	<table>
	<thead>
	<tr>
	<th>配置项</th>
	<th>说明</th>
	</tr>
	</thead>
	<tbody><tr>
	<td>功能</td>
	<td><ul><li>免费体验：拨测点不支持选择，仅限体验一次</li><li>高级定制：高级定制版需要收费。详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a></li></ul></td>
	</tr>
	<tr>
	<td>地域</td>
	<td>根据网站所在区域选择，不同的地域收费不同，详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a></td>
	</tr>
	<tr>
	<td>任务名称</td>
	<td>填写拨测任务名称，建议以监测对象来命名</td>
	</tr>
	<tr>
	<td>拨测类型</td>
	<td><ul><li>浏览：适用于监控网页的性能质量。</li><li>上传：适用于监控网页的资源上传速度。</li><li>下载：适用于监控网页的资源下载速度。</li><li>协议：适用于监控网页后端协同的性能速度。</li></ul></td>
	</tr>
	<tr>
	<td>拨测地址</td>
	<td>请填写以 http:// 或 https:// 开头的拨测地址</td>
	</tr>
	</tbody></table>
	- **拨测点选择**：
	<table>
	<thead>
	<tr>
	<th>配置项</th>
	<th>说明</th>
	</tr>
	</thead>
	<tbody><tr>
	<td>拨测点类型</td>
	<td>不同的拨测点类型收费规则不同，详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a><br><ul> <li>骨干IDC：部署在骨干线路中IDC机房的拨测点，代表骨干线路</li> <li>终端网民 LastMile：部署在终端用户PC电脑上的拨测点，代表终端PC用户体验</li><li>手机端：部署在终端移动手机上的拨测点，代表终端移动用户体验</li></ul></td>
	</tr>
	<tr>
	<td>拨测点选择</td>
	<td>您可以选择系统推荐的节点组，也可以自定义节点组。Web 应用性能体验按拨测点收费，拨测点越多收费越高，详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a>。您可以根据需求勾选拨测点组，勾选后单击【<img src="https://main.qcloudimg.com/raw/b0ef53201062fcb9d4e22b727b8a334b.jpg" width="3.5%">】即可。如需取消拨测点选择单击【<img src="https://main.qcloudimg.com/raw/c11fd0c6306294fd07a7208dd6cffdf7.jpg" width="3.5%">】即可。</td>
	</tr>
	</tbody></table>
	- **拨测参数**
	<table>
	<thead>
	<tr>
	<th>配置项</th>
	<th>说明</th>
	</tr>
	</thead>
	<tbody><tr>
	<td>IP类型</td>
	<td>支持自动、IPV4、IPV6三种类型</td>
	</tr>
	<tr>
	<td>自定义 Host</td>
	<td>填写您需要检测的主机信息。支持按 IP 地址轮询或随机监测，多个IP请用半角逗号分隔符，例如<code> IPv4：192.168.2.1,192.168.2.5:img.a.com|192.168.2.1󠉀]:img.a.com|ipv6:[0:0:0:0:0:0:0:1][8080],[0:0:0:0:0:0:0:2][8081]:www.a.com|]</code></td>
	</tr>
	</tbody></table>
	- **拨测周期配置**
	<table>
	<thead>
	<tr>
	<th>配置项</th>
	<th>说明</th>
	</tr>
	</thead>
	<tbody><tr>
	<td>拨测时长</td>
	<td>支持7天和30天拨测时长，拨测时长不同收费规则不同，详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a></td>
	</tr>
	<tr>
	<td>拨测频率</td>
	<td>默认只支持30分钟的拨测频率</td>
	</tr>
	<tr>
	<td>分析报告</td>
	<td>支持三种人工分析报告，不同报告适用场景不同。
<ul><li> 性能分析报告：常规人工分析报告，分析影响用户体验性能的问题定位和优化建议
<li> 竞品对比分析报告：图文结合的对比，分析与竞品的性能差异，提供优化建议
<li>专项性能优化报告：针对版本迭代的场景，分析性能差异以及优化的程度
<br>购买后需填写邮箱信息。云拨测将会把拨测报告发送到用户指定的邮箱。不同报告类型收费不一致，详情请参见 <a href="https://cloud.tencent.com/document/product/280/52111">产品定价</a></ul></td>
	</tr>
	</tbody></table>
4. 若选择【免费体验版】请单击【确定】，即可新建 Web 应用性能拨测任务；若选择【高级定制版】请单击【立即购买】进行购买，即可新建 Web 应用性能的拨测任务。
