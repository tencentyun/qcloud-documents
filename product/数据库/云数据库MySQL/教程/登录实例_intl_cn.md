## 1 使用命令行方式登录

1.登录[www.qcloud.com][1]后，进入管理中心，在“云产品”模块点击“云数据库”，进入云数据库管理视图。

![][image-1]

2.获取要登录的云数据库的“IP”及“端口号”。

![][image-2]

3.设置云数据库的密码。点击云数据库实例的“初始化”按钮，进行初始化时设置。

![](https://mc.qcloudimg.com/static/img/de1bf7376fde758eba7fc916a3b44e22/999.png)

如果忘记云数据库密码，可以重置该密码，详见[密码重置][2]。

4.登录云服务器，在云服务器上使用下面标准MYSQL语句登录云数据库（云数据库的帐号默认为 root）。


```
mysql -h [云数据库IP] -P [云数据库端口号] -uroot -p[云数据库密码]
```

> 注：
> 需要先安装MySQL客户端，可到[\[MySQL官方下载安装]][3]
> 命令行中第一个“-P”为大写，第二个“-p”为小写。

示例如下：

![][image-4]

5.登录云数据库后，即可执行MYSQL语句管理云数据库。MySQL语句说明详见：[MySQL手册][4]。

示例如下：

![][image-5]

## 2 使用云数据库管理界面登录

1. 登录[www.qcloud.com][5]后，进入管理中心，在“云产品”模块点击“云数据库”，进入云数据库管理视图。

![][image-6]

2.设置云数据库的密码。点击云数据库实例的“初始化”按钮，进行初始化时设置。

![](https://mc.qcloudimg.com/static/img/de1bf7376fde758eba7fc916a3b44e22/999.png)

如果忘记云数据库密码，可以重置该密码，详见[密码重置][6]。

3.在云数据库“实例列表”页面，找到要登录的云数据库实例，点击右侧的“登录”按钮。

![][image-8]

4.在phpMyAdmin登录界面，输入正确的云数据库密码，点击“执行”后进入phpMyAdmin管理界面。

![][image-9]

5. 在phpMyAdmin管理界面，即可对数据库进行相关操作。

![][image-10]

[1]:	http://www.qcloud.com
[2]:	/doc/product/236/%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE
[3]:	https://dev.mysql.com/downloads/installer/
[4]:	http://dev.mysql.com/doc/
[5]:	http://www.qcloud.com
[6]:	/doc/product/236/%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE

[image-1]:	//mc.qcloudimg.com/static/img/313d5fd529bfe4898651efa2b3b08dc6/1.png
[image-2]:	//mc.qcloudimg.com/static/img/31d1ad4d65d8ada9ebcdc795fcc0ae22/2.png
[image-3]:	//mc.qcloudimg.com/static/img/7c1fe616342da0045d55abbd869e215b/3.png
[image-4]:	//mccdn.qcloud.com/img568127c27a3a6.png
[image-5]:	//mccdn.qcloud.com/img568127e32312e.png
[image-6]:	//mc.qcloudimg.com/static/img/313d5fd529bfe4898651efa2b3b08dc6/1.png
[image-7]:	//mc.qcloudimg.com/static/img/7c1fe616342da0045d55abbd869e215b/3.png%0A
[image-8]:	//mc.qcloudimg.com/static/img/3945a72eb332d620658e95f16da5fc91/6.png
[image-9]:	//mccdn.qcloud.com/img568128dbefa9b.png
[image-10]:	//mccdn.qcloud.com/img568128e2b6f6a.png
