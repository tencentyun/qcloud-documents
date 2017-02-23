## 步骤2：创建Web服务器

在此步中，创建连接到您在步骤 1：创建数据库实例中创建的 腾讯云数据库MySQL实例的 Web 服务器。

### 1. 创建Linux服务器
首先需要根据[云主机创建Linux教程][1]创建Linux服务器并[部署应用环境][2]

### 2. 在Linux服务器中安装MySQL客户端
可登陆[MySQL官方网站][3]下载并安装客户端

### 3. 访问云数据库MySQL服务
您可以在和云数据库MySQL所属网络相同的云服务器上，直接连接实例的内网地址访问MySQL服务。
MySQL语句说明详见：[MySQL手册][4]。
![][image-1]

[1]:	https://www.qcloud.com/document/product/213/2936
[2]:	https://www.qcloud.com/document/product/213/2975
[3]:	https://dev.mysql.com/downloads/installer/
[4]:	http://dev.mysql.com/doc/

[image-1]:	//mccdn.qcloud.com/img568127c27a3a6.png