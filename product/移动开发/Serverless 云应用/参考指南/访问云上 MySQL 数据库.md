云托管应用可以通过其所在的 [VPC（私有网络）](https://cloud.tencent.com/document/product/215)访问您在云上的 MySQL 数据库。

>? 
> - 目前暂不支持开通后更改云托管所在环境绑定的 VPC，如果您的云托管应用和数据库不在同一个 VPC 内，可选择 [打通多个 VPC](https://cloud.tencent.com/document/product/215/36698)，或 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请销毁当前环境的云托管后，重新开通并选择正确的网络配置。
> - 关于使用 VPC 连接 MySQL，可以参考 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130)。

## 示例

**以下示例需要您的云托管应用和 MySQL 数据库处于同一 VPC 内。**

### 第 1 步：查询 MySQL 实例所在 VPC

1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，找到您的 MySQL 实例；
2. 在左侧菜单中，单击【实例列表】，进入实例列表。单击实例名进入详情页，进入【实例详情】选项卡，在基本信息版块中，查找到**所属网络**信息：
   ![](https://main.qcloudimg.com/raw/587ff2bf466ce705cd1b559d36d48cf8.jpg)

### 第 2 步：开通云托管

具体流程可以参考：[开通云托管](https://cloud.tencent.com/document/product/1243/47080)。

创建时，在**云托管网络**中选择【自定义配置】，下拉选择步骤 1 中查询到 MySQL 实例所在的 VPC 和子网。
![](https://main.qcloudimg.com/raw/0a0d75d92a19a9abbd66ec318d3af591.png)

开通成功后，您将自动跳转到云托管的服务列表页面。当前您还没有创建任何服务，列表为空。
至此您已经成功开通后**云托管**服务，您可以单击【新建服务】开始新建您的第一个服务。

您在该环境下创建的所有服务，都可以访问您选定的 MySQL 实例，以及同 VPC 下其他 MySQL 实例。
![](https://main.qcloudimg.com/raw/6b5051cc990cafee831e002416b5e67e.png)

## 说明

- 若您需要复用多个不在同一 VPC 下的 MySQL 实例，可在多个云开发环境开通云托管分别对应不同 VPC，或打通多个 VPC。如何打通多个 VPC，请参见 [连接其它 VPC](https://cloud.tencent.com/document/product/215/36698) 文档。
- 若您已开通云托管，误选了和 MySQL 实例不相同的 VPC，可选择打通多个 VPC，或 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请销毁当前环境的云托管后，重新开通并选择正确的网络配置。
- 云托管暂时仅支持上海地域。若您的 MySQL 实例不在上海地域则无法复用。更多地域将陆续开放，敬请期待。
