如果您的云服务器与云数据库部署在同一地域上，则无需申请外网地址。如果在不同地域或腾讯云以外的系统上，需开启外网地址来连接 CDB MySQL 数据库。本文档将介绍如何开启外网访问地址及登录示例说明。

## 开启外网访问地址

1.进入管理控制台，实例列表中，找到需要修改的实例，点击操作里的【管理】：

![](//mccdn.qcloud.com/img56825925da077.png)

2.在实例信息里找到【外网地址】，点击【开启】：

![](//mccdn.qcloud.com/img5682595c5d4e7.png)

3.为外网访问账号配置密码，8-16个字符，至少包含字母、数字、字符（!@#$%^*()）中的两种，外网访问账号为系统默认分配，暂不支持修改。

![](//mccdn.qcloud.com/img56825964bf4e6.png)

4.输入密码后，外网开通进入处理状态：

![](//mccdn.qcloud.com/img5682596b1222d.png)

5.开启成功后，会显示外网访问地址及访问账号和密码，相关信息会同时通过站内信发出：

![](//mccdn.qcloud.com/img568259720d52d.png)

![](//mccdn.qcloud.com/img5682597c603ca.png)


6.通过开关可以关闭外网访问权限，关闭后访问地址将回收，再次开启会重新分配：

![](//mccdn.qcloud.com/img5682598beba65.png)

## 登录示例

1.登录云服务器，在云服务器上使用下面标准 MySQL 语句登录云数据库（云数据库的帐号默认为 `root`）。

```
mysql -h [云数据库外网地址] -P [云数据库端口号] -uroot -p[云数据库密码]
```

>注：命令行中第一个“-P”为大写，第二个“-p”为小写。

示例如下：

![](//mccdn.qcloud.com/static/img/1ad43e0d40701c303fc00b8853cb4d3e/image.png)

2.登录云数据库后，即可执行 MySQL 语句管理云数据库。MySQL 语句说明详见 [MySQL手册>>](http://dev.mysql.com/doc/)。

示例如下：

![](//mccdn.qcloud.com/static/img/751ff4b57b51b21bf687bff6487a69a4/image.png)
