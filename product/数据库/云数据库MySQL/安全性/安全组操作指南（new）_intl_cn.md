本文是对创建安全组、为云数据库配置安全组、删除安全组、克隆安全组、向安全组中添加规则、导入导出安全组规则的介绍。
>**注意：**
云数据库安全组目前仅支持私有网络 VPC 内网访问和外网访问的网络控制，暂不支持对基础网络的网络控制。目前云数据库仅 CDB for MySQL 支持安全组。

### 创建安全组

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，在 **使用中的云产品** 栏目单击【云服务器】，进入云服务器管理页面。在左侧导航栏中，单击【安全组】，进入安全组管理页面。
![](//mc.qcloudimg.com/static/img/605d8758a359487291240d791ce4e90f/image.png)
![](//mc.qcloudimg.com/static/img/d6c8d4e12d497e3f55a4d5fbbae84e84/image.png)
2. 单击【新建】按钮，选择【模板】创建或【自定义】创建，输入安全组的 **名称**（例如 my-security-group），选择 **所属项目**，选填 **备注**，确认后单击【确定】。
![](//mc.qcloudimg.com/static/img/9dc27b43803588b7abb92ec1699ac89c/image.png)
![](//mc.qcloudimg.com/static/img/b1ca53ce95a6a908effec0cb71a81e57/image.png)

### 为云数据库配置安全组
[安全组](https://cloud.tencent.com/doc/product/213/500) 是腾讯云提供的实例级别防火墙，可以对云数据库进行入/出流量控制。您可以在购买实例时绑定安全组，也可以购买实例后在控制台绑定安全组。
>**注意：**
目前安全组仅支持**私有网络云数据库**配置。

进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，在实例列表选中需要配置安全组的实例，单击【管理】，选择【安全组】标签页 > 单击【配置安全组】，选择需要绑定的安全组，即可完成安全组绑定云数据库的操作。 
![](//mc.qcloudimg.com/static/img/2331e6b96fa1af3c9754cac0f8fe3854/image.png)

### 删除安全组

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，单击列表中安全组项后面的【删除】按钮。
![](//mc.qcloudimg.com/static/img/43f705a8efd4426f18e547e6046b2149/image.png)
2. 在删除安全组对话框中，单击【确定】。若当前安全组有关联的 CVM 则需要先解除安全组才能进行删除。

### 克隆安全组

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，单击列表中安全组项后面的【克隆】按钮。
![](//mc.qcloudimg.com/static/img/88ca3f6b17c21a2bd9d78f9e30a6c1b7/image.png)
2. 在克隆安全组对话框中，选定目标地域、目标项目后，单击【确定】。若新安全组需关联 CVM，请重新进行管理安全组内云主机。

### 向安全组中添加规则

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，选择需要更新的安全组，点击安全组 ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. 在入/出站规则选项卡上，单击【添加规则】。从选项卡中选择用于入/出站规则的选项，然后填写所需信息。例如，将来源/目标指定为 0.0.0.0/0，协议端口指定为 ALL，设置策略为 允许，单击【完成】。单击【新增一行】可以同时配置多个规则。
>**注意：**
>对于安全组的每条规则，有以下几项注意事项：
>- 协议端口：云数据库协议端口仅支持 **ALL**，若指定端口则该条规则对云数据库不生效。
>- 授权类型：地址段（CIDR/IP）访问；
>- 来源（入站规则）或目标（出站规则），请指定以下选项之一：
>    - 用 CIDR 表示法，指定的单个 IP 地址。
>    - 用 CIDR 表示法，指定的 IP 地址范围（例如，203.0.113.0/24）。
>- 策略：允许或拒绝。
</blockquote>
![安全组规则指定端口为ALL](//mc.qcloudimg.com/static/img/8c5fa48b305592762e1e86acb30376b6/image.png)

### 导入导出安全组规则

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，选择需要更新的安全组，点击安全组 ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. 从选项卡中选择用于入/出站规则的选项，然后点击【导入规则】按钮。如原来您已有规则，则推荐您先导出现有规则，因为规则导入将覆盖原有规则，如原来为空规则，则可先导出模板，编辑好模板文件后，再将文件导入。
![](//mc.qcloudimg.com/static/img/c338b1cd919986000468371e83a43655/image.png)
	




