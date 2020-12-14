当云联网与专线网关关联时，需要配置下一跳为专线网关、目的端为 IDC 网段的路由策略，才可以实现网络通信。配置云联路由策略有手动填写（静态）和动态学习（BGP）两种方式，详情请参见[ 路由概述](https://cloud.tencent.com/document/product/877/38801)。本文将介绍如何在专线网关上配置 IDC 网段实现云联网路由传递。

## 背景信息
在使用云联网专线网关的专线网络架构中，云上 VPC 到 IDC 方向，目的网段为 192.168.0.0/24。在专线网关上配置 IDC 网段后，云联网的路由表中将增加一条下一跳为专线网关、目的网段为 192.168.0.0/24 的路由策略，实现路由传递。详情如下图所示。
>?若您在专线网关上配置多个 IDC 网段，云联网将根据最长掩码匹配原则进行路由转发。
>
![](https://main.qcloudimg.com/raw/f9d75fe01ea90d8e66c1fc0dde8540d8.png)

## 前提条件
您已创建云联类型的专线网关，并关联云联网，详情请参见[创建专线网关](https://cloud.tencent.com/document/product/216/19256)。

## 操作步骤
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，并在左侧导航栏单击【专线网关】。
2. 在“专线网关”页面上方选择地域和私有网络，然后在专线网关列表中单击目标实例 ID。
   ![](https://main.qcloudimg.com/raw/d4ee4863ce89963496d990418a0329da.png)
3. 在专线网关详情页面单击【IDC 网段】。
专线网关上的 IDC 网段是指专线网关发送至云联网的路由。云联网收到该路由后，将自动新增一条下一跳为此专线网关、目的端为 IDC 网段的路由。
4. 按需选择以下方式配置 IDC 网段。
 - 手动填写（静态）
    1. 在 ”IDC 网段” 页签中单击【添加】。
     ![](https://main.qcloudimg.com/raw/e6894da99e8ac4bc4fb8aba3f01706b5.png)
    2. 在编辑区域填写 IDC 网段并单击【保存】。若需添加多个网段，则单击【添加】并重复此步骤。![](https://main.qcloudimg.com/raw/7a6622da9c9d69708a6e5ae3e11305e1.png)
    3. （可选）若需传递连通的腾讯云 VPC 信息，则在页面右上角开启【 Community 属性】开关。![](https://main.qcloudimg.com/raw/1d5ea75799d08694bf3a2c47fe69ad72.png)
 - 动态学习（BGP）
  >?BGP 路由目前内测中，若需使用，请提工单申请。
  >
    1. 单击【BGP 路由】页签。BGP 路由模式下，专线网关将自动学习到 IDC 网段信息，并发送至云联网。更新时间存在一分钟延时，若当前 IDC 网段有更新，请手动刷新页面。![](https://main.qcloudimg.com/raw/e13374389b8213ba6941a0ac8acb83a7.png)
    2. 在页面上方单击“静态路由”右侧的铅笔图标，并在“编辑云联网学习 IDC 网段路由方式”对话框中选择模式为 【BGP 路由】，然后单击【确定】。![](https://main.qcloudimg.com/raw/afdd8e1e4925e18058ec07dfe096c7d6.png)
    3. （可选）若需传递连通的腾讯云 VPC 信息，则在页面右上角开启【 Community 属性】开关。
    ![](https://main.qcloudimg.com/raw/85ef415b4e20ad439d4c96871bc896c0.png)

