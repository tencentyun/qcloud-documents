本入门教程将向您展示如何快速选购并使用轻量应用服务器。

## 步骤1：注册和充值
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，并进行实名认证。
如果您已在腾讯云注册，可忽略此步骤。
2. [在线充值](https://console.cloud.tencent.com/expense/recharge)。
轻量应用服务器以包年包月模式售卖，购买前，需要在账号中进行充值。具体操作请参考 [在线充值](https://cloud.tencent.com/document/product/555/7425) 文档。

## 步骤2：购买轻量应用服务器 Windows 实例

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 单击**新建**，进入轻量应用服务器购买页面。如下图所示：
![](https://main.qcloudimg.com/raw/3de27e872fdf901da021a17a6581c1a6.png)
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择您需要的轻量应用服务器操作系统。此处我们选择 Windows Server 2012 R2 中文版系统镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、带宽或峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用“镜像名称+四位随机字符”。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **登录方式**：当您选择 Windows 镜像时，可通过该项设置实例的登录密码：
    - **设置密码**： 自定义设置实例的登录密码。
    - **自动生成密码**：自动生成的密码将会以 [站内信](https://console.cloud.tencent.com/message) 方式发送。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击**立即购买**。
4. 核对配置信息后，单击**提交订单**，并根据页面提示完成支付。

## 步骤3：登录轻量应用服务器 Windows 实例

1. 在 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index) 的服务器列表中，找到刚购买的服务器，单击**登录**。
Windows 实例将通过 VNC 终端登录。
![](https://main.qcloudimg.com/raw/8255eaade6b397131f48a99aec108b68.png)
2. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)
3. 输入登录密码，按 **Enter**，即可登录该实例。

此外，您也可以使用本地的 RDP 工具（如 Windows 自带的 MSTSC）远程连接 Windows 实例。
