
## 操作指南

### 创建安全组

1. 登录 [腾讯云控制台](https://console.qcloud.com/)，单击导航条【云服务器】选项卡，在左导航窗格中，单击【安全组】。
![](//mc.qcloudimg.com/static/img/605d8758a359487291240d791ce4e90f/image.png)
![](//mc.qcloudimg.com/static/img/d6c8d4e12d497e3f55a4d5fbbae84e84/image.png)
2. 单击【新建】按钮，输入安全组的名称（例如 my-security-group），选择【模板】创建或【自定义】创建，单击【显示模板规则】可以显示【出/入站规则】，确认后单击【确定】。
![](//mc.qcloudimg.com/static/img/9dc27b43803588b7abb92ec1699ac89c/image.png)
![](//mc.qcloudimg.com/static/img/b1ca53ce95a6a908effec0cb71a81e57/image.png)

### 为云数据库配置安全组
[安全组](https://www.qcloud.com/doc/product/213/500) 是腾讯云提供的实例级别防火墙，可以对云数据库进行入/出流量控制。
>**注意：**
目前安全组仅支持**私有网络云数据库**配置。

1. 进入 [云数据库控制台](https://console.qcloud.com/cdb)，在实例列表选中需要的实例，单击【管理】，选择【安全组】标签页 > 单击【配置安全组】，选择需要绑定的安全组，即可完成安全组绑定云数据库的操作。 
![](//mc.qcloudimg.com/static/img/2331e6b96fa1af3c9754cac0f8fe3854/image.png)
2. 您还可以在新购实例时，选择安全组绑定。

### 删除安全组

1. 打开云服务器CVM控制台 [安全组页面](https://console.qcloud.com/cvm/securitygroup)，单击列表中安全组项后面的【删除】按钮。
![](//mc.qcloudimg.com/static/img/43f705a8efd4426f18e547e6046b2149/image.png)
2. 在删除安全组对话框中，单击【确定】。若当前安全组有关联的CVM则需要先解除安全组才能进行删除。

### 克隆安全组

1. 打开云服务器CVM控制台 [安全组页面](https://console.qcloud.com/cvm/securitygroup)，单击列表中安全组项后面的【克隆】按钮。
![](//mc.qcloudimg.com/static/img/88ca3f6b17c21a2bd9d78f9e30a6c1b7/image.png)
2. 在克隆安全组对话框中，选定目标地域、目标项目后，单击【确定】。若新安全组需关联CVM，请重新进行管理安全组内云主机。

### 向安全组中添加规则

1. 打开云服务器CVM控制台 [安全组页面](https://console.qcloud.com/cvm/securitygroup)，选择需要更新的安全组，点击安全组ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. 在入/出站规则选项卡上，单击【添加规则】。从选项卡中选择用于入/出站规则的选项，然后填写所需信息。例如，将来源/目标指定为 0.0.0.0/0，协议端口指定为 TCP:80，完成后，单击【保存】。（单击【新增一行】可以同时配置多个规则）
![](//mc.qcloudimg.com/static/img/9a4c41f6c60d385b0fb394740ab4bf65/image.png)

### 导入导出安全组规则

1. 打开云服务器CVM控制台 [安全组页面](https://console.qcloud.com/cvm/securitygroup)，选择需要更新的安全组，点击安全组ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. 从选项卡中选择用于入/出站规则的选项，然后点击【导入规则】按钮。如原来您已有规则，则推荐您先导出现有规则，因为规则导入将覆盖原有规则，如原来为空规则，则可先导出模板，编辑好模板文件后，再将文件导入。
![](//mc.qcloudimg.com/static/img/c338b1cd919986000468371e83a43655/image.png)
	




