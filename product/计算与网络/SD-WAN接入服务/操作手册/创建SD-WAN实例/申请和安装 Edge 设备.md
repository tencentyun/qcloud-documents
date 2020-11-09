为满足您的业务需求，腾讯云提供 Edge-100 和 Edge-1000 两种 Edge 设备。本文将介绍如何在 SD-WAN 接入服务控制台申请 Edge 设备。
>?SD-WAN 接入服务目前处于内测阶段，如需使用请提交 [内测申请](https://cloud.tencent.com/apply/p/v70vi3xrgr)，内测阶段暂不支持 Edge-1000 设备。
>
## 背景信息
**Edge 设备**：硬件设备形态，在用户 IDC、分支和门店安装 Edge 设备后，可自动与腾讯云网络连接。Edge 设备详情如下：
<table>
<thead>
<tr>
<th>设备型号</th>
<th>内网带宽</th>
<th>接入方式</th>
<th>使用场景</th>
</tr>
</thead>
<tbody><tr>
<td>Edge-100</td>
<td>100Mbps</td>
<td><ul><li>WAN 侧支持宽带与 4G 接入</li><li>LAN 侧支持有线与 Wi-Fi 接入</li><ul></ul></ul></td>
<td>智慧零售、连锁酒店、办公职场、多节点小带宽内网互通场景</td>
</tr>
<tr>
<td>Edge-1000</td>
<td>500Mbps</td>
<td><ul><li>WAN 侧支持宽带与 4G 接入</li><li>LAN 侧支持有线与 Wi-Fi 接入</li><ul></ul></ul></td>
<td>IDC 数据中心、企业总部、区域中心机构等核心节点大带宽内网互通场景</td>
</tr>
</tbody></table>



## 申请 Edge 设备
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)，并在 “Edge 设备”页面上方，单击【新建】。
2. 在“新建 EDGE” 对话框中，编辑 Edge 名称、并选择带宽峰值、带宽时长、申请数量等申请信息，并填写收货信息，填写完后，单击【确定】。
![](https://main.qcloudimg.com/raw/1813ea942315e8134c84e07e97e7765e.png)

## 安装 Edge 设备
收到 Edge 设备后，您需要安装 Edge 设备以将本地分支接入腾讯云网络。
1. 检查配件是否完整。配件详情请参见 [硬件特性说明](https://cloud.tencent.com/document/product/1277/47251)。
2. 使用 Internet 或者专线通信，启动 Edge 设备。
	1. 将 WAN 口 和 Modem 相连，LAN 口和本地客户端相连，然后接通电源。
	2. 使用以下任意一种方式配置 WAN 口。
		- 方式一：通过本地 Web 控制台配置。具体操作请参见 [在本地 Web 控制台配置 WAN 和 WLAN](https://cloud.tencent.com/document/product/1277/47252)。
		- 方式二：（推荐）在 SD-WAN 接入服务控制台配置。具体操作请参见 [在控制台配置 WAN 口](https://cloud.tencent.com/document/product/1277/47271)。
>? 当 Edge 设备的 4G 网络正常（即插电后，LTE 灯长亮），或 Modem 可正常拨号上网时，才可以使用此方式。
	3. 配置 LAN 口，具体操作请参见  [配置 LAN 接口](https://cloud.tencent.com/document/product/1277/47270)。

## 后续操作
- [新建静态路由](https://cloud.tencent.com/document/product/1277/47273)
- [配置防火墙](https://cloud.tencent.com/document/product/1277/47266)
- [关联云联网](https://cloud.tencent.com/document/product/1277/47262)
