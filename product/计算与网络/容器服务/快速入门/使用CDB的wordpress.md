### 说明
在单实例版wordpress示例中我们展示了如何快速安装WordPress。 
在那个示例中数据是写到同一个容器中运行的mysql数据库中，虽然这样的配置可以快速启动，但它也有一个问题：如果容器因任何原因停止，数据库和存储类的文件将会丢失。

在本教程中，我们将展示如何设置MySQL数据库，它将在实例/容器重新启动后继续存在。通过使用云数据库CDB可以实现永久存储。

### 详细步骤
#### 第一步：创建容器服务集群
首先要拥有一个可运行容器的集群。如无集群新建一个集群，详情查看[新建集群](https://www.qcloud.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4)。

#### 第二步：创建云数据库CDB
选择集群所属网络，添加Mysql数据库。(也可不在VPC内，但只能通过公网访问)
![Alt text](https://mc.qcloudimg.com/static/img/22ae8f766708955e4badfa4dd8d3cc8a/Image+036.png)

选择购买配置后，等待创建完成，初始化CDB数据库。也可使用自建的MySQL服务或已有的CDB服务。

![Alt text](https://mc.qcloudimg.com/static/img/f3d39903a1d54a2927e9bcbf7e749744/Image+037.png)
#### 第三步：创建wordpress服务
环境变量填写：
WORDPRESS_DB_HOST = 云数据库MySQL的地址
WORDPRESS_DB_PASSWORD = 初始化时填写的密码
点击【完成】以完成创建。

![Alt text](https://mc.qcloudimg.com/static/img/523f276c9c722503ff538392d4d63c9c/Image+039.png)
#### 第四步：访问测试
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)
