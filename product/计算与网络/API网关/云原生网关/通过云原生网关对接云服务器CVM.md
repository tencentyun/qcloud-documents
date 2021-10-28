## 操作场景

该任务指导您通过云原生网关快速将部署在 [云服务器 CVM](https://cloud.tencent.com/product/cvm) 内的服务对第三方开放出来。

## 前提条件

- 准备一台 [云服务器 CVM](https://console.cloud.tencent.com/cvm/instance)（参考 [创建实例](https://cloud.tencent.com/document/product/213/44264)），部署在 VPC 内作为后端服务，以下简称为“后端 CVM”。
- 已创建类型为 Kong 的云原生网关（参考 [创建云原生网关](https://cloud.tencent.com/document/product/628/63034)），创建的云原生网关必须和后端 CVM 处于同一地域和同一 VPC 下。

## 操作步骤

### 步骤1：放通云原生网关内网网段

1. 登录 [云服务器 CVM](https://console.cloud.tencent.com/cvm/instance) 控制台，在左侧导航栏单击**安全组**，进入安全组列表。
2. 选择地域后，单击**+新建**，在弹出的对话框中填写内容，创建一个安全组。
![](https://qcloudimg.tencent-cloud.cn/raw/7c45b66922d6575d482bd8b23e991ae5.png)
3. 单击**确定**后进入安全组详情页面，依次选择**安全组规则** > **入站规则**，即可到达入站规则列表。
4. 单击**添加规则**，在弹出的对话框中依次添加10.0.0.0/8 、192.168.0.0/16、172.16.0.0/12三个 VPC 内网网段，协议端口均填写“ALL”，策略均配置为“允许”。单击**完成**，添加三条入站规则。
![](https://qcloudimg.tencent-cloud.cn/raw/ce99faf32afb9d6ff67e4ac1eea8a52f.png)
5. 返回安全组详情页面，依次选择**关联实例** > **云服务器** > **新增关联**，将刚创建好的安全组关联到后端 CVM 上，即可实现放通 VPC 内网网段。

### 步骤2：在云原生网关的管理控制台上配置服务和路由

1. 登录 [云原生网关](https://console.cloud.tencent.com/apigateway/cnapigw) 控制台。
2. 在云原生网关列表中选择已创建的云原生网关，单击网关 ID 即可进入网关详情页。
3. 在网关详情页上方导航栏选择**配置管理**，找到 Kong 管理控制台的地址和管理员账号、密码，使用账号和密码登录 Kong 的管理控制台。
![](https://qcloudimg.tencent-cloud.cn/raw/d1a9702d03898ca497d581d8f434d9d5.png)
4. 在 Kong 管理控制台左侧导航栏单击**Services**，进入服务列表。
5. 单击 **ADD NEW SERVICE**，在弹出的对话框中填写内容，创建一个 Service。
   创建 Service 时，URL 字段请填写后端 CVM 的内网 IP，端口为 80，填写格式为“协议://CVM 内网 IP:80”，其他字段可选填。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4e8e9c6275265a1abf59daeb33f991ed.png)
6. 在 Service 列表中单击已创建好的 Service 名称，进入 Service 详情页。
   ![](https://qcloudimg.tencent-cloud.cn/raw/22983ffbc7a7cf599858a21dcab7ac7e.png)
7. 在 Service 详情页的左侧导航栏单击 **Routes**，进入 Route 列表。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4a5519e86c61881cfe0d4d2b140b33a9.png)
8. 单击**ADD ROUTE**，在弹出的对话框中填写内容，创建一个 Route。
   Route的 Path 必填，其他字段可选填。Path 代表路径，必须以“/”开头，您可用代理地址+路径访问到后端服务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/86e31438984ead06d74910cfc1f6c947.png)
>!由于 Konga 控制台的限制，创建 Route 时，输入 Path 后必须按回车键确认，才能创建成功。

### 步骤3：通过云原生网关访问后端服务

1. 登录 [云原生网关](https://console.cloud.tencent.com/apigateway/cnapigw) 控制台。
2. 在云原生网关列表中选择已创建的云原生网关，单击网关id即可进入网关详情页。
3. 在网关详情页上方导航栏选择配置管理，找到 Kong 代理地址，其中公网代理地址用于从公网发起访问，内网代理地址用于从腾讯云 VPC 网络环境发起访问。
4. 在浏览器中打开“公网代理地址+步骤2中 Route 的路径”即可访问到 CVM 中部署的服务。
