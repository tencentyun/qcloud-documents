## 操作场景
iPaaS Database 连接器支持 MySQL 数据库的连接及增删改查等数据库常用操作。


## 前期准备
您需要先开通 MySQL，并且已配置好安全组规则和外网访问域名。

### 购买云数据库 RDS MySQL 实例

1. 进入 [阿里云云数据库RDS控制台](https://rdsnext.console.aliyun.com/rdsList/cn-hangzhou/basic)，配置数据库基础资源。
![image-20220401154807678](https://qcloudimg.tencent-cloud.cn/raw/3e39baa4b791286f3c9204384c75cde2.png)
2. 配置基础资源后，进入实例配置界面，配置成功后，创建 RDS 实例。[](id:method3)
![](https://qcloudimg.tencent-cloud.cn/raw/aa0b0e8724f46bed378c95e57d4d0f8f.png)

### 申请外网地址
1. 登录 [云数据库RDS控制台](https://rdsnext.console.aliyun.com/rdsList/cn-hangzhou/basic)。
![](https://qcloudimg.tencent-cloud.cn/raw/8e2bbb2313654875f7ce68ed806f50dd.png)
2. 进入 [实例列表管理](https://rdsnext.console.aliyun.com/rdsList/cn-hangzhou/basic) 界面，单击目标实例 ID，点击左侧数据库连接，申请外网地址。[](id:method1)
![](https://qcloudimg.tencent-cloud.cn/raw/6f626668c8c54b525e6eec628ec48e17.png)
3. 在外网地址处，单击**设置白名单**，设置 iPaaS 出口 IP 白名单。设置为0.0.0.0/0即可。
>!若需配置指定的iPaaS出口IP访问，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3896ae123319994937f3daba2286aee6.png)
4. 设置成功后，会显示外网地址。
![](https://qcloudimg.tencent-cloud.cn/raw/310c8b2b93a75a3c2468c97000a63359.png)


## 接入配置
### 步骤1：创建测试数据库[](id:method2)

1. 单击目标实例ID，单击**数据库管理**>**创建数据库**。输入数据库的登录账密后进入库管理页面再次单击创建数据库。
![](https://qcloudimg.tencent-cloud.cn/raw/b6eed314122be19545945e90e29fb856.png)
2. 输入数据库的登录账密后进入库管理页面单击**新建数据库**。
![](https://qcloudimg.tencent-cloud.cn/raw/03107f7b88d768dc7483372cc7349fa8.png)

### 步骤2：配置鹊桥 iPaaS Database 连接器连接属性

1. 在 [千帆鹊桥 iPaaS 控制台](https://console.cloud.tencent.com/ipaas)，单击**新建应用**，选择**空白应用**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3a02558a61e6168e4a6c993931820.png)
2. 单击左侧的**集成流**展开选择**NewFlow**在画布中单击**+**选择Database连接器相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/d9c19f62caa7e148b330f90c69ee6a5f.png)
3. 单击右侧的**新建连接器配置**并按照指引填入相关参数。
![image-20220401160819999](https://qcloudimg.tencent-cloud.cn/raw/14e0018d4398c500a088685161920d57.png)
4. 填写连接器配置参数后，单击**测试连接**，测试连通性，测试成功后，会出现”连接配置正确“的提示，保存连接器配置即可，失败根据提示来重新填写对应信息。
 - 数据库类型：此处选择MySQL
 - 地址：填写数据库外网访问域名，可参考 [申请外网地址](#method1) 中的外网地址进行填写
 - 端口号：填写数据库访问端口号，可参考 [申请外网地址](#method1) 中的端口号进行填写
 - 数据库：填写 [步骤1](#method2) 中创建的测试数据库名称
 - 用户名：填写购买时设置的用户名称，可参考 [创建RDS实例](#method3)
 - 密码：填写购买时设置的用户密码，可参考 [创建RDS实例](#method3)
![](https://qcloudimg.tencent-cloud.cn/raw/a51d9a5b78c3008ed93c805d4930ba06.png)
5. 其他相关配置可参考 [Database 连接器使用指南](https://cloud.tencent.com/document/product/1270/55449)。

