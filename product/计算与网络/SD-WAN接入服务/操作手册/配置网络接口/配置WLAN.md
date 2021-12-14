WLAN 配置用于管理 Edge 设备自带的 Wi-Fi 功能，本文将介绍如何在 SD-WAN 接入服务控制台配置 WLAN。

## 操作步骤
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)，并在实例列表中，单击目标实例 ID。
2. 在实例详情页的左侧导航栏，选择**设备配置** > **WLAN** 配置。
3. 在“WLAN 设置”页面进行以下配置，完成后单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/a1d0deecc8f09cd96cfa2e021aff80ec.png)
**字段说明**：
	- **WIFI 能力**：开启后才能使用 Edge 设备自带的 Wi-Fi 功能。
	- **国家码**：默认为中国。
	- **SSID**：服务集标识（Service Set Identifier），用于身份验证。
	- **SSID 广播**：选择展示或隐藏 Edge 设备名称。
	- **安全认证**：选择是否加密访问，若选择 “WAP-PSK” 或 “WAP-PSK2” 加密方式，还需配置安全密钥。
	- **关联 vPort**：关联的逻辑接口，您可以按需更换为已开启 DHCP 模式的逻辑接口。
>? WLAN 的 DHCP 系统默认为第一个 VPORT 的 DHCP 池。
>
	- **频段**： Edge-100 仅支持2.4G，Edge-1000 支持2.4G和5G。
>?SD-WAN 接入服务目前处于内测阶段，仅支持硬件规格为 Edge-100 的设备。
>


