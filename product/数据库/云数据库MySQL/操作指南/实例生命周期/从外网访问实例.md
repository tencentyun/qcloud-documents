## 操作场景
如果您的云服务器 CVM 与云数据库 MySQL 部署在同一地域上，则无需申请外网地址。如果在不同地域或者在腾讯云以外的系统上，则需开启外网地址来连接云数据库 MySQL（中国香港及国外地区 MySQL 实例暂不支持开通外网），本文为您介绍如何开启外网访问地址及登录实例。

## 操作步骤

### 开启外网访问地址
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb/ )。
2. 在实例列表中，选择需要修改的实例，单击实例名或操作列的【管理】，进入实例详情页面。
![](https://main.qcloudimg.com/raw/6f41c4bdd00b2900369f3d220f7d346f.png)
3. 在实例详情页下的基本信息里找到【外网地址】，单击【开启】。
![](https://main.qcloudimg.com/raw/c1ef4d6d01fe9cd3f7e9caabae440fc6.png)
4. 单击【确定】后，外网开通进入处理状态。
![](https://main.qcloudimg.com/raw/b2a407e7609fa0c31b0e7ee06c94a3de.png)
5. 开启成功后，即可在基本信息中查看到外网地址。
6. 通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。

### 登录实例
1. 在连接到网络并且安装了 MySQL 客户端的服务器上使用以下标准 MySQL 语句登录云数据库。云数据库的帐号可以是【帐号管理】中的任意帐号。
```
mysql -h hostname -P port -u username -p
```
>?
>- 请将 hostname 替换为目标 MySQL 数据库实例的外网 IP 地址；将 port 替换为外网端口号；将 username 替换为外网访问用户名，例如 cdb_outerroot；并在提示 Enter password：后输入 cdb_outerroot 帐号对应的密码。
>- 外网访问用户名用于外网访问，建议您单独创建便于访问控制管理。
>
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
2. 登录云数据库后，即可执行 MySQL 语句管理云数据库。MySQL 语句请参见 [MySQL 官方文档](http://dev.mysql.com/doc/)。
示例如下：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)
