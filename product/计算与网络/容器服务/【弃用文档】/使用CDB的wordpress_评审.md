在 [单实例版 WordPress](/doc/product/457/7205) 示例中我们介绍了如何快速创建 WordPress 服务。 单实例版 WordPress 的数据是写到同一个容器运行的 MySQL 数据库中，虽然这样的配置可以快速启动，但它也存在一个问题：如果容器因某种原因停止，数据库和存储类的文件将会丢失。

本文档旨在介绍如何设置 MySQL 数据库，它将在实例/容器重新启动后继续存在。通过使用 [云数据库CDB](https://cloud.tencent.com/product/cdb-overview) 可以实现永久存储。

>**注意：**
> 在创建使用 CDB 的 WordPress 服务之前，您必须拥有:
1. 一个腾讯云帐户。有关如何创建腾讯云帐户，请在 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云帐户。
2. 一个创建好的集群。有关如何创建集群的详细信息，参见 [新建集群](https://cloud.tencent.com/document/product/457/9091) 。

## 创建 WordPress 服务
### 第一步：创建云数据库 CDB
1) 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 。
2) 单击私有网络列表页的 ID/名称（如：vpc-xxxxx）。
![](//mc.qcloudimg.com/static/img/33830d9c88d9cb332b1ce148588cdbf5/image.png)
3) 在私有网络详情页，选择数据库目录下的 **MySQL**，单击右侧**添加**。
![](//mc.qcloudimg.com/static/img/6b93fb0bc0ea4937a77ce77564934ed5/image.png)
4) 选择购买配置，完成系列支付操作。相关详情请参见 [数据库MySQL](/doc/product/236/5147)。
5) 购买的 MySQL 将出现在 MySQL 实例列表中。
![](//mc.qcloudimg.com/static/img/d5d50b0f9406856b875ba1171e7e8a1f/image.png)
6) 初始化 MySQL 实例。单击右侧 **操作** 栏下的**初始化**。
![](//mc.qcloudimg.com/static/img/2f548123653b1b80b90bd61c74ac495f/image.png)
7) 配置初始化相关参数，然后单击**确定**开始初始化。
 - **支持字符集**：选择 MySQL 数据库支持的字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为 3306。
 - **root账户密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置此 root 账户的密码。
 - **确认密码**：再次输入密码。
 ![](//mc.qcloudimg.com/static/img/9d4b57c8c8dd4b5000521ff9049dbb81/image.png)
 
8) 目标 MySQL 实例的状态变为 **运行中**，说明已初始化成功。
![](//mc.qcloudimg.com/static/img/c285fb82e354ba127cd0cce01804a197/image.png)

### 第二步：创建使用 CDB 的 WordPress 服务
1) 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2) 单击左侧导航栏中的**服务**，单击服务列表页的**+ 新建**。
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3) 设置服务的基本信息。
 - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。
 - **运行集群**：选择服务所要运行的集群。运行集群需要选择运行中和集群内有可用主机的集群。
 - **服务描述**：创建服务的相关信息。该信息将显示在 **服务信息** 页面。
![](//mc.qcloudimg.com/static/img/9254649a08d86761bcb8287fe5a45141/image.png)

4) 镜像配置。
 - **名称**：输入运行容器的名称，此处以 wordpress 为例。
 - **镜像**：填写 `tutum/wordpress` 。
 - **版本（Tag）**：填写 latest。
![](//mc.qcloudimg.com/static/img/b5c035081625c15a1dcbdf0a3cabf6a7/image.png)

5) 单击运行容器下的 **显示高级设置**，在弹出的下拉列表中，单击环境变量下的**新增变量**。依次填写：
WORDPRESS_DB_HOST = 云数据库 MySQL 的地址
WORDPRESS_DB_PASSWORD = 初始化时填写的密码
![](//mc.qcloudimg.com/static/img/6508b3858d0bba46510a81279aad2e15/image.png)
6) 设置端口映射。将容器端口和服务端口都设置为 80 。
>**注意**：服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000-32768端口，否则可能会出现容器服务无法使用问题。详情参见[容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)

![](//mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)

7) 单击 **创建服务**。完成 WordPress 服务的创建。
>**注意**：其他选项保持为默认设置。

## 访问 WordPress 服务
1) 提供三种方式访问 WordPress 服务。
 - 通过**负载均衡 IP**来访问 WordPress 服务。单击服务页面的**服务信息**查看负载均衡 IP和负载均衡ID。 
![](//mc.qcloudimg.com/static/img/f92f30a3360c46ac0e6e76d045f4484f/image.png) 
 - 通过 **域名** 来访问 WordPress 服务。在容器服务控制台左侧导航栏中，单击**负载均衡**，单击**TCP/UDP**，找到对应的负载均衡ID，复制域名访问服务。
 - 集群内的其他服务或容器可以直接通过服务名称访问。
 
2) 进入 WordPress 服务器的默认欢迎页。
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)

若容器创建失败，可查看[事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
