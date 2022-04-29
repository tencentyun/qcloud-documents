## 操作场景
iPaaS Database 连接器支持 MySQL 数据库的连接及增删改查等数据库常用操作。

## 前期准备

您需要开通 MySQL，并已配置好安全组规则和公网 IP。 

### 购买 MySQL实例

购买 [云数据库 RDS for MySQL](https://console.huaweicloud.com/rds/?agencyId=344eb50173f9430489ff1be6c4769e54&region=cn-south-1&locale=zh-cn#/rds/createIns) 服务，根据需求购买云数据库。
>?默认内网端口为3306，可自定义，后面安全组的端口配置需根据此处选择的端口号填写。


### 设置数据库密码[](id:method3)

 ![image-20220401150233064](https://qcloudimg.tencent-cloud.cn/raw/c9294d2f7fa67bab147c0753c3e1b843.png)
 
### 设置安全组

1. 登录华为云控制台，进入 [安全组](https://console.huaweicloud.com/vpc/?region=cn-south-1#/secGroups) 设置。
2. 修改新建安全组或者已有安全组。
![](https://qcloudimg.tencent-cloud.cn/raw/23cd4b4c5da4e5d16934f86dd0e342a7.png)
<dx-tabs>
:::新建安全组
1. 单击控制台右上角的**创建安全组**，进入安全组创建页面，模板选择自定义。
![image-20220325104730507](https://qcloudimg.tencent-cloud.cn/raw/d3ca1fde6c2d3c47b7467ce786426fb6/image-20220325104730507.png)
2. 单击配置规则。
![image-20220325104804412](https://qcloudimg.tencent-cloud.cn/raw/548e0e1698827d26b9888b0adf3640ce/image-20220325104804412.png)
3. 添加如下入站规则。


 | 方向   | 协议 | 端口 | 源地址    | 说明              |
 | ------ | ---- | ---- | --------- | ----------------- |
 | 入方向 | TCP  | 3306 | 0.0.0.0/0 | 通过公网访问MySQL |
 
>!若需配置指定的 iPaaS 出口IP访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
>
 ![](https://qcloudimg.tencent-cloud.cn/raw/f61626b645f633082a737ee1c1db34f6.png)
 3. 在 [实例管理](https://console.huaweicloud.com/rds/?agencyId=0d6513274680f2a11fe9c008e8660bbb&region=cn-east-3&locale=zh-cn#/rds/management/list) 页面，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航栏，单击**连接管理**，可切换为新建的安全组绑定。
 ![](https://qcloudimg.tencent-cloud.cn/raw/5b38c1657496de2458cf251d9778df94.png)
 :::

 ::: 修改已有安全组

 1. 在 [实例管理](https://console.huaweicloud.com/rds/?agencyId=0d6513274680f2a11fe9c008e8660bbb&region=cn-east-3&locale=zh-cn#/rds/management/list) 页面，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航栏，单击**连接管理**，可对默认绑定的安全组规则进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/e6f03e2aaca9d1d2be6bded81cd93046.png)
2. 修改入方向规则，添加如下入站规则。



 | 方向   | 协议 | 端口 | 源地址    | 说明              |
 | ------ | ---- | ---- | --------- | ----------------- |
 | 入方向 | TCP  | 3306 | 0.0.0.0/0 | 通过公网访问MySQL |
>!若需配置指定的 iPaaS 出口 IP 访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
 :::

</dx-tabs>
 

### 绑定弹性公网 IP
您可以购买弹性公网 IP 绑定到 MySQL，或者绑定已有的弹性公网 IP 到 MySQL。
<dx-tabs>
 ::: 购买弹性公网IP绑定到 MySQL

1. 单击**查看弹性公网IP**，获取弹性公网 IP，单击右上角的**购买弹性公网IP**。
>!购买弹性公网 IP 需要和 MySQL 处于同一可用区。
>
![image-20220325105957204](https://qcloudimg.tencent-cloud.cn/raw/da9d0685e106381d7ddf3ce35933d556/image-20220325105957204.png)
2. 按实际情况选择计费模式，设置区域，线路和带宽等参数，点击立即购买。
 ![image-20220325110114446](https://qcloudimg.tencent-cloud.cn/raw/0c3582d96bbb61f27db682f8b636f852/image-20220325110114446.png)
3. 购买弹性公网IP后，在 [实例管理](https://console.huaweicloud.com/rds/?agencyId=0d6513274680f2a11fe9c008e8660bbb&region=cn-east-3&locale=zh-cn#/rds/management/list)页面，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航栏，单击**连接管理**，在**连接信息**>**公网地址**处，单击**绑定**。
 ![image-20220401155129644](https://qcloudimg.tencent-cloud.cn/raw/9e998721254b996b7175f803d1bcf7b3.png)
 4. 绑定成功后，界面显示公网地址：[](id:method1)
![](https://qcloudimg.tencent-cloud.cn/raw/37a938431fa4adb8e28532b30fd2d652.png)
:::
::: 已有弹性公网 IP 绑定到 MySQL

1. 购买实例后，在 [实例管理](https://console.huaweicloud.com/rds/?agencyId=0d6513274680f2a11fe9c008e8660bbb&region=cn-east-3&locale=zh-cn#/rds/management/list)页面，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航栏，单击**连接管理**，在**连接信息**>**公网地址**处，单击**绑定**。
 ![image-20220401155129644](https://qcloudimg.tencent-cloud.cn/raw/9e998721254b996b7175f803d1bcf7b3.png)
 2. 在弹出框的弹性公网IP地址列表中，选择目标弹性公网IP，单击“确定”，提交绑定任务。 绑定成功后，界面显示公网地址：
![](https://qcloudimg.tencent-cloud.cn/raw/37a938431fa4adb8e28532b30fd2d652.png)
 :::
 
</dx-tabs>

## 接入配置
### 步骤1：创建测试数据库[](id:method2)

在[实例管理](https://console.huaweicloud.com/rds/?agencyId=0d6513274680f2a11fe9c008e8660bbb&region=cn-east-3&locale=zh-cn#/rds/management/list)页面，选择目标实例，单击**实例名称**，进入实例的**基本信息**页面。在左侧导航栏，单击**数据库管理**>**创建数据库**，创建测试数据库。
![image-20220401160001490](https://qcloudimg.tencent-cloud.cn/raw/1a8070b507ac93a3ca3c9c1195eeaab1.png)

### 步骤2：配置鹊桥 iPaaS Database 连接器连接属性

1. 在 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择Database连接器相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/d9c19f62caa7e148b330f90c69ee6a5f.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![image-20220401160819999](https://qcloudimg.tencent-cloud.cn/raw/14e0018d4398c500a088685161920d57.png)
4. 填写连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。
 - 数据库类型：此处选择 MySQL
 - 地址：填写绑定的弹性公网IP，可参考 [弹性公网IP信息](#method1) 进行填写
 - 端口号：填写数据库访问端口号，可参考 [访问端口号](#method1) 进行填写
 - 数据库：填写 [步骤1](#method2) 中创建的测试数据库名称
 - 用户名：填写购买时设置的用户名称，可参考 [设置数据库密码](#method3)
 - 密码：填写购买时设置的用户密码，可参考 [设置数据库密码](#method3)
![](https://qcloudimg.tencent-cloud.cn/raw/28ac4b468b4fad33c1a9d42f9f189ef7.png)
5. 其他相关配置可参考 [Database 连接器使用指南](https://cloud.tencent.com/document/product/1270/55449)。
