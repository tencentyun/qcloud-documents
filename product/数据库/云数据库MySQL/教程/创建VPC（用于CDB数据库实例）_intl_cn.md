腾讯云提供托管腾讯云 CDB 数据库的平台：腾讯云 VPC。利用腾讯云 VPC ，您可以在 VPC 中启动腾讯云资源，如腾讯云 CDB 数据库实例。VPC 产品详细说明请参照 [私有网络](https://cloud.tencent.com/document/product/215/535)。  
一种常见的方案是运行在同一 VPC 的腾讯云 CDB 数据库实例和 Web 服务器共享数据。在本教程中，针对此方案创建 VPC，并将云数据库添加进 VPC 以配合使用。

### 步骤一：创建私有网络、初始化子网和路由表
私有网络至少包含一个子网，只有在子网中才可以添加云服务资源。

1. 登录 [腾讯云控制台][1]，单击导航条【云产品】 > 【基础产品】 > 【云计算与网络】 > 【私有网络】，或者单击腾讯云 [私有网络介绍页中][2] 的【立即使用】按钮，进入 [私有网络控制台][3]。

2. 选择列表上方下拉框中的地域，单击【新建】创建私有网络，例如，选择地域：华南地区（广州）。

3. 填写私有网络和子网的名称和 CIDR，并选择子网的可用区，单击【创建】。
![](//mc.qcloudimg.com/static/img/bdc491002ac8b6413cc5f540ca3770fc/image.png)


### 步骤二：创建子网
您可以同时创建一个或多个子网。

1. 在 [私有网络控制台][3] 中，单击左导航栏中的【子网】。

2. 选择下拉框中的地域和私有网络，单击【新建】。

3. 填写子网络名称、CIDR、可用区和关联路由表，单击【创建】。单击【新增一行】，可以同时创建多个子网。
![](//mc.qcloudimg.com/static/img/79e6800671416941767ef285e2849396/image.png)

### 步骤三：新建路由表关联子网
您可以创建自定义路由表、编辑路由策略、然后关联指定子网，子网关联的路由表用于指定该子网的出站路由。

1. 在 [私有网络控制台][3] 中，单击左导航栏中的【路由表】，选择下拉框中的地域和私有网络，单击【新建】。

2. 在创建路由表弹出框中输入名称、所属网络及新建路由策略。单击【创建】，即可在路由表列表中看到您新建的路由表。

3. 单击左导航栏中的【子网】。鼠标移动到需要关联该路由表的【子网】一行， 编辑按钮即会出现在【关联路由表】列中。单击【编辑按钮】，在下拉框中选择关联路由表。单击【保存】。
![](//mc.qcloudimg.com/static/img/5662a3998871f061c3ddd0628d98c1ff/image.png)

### 步骤四：添加云数据库
新购的云数据库支持在私有网络中使用，需要注意的是，网络一旦选定将不可更改。

1. 登录腾讯云 [管理控制台][1]，将鼠标移至导航条中的【云产品】>【数据库】单击【云数据库MySQL】，进入 [云数据库控制台][11]，单击【新建】按钮，进入云数据库 MySQL 购买界面。

2. 在云数据库选购页【网络】选项，单击私有网络，选择之前创建的私有网络以及相应子网，将新购的云数据库添加进私有网络。


### 步骤五：添加云服务器
新购的云服务器支持在私有网络中使用，需要注意的是，**网络一旦选定将不可更改。**
进入云服务器 [产品介绍页](https://cloud.tencent.com/product/cvm)，单击【立即选购】后，在产品购买页的【网络类型】选择【私有网络】，选择与之前数据库相同的 VPC，将新购的云服务器添加到与云数据库相同的 VPC 内。
![](https://mc.qcloudimg.com/static/img/ede1b30456b4fe9f46e6f0ea954f8c22/step11.png)


[1]:	https://console.cloud.tencent.com/
[2]:	https://cloud.tencent.com/product/vpc.html
[3]:	https://console.cloud.tencent.com/vpc/
[4]:	https://console.cloud.tencent.com/
[5]:	https://cloud.tencent.com/product/vpc.html
[6]:	https://console.cloud.tencent.com/vpc/
[7]:	https://console.cloud.tencent.com/
[8]:	https://cloud.tencent.com/product/vpc.html
[9]:	https://console.cloud.tencent.com/vpc/
[10]:	https://console.cloud.tencent.com/
[11]:	https://console.cloud.tencent.com/cdb/ 
