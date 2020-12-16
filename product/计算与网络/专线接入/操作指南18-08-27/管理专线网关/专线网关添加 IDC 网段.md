当云联网与专线网关关联时，需配置下一跳为专线网关、目的端为 IDC 网段的路由策略，才可以实现网络通信。配置云联路由策略有手动填写（静态）和动态学习（BGP）两种方式，详情请参见[ 路由概述](https://cloud.tencent.com/document/product/877/38801)。本文将介绍如何在专线网关上配置 IDC 网段实现云联网路由传递。

## 背景信息
在下图所示的专线网络架构中，本地 IDC 通过关联云联网专线网关、云联网实现与腾讯云 VPC 通信，云上 VPC 到 IDC 方向的目的网段为 192.168.0.0/24 。在专线网关上配置 IDC 网段后，云联网的路由表中将增加一条下一跳为专线网关、目的网段为 192.168.0.0/24 的路由策略，实现路由传递。
>?若您在专线网关上配置多个 IDC 网段，云联网将根据最长掩码匹配原则进行路由转发，详情请参见[ 云联网路由概述](https://cloud.tencent.com/document/product/877/38801)。
>
![](https://main.qcloudimg.com/raw/f9d75fe01ea90d8e66c1fc0dde8540d8.png)

## 前提条件
您已创建云联类型的专线网关，并关联云联网，详情请参见[ 创建专线网关](https://cloud.tencent.com/document/product/216/19256)。

## 操作步骤
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，并在左侧导航栏单击【专线网关】。
2. 在“专线网关”页面上方选择地域和私有网络，然后在专线网关列表中单击目标实例 ID。
   ![](https://main.qcloudimg.com/raw/d4ee4863ce89963496d990418a0329da.png)
3. 在专线网关详情页面单击【IDC 网段】。
专线网关上的 IDC 网段是指专线网关发送至云联网的路由。云联网收到该路由后，将自动新增一条下一跳为此专线网关、目的端为 IDC 网段的路由。
4. 按需选择以下方式配置 IDC 网段。
 - 手动填写（静态）
    1. 在 “IDC 网段” 页签中单击【添加】。
    ![](https://main.qcloudimg.com/raw/6c576ea2f7c6a7c0caa3cd8ebc8aa45d.png)
    2. 在编辑区域填写 IDC 网段，例如本示例中 IDC 网段填写为192.168.0.0/24，单击【保存】。若需添加多个网段，则单击【添加】并重复此步骤。
    ![](https://main.qcloudimg.com/raw/2ae4f104d1d50da85739773c4f459894.png)
 - 动态学习（BGP）
  >?BGP 路由目前内测中，若需使用，请提交[ 工单申请](https://console.cloud.tencent.com/workorder/category)。
  >
    1. 单击【BGP 路由】页签。BGP 路由模式下，专线网关将自动学习到 IDC 网段信息，并发送至云联网。更新时间存在一分钟延时，若当前 IDC 网段有更新，请手动刷新页面。
    ![](https://main.qcloudimg.com/raw/6a2375196761d04e4345e4a035a72f8e.png)
    2. 在页面上方单击“静态路由”右侧的铅笔图标，并在“编辑云联网学习 IDC 网段路由方式”对话框中选择模式为 【BGP 路由】，然后单击【确定】。
    ![](https://main.qcloudimg.com/raw/a37b792bf1639eb373ff16741a6ea571.png)



