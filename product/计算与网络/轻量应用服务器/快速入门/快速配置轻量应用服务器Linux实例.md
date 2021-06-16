本入门教程将向您展示如何快速选购并使用轻量应用服务器。

## 步骤1：注册和充值
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，并进行实名认证。
如果您已在腾讯云注册，可忽略此步骤。
2. [在线充值](https://console.cloud.tencent.com/expense/recharge)。
轻量应用服务器以包年包月模式售卖，购买前，需要在账号中进行充值。具体操作请参考 [在线充值](https://cloud.tencent.com/document/product/555/7425) 文档。

## 步骤2：购买轻量应用服务器 Linux 实例

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 单击【新建】，进入轻量应用服务器购买页面。
![](https://main.qcloudimg.com/raw/0eed4167d91b57868189705beb964e97.png)
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择您需要的轻量应用服务器操作系统。此处我们选择 CentOS 8.0 系统镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、带宽或峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用“镜像名称-四位随机字符”。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击【立即购买】。
4. 核对配置信息后，单击【提交订单】，并根据页面提示完成支付。

当您付费完成后，即完成了轻量应用服务器的购买。接下来，您可以登录您购买的这台服务器。

## 步骤3：登录轻量应用服务器 Linux 实例
登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在服务器列表中找到刚购买的服务器，单击【登录】。
Linux 实例将通过 Webshell 终端并以免密方式登录。
![](https://main.qcloudimg.com/raw/71162a6e915198b66810b7919dfcdb66.png)



## 步骤4：重置轻量应用服务器 Linux 实例密码（可选）
如果您需要使用 SSH 或者远程登录软件连接 Linux 实例，请先 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 或 [设置密钥](https://cloud.tencent.com/document/product/1207/44573)。此步骤以重置密码为例，请结合实际情况按需操作。

1. 在 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index) 的服务器列表中，找到并进入刚购买的服务器详情页。
2. 在“实例信息”栏中，单击【重置密码】。如下图所示：
![](https://main.qcloudimg.com/raw/fcbc4f5968c1f70220f410da5e916ca5.png)
3. 在弹出的“重置密码”窗口中，输入并确认密码，并根据界面提示完成重置密码操作。 
>?
>- 重置密码需要在实例关机状态下操作，建议您先将实例关机再执行重置密码的操作。如果您选择在开机状态下重置密码，则需要勾选“同意强制关机”才能执行操作。
>- 若您使用 Ubuntu 镜像创建实例，则该实例默认禁用 root 用户名通过密码的方式登录实例。如需开启，[请参考 Ubuntu 系统如何使用 root 用户登录实例？](https://cloud.tencent.com/document/product/1207/44569#ubuntu-.E7.B3.BB.E7.BB.9F.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8-root-.E7.94.A8.E6.88.B7.E7.99.BB.E5.BD.95.E5.AE.9E.E4.BE.8B.EF.BC.9F)。
>
![](https://main.qcloudimg.com/raw/b6605b372bc1c84b3e30ba4f0e198467.png)
