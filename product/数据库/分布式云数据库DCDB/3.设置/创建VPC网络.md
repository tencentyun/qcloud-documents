如下图所示，在本练习中，您将创建一个 VPC 和子网，并在您的子网中部署一个云服务器，通过绑定弹性 IP 使其能与 Internet 通信，最后通过安全组对进出该云服务器的流量进行筛选，保证主机通信的安全。在真实应用环境下，您能够从本地计算机访问您的云服务器，并使用此方案创建面向公众的 Web 服务器；例如，托管一个博客。
![](//mccdn.qcloud.com/static/img/7a428200fc9782b02d05d220ae6328bb/image.png)



### 第一步：创建私有网络、初始化子网和路由表
私有网络至少包含一个子网，只有在子网中才可以添加云服务资源。

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【私有网络】，或者进入腾讯云 [私有网络介绍页中](https://cloud.tencent.com/product/vpc.html) 的【立即体验】按钮，进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2)	选择列表上方下拉框中的地域，点击【新建】创建私有网络，例如，选择地域“华北地区（北京）”。
3)	填写私有网络和子网的名称和 CIDR，并选择子网的可用区。
4)	点击【创建】。

![](//mccdn.qcloud.com/static/img/55cdba64e785d9b073bc4169a9459e39/image.png)

### 第二步：创建子网
您可以同时创建一个或多个子网。

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【私有网络】，或者进入腾讯云[私有网络介绍页中](https://cloud.tencent.com/product/vpc.html)的【立即体验】按钮，进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2)	点击左导航栏中的【子网】。
3)	选择下拉框中的地域和私有网络。
4)	点击【新建】，填写子网络名称、CIDR、可用区和关联路由表。
5)	（可选）点击【新增一行】，可以同时创建多个子网。
6)	点击【创建】。

![](//mccdn.qcloud.com/static/img/66a4e93f7f8dfeeed421fb799fd09137/image.png)


### 第三步：新建路由表关联子网
您可以创建自定义路由表、编辑路由策略、然后关联指定子网，子网关联的路由表用于指定该子网的出站路由。

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【私有网络】，或者进入腾讯云 [私有网络介绍页中](https://cloud.tencent.com/product/vpc.html) 的【立即体验】按钮，进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2) 选择左导航栏中的【路由表】，点击列表上方【新建】按钮，在创建路由表弹出框中输入名称、所属网络及新建路由策略。
3) 点击【创建】，即可在路由表列表中看到您新建的路由表。
4) 点击左导航栏中的【子网】。
5) 鼠标移动到需要关联该路由表的【子网】一行， 编辑按钮即会出现在【关联路由表】列中。
6) 点击【编辑按钮】，在下拉框中选择关联路由表。
7) 点击【保存】。

![](//mccdn.qcloud.com/static/img/a41758221e11cacef5dbdbd53f06049a/image.png)


### 第四步：向子网中添加云主机

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【私有网络】，或者进入腾讯云 [私有网络介绍页中](https://cloud.tencent.com/product/vpc.html) 的【立即体验】按钮，进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2) 选择左导航栏中的【子网】。
3) 在需要添加云主机的子网所在行，点击增加云主机图标。注意这里创建的云服务器实例请选择一个大于 0 的带宽或选择使用流量收费，因为本教程中的其他步骤需要对 Internet 进行访问。

或者

1)	在 [云服务器介绍页](https://cloud.tencent.com/product/cvm.html) 中点击【立即选购】按钮。
2)	在第三步选择存储与网络时选择刚刚创建的私有网络和对应的子网。注意这里创建的云服务器实例请选择一个大于 0 的带宽或选择使用流量收费，因为本教程中的其他步骤需要对 Internet 进行访问。

### 第五步：为云主机绑定弹性 IP 访问公网
[弹性 IP](https://cloud.tencent.com/doc/product/213/1941) 是一种与用户帐号相关联的公网 IP 地址，用于与 Internet 的通信，用户可以使用弹性 IP 快速绑定任何云服务器使其可以与公网通信。

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【云服务器】选项卡，在左导航窗格中，单击【弹性公网 IP】。
2) 单击【申请】按钮。
3) 选择申请与私有网络在同一地域的 EIP，完成后即可在 EIP 列表中看到您申请的 EIP。
4) 在 EIP 列表中选择指定 IP，点击【绑定】，选择刚刚创建的私有网络内云服务器绑定。绑定完成之后，您的云主机即可访问公网。
![](//mccdn.qcloud.com/static/img/4853aa0215993d8ce40e965cafee6bf8/image.png)

### （可选）第六步：创建安全组进行网络流量控制
[安全组](https://cloud.tencent.com/doc/product/213/500) 是腾讯云提供的实例级别防火墙，可以对任意云服务器进行入/出流量控制。

1) 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，点击导航条【云服务器】选项卡，在左导航窗格中，单击【安全组】。
2) 单击【新建】按钮，输入安全组的名称（例如 my-security-group）并提供说明，即可创建完成。
3) 点击安全组列表后的【加入云主机】按钮，选择需要刚刚创建的云主机。
6) 点击上方【入站规则】、【出站规则】选项卡，编辑入站、出站规则，控制流量。

例如：允许来自您本地计算机（IP：186.23.55.90）通过 HTTP 请求云服务器，可以创建一条类似下图的规则。

![](//mccdn.qcloud.com/static/img/3dab4565be71898ca2e0e9cf79639c92/image.png)

