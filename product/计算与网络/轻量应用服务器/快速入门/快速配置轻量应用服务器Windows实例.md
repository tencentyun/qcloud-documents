本入门教程将向您展示如何快速选购并使用轻量应用服务器。

## 步骤1：注册和充值
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，并进行实名认证。
如果您已在腾讯云注册，可忽略此步骤。
2. [在线充值](https://console.cloud.tencent.com/expense/recharge)。
轻量应用服务器以包年包月模式售卖，购买前，需要在账号中进行充值。具体操作请参考 [在线充值](https://cloud.tencent.com/document/product/555/7425) 文档。

## 步骤2：购买轻量应用服务器 Windows 实例

1. 登录 [Lighthouse 控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 单击【新建】，进入轻量应用服务器购买页面。
![](https://main.qcloudimg.com/raw/f7609c52eb358d9563502f351f2eb941.png)
 - 地域：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - 镜像：选择您需要的轻量应用服务器操作系统。此处我们选择 “ASP.NET 4.8” 应用镜像（基于 Windows Server 2012 R2 操作系统）。
 - 实例套餐：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - 购买时长：默认1个月。
 - 服务器数量：默认1台。
3. 单击【立即购买】。
4. 核对配置信息后，单击【提交订单】，并根据页面提示完成支付。

当您付费完成后，即完成了轻量应用服务器的购买。接下来，您可以登录您购买的这台服务器。

## 步骤3：登录轻量应用服务器 Windows 实例
>? 轻量应用服务器 Windows 实例的登录密码将通过 [站内信](https://console.cloud.tencent.com/message) 发送给您。此密码为登录轻量应用服务器 Windows 实例的凭据。
>

登录 [Lighthouse 控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在服务器列表中找到刚购买的服务器，单击【登录】。

Windows 实例通过 VNC 终端登录，只需输入用户名（Administrator）和密码即可登录该实例。您也可以使用本地的 RDP 工具（如 Windows 自带的 MSTSC）远程连接 Windows 实例。
