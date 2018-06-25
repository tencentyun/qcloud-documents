如果您的云服务器与云数据库部署在同一地域上，则无需申请外网地址。如果在不同地域或者在腾讯云以外的系统上，则需开启外网地址来连接 CDB for  MySQL 数据库，本文档将介绍如何开启外网访问地址及登录示例说明。

## 开启外网访问地址

1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb/ )，实例列表中，找到需要修改的实例，单击操作里的【管理】。
![](https://mc.qcloudimg.com/static/img/067a823712584842fc983ab34fa79b55/step1.png)
2. 在实例信息里找到【外网地址】，单击【开启】。
![](https://mc.qcloudimg.com/static/img/320b345a398b918c1d3a103c3accdef7/step2.png)
3. 单击【确定】后，外网开通进入处理状态。
![](https://mc.qcloudimg.com/static/img/676fad059f9dc83ac7faac68ae5531cc/step3.png)
![](https://mc.qcloudimg.com/static/img/d5511d9493fa18ccd52e8f41934f513e/step4.png)
4. 开启成功后，即可在基本信息中查看到外网地址。
![](https://mc.qcloudimg.com/static/img/bb8a03a752acf0e3ca59f3009d911eb0/step5.png)
5. 通过开关可以关闭外网访问权限，关闭后访问地址将回收，再次开启会重新分配。
![](https://mc.qcloudimg.com/static/img/5dbd6ccaac4f2a893fbbbac871072eea/step6.png)

## 登录示例

1.  在连接到网络并且安装了 MySQL 客户端的服务器上使用下面标准 MySQL 语句登录云数据库。云数据库的帐号可以为【账号管理】中的任意账号。
```
mysql -h [云数据库外网地址] -P [云数据库端口号] -u [云数据库帐号] -p[云数据库密码]
```
>**注意：**
命令行中第一个“-P”为大写，第二个“-p”为小写。</blockquote>
示例如下：
![](https://mc.qcloudimg.com/static/img/59c193b46229a88338bcd51cadad9aaf/step7.png)
2.  登录云数据库后，即可执行 MySQL 语句管理云数据库。MySQL语句说明详见：[MySQL手册](http://dev.mysql.com/doc/)。
示例如下：
![](https://mc.qcloudimg.com/static/img/ab2e159d88201f6bf29cee91611a9864/step8.png)
