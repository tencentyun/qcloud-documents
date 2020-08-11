为满足您的业务需求，腾讯云提供 Edge-100 和 Edge-1000 两种 Edge 设备。本文将介绍如何在 SD-WAN 接入服务控制台申请 Edge 设备。
>?SD-WAN 接入服务目前处于内测阶段，不收取任何费用，且内测阶段仅支持创建硬件规格为 Edge-100 的设备。
>
## 背景信息
 Edge-100 和 Edge-1000 的使用场景及支持混合接入的设备如下：
- Edge-100：适用于智慧零售、连锁酒店、办公职场、多节点小带宽内网互通场景，支持接入 SPF/RJ45、DSL、4G、WIFI 5 等设备，详情请参见 [Edge-100 硬件特性说明](https://cloud.tencent.com/document/product/1277/47251)。
- Edge-1000：适用于 IDC 数据中心、企业总部及区域中心机构等核心节点大带宽内网互通场景，支持接入 SPF/RJ45、DSL、4G/5G、WIFI 6 等设备，详情请参见 [Edge-1000 硬件特性说明](https://cloud.tencent.com/document/product/1277/47321)。


## 申请 Edge 设备
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)，并在 “Edge 设备”页面上方，单击【新建】。
2. 在“新建 EDGE” 对话框中，编辑 Edge 名称、并选择带宽峰值、带宽时长、申请数量等申请信息，并填写收货信息，填写完后，单击【确定】。
![](https://main.qcloudimg.com/raw/1813ea942315e8134c84e07e97e7765e.png)

## 安装 Edge 设备
收到 Edge 设备后，您需要安装 Edge 设备以将本地分支接入腾讯云网络。
1. 检查配件是否完整。配件详情请参见 [硬件特性说明](https://cloud.tencent.com/document/product/1277/47251)。
2. 选择您适用的场景，启动 Edge 设备。
	- 使用 4G 网络通信。
		1. 将 Edge 设备通电。
		2. 在控制台配置 Edge 设备 WLAN 配置，具体操作请参见 [配置 WLAN](https://cloud.tencent.com/document/product/1277/47272)。
		3. 将本地分支接入 Edge 设备的 WLAN。
		>? 4G开局无需配置网络接口，插电即用。
	- 使用 Internet 或者专线通信。
		1. 将 WAN 口 和 Modem 相连，LAN 口和本地客户端相连。
		2. 使用以下任意一种方式配置 WAN 口。
			- 方式一：通过本地 Web 控制台配置。具体操作请参见 [在本地 Web 控制台配置 WAN 和 WLAN](https://cloud.tencent.com/document/product/1277/47252)。
			- 方式二：（推荐）在 SD-WAN 接入服务控制台配置。具体操作请参见 [在控制台配置 WAN 口](https://cloud.tencent.com/document/product/1277/47271)。
>? 当 Edge 设备的 4G 网络正常（即插电后，LTE 灯长亮），或 Modem 可正常拨号上网时，才可以使用此方式。
		3. 配置 LAN 口，具体操作请参见  [配置 LAN 接口](https://cloud.tencent.com/document/product/1277/47270)。
