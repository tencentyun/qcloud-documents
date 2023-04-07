TDSQL-C MySQL 版支持实例级独立 IP 地址，即您可以通过集群下读写实例或任一只读实例的 IP 地址连接访问对应实例。本文为您介绍，如何使用内网或外网地址通过 Linux 云服务器连接集群下的任一实例。

## 前提条件[](id:QTTJ)
已创建数据库集群账号，具体请参见 [创建数据库账号](https://cloud.tencent.com/document/product/1003/62730)。

## 步骤一：查询需要连接的实例内/外网 IP 地址[](id:SLIPDZ)
1. 登录 [TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/cynosdb/mysql/ap-beijing/cluster/cynosdbmysql-fo7dcbse/detail)。
2. 在集群列表页，根据实际使用的视图模式进行操作：
<dx-tabs>
::: 页签视图
1. 在左侧集群列表，单击目标集群，进入集群管理页。
2. 在集群详情下，找到需要查询内/外网 IP 地址的实例，在其所属网络下方可查看该实例的内/外网 IP 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/b3edce7cf890c03e1409b3c65bef4bb4.png)
:::
::: 列表视图
1. 在集群列表中，找到目标集群，单击**集群 ID** 或操作列的**管理**，进入集群管理页面。
2. 在集群管理页面，选择实例列表页，选择读写实例或只读实例，在**字段：内/外网地址**下查看对应实例的内/外网 IP 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/4bb088d5a196ec6ea6d6d4c4baef7cd2.png)
:::
</dx-tabs>

## 步骤二：连接集群下的目标实例
1. 登录到 Linux 云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/1003/79661)。
2. 以 CentOS 7.2 64 位系统的云服务器为例，执行如下命令安装 MySQL 客户端。
```
yum install mysql
```
提示 `Complete!` 说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/16c77e28c40ae9be9a182b1c61843ecd.png)
3. 根据不同连接方式，选择相应的操作：
 - **内网连接时：**
    1. 执行如下命令，登录到 TDSQL-C MySQL 版集群。
```
mysql -h hostname -P port -u username -p
```
      - hostname：替换为 TDSQL-C MySQL 版集群下目标实例的内网地址，内网地址查询方法参见 [步骤一](#SLIPDZ)。
      - port：替换为内网端口号。
		- username：替换为在 [前提条件](#QTTJ) 中创建的账号名，此处以默认的账号名 root 为例。
示例：内网地址为10.0.168.14:5308，账号名为 root，连接命令输入为 `mysql -h 10.0.168.14 -P 5308 -u root -p`。
    2. 在提示 `Enter password：` 后输入以上命令中账号对应的密码，如忘记密码可参见 [重置密码](https://cloud.tencent.com/document/product/1003/62731) 进行修改。
    本例中提示 `MySQL [(none)]>` 说明成功登录到 TDSQL-C MySQL 版。
   ![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
   - **外网连接时：**
    1. 执行如下命令，登录到 TDSQL-C MySQL 版集群。
```
mysql -h hostname -P port -u username -p
```
      - hostname：替换为 TDSQL-C MySQL 版集群下目标实例的外网地址，外网地址查询方法参见 [步骤一](#SLIPDZ)。若外网地址未开启，请参见 [开启或关闭外网地址](https://cloud.tencent.com/document/product/1003/79682)。
      - port：替换为外网端口号。
      - username：替换为外网连接的账号名，用于外网连接，建议您在控制台单独创建账号便于连接控制管理。
    2. 在提示 `Enter password：` 后输入外网连接账号名对应的密码，如忘记密码可参见 [重置密码](https://cloud.tencent.com/document/product/1003/62731) 进行修改。
    本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
4. 在 `MySQL \[(none)]>` 提示符下可以发送 SQL 语句到要执行的 TDSQL-C MySQL 版服务器，具体命令行请参见 [mysql Client Commands](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以 `show databases;` 为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

## 常见问题
#### 如果忘记账号名以及密码，怎么重置后登录集群？
您可以在 TDSQL-C MySQL 版控制台，集群管理页面的**账号管理**下查看您创建的用于连接集群的账号名，当您忘记密码时，可通过重置密码操作修改密码后再登录集群。
![](https://qcloudimg.tencent-cloud.cn/raw/aa0aebe262c7b0d2f26e4218cafeefed.png)

#### 通过内网或外网连接 TDSQL-C MySQL 版是否需要为集群配置安全组？
需要配置安全组，详细步骤请参见 [配置安全组](https://cloud.tencent.com/document/product/1003/62745)。注意，若开启外网，通过外网连接时，配置的安全组规则需放通内网的访问端口。

#### 如果云服务器的安全组规则匹配不当，导致无法登录 Linux 实例怎么办？
如果云服务器的安全组规则匹配不当，如未放通相应端口导致无法登录 Linux 实例，您可以通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 检查实例当前配置的安全组连通性。
![](https://main.qcloudimg.com/raw/9fc46a7133fdb07b631876cd9fa4c253.png)
通过一键检测可得知登录失败的可能原因。
![](https://qcloudimg.tencent-cloud.cn/raw/f0eccdbd666a04e73de610d42d3e3b49.png)
然后在云服务器实例详情页，选择**安全组** > **编辑规则**，然后放通对应端口，详细操作请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

#### 无法连接集群还与哪些设置有关？
当无法连接集群时，您可以检查云服务器 CVM 和 TDSQL-C MySQL 是否在同一腾讯云账号下，是否处于同一地域，是否为同一 VPC 网络。需确保以上三点设置相同，才可以正常连接集群。
