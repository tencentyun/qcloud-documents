当云联网与专线网关关联时，需为云联网配置下一跳为专线网关、目的端为 IDC 网段的路由策略，才可以实现网络通信。配置云联网路由策略有自定义手动填写（静态）和自动学习传递自动学习（BGP）两种方式，详情请参见[ 路由概述](https://cloud.tencent.com/document/product/877/38801)。本文将介绍如何在专线网关上 发布网段至云联网。
>?专线网关发往云联网的路由条目数小于等于20条，如需提升额度请提交[ 工单申请](https://console.cloud.tencent.com/workorder/category)。
>

## 背景信息
在下图所示的专线网络架构中，本地 IDC 通过关联云联网专线网关、云联网实现与腾讯云 VPC 通信，云上 VPC 到 IDC 方向的目的网段为 192.168.0.0/24 。在专线网关上配置 IDC 网段后，云联网的路由表中将增加一条下一跳为专线网关、目的网段为 192.168.0.0/24 的路由策略，实现路由传递。
>?若您在专线网关上配置多个 IDC 网段，云联网将根据最长掩码匹配原则进行路由转发，详情请参见[ 云联网路由概述](https://cloud.tencent.com/document/product/877/38801)。
>
![](https://main.qcloudimg.com/raw/f9d75fe01ea90d8e66c1fc0dde8540d8.png)

## 前提条件
您已创建云联类型的专线网关，详情请参见[ 创建专线网关](https://cloud.tencent.com/document/product/216/19256)。

## 操作步骤
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，并在左侧导航栏单击**专线网关**。
2. 在“专线网关”页面上方选择地域和私有网络，然后在专线网关列表中单击目标实例 ID。
	 ![](https://main.qcloudimg.com/raw/b2c74e240ce219c8f8d19413295037df.png)
3. 在专线网关详情页面单击**发布网段**。
专线网关上的发布网段（即 IDC 网段）是指专线网关发送至云联网的路由。云联网收到该路由后，将自动新增一条下一跳为此专线网关、目的端为 IDC 网段的路由。
4. （可选）关联云联网。
    如果[ 创建专线网关](https://cloud.tencent.com/document/product/216/19256) 时没有指定具体的云联网实例，请单击**关联云联网**，然后在弹出的对话框中选择待关联的云联网实例并单击**确定**。
	![](https://main.qcloudimg.com/raw/bb42fe39d2749369dcb201a9cc03d3a4.png)
	成功添加云联网实例后，云联网图标将显示已关联且图标颜色显示为绿色，专线网关与云联网之间的虚线变为实线。即专线网关与云联网已互联。
5. 创建专用通道。
    专用通道是物理专线的网络链路划分，提供了用户 IDC 和腾讯云之间的网路链路。
	在与专线网关相连的专用通道图标下，单击**创建专用通道**。自动跳转至专业通道创建页面，您可在该页面配置专用通道信息。
	![](https://main.qcloudimg.com/raw/407d83a3b3fde8f7dc07424632f8d276.png)
	专业通道创建详情请参见 [申请专用通道](https://cloud.tencent.com/document/product/216/19250)。
	成功创建专用通道后，专用通道图标将显示已创建且图标颜色显示为绿色，专线网关与云联网之间的虚线变为实线。即已为专线网关配置专用通道。
6. 发布 IDC 网段至云联网。
   发布 IDC 网段到云联网，专线网关可以学习到云联网路由；云联网是否学习到的专线网关路由，由IDC 网段发布方式决定。
    - 自定义方式：用户手动配置模式，云联网学会指定的专线网关路由。
    - 自动传递方式：即 BGP 模式，云联网自动获取专用通道发来的网关路由，但取决于专用通道的发布时间。
 <dx-tabs>
::: 自定义方式
即原静态/手动配置模式。
   1. （可选）在**发布规则**区域选择云联网实例。
      当前专线网关未配云联网或者更换云联网情况下可执行本步骤。
	![](https://main.qcloudimg.com/raw/f50623ebd48351c081b5ea4ca7b21bde.png)
	<dx-alert infotype="explain" title="">
发布方式系统自动填充，默认**自定义**方式，如果需要**自动传递**方式请提交[ 工单申请](https://console.cloud.tencent.com/workorder/category)。
</dx-alert>
   2. 在**网段详情**页面的**自定义**页签中单击**新建**，并填写发往云联网的网关信息，然后单击**保存**。
	  ![](https://main.qcloudimg.com/raw/296ba61bf58e98f1496026909e74b994.png)
		单击**保存**后，专线网关将配置的 IDC 网段发送给云联网。
<dx-alert infotype="explain" title="">
发布的 IDC 网段数须小于等于100个。如需超额请提交[ 工单申请](https://console.cloud.tencent.com/workorder/category)。
</dx-alert>

:::
::: 自动传递方式
即原BGP模式。如需使用请提交[ 工单申请](https://console.cloud.tencent.com/workorder/category)。
   1. （可选）在**发布规则**区域选择云联网实例。
      当前专线网关未配云联网或者更换云联网情况下可执行本步骤。
	![](https://main.qcloudimg.com/raw/8b4156d0ee5f0ff6233abb01f6d651da.png)
<dx-alert infotype="explain" title="">
- 开启本功能后系统勾选**自动传递**。如果有自定义使用场景，请勾选**自定义**进行配置。
- 自定义模式和自动传递模式二者只能生效其一。
</dx-alert>
   2. 配置 IDC 网段。
     在**自动传递**方式下专线网关自动学习 IDC 网段信息，无须配置。![](https://main.qcloudimg.com/raw/b3070526cb406520ec6bf83447a9754e.png)
		 <dx-alert infotype="explain" title="">
更新时间存在一分钟延时，若当前 IDC 网段有更新，请手动刷新页面。
</dx-alert>
     :::
     ::: 模式切换须知
     发送网关的 IDC 网段到云联网的两种方式支持互相切换。
- 自定义切换为自动传递
   需要提交[ 工单申请 ](https://console.cloud.tencent.com/workorder/category)开启自动传递发布发布功能。
	 自定义方式切换为自动传递方式后，当前已发布到云联网的自定义 IDC 网段信息将被撤回，专线网关自动学习 IDC 网段信息并将其传递给云联网。
- 自动传递切换为自定义
   自动传递方式切换为自定义方式后，需要在**网段详情**页面的**自定义**页签中配置待发布的网段。
   :::
   </dx-tabs>
7. 查看发布的 IDC 网段。
    在**网段详情**页面的网段列表中可查看发布的 IDC 网段信息。
