
## 操作场景
安全组是一种有状态的包含过滤功能的虚拟防火墙，用于设置单台或多台云数据库的网络访问控制，是腾讯云提供的重要的网络安全隔离手段。安全组是一个逻辑上的分组，您可以将同一地域内具有相同网络安全隔离需求的云数据库实例加到同一个安全组内。云数据库与云主机等共享安全组列表，安全组内基于规则匹配，具体规则与限制请查看[安全组详细说明](https://cloud.tencent.com/document/product/215/20089)。
>!
> 1. 云数据库安全组目前**仅支持私有网络 VPC 内网访问和外网访问的网络控制，暂不支持对基础网络的网络控制**。
> 2. 仅广州、上海、北京、成都地域支持数据库**外网访问**的安全组，其他地域暂不支持。
> 3.  **由于云数据库没有主动出站流量，因此出站规则对云数据库不生效**。
> 4. 云数据库 MySQL 安全组支持主实例、只读实例与灾备实例。
> 5. 关于安全组默认提供模板需注意如下：
 - Linux 放通 22 端口 ：仅暴露 SSH 登录的 TCP 22 端口到公网，内网端口全通，**此模板对云数据库不生效**。
 - Windows 放通 3389 端口：仅暴露 MSTSC 登录的 TCP 3389 端口到公网，内网端口全通，**此模板对云数据库不生效**。
 - 放通全部端口：允许全部 IP 访问云数据库，有一定安全风险。


## 操作步骤
### 创建安全组

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，在 **使用中的云产品** 栏目单击【云服务器】，进入云服务器管理页面。在左侧导航栏中，单击【安全组】，进入安全组管理页面。
![](https://main.qcloudimg.com/raw/cca9811bbb94a868293ce16a9966bbaa.png)
![](https://main.qcloudimg.com/raw/9c154ef45b104ffebef99a3de249b50c.png)
2. 单击【新建】按钮，选择【模板】创建或【自定义】创建，输入安全组的 **名称**（例如 my-security-group），选择 **所属项目**，选填 **备注**，确认后单击【确定】。
![](https://main.qcloudimg.com/raw/3034233f4350444678095efc87b715d4.png)
![](//mc.qcloudimg.com/static/img/b1ca53ce95a6a908effec0cb71a81e57/image.png)

### 为云数据库配置安全组
[安全组](https://cloud.tencent.com/doc/product/213/500) 是腾讯云提供的实例级别防火墙，可以对云数据库进行入/出流量控制。您可以在购买实例时绑定安全组，也可以购买实例后在控制台绑定安全组。

>! 目前云数据库 MySQL 安全组仅支持**私有网络云数据库**配置。

1. 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，在实例列表选中需要配置安全组的实例，单击【管理】，选择【安全组】标签页 > 单击【配置安全组】。
![](https://main.qcloudimg.com/raw/32a003ce61591462de06e3482b5e2f99.png)

2. 选择需要绑定的安全组，单击【确认】，即可完成安全组绑定云数据库的操作。 
![](https://main.qcloudimg.com/raw/b63568e07e679628d17d61b75fb453f5.png)

### 删除安全组

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，单击列表中安全组项后面的【更多】 > 【删除】。
![](https://main.qcloudimg.com/raw/794d76f9f7969fe66f250b63e7a99415.png)
2. 在删除安全组对话框中，单击【确定】。若当前安全组有关联的 CVM 则需要先解除安全组才能进行删除。

### 克隆安全组

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，单击列表中安全组项后面的【更多】 > 【克隆】。
![](https://main.qcloudimg.com/raw/28810c1f2b863caac6d4598d3b4c5c07.png)
2. 在克隆安全组对话框中，选定目标地域、目标项目后，单击【确定】。若新安全组需关联 CVM，请重新进行管理安全组内云主机。

### 向安全组中添加规则

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，选择需要更新的安全组，单击安全组 ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](https://main.qcloudimg.com/raw/367ec0d34a4dbb0cbc9ca800dcfc00e3.png)
2. 在入/出站规则选项卡上，单击【添加规则】。
![](https://main.qcloudimg.com/raw/c2c4533dc6ff96e4f2af2fb8ee0fea30.png)
3. 从选项卡中选择用于入/出站规则的选项，然后填写所需信息。例如，将来源/目标指定为 0.0.0.0/0，协议端口指定为TCP:3306，设置策略为 允许，单击【完成】。单击【新增一行】可以同时配置多个规则。
![](https://main.qcloudimg.com/raw/2f48931b61d45ab8275e12cf0cf70945.png)


### 导入导出安全组规则

1. 打开云服务器 CVM 控制台 [安全组页面](https://console.cloud.tencent.com/cvm/securitygroup)，选择需要更新的安全组，单击安全组 ID。详细信息窗格内会显示此安全组的详细信息，以及可供您使用入站规则和出站规则的选项卡。
![](https://main.qcloudimg.com/raw/367ec0d34a4dbb0cbc9ca800dcfc00e3.png)
2. 从选项卡中选择用于入/出站规则的选项，然后单击【导入规则】按钮。
![](https://main.qcloudimg.com/raw/ab01ffb53084acf3e88219df7aca7b25.png)
3. 如原来您已有规则，则推荐您先导出现有规则，因为规则导入将覆盖原有规则，如原来为空规则，则可先导出模板，编辑好模板文件后，再单击【选择文件】选择您的模板文件，单击【开始导入】即可。	
![](https://main.qcloudimg.com/raw/fda954cd9eaa9058a1fea6ca52d12f50.png)




