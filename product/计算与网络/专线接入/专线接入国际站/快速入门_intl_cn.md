选择专线接入产品打通您的 IDC 和腾讯云 VPC，您需要完成以下步骤：
![](https://main.qcloudimg.com/raw/58f595324abb56461e3df9eef259a8a6.png)
下面将为您详细说明操作步骤。
## 步骤 1：创建物理专线
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，单击左侧导航【物理专线】，进入物理专线页面，单击【+新建】。
![2](https://main.qcloudimg.com/raw/4b96f1b984537210566d7cebc6e71c2a.png)
2. 在弹出框中，根据您的需求填写对应的信息，提交申请。
腾讯云物理专线支持合作伙伴申请和自助申请：
 - 合作伙伴申请：单击申请专线窗口内【单击了解】，可跳转至腾讯云云市场专线合作伙伴页，您可自行选择合适的专线服务商，为您提供物理专线接入服务。
 - 自助申请：若腾讯云专线合作伙伴未能满足您的需求，请填写相应的参数信息（如上图所示），详情请参见 [申请物理专线](https://cloud.tencent.com/document/product/216/19244)。     

## 步骤 2：创建专线网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，单击左侧导航【专线网关】，进入管理页面。
2. 单击【+新建】，在弹出框中，选择所在网络、网关类型、填写名称，单击【确认】即可，详情请参见 [创建专线网关](https://cloud.tencent.com/document/product/216/19256)。

## 步骤 3：创建专用通道
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，单击左侧导航【专用通道】，进入管理页面，单击【+新建】。
![](https://main.qcloudimg.com/raw/cd1780e0c7413890e44e08938b175a75.png)
2. 专用通道指腾讯云内网部分，起点是腾讯云物理专线接入点，终点是您的 VPC。请填写相应的技术参数（如上图所示），详情请参见 [申请通道](https://cloud.tencent.com/document/product/216/19250)。

## 步骤 4：（可选配置）专线 NAT
登录 [专线网关控制台](https://console.cloud.tencent.com/vpc/dcGw) ，配置网关的网络地址转换，网络地址转换分为 IP 转换和 IP 端口转换两种，详情请参见 [配置网络地址转换（NAT）](https://cloud.tencent.com/document/product/216/19257)。

## 步骤 5：配置路由表
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com)，选择【云产品】>【云计算与网络】>【私有网络】，进入私有网络控制台。
2. 单击左导航栏中【路由表】，单击需要通信的子网所关联的路由表 ID，进入详情页。
3. 单击【+新增路由策略】，输入目的端网段，选择下一跳类型【专线网关】，再选择下一跳网关名，保存即可。详情请参见 [配置路由表](https://cloud.tencent.com/document/product/216/19259)。

## 步骤 6：设置告警
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com)，选择【云产品】 >【管理工具】 > 【云监控】，单击左侧导航【我的告警】>【告警策略】，进入告警策略页面。
2. 单击【+新增告警策略】，填写告警策略名称，在策略类型中选择【物理专线】或【专用通道】，添加告警触发条件、关联告警对象，保存即可。详情请参见 [设置告警](https://cloud.tencent.com/document/product/216/19248)。
