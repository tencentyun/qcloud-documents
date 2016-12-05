## 使用云数据库CDB的wordpress服务
### 说明
在单实例版wordpress示例中您学会了如何快速安装WordPress。 
其中数据是写到同一个容器中运行的mysql数据库中，虽然这样的配置可以快速且容易启动，但它也有一个问题，如果容器因任何原因停止，数据库和WordPress文件丢失。

在本教程中，您将学习如何设置MySQL数据库，它将在实例/容器重新启动后继续存在。 这是通过使用云数据库CDB来实现永久存储。

### 详细步骤
#### 创建容器服务集群
详情见快速入门中步骤二[创建集群](https://www.qcloud.com/doc/product/457/6774)

#### 创建云数据库CDB
选择集群所属网络，添加Mysql数据库,(也可不在VPC内，但只能通过公网访问)

选择购买配置后。等待创建完成，初始化cdb数据库

#### 创建wordpress服务
环境变量填写

WORDPRESS_DB_HOST  =  云数据库MYsql的地址

WORDPRESS_DB_PASSWORD  = 初始化时填写的密码

#### 创建完成，访问测试
![Alt text](https://mc.qcloudimg.com/static/img/7bc02b10d802999c755f187351e64d63/%7B9A1566DD-C111-4AAB-96CA-88AF7768661E%7D.png)