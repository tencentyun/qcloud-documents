访问云数据库 MySQL 的方式如下两种：

- **内网访问**：使用云服务器 CVM 直接访问云数据库的内网地址，这种访问方式使用内网高速网络，延迟低。
 - 云服务器和数据库须是同一账号，且同一个[ VPC](https://cloud.tencent.com/document/product/215/20046) 内（保障同一个地域），或同在基础网络内。
 - 内网地址系统默认提供，可在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例列表或实例详情页查看。

- **外网访问**：无法通过内网连接时，可通过外网地址访问云数据库 MySQL。
 - 仅广州、上海、北京、成都、重庆、中国香港、新加坡、首尔、东京、硅谷的实例支持开启外网访问地址。
 - 外网地址需 [手动开启](#waiwang)，可在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例详情页查看，不需要时也可关闭。
 - 开启外网地址，会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网访问数据库。 
 - 云数据库外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。


下面示例分别介绍如何从 Windows 云服务器或 Linux 云服务器登录，以内外网两种不同的方式访问云数据库 MySQL。
## 从 Windows 云服务器访问
1. 登录到 Windows 云服务器，请参见 <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank">快速配置 Windows 云服务器</a>。
2. 下载一个标准的 SQL 客户端。
>?推荐您下载 MySQL Workbench，并根据您的系统来下载适配版本的安装程序，下载地址请参见 https://dev.mysql.com/downloads/workbench/。
>
![](https://main.qcloudimg.com/raw/25e78e6614b2967e8c70140b8849a6d6.png)
3. 界面将提示【Login】、【Sign Up】和【No, thanks, just start my download.】， 选择【No thanks, just start my download.】来快速下载。
![](https://main.qcloudimg.com/raw/f98f84df777a8f8927bec3375781f517.png)
4. 在此台云服务器上安装 MySQL Workbench。
>?
>- 此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。
>- 您可以单击 MySQL Workbench 安装向导中的【Download Prerequisites】，跳转至对应页面下载并安装这两个软件，然后安装 MySQL Workbench。
>
![](https://main.qcloudimg.com/raw/1af292f989f03f3e02e1200b77cb70c1.png)
5. 打开 MySQL Workbench，选择【Database】>【Connect to Database】，输入 MySQL 数据库实例的内网（或外网）地址和用户名、密码，单击【OK】进行登录。
 - Hostname：输入内网（或外网）地址。在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例详情页可查看内网（或外网）地址和端口号。若为外网地址，请确认是否已开启，请参见 [开启外网地址](#waiwang)。
 - Port：内网（或外网）对应端口。
 - Username：默认为 root，外网访问时建议您单独 [创建帐号](https://cloud.tencent.com/document/product/236/35794) 便于访问控制管理。
 - Password：Username 对应的密码，如忘记密码可参见 [重置密码](https://cloud.tencent.com/document/product/236/10305) 进行修改。
![](https://main.qcloudimg.com/raw/8f2aeea985388e545ccf5da8fec908b7.png)
6. 登录成功的页面如图 所示，在此页面上您可以看到 MySQL 数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/9ec2f9393a3652727acbb8dfc41ad5b7.png)

## 从 Linux 云服务器访问
1. 登录到 Linux 云服务器，请参见 <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">快速配置 Linux 云服务器</a>。
2. 以 CentOS 7.2 64 位系统的云服务器为例，执行如下命令安装 MySQL 客户端：
```
yum install mysql
```
提示`Complete!`说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/907e047fed90f6cf68752fb386382927.png)
3. 根据不同访问方式，选择相应的操作：
 - **内网访问时：**
    1. 执行如下命令登录到 MySQL 数据库实例。
```
mysql -h hostname -u username -p
```
      - hostname：替换为目标 MySQL 数据库实例的内网地址，在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例详情页可查看内网地址。
		- username：替换为默认的用户名 root。
    2. 在提示`Enter password：`后输入 MySQL 实例的 root 帐号对应的密码，如忘记密码可参见 [重置密码](https://cloud.tencent.com/document/product/236/10305) 进行修改。
    本例中提示`MySQL [(none)]>`说明成功登录到 MySQL。
![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
   - **外网访问时：**
    1. 执行如下命令登录到 MySQL 数据库实例。
```
mysql -h hostname -P port -u username -p
```
      - hostname：替换为目标 MySQL 数据库实例的外网地址，在 [MySQL 控制台](https://console.cloud.tencent.com/cdb) 的实例详情页可查看外网地址和端口号。若外网地址未开启，请参见 [开启外网地址](#waiwang) 开启。
      - port：替换为外网端口号。
      - username：替换为外网访问用户名，用于外网访问，建议您单独 [创建帐号](https://cloud.tencent.com/document/product/236/35794) 便于访问控制管理。
    2. 在提示`Enter password：`后输入外网访问用户名对应的密码，如忘记密码可参见 [重置密码](https://cloud.tencent.com/document/product/236/10305) 进行修改。
    本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
4. 在`MySQL \[(none)]>`提示符下可以发送 SQL 语句到要执行的 MySQL 服务器，具体命令行请参见 [mysql Client Commands](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)


<span id = "waiwang"></span>
## 附录1：开启外网访问地址
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb/ )，在实例列表中，单击实例名或“操作”列的【管理】，进入实例详情页面。
3. 在实例详情页下的基本信息里找到【外网地址】，单击【开启】。
![](https://main.qcloudimg.com/raw/9253a96d19c982a909e3e73e19f5d20c.png)
4. 单击【确定】后，外网开通进入处理状态。
5. 开启成功后，即可在基本信息中查看到外网地址。
>?通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网地址不变。

## 附录2：常见问题排查
如无法连接云数据库 MySQL，请参见 [无法连接实例问题](https://cloud.tencent.com/document/product/236/32537) 进行排查。


