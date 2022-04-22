## 操作场景
iPaaS Database 连接器支持 MySQL 数据库的连接及增删改查等数据库常用操作。


## 前期准备
您需要先开通 MySQL，并已配置好安全组规则和外网访问域名。 

### 购买云数据库 MySQL[](id:method3)
登录 [腾讯云数据库 MySQL](https://buy.cloud.tencent.com/cdb) 购买页面，根据需求购买云数据库。详细操作可参考 [购买方式](https://cloud.tencent.com/document/product/236/5160)。
>!默认内网端口为3306，可自定义，后面安全组的端口配置需根据此处选择的端口号填写（外网端口映射至内网端口进行访问）。


### 设置安全组
设置允许 iPaaS 出口 IP 访问数据库的操作。详细操作可参考 [MySQL安全组配置](https://cloud.tencent.com/document/product/236/9537)。
<dx-tabs>
:::新建安全组
  
1. 单击 [安全组](https://console.cloud.tencent.com/vpc/securitygroup?rid=8&rid=8) 或购买页面的**新建**，进入安全组创建页面，模板选择自定义或放通全部端口。
    ![](https://qcloudimg.tencent-cloud.cn/raw/31cf4340d5c42857a277ebcb2545cc5e.jpg)
2. 单击配置规则（选择自定义需操作此步骤，上一步选择全部端口放通单击确定即可）。
![](https://qcloudimg.tencent-cloud.cn/raw/de71cb94854233ad1ce7be789075b3d6.png)
3. 添加如下入站规则。




| 方向   | 协议 | 端口 | 源地址    | 说明                                |
| :------------- | ---- | ---- | --------- | ------------------------------------- |
| 入方向 | TCP  | 3306（若数据库自定义端口填写自定义端口号） | 0.0.0.0/0 | 开启通过公网访问 MySQL|

>! 若需配置指定的iPaaS出口IP访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。 
:::
::: 修改已有安全组

1. 在 [安全组实例列表](https://console.cloud.tencent.com/vpc/securitygroup?rid=8&rid=8) 中，单击要修改的安全组实例右侧的**修改规则**，对已有规则进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/c7413fc7c2727bbfbd5031290498d4bb.png)
2. 修改入方向规则，添加如下入站规则。




 | 方向   | 协议 | 端口 | 源地址    | 说明                                |
 | :-------------  | ---- | ---- | --------- | ------------------------------------- |
 | 入方向 | TCP  | 3306（若数据库自定义端口填写自定义端口号） | 0.0.0.0/0 | 开启通过公网访问 MySQL    |
 
>!若需配置指定的 iPaaS 出口 IP 访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
:::

</dx-tabs>


### 开启外网地址访问[](id:method1)
1. 购买成功后， 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)。
2. 在实例列表中选中想要设置的实例，进入实例管理页面。
3. 单击**开启**，开启外网地址访问。
![](https://qcloudimg.tencent-cloud.cn/raw/159b81af0fbd86d819be0c9a64c57c66.png)

## 接入配置
### 步骤1：创建测试数据库[](id:method2)

1. 进入数据库管理页面，单击**创建数据库**。输入数据库的登录账密后进入库管理页面再次单击创建数据库。
![](https://qcloudimg.tencent-cloud.cn/raw/29b114ed27a89e63ea5448caf7b16350.png)
2. 输入数据库的登录账密后进入库管理页面单击**新建数据库**。
![](https://qcloudimg.tencent-cloud.cn/raw/d9c7046fd6878685efd942fb509e2dc1.png)

### 步骤2：配置鹊桥 iPaaS Database连接器连接属性

1. 在 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择 **NewFlow** 在画布中单击**+**选择 Database 连接器相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/d9c19f62caa7e148b330f90c69ee6a5f.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![image-20220401160819999](https://qcloudimg.tencent-cloud.cn/raw/14e0018d4398c500a088685161920d57.png)
4. 填写连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。
 - 数据库类型：此处选择MySQL
 - 地址：填写数据库外网访问域名，可参考 [开启外网地址访问](#method1)中的外网地址进行填写 
 - 端口号：填写数据库外网访问端口号，可参考 [开启外网地址访问](#method1)中的端口号进行填写
 - 数据库：填写 [步骤1](#method2) 中创建的测试数据库名称
 - 用户名：填写购买时设置的用户名称，可参考 [购买云数据库 MySQL](#method3)
 - 密码：填写购买时设置的用户密码，，可参考 [购买云数据库 MySQL](#method3)
![](https://qcloudimg.tencent-cloud.cn/raw/70746f2ffb7a65a65419c2a0863c3cbd.png)
5. 其他相关配置可参考 [Database 连接器使用指南](https://cloud.tencent.com/document/product/1270/55449)。
