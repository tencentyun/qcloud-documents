## 操作场景
如果您的云服务器与云数据库部署在同一地域上，则无需申请外网地址。如果在不同地域或者在腾讯云以外的系统上，则需开启外网地址来连接 TencentDB for  MySQL 数据库（**中国香港及国外地区 MySQL 实例暂不支持开通外网**），本文档将介绍如何开启外网访问地址及登录实例说明。

## 操作步骤
## 1. 开启外网访问地址

1.1 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb/ )，实例列表中，找到需要修改的实例，单击操作里的【管理】。
![](https://main.qcloudimg.com/raw/c029884f7fd3c2804cf3ab30fec6991c.png)

1.2 在实例信息里找到【外网地址】，单击【开启】。
![](https://main.qcloudimg.com/raw/678a04f0cc5dc9131d86c3f8d7a38727.png)

1.3  单击【确定】后，外网开通进入处理状态。
![](https://main.qcloudimg.com/raw/5be4810055e3d2d29fc296a02c2c5caa.png)

1.4 开启成功后，即可在基本信息中查看到外网地址。
![](https://main.qcloudimg.com/raw/6ab0f36759a25b18dbf940f18fc526e6.png)

1.5 通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。
![](https://main.qcloudimg.com/raw/b5cb73de436d096ebbbbcf5c05e3928d.png)

## 2. 登录实例

2.1  在连接到网络并且安装了 MySQL 客户端的服务器上使用下面标准 MySQL 语句登录云数据库。云数据库的帐号可以是【帐号管理】中的任意帐号。
```
mysql -h [云数据库外网地址] -P [云数据库端口号] -u [云数据库帐号] -p[云数据库密码]
```
>!命令行中第一个“-P”为大写，第二个“-p”为小写。</blockquote>
示例如下：
![](https://mc.qcloudimg.com/static/img/59c193b46229a88338bcd51cadad9aaf/step7.png)

2.2  登录云数据库后，即可执行 MySQL 语句管理云数据库。MySQL语句说明详见：[MySQL手册](http://dev.mysql.com/doc/)。
示例如下：
![](https://mc.qcloudimg.com/static/img/ab2e159d88201f6bf29cee91611a9864/step8.png)
